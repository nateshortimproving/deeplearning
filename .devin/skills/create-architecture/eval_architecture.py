#!/usr/bin/env python3
"""
Evaluation script for the create-architecture skill.

Reads each architecture markdown output and applies the EC from
eval-criteria.md:

DETERMINISTIC CHECKS (pure Python, no model call):
  1. required_sections_present - Overview, Components, Data Flow,
       Key Technical Decisions, and Constraints headings all exist and
       are non-empty (EC 1). Headings are matched case-insensitively
       against aliases.
  2. components_min_3          - at least three components defined, each
       with a Responsibility entry (EC 2). Components are detected as
       subheadings inside the Components section; if none are found,
       top-level list items are treated as components.
  3. decisions_table_min_2     - the Key Technical Decisions section
       contains a markdown table with at least two data rows, each row
       having at least three non-empty cells (Decision, Choice,
       Rationale) (EC 3).
  4. constraints_min_2         - the Constraints section lists at least
       two items (EC 4).
  5. no_orphan_components      - every named component appears in the
       Data Flow section text (EC 5).

LLM JUDGE CHECK (qualitative EC from eval-criteria.md):
  6. llm_judge_specificity     - a model grades whether each section's
       content aligns with the [Definitions], is specific (real
       technologies, not vague filler), decisions carry real tradeoff
       rationale, the design is internally consistent, and it traces
       back to the source requirements.
       The script reads verdicts from judge_verdicts.json so the judge
       can be any model (or Devin acting as the judge). Run with
       --write-judge-prompts to generate the prompts file for a judge
       to fill in.

Usage:
  python3 eval_architecture.py                            # eval all cases in outputs/*/architecture.md
  python3 eval_architecture.py path/to/arch.md [...]      # eval specific files
  python3 eval_architecture.py --write-judge-prompts      # emit judge_prompts.md
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
RESPONSIBILITY_RE = re.compile(r"responsibilit", re.I)
TABLE_SEP_RE = re.compile(r"^\s*\|?[\s:|-]*-[\s:|-]*\|?\s*$")

MIN_COMPONENTS = 3
MIN_DECISION_ROWS = 2
MIN_CONSTRAINT_ITEMS = 2

# Each entry: (key, display name, [keyword groups]). Every keyword group
# must match at least one heading title; a group is a list of alternative
# patterns.
REQUIRED_SECTIONS = [
    ("overview", "Overview",
     [[r"overview", r"summary", r"introduction"]]),
    ("components", "Components",
     [[r"component"]]),
    ("data_flow", "Data Flow",
     [[r"data[ -]?flow", r"flow of data"]]),
    ("decisions", "Key Technical Decisions",
     [[r"technical decision", r"key decision", r"decision"]]),
    ("constraints", "Constraints",
     [[r"constraint", r"limitation", r"non-functional"]]),
]

# Generic words that don't distinguish a component name when doing the
# orphan-component text match.
NAME_STOPWORDS = {
    "service", "component", "system", "layer", "module", "manager",
    "handler", "engine", "the", "and", "for",
}

JUDGE_RUBRIC = """You are grading output from a "create-architecture" skill that writes a
system architecture document (typically produced from a PRD).

Section definitions (from eval-criteria.md):
- Overview: 1-2 paragraph summary of the architectural approach - the "why" of the design.
- Components: Named units of the system, each with Responsibility, Interfaces, and Dependencies.
- Data Flow: How data moves through the system between components.
- Key Technical Decisions: Significant technology/design choices, each with the chosen option and rationale.
- Constraints: Technical and non-functional limits the design must respect.

Grade the architecture document below against these criteria:
1. DEFINITION ALIGNMENT: each section's content matches its definition above.
2. SPECIFICITY: content is concrete - real technologies, named components,
   specific interfaces (e.g., "Postgres 16", "REST + webhooks") - not vague
   filler like "a database" or "some service".
3. RATIONALE QUALITY: each Key Technical Decision's rationale states a real
   tradeoff or constraint, not a restatement of the choice.
4. CONSISTENCY: the interfaces/dependencies declared in Components agree
   with what the Data Flow describes; no contradictions.
5. TRACEABILITY: the design plausibly covers the requirements an architect
   would be asked to address; no major concern (data model, failure
   handling, scaling) is silently skipped.

Respond with exactly this JSON on one line:
{{"pass": true/false, "definition_alignment": true/false, "specific": true/false, "rationale_quality": true/false, "consistent": true/false, "traceable": true/false, "notes": "one sentence"}}

--- BEGIN architecture document ---
{content}
--- END architecture document ---
"""


def find_cases():
    cases = []
    if os.path.isdir(OUTPUTS_DIR):
        for name in sorted(os.listdir(OUTPUTS_DIR)):
            path = os.path.join(OUTPUTS_DIR, name, "architecture.md")
            if os.path.isfile(path):
                cases.append((name, path))
    return cases


def parse_sections(content):
    """Return list of (level, title, body) for each markdown heading.

    A section's body runs until the next heading of the same or higher
    level, so nested subsections (e.g. '### Component A' under
    '## Components') are captured inside the parent's body.
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


def normalize_text(text):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", text.lower())).strip()


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


def find_component_blocks(components_body):
    """Return list of (name, block_body) for each component.

    Prefers subheadings inside the Components section; falls back to
    top-level list items when no subheadings exist.
    """
    matches = list(HEADING_RE.finditer(components_body))
    if matches:
        blocks = []
        for i, m in enumerate(matches):
            end = (matches[i + 1].start() if i + 1 < len(matches)
                   else len(components_body))
            blocks.append((m.group(2).strip(),
                           components_body[m.end():end]))
        return blocks
    blocks = []
    for m in re.finditer(r"^\s*(?:[-*+]|\d+[.)])\s+(.*)$",
                         components_body, re.M):
        text = m.group(1).strip()
        name = component_name_from_item(text)
        if name:
            blocks.append((name, text))
    return blocks


def component_name_from_item(text):
    """Extract a component name from a list item like '**API** - does X'
    or 'Auth service: handles login'."""
    m = re.match(r"\*\*(.+?)\*\*", text)
    if m:
        return m.group(1).strip()
    head = re.split(r"\s[:—–-]\s", text)[0].strip()
    return " ".join(head.split()[:5])


def check_required_sections(sections, found):
    problems = [name for key, name, _g in REQUIRED_SECTIONS
                if key not in found]
    empty = [name for key, name, _g in REQUIRED_SECTIONS
             if key in found and
             not any(sentence_count(sections[i][2]) > 0 for i in found[key])]
    ok = not problems and not empty
    parts = []
    if problems:
        parts.append("missing: " + "; ".join(problems))
    if empty:
        parts.append("empty: " + "; ".join(empty))
    detail = ("all 5 required sections present and non-empty" if ok
              else " | ".join(parts))
    return ok, detail


def check_components(sections, found):
    if "components" not in found:
        return False, "Components section missing"
    body = sections[found["components"][0]][2]
    blocks = find_component_blocks(body)
    no_resp = [name for name, b in blocks if not RESPONSIBILITY_RE.search(b)]
    n = len(blocks)
    if n < MIN_COMPONENTS:
        return False, f"{n} components found (need >= {MIN_COMPONENTS})"
    if no_resp:
        return False, ("components missing a Responsibility entry: "
                       + "; ".join(no_resp))
    return True, f"{n} components, each with a Responsibility entry"


def check_decisions_table(sections, found):
    if "decisions" not in found:
        return False, "Key Technical Decisions section missing"
    body = sections[found["decisions"][0]][2]
    lines = body.splitlines()
    sep_idx = next((i for i, l in enumerate(lines)
                    if TABLE_SEP_RE.match(l) and "|" in l), None)
    if sep_idx is None:
        return False, "no markdown table found in Key Technical Decisions"
    valid = 0
    for line in lines[sep_idx + 1:]:
        if "|" not in line:
            break
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if sum(1 for c in cells if c) >= 3:
            valid += 1
    ok = valid >= MIN_DECISION_ROWS
    return ok, (f"{valid} decision rows with >= 3 filled cells "
                f"(need >= {MIN_DECISION_ROWS})")


def check_constraints_items(sections, found):
    if "constraints" not in found:
        return False, "Constraints section missing"
    body = sections[found["constraints"][0]][2]
    items = LIST_ITEM_RE.findall(body)
    n = len(items) if items else sum(
        1 for l in body.splitlines() if l.strip())
    ok = n >= MIN_CONSTRAINT_ITEMS
    return ok, f"{n} constraint items (need >= {MIN_CONSTRAINT_ITEMS})"


def name_in_text(name, text_norm):
    n = normalize_text(name)
    if not n:
        return False
    if n in text_norm:
        return True
    words = [w for w in n.split()
             if len(w) >= 3 and w not in NAME_STOPWORDS]
    return bool(words) and all(w in text_norm for w in words)


def check_orphan_components(sections, found):
    if "components" not in found:
        return False, "Components section missing"
    if "data_flow" not in found:
        return False, "Data Flow section missing"
    comp_body = sections[found["components"][0]][2]
    blocks = find_component_blocks(comp_body)
    if not blocks:
        return False, "no components to check"
    flow_norm = normalize_text(sections[found["data_flow"][0]][2])
    orphans = [name for name, _b in blocks
               if not name_in_text(name, flow_norm)]
    ok = not orphans
    return ok, ("all components referenced in Data Flow" if ok
                else "not found in Data Flow: " + "; ".join(orphans))


def write_judge_prompts(cases):
    with open(PROMPTS_FILE, "w") as f:
        for name, path in cases:
            f.write(f"## {name}\n\n")
            f.write(JUDGE_RUBRIC.format(content=open(path).read()))
            f.write("\n\n")
    print(f"Wrote {PROMPTS_FILE}. Have a judge answer each section, then "
          f"save verdicts to judge_verdicts.json as:")
    print('  {"case-name": {"pass": true, "definition_alignment": true, '
          '"specific": true, "rationale_quality": true, "consistent": true, '
          '"traceable": true, "notes": "..."}, ...}')


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
        "components_min_3": check_components(sections, found),
        "decisions_table_min_2": check_decisions_table(sections, found),
        "constraints_min_2": check_constraints_items(sections, found),
        "no_orphan_components": check_orphan_components(sections, found),
    }


def main():
    write_prompts = "--write-judge-prompts" in sys.argv
    paths = [a for a in sys.argv[1:] if not a.startswith("--")]
    if paths:
        cases = [(os.path.splitext(os.path.basename(p))[0], p) for p in paths]
    else:
        cases = find_cases()
    if not cases:
        sys.exit(f"No cases found under {OUTPUTS_DIR}/*/architecture.md "
                 f"(or pass architecture file paths as arguments)")

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

    out = os.path.join(HERE, "eval_results_architecture.json")
    with open(out, "w") as f:
        json.dump({k: {c: {"pass": ok, "detail": d} for c, (ok, d) in v.items()}
                   for k, v in results.items()}, f, indent=2)
    print(f"Machine-readable results written to {out}")


if __name__ == "__main__":
    main()
