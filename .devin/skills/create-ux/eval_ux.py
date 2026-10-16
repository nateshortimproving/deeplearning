#!/usr/bin/env python3
"""
Evaluation script for the create-ux skill.

Reads each UX guidance markdown output and applies the EC from
eval-criteria.md:

DETERMINISTIC CHECKS (pure Python, no model call):
  1. required_sections_present - User Personas, User Flows, Key
       Interactions, Design Considerations, and Error States headings
       all exist and are non-empty (EC 1). Headings are matched
       case-insensitively against aliases.
  2. personas_min_2            - at least two personas, each with Role,
       Goals, and Pain Points entries (EC 2). Personas are detected as
       subheadings inside User Personas; if none are found, top-level
       list items are treated as personas.
  3. flows_min_2               - at least two user flows, each with at
       least three numbered steps plus a Decision Point and an Error
       Risk entry (EC 3). Flows are detected as subheadings inside
       User Flows.
  4. error_table_min_2         - the Error States section contains a
       markdown table with at least two data rows, each with at least
       three non-empty cells (Scenario, User Sees, Recovery Action)
       (EC 4).
  5. design_covers_a11y_responsive - the Design Considerations section
       addresses both accessibility (accessib*, a11y, WCAG, screen
       reader, keyboard) and responsiveness (responsiv*, mobile,
       tablet, breakpoint, screen size, touch) (EC 5).

LLM JUDGE CHECK (qualitative EC from eval-criteria.md):
  6. llm_judge_specificity     - a model grades whether each section's
       content aligns with the [Definitions], flows and error states
       are plausible for THIS feature, personas trace to the source
       audience, decision points are real choices, and both happy and
       failure paths are covered.
       The script reads verdicts from judge_verdicts.json so the judge
       can be any model (or Devin acting as the judge). Run with
       --write-judge-prompts to generate the prompts file for a judge
       to fill in.

Usage:
  python3 eval_ux.py                            # eval all cases in outputs/*/ux.md
  python3 eval_ux.py path/to/ux.md [...]        # eval specific files
  python3 eval_ux.py --write-judge-prompts      # emit judge_prompts.md
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUTS_DIR = os.path.join(HERE, "outputs")
VERDICTS_FILE = os.path.join(HERE, "judge_verdicts.json")
PROMPTS_FILE = os.path.join(HERE, "judge_prompts.md")

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$", re.M)
LIST_ITEM_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+\S", re.M)
NUMBERED_STEP_RE = re.compile(r"^\s*\d+[.)]\s+\S", re.M)
TABLE_SEP_RE = re.compile(r"^\s*\|?[\s:|-]*-[\s:|-]*\|?\s*$")

DECISION_POINT_RE = re.compile(r"decision\s*point", re.I)
ERROR_RISK_RE = re.compile(r"error\s*risk", re.I)
ROLE_RE = re.compile(r"\brole\b", re.I)
GOALS_RE = re.compile(r"goal", re.I)
PAIN_RE = re.compile(r"pain", re.I)

A11Y_RE = re.compile(
    r"accessib|a11y|wcag|screen\s*reader|keyboard|contrast|alt\s*text",
    re.I)
RESPONSIVE_RE = re.compile(
    r"responsiv|mobile|tablet|breakpoint|screen\s*size|touch|viewport",
    re.I)

MIN_PERSONAS = 2
MIN_FLOWS = 2
MIN_FLOW_STEPS = 3
MIN_ERROR_ROWS = 2

REQUIRED_SECTIONS = [
    ("personas", "User Personas",
     [[r"persona", r"user role", r"audience"]]),
    ("flows", "User Flows",
     [[r"user flow", r"flow"]]),
    ("interactions", "Key Interactions",
     [[r"interaction"]]),
    ("design_considerations", "Design Considerations",
     [[r"design consideration", r"consideration", r"usability"]]),
    ("error_states", "Error States",
     [[r"error state", r"error", r"edge case", r"failure"]]),
]

JUDGE_RUBRIC = """You are grading output from a "create-ux" skill that writes a UX guidance
document (typically produced from a PRD and architecture document).

Section definitions (from eval-criteria.md):
- User Personas: Who uses the feature - their role, goals, and pain points.
- User Flows: Step-by-step user/system interactions, each with a decision point and error risk.
- Key Interactions: Important UI patterns and their expected behavior.
- Design Considerations: Accessibility, responsiveness, and usability requirements.
- Error States: What can go wrong, what the user sees, and how they recover.

Grade the UX document below against these criteria:
1. DEFINITION ALIGNMENT: each section's content matches its definition above.
2. PLAUSIBILITY: flows are realistic for THIS feature - concrete sequential
   steps a user and system would actually exchange - not generic
   "log in -> click -> done" filler.
3. ERROR REALISM: error-state scenarios are ones this feature genuinely
   produces (e.g., sync conflicts, invalid scans, offline failures) - not
   boilerplate ("404", "server error").
4. PERSONA TRACEABILITY: personas plausibly come from the source PRD's
   target audience, not invented users.
5. DECISION QUALITY: each flow's Decision Point is a real user choice,
   not just another step; and both happy and failure/alternate paths are
   represented across the flows.
6. SPECIFICITY: interactions describe concrete expected behavior
   ("undo toast for 5s"), not vague phrases ("intuitive controls").

Respond with exactly this JSON on one line:
{{"pass": true/false, "definition_alignment": true/false, "plausible_flows": true/false, "realistic_errors": true/false, "persona_traceable": true/false, "real_decisions": true/false, "specific": true/false, "notes": "one sentence"}}

--- BEGIN ux document ---
{content}
--- END ux document ---
"""


def find_cases():
    cases = []
    if os.path.isdir(OUTPUTS_DIR):
        for name in sorted(os.listdir(OUTPUTS_DIR)):
            path = os.path.join(OUTPUTS_DIR, name, "ux.md")
            if os.path.isfile(path):
                cases.append((name, path))
    return cases


def parse_sections(content):
    """Return list of (level, title, body) for each markdown heading."""
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


def find_subblocks(section_body):
    """Return list of (name, block_body) for ### subsections inside a
    section body; falls back to top-level list items."""
    matches = list(HEADING_RE.finditer(section_body))
    if matches:
        blocks = []
        for i, m in enumerate(matches):
            end = (matches[i + 1].start() if i + 1 < len(matches)
                   else len(section_body))
            blocks.append((m.group(2).strip(),
                           section_body[m.end():end]))
        return blocks
    return [(m.group(1).strip()[:60], m.group(1).strip())
            for m in re.finditer(r"^\s*(?:[-*+]|\d+[.)])\s+(.*)$",
                                 section_body, re.M)]


def check_required_sections(sections, found):
    missing = [name for key, name, _g in REQUIRED_SECTIONS
               if key not in found]
    empty = [name for key, name, _g in REQUIRED_SECTIONS
             if key in found and
             not any(sentence_count(sections[i][2]) > 0 for i in found[key])]
    ok = not missing and not empty
    parts = []
    if missing:
        parts.append("missing: " + "; ".join(missing))
    if empty:
        parts.append("empty: " + "; ".join(empty))
    detail = ("all 5 required sections present and non-empty" if ok
              else " | ".join(parts))
    return ok, detail


def check_personas(sections, found):
    if "personas" not in found:
        return False, "User Personas section missing"
    body = sections[found["personas"][0]][2]
    blocks = find_subblocks(body)
    n = len(blocks)
    if n < MIN_PERSONAS:
        return False, f"{n} personas found (need >= {MIN_PERSONAS})"
    incomplete = []
    for name, b in blocks:
        missing = []
        if not ROLE_RE.search(b):
            missing.append("Role")
        if not GOALS_RE.search(b):
            missing.append("Goals")
        if not PAIN_RE.search(b):
            missing.append("Pain Points")
        if missing:
            incomplete.append(f"{name} (no {', '.join(missing)})")
    if incomplete:
        return False, "incomplete personas: " + "; ".join(incomplete)
    return True, f"{n} personas, each with Role/Goals/Pain Points"


def check_flows(sections, found):
    if "flows" not in found:
        return False, "User Flows section missing"
    body = sections[found["flows"][0]][2]
    blocks = find_subblocks(body)
    n = len(blocks)
    if n < MIN_FLOWS:
        return False, f"{n} flows found (need >= {MIN_FLOWS})"
    bad = []
    for name, b in blocks:
        steps = len(NUMBERED_STEP_RE.findall(b))
        issues = []
        if steps < MIN_FLOW_STEPS:
            issues.append(f"{steps} steps")
        if not DECISION_POINT_RE.search(b):
            issues.append("no Decision Point")
        if not ERROR_RISK_RE.search(b):
            issues.append("no Error Risk")
        if issues:
            bad.append(f"{name} ({', '.join(issues)})")
    if bad:
        return False, "flows incomplete: " + "; ".join(bad)
    return True, (f"{n} flows, each with >= {MIN_FLOW_STEPS} steps, "
                  f"Decision Point, and Error Risk")


def check_error_table(sections, found):
    if "error_states" not in found:
        return False, "Error States section missing"
    body = sections[found["error_states"][0]][2]
    lines = body.splitlines()
    sep_idx = next((i for i, l in enumerate(lines)
                    if TABLE_SEP_RE.match(l) and "|" in l), None)
    if sep_idx is None:
        return False, "no markdown table found in Error States"
    valid = 0
    for line in lines[sep_idx + 1:]:
        if "|" not in line:
            break
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if sum(1 for c in cells if c) >= 3:
            valid += 1
    ok = valid >= MIN_ERROR_ROWS
    return ok, (f"{valid} error-state rows with >= 3 filled cells "
                f"(need >= {MIN_ERROR_ROWS})")


def check_design_coverage(sections, found):
    if "design_considerations" not in found:
        return False, "Design Considerations section missing"
    body = sections[found["design_considerations"][0]][2]
    has_a11y = bool(A11Y_RE.search(body))
    has_resp = bool(RESPONSIVE_RE.search(body))
    ok = has_a11y and has_resp
    detail = ("covers accessibility and responsiveness" if ok
              else "missing: "
              + ", ".join(x for x, ok2 in
                          [("accessibility", has_a11y),
                           ("responsiveness", has_resp)] if not ok2))
    return ok, detail


def write_judge_prompts(cases):
    with open(PROMPTS_FILE, "w") as f:
        for name, path in cases:
            f.write(f"## {name}\n\n")
            f.write(JUDGE_RUBRIC.format(content=open(path).read()))
            f.write("\n\n")
    print(f"Wrote {PROMPTS_FILE}. Have a judge answer each section, then "
          f"save verdicts to judge_verdicts.json as:")
    print('  {"case-name": {"pass": true, "definition_alignment": true, '
          '"plausible_flows": true, "realistic_errors": true, '
          '"persona_traceable": true, "real_decisions": true, '
          '"specific": true, "notes": "..."}, ...}')


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
        "personas_min_2": check_personas(sections, found),
        "flows_min_2": check_flows(sections, found),
        "error_table_min_2": check_error_table(sections, found),
        "design_covers_a11y_responsive": check_design_coverage(sections, found),
    }


def main():
    write_prompts = "--write-judge-prompts" in sys.argv
    paths = [a for a in sys.argv[1:] if not a.startswith("--")]
    if paths:
        cases = [(os.path.splitext(os.path.basename(p))[0], p) for p in paths]
    else:
        cases = find_cases()
    if not cases:
        sys.exit(f"No cases found under {OUTPUTS_DIR}/*/ux.md "
                 f"(or pass UX file paths as arguments)")

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

    out = os.path.join(HERE, "eval_results_ux.json")
    with open(out, "w") as f:
        json.dump({k: {c: {"pass": ok, "detail": d} for c, (ok, d) in v.items()}
                   for k, v in results.items()}, f, indent=2)
    print(f"Machine-readable results written to {out}")


if __name__ == "__main__":
    main()
