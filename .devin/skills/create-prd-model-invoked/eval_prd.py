#!/usr/bin/env python3
"""
Evaluation script for the create-prd skill.

Reads each PRD markdown output and applies the EC from eval-criteria.md:

DETERMINISTIC CHECKS (pure Python, no model call):
  1. required_sections_present - all required section headings exist (EC 1):
       Problem Statement (or Context), Target Audience (or Personas),
       Goals (or Success Metrics), Functional Requirements, User Stories
       (or Use Cases), Assumptions + Constraints + Dependencies, and
       Out of Scope. Headings are matched case-insensitively against
       aliases; the AC&D requirement is met by one combined heading or
       separate Assumptions / Constraints / Dependencies headings.
  2. sections_non_empty        - every required section has at least one
       sentence (a line/bullet with >= 3 words) (EC 2, EC 5)
  3. out_of_scope_min_items    - the Out of Scope section lists >= 2 items
       (EC 4)
  Any missing or empty required section fails the whole eval (EC 5).

LLM JUDGE CHECK (qualitative EC from eval-criteria.md):
  4. llm_judge_specificity     - a model grades whether each section's
       content is specific (concrete details, numbers, named users or
       systems - no vague placeholders) and aligns with the section
       definitions in eval-criteria.md (EC 3).
       The script reads verdicts from judge_verdicts.json so the judge
       can be any model (or Devin acting as the judge). Run with
       --write-judge-prompts to generate the prompts file for a judge
       to fill in.

Usage:
  python3 eval_prd.py                            # eval all cases in ../create-prd-outputs/*/prd.md
  python3 eval_prd.py path/to/prd.md [...]       # eval specific PRD files
  python3 eval_prd.py --write-judge-prompts      # emit judge_prompts.md
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUTS_DIR = os.path.join(HERE, "..", "create-prd-outputs")
VERDICTS_FILE = os.path.join(HERE, "judge_verdicts.json")
PROMPTS_FILE = os.path.join(HERE, "judge_prompts.md")

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$", re.M)
LIST_ITEM_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+\S", re.M)

MIN_OUT_OF_SCOPE_ITEMS = 2

# Each entry: (key, display name, [keyword groups]). Every keyword group
# must match at least one heading title; a group is a list of alternative
# patterns. AC&D has three groups so separate headings or one combined
# heading both satisfy it.
REQUIRED_SECTIONS = [
    ("problem_statement", "Problem Statement / Context",
     [[r"problem statement", r"context", r"problem"]]),
    ("target_audience", "Target Audience / Personas",
     [[r"target audience", r"persona", r"audience"]]),
    ("goals_metrics", "Goals / Success Metrics",
     [[r"goal", r"success metric", r"metric", r"objective"]]),
    ("functional_requirements", "Functional Requirements",
     [[r"functional requirement", r"requirement"]]),
    ("user_stories", "User Stories / Use Cases",
     [[r"user stor", r"use case"]]),
    ("acd", "Assumptions, Constraints, Dependencies",
     [[r"assumption"], [r"constraint"], [r"dependenc"]]),
    ("out_of_scope", "Out of Scope",
     [[r"out of scope"]]),
]

# The rubric text sent to the LLM judge. Covers EC 3 (sections align with
# the [Definitions] in eval-criteria.md) plus specificity.
JUDGE_RUBRIC = """You are grading output from a "create-prd" skill that writes a Product
Requirements Document.

Section definitions (from eval-criteria.md):
- Problem Statement / Context: The user pain point or market opportunity the product addresses.
- Target Audience / Personas: Who is using the feature and in what scenario.
- Goals & Success Metrics: Quantifiable ways to measure if the product succeeded (e.g., conversion lift, error rates).
- Functional Requirements: Specific capabilities, user flows, and behavior broken down by priority (e.g., P0, P1, P2).
- User Stories / Use Cases: Step-by-step breakdowns of how users interact with the feature.
- Assumptions, Constraints, and Dependencies: Technical or resource limitations, timeline bounds, and external factors.
- Out of Scope: Explicitly states what will not be built in this release to prevent scope creep.

Grade the PRD content below against these criteria:
1. DEFINITION ALIGNMENT: each section's content matches its definition above
   (e.g., Goals/Success Metrics are measurable, Functional Requirements are
   capabilities/flows, Out of Scope states what will not be built).
2. SPECIFICITY: content is concrete - named users/personas, quantified
   metrics, specific capabilities and flows. Fail vague placeholder text
   like "TBD", "improve UX", or "users will like it".
3. PRIORITIZATION: Functional Requirements are broken down by priority
   (e.g., P0/P1/P2, must/should/could) or an equivalent ordering.
4. INTERNAL CONSISTENCY: goals, requirements, and out-of-scope items do not
   contradict each other.

Respond with exactly this JSON on one line:
{{"pass": true/false, "definition_alignment": true/false, "specific": true/false, "prioritized": true/false, "consistent": true/false, "notes": "one sentence"}}

--- BEGIN PRD ---
{content}
--- END PRD ---
"""


def find_cases():
    cases = []
    if os.path.isdir(OUTPUTS_DIR):
        for name in sorted(os.listdir(OUTPUTS_DIR)):
            path = os.path.join(OUTPUTS_DIR, name, "prd.md")
            if os.path.isfile(path):
                cases.append((name, path))
    return cases


def parse_sections(content):
    """Return list of (level, title, body) for each markdown heading.

    A section's body runs until the next heading of the same or higher
    level, so nested subsections (e.g. '### Out of Scope' under '## Scope')
    are captured both inside the parent and as their own section.
    """
    matches = list(HEADING_RE.finditer(content))
    sections = []
    for i, m in enumerate(matches):
        level = len(m.group(1))
        end = len(content)
        for m2 in matches[i + 1:]:
            if len(m2.group(1)) <= level:
                end = m2.start()
                break
        sections.append((level, m.group(2).strip(), content[m.end():end]))
    return sections


def normalize_title(title):
    return re.sub(r"\s+", " ", re.sub(r"[*_`#]", "", title)).strip().lower()


def find_required_sections(sections):
    """Map each required key -> list of section indexes satisfying it."""
    found = {}
    for key, _name, groups in REQUIRED_SECTIONS:
        hits = []
        for group in groups:
            match = None
            for i, (_level, title, _body) in enumerate(sections):
                t = normalize_title(title)
                if any(re.search(p, t) for p in group):
                    match = i
                    break
            if match is not None and match not in hits:
                hits.append(match)
            elif match is None:
                break
        if len(hits) == len(groups):
            found[key] = hits
    return found


def sentence_count(body):
    """Count sentence-like segments: lines/bullets with >= 3 words."""
    n = 0
    in_fence = False
    for line in body.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        seg = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", line).strip()
        for part in re.split(r"[.!?]", seg):
            if len(part.split()) >= 3:
                n += 1
    return n


def check_required_sections(sections, found):
    missing = [name for key, name, _g in REQUIRED_SECTIONS if key not in found]
    ok = not missing
    detail = ("all 7 required sections present" if ok
              else "missing: " + "; ".join(missing))
    return ok, detail


def check_sections_non_empty(sections, found):
    empty = []
    for key, name, _g in REQUIRED_SECTIONS:
        if key not in found:
            empty.append(name + " (missing)")
            continue
        if not any(sentence_count(sections[i][2]) > 0 for i in found[key]):
            empty.append(name)
    ok = not empty
    detail = ("every required section has >= 1 sentence" if ok
              else "no sentence in: " + "; ".join(empty))
    return ok, detail


def check_out_of_scope_items(sections, found):
    if "out_of_scope" not in found:
        return False, "Out of Scope section missing"
    body = sections[found["out_of_scope"][0]][2]
    items = LIST_ITEM_RE.findall(body)
    n = len(items) if items else sum(
        1 for l in body.splitlines() if l.strip())
    ok = n >= MIN_OUT_OF_SCOPE_ITEMS
    return ok, f"{n} out-of-scope items (need >= {MIN_OUT_OF_SCOPE_ITEMS})"


def write_judge_prompts(cases):
    with open(PROMPTS_FILE, "w") as f:
        for name, path in cases:
            f.write(f"## {name}\n\n")
            f.write(JUDGE_RUBRIC.format(content=open(path).read()))
            f.write("\n\n")
    print(f"Wrote {PROMPTS_FILE}. Have a judge answer each section, then "
          f"save verdicts to judge_verdicts.json as:")
    print('  {"case-name": {"pass": true, "definition_alignment": true, '
          '"specific": true, "prioritized": true, "consistent": true, '
          '"notes": "..."}, ...}')


def run_llm_judge(case_name):
    if not os.path.isfile(VERDICTS_FILE):
        return None, "no judge_verdicts.json (run --write-judge-prompts first)"
    verdicts = json.load(open(VERDICTS_FILE))
    v = verdicts.get(case_name)
    if v is None:
        return None, "no verdict recorded for this case"
    return v["pass"], v.get("notes", "")


def evaluate(path):
    content = open(path).read()
    sections = parse_sections(content)
    found = find_required_sections(sections)
    return {
        "required_sections_present": check_required_sections(sections, found),
        "sections_non_empty": check_sections_non_empty(sections, found),
        "out_of_scope_min_items": check_out_of_scope_items(sections, found),
    }


def main():
    write_prompts = "--write-judge-prompts" in sys.argv
    paths = [a for a in sys.argv[1:] if not a.startswith("--")]
    if paths:
        cases = [(os.path.splitext(os.path.basename(p))[0], p) for p in paths]
    else:
        cases = find_cases()
    if not cases:
        sys.exit(f"No cases found under {OUTPUTS_DIR}/*/prd.md "
                 f"(or pass PRD file paths as arguments)")

    if write_prompts:
        write_judge_prompts(cases)
        return

    results = {}
    for name, path in cases:
        checks = evaluate(path)
        checks["llm_judge_specificity"] = run_llm_judge(name)
        results[name] = checks
        passed = sum(1 for ok, _ in checks.values() if ok)
        skipped = sum(1 for ok, _ in checks.values() if ok is None)
        print(f"\n=== {name} ===")
        for check, (ok, detail) in checks.items():
            mark = "SKIP" if ok is None else ("PASS" if ok else "FAIL")
            print(f"  [{mark}] {check}: {detail}")
        print(f"  -> {passed}/{len(checks)} checks passed"
              + (f" ({skipped} skipped)" if skipped else ""))

    n_pass = sum(1 for c in results.values() if all(ok for ok, _ in c.values()))
    print(f"\nSummary: {n_pass}/{len(results)} cases fully passed")

    out = os.path.join(HERE, "eval_results_prd.json")
    with open(out, "w") as f:
        json.dump({k: {c: {"pass": ok, "detail": d} for c, (ok, d) in v.items()}
                   for k, v in results.items()}, f, indent=2)
    print(f"Machine-readable results written to {out}")


if __name__ == "__main__":
    main()
