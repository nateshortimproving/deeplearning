#!/usr/bin/env python3
"""
Evaluation script for the implement-story skill.

Reads each IMPLEMENTATION.md output (or a SKILL.md containing a fenced
implementation-summary template) and applies the EC from
eval-criteria.md:

DETERMINISTIC CHECKS (pure Python, no model call):
  1. summary_sections        - Tasks Implemented, Assumptions,
       Deviations, and Test Files sections all exist and are non-empty
       (or an explicit "None") (EC 5)
  2. task_refs_listed        - the Tasks Implemented section lists at
       least one task identifier (e.g., PANTRY-001-T1) (EC 1)
  3. ac_refs_listed          - the document references at least one
       acceptance criterion id (e.g., PANTRY-001-AC1) (EC 2)
  4. test_files_listed       - the Test Files section lists at least
       one test/spec file path (EC 3)

LLM JUDGE CHECK (qualitative EC from eval-criteria.md):
  5. llm_judge_specificity   - a model grades whether the summary is
       honest and specific (real deviations explained, real
       assumptions), traceable to plan tasks and AC, aligned with the
       declared architecture (EC 4), and free of scope creep (EC 6).
       Reads verdicts from judge_verdicts.json; run with
       --write-judge-prompts to emit judge_prompts.md.

Usage:
  python3 eval_implementation.py                            # eval all cases in outputs/*/IMPLEMENTATION.md
  python3 eval_implementation.py path/to/file [...]         # eval specific files (md or SKILL.md)
  python3 eval_implementation.py --write-judge-prompts      # emit judge_prompts.md
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
TASK_ID_RE = re.compile(r"\b[A-Z]{2,}-\d+-T\d+\b")
AC_ID_RE = re.compile(r"\b[A-Z]{2,}-\d+-AC\d+\b")
TEST_FILE_RE = re.compile(
    r"[\w./-]+\.(?:test|spec)\.[a-z]+|tests?/[\w./-]+|[\w./-]+_test\.[a-z]+",
    re.I)
NONE_RE = re.compile(r"\bnone\b|\bn/?a\b|\bnothing\b", re.I)

REQUIRED_SUMMARY = [
    ("tasks", "Tasks Implemented", [[r"task"]]),
    ("assumptions", "Assumptions", [[r"assumption"]]),
    ("deviations", "Deviations", [[r"deviation", r"change", r"differ"]]),
    ("test_files", "Test Files", [[r"test"]]),
]

JUDGE_RUBRIC = """You are grading output from an "implement-story" skill that implements a
user story from a plan and writes an IMPLEMENTATION.md summary.

Grade the implementation summary below against these criteria:
1. TRACEABILITY: every task claimed maps to a plan task id, and the AC it
   satisfies are named - a reviewer can verify coverage without guessing.
2. HONEST DEVIATIONS: deviations (if any) explain WHAT changed and WHY;
   assumptions state real decisions made, not filler.
3. TEST ADEQUACY: listed tests plausibly exercise the referenced AC -
   positive, negative, and edge paths are covered or gaps are admitted.
4. ARCHITECTURE ALIGNMENT: the described implementation fits the declared
   stack (Fastify/Prisma/TypeScript backend, React/hooks frontend) -
   nothing contradicts it.
5. SCOPE DISCIPLINE: nothing is claimed beyond the plan's task and AC
   references.
6. SPECIFICITY: content is concrete - real file paths, real reasons -
   not placeholder or boilerplate.

Respond with exactly this JSON on one line:
{{"pass": true/false, "traceable": true/false, "honest_deviations": true/false, "tests_adequate": true/false, "arch_aligned": true/false, "in_scope": true/false, "specific": true/false, "notes": "one sentence"}}

--- BEGIN implementation summary ---
{content}
--- END implementation summary ---
"""


def find_cases():
    cases = []
    if os.path.isdir(OUTPUTS_DIR):
        for name in sorted(os.listdir(OUTPUTS_DIR)):
            path = os.path.join(OUTPUTS_DIR, name, "IMPLEMENTATION.md")
            if os.path.isfile(path):
                cases.append((name, path))
    return cases


def parse_sections(content):
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


def find_summary_sections(sections):
    found = {}
    for key, _name, groups in REQUIRED_SUMMARY:
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


def body_has_content(body):
    """Non-empty section: a list item, a sentence, or an explicit None."""
    if NONE_RE.search(body):
        return True
    for line in body.splitlines():
        seg = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", line).strip()
        if len(seg.split()) >= 2:
            return True
    return False


def check_summary_sections(sections, found):
    missing = [name for key, name, _g in REQUIRED_SUMMARY
               if key not in found]
    empty = [name for key, name, _g in REQUIRED_SUMMARY
             if key in found and
             not any(body_has_content(sections[i][2]) for i in found[key])]
    ok = not missing and not empty
    parts = []
    if missing:
        parts.append("missing: " + "; ".join(missing))
    if empty:
        parts.append("empty: " + "; ".join(empty))
    return ok, ("all 4 summary sections present with content" if ok
                else " | ".join(parts))


def section_body(sections, found, key):
    if key not in found:
        return ""
    return "\n".join(sections[i][2] for i in found[key])


def check_task_refs(sections, found):
    body = section_body(sections, found, "tasks")
    if not body:
        return False, "Tasks Implemented section missing"
    ids = TASK_ID_RE.findall(body)
    items = [l for l in body.splitlines() if l.strip()]
    if ids:
        return True, f"{len(ids)} task ids listed ({', '.join(ids)})"
    if items:
        return True, f"{len(items)} task entries listed (no id pattern)"
    return False, "no tasks listed in Tasks Implemented"


def check_ac_refs(sections, found):
    doc = "\n".join(b for _l, _t, b in sections)
    ids = AC_ID_RE.findall(doc)
    ok = bool(ids)
    return ok, (f"{len(ids)} AC ids referenced ({', '.join(ids)})" if ok
                else "no AC identifiers referenced")


def check_test_files(sections, found):
    body = section_body(sections, found, "test_files")
    if not body:
        return False, "Test Files section missing"
    files = TEST_FILE_RE.findall(body)
    ok = bool(files)
    return ok, (f"{len(files)} test file(s) listed" if ok
                else "no test file paths listed")


def write_judge_prompts(cases):
    with open(PROMPTS_FILE, "w") as f:
        for name, path in cases:
            f.write(f"## {name}\n\n")
            f.write(JUDGE_RUBRIC.format(content=open(path).read()))
            f.write("\n\n")
    print(f"Wrote {PROMPTS_FILE}. Have a judge answer each section, then "
          f"save verdicts to judge_verdicts.json")


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
    found = find_summary_sections(sections)
    return {
        "summary_sections": check_summary_sections(sections, found),
        "task_refs_listed": check_task_refs(sections, found),
        "ac_refs_listed": check_ac_refs(sections, found),
        "test_files_listed": check_test_files(sections, found),
    }


def main():
    write_prompts = "--write-judge-prompts" in sys.argv
    paths = [a for a in sys.argv[1:] if not a.startswith("--")]
    if paths:
        cases = [(os.path.splitext(os.path.basename(p))[0], p) for p in paths]
    else:
        cases = find_cases()
    if not cases:
        sys.exit(f"No cases found under {OUTPUTS_DIR}/*/IMPLEMENTATION.md "
                 f"(or pass file paths as arguments)")

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

    out = os.path.join(HERE, "eval_results_implementation.json")
    with open(out, "w") as f:
        json.dump({k: {c: {"pass": ok, "detail": d} for c, (ok, d) in v.items()}
                   for k, v in results.items()}, f, indent=2)
    print(f"Machine-readable results written to {out}")


if __name__ == "__main__":
    main()
