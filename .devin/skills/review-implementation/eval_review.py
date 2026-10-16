#!/usr/bin/env python3
"""
Evaluation script for the review-implementation skill.

Reads each review.yaml output (or a SKILL.md containing a fenced
```yaml template) and applies the EC from eval-criteria.md:

DETERMINISTIC CHECKS (pure Python, no model call, line-based YAML scan):
  1. review_header          - review_id, story_id, reviewed_at, verdict,
       issues, ac_assessment, summary all present (EC 1)
  2. verdict_valid          - verdict is passed | failed |
       changes_requested (EC 2)
  3. issues_well_formed     - every issue has severity, category,
       description, recommendation, ac_ref; severity and category are
       in their allowed enums (EC 3)
  4. ac_assessment_valid    - at least one ac_assessment entry with
       ac_id, status (satisfied | not_satisfied |
       partially_satisfied), notes (EC 4)
  5. verdict_consistent     - "passed" requires all AC statuses
       satisfied; non-passed requires at least one non-satisfied AC or
       one issue (EC 5)

LLM JUDGE CHECK (qualitative EC from eval-criteria.md):
  6. llm_judge_specificity  - a model grades whether issues are
       actionable with real severity and AC refs, the verdict matches
       the evidence, and the summary is honest. Reads verdicts from
       judge_verdicts.json; run with --write-judge-prompts to emit
       judge_prompts.md.

Usage:
  python3 eval_review.py                            # eval all cases in outputs/*/review.yaml
  python3 eval_review.py path/to/file [...]         # eval specific files (yaml or SKILL.md)
  python3 eval_review.py --write-judge-prompts      # emit judge_prompts.md
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUTS_DIR = os.path.join(HERE, "outputs")
VERDICTS_FILE = os.path.join(HERE, "judge_verdicts.json")
PROMPTS_FILE = os.path.join(HERE, "judge_prompts.md")

YAML_FENCE_RE = re.compile(r"```ya?ml\s*\n(.*?)```", re.S)

HEADER_FIELDS = ["review_id", "story_id", "reviewed_at", "verdict",
                 "issues", "ac_assessment", "summary"]
ISSUE_FIELDS = ["severity", "category", "description",
                "recommendation", "ac_ref"]
AC_FIELDS = ["ac_id", "status", "notes"]

VERDICTS = {"passed", "failed", "changes_requested"}
SEVERITIES = {"blocker", "major", "minor", "nit"}
CATEGORIES = {"correctness", "edge_case", "readability",
              "test_coverage", "ac_violation"}
STATUSES = {"satisfied", "not_satisfied", "partially_satisfied"}

JUDGE_RUBRIC = """You are grading output from a "review-implementation" skill that reviews
an implementation against a story's acceptance criteria (review.yaml).

Grade the review.yaml content below against these criteria:
1. ACTIONABLE ISSUES: each issue names a concrete problem and a specific
   fix - not "looks wrong" or "improve this".
2. HONEST SEVERITY: severities match the real impact (a blocker blocks;
   a nit is cosmetic) and are not inflated or deflated.
3. AC GROUNDING: findings reference real AC ids; the ac_assessment
   covers every AC of the reviewed story.
4. VERDICT HONESTY: the verdict reflects the evidence - a "passed" with
   open issues or a "failed" on clean code are both wrong.
5. SUMMARY QUALITY: the summary captures the true state in 2-3 sentences
   without spin.
6. SPECIFICITY: content is concrete - real AC ids, real failure modes -
   not placeholder or boilerplate.

Respond with exactly this JSON on one line:
{{"pass": true/false, "actionable": true/false, "honest_severity": true/false, "ac_grounded": true/false, "verdict_honest": true/false, "summary_quality": true/false, "specific": true/false, "notes": "one sentence"}}

--- BEGIN review.yaml ---
{content}
--- END review.yaml ---
"""


def find_cases():
    cases = []
    if os.path.isdir(OUTPUTS_DIR):
        for name in sorted(os.listdir(OUTPUTS_DIR)):
            path = os.path.join(OUTPUTS_DIR, name, "review.yaml")
            if os.path.isfile(path):
                cases.append((name, path))
    return cases


def doc_of(content):
    m = YAML_FENCE_RE.search(content)
    return m.group(1) if m else content


def indent_of(line):
    return len(line) - len(line.lstrip())


def collect_block(lines, start):
    base = indent_of(lines[start])
    out = []
    for l in lines[start + 1:]:
        if l.strip() and indent_of(l) <= base:
            break
        out.append(l)
    return out


def top_key(lines, name):
    for i, l in enumerate(lines):
        if re.match(rf"^{re.escape(name)}\s*:", l):
            return i
    return None


def split_items(block_lines):
    items = [(i, indent_of(l)) for i, l in enumerate(block_lines)
             if re.match(r"^\s*-\s*\S", l)]
    if not items:
        return []
    base = min(ind for _, ind in items)
    idxs = [i for i, ind in items if ind == base]
    chunks = []
    for j, i in enumerate(idxs):
        end = idxs[j + 1] if j + 1 < len(idxs) else len(block_lines)
        chunks.append("\n".join(block_lines[i:end]))
    return chunks


def has_field(text, field):
    return bool(re.search(rf"^\s*-?\s*{re.escape(field)}\s*:", text, re.M))


def field_value(text, field):
    m = re.search(rf"^\s*-?\s*{re.escape(field)}\s*:\s*(.+?)\s*(?:#|$)",
                  text, re.M)
    return m.group(1).strip().strip('"\'') if m else None


def check_header(lines):
    missing = [f for f in HEADER_FIELDS if top_key(lines, f) is None]
    ok = not missing
    return ok, ("all review fields present" if ok
                else "missing: " + ", ".join(missing))


def check_verdict(lines):
    v = field_value("\n".join(lines), "verdict")
    if v is None:
        return False, "no verdict field"
    ok = v in VERDICTS
    return ok, (f"verdict '{v}' is valid" if ok
                else f"verdict '{v}' not in {sorted(VERDICTS)}")


def issue_chunks(lines):
    ii = top_key(lines, "issues")
    if ii is None:
        return []
    return split_items(collect_block(lines, ii))


def ac_chunks(lines):
    ai = top_key(lines, "ac_assessment")
    if ai is None:
        return []
    return split_items(collect_block(lines, ai))


def check_issues(lines):
    chunks = issue_chunks(lines)
    if not chunks:
        return False, "no issues found"
    bad = []
    for c in chunks:
        label = field_value(c, "description") or field_value(c, "ac_ref") \
            or "?"
        label = label[:40]
        missing = [f for f in ISSUE_FIELDS if not has_field(c, f)]
        if missing:
            bad.append(f"{label} (no {', '.join(missing)})")
            continue
        sev = field_value(c, "severity")
        cat = field_value(c, "category")
        if sev and sev not in SEVERITIES:
            bad.append(f"{label} (severity '{sev}')")
        if cat and cat not in CATEGORIES:
            bad.append(f"{label} (category '{cat}')")
    if bad:
        return False, "; ".join(bad)
    return True, f"{len(chunks)} well-formed issues with valid enums"


def check_ac_assessment(lines):
    chunks = ac_chunks(lines)
    if not chunks:
        return False, "no ac_assessment entries"
    bad = []
    for c in chunks:
        label = field_value(c, "ac_id") or "?"
        missing = [f for f in AC_FIELDS if not has_field(c, f)]
        if missing:
            bad.append(f"{label} (no {', '.join(missing)})")
            continue
        st = field_value(c, "status")
        if st and st not in STATUSES:
            bad.append(f"{label} (status '{st}')")
    if bad:
        return False, "; ".join(bad)
    return True, f"{len(chunks)} ac_assessment entries with valid status"


def check_verdict_consistent(lines):
    v = field_value("\n".join(lines), "verdict")
    if v is None:
        return False, "no verdict field"
    statuses = [field_value(c, "status") for c in ac_chunks(lines)]
    n_issues = len(issue_chunks(lines))
    if v == "passed":
        ok = bool(statuses) and all(s == "satisfied" for s in statuses)
        return ok, ("verdict passed and all AC satisfied" if ok
                    else "verdict passed but not all AC satisfied")
    ok = any(s in {"not_satisfied", "partially_satisfied"}
             for s in statuses) or n_issues > 0
    return ok, (f"verdict '{v}' backed by findings" if ok
                else f"verdict '{v}' but no failing AC or issues found")


def write_judge_prompts(cases):
    with open(PROMPTS_FILE, "w") as f:
        for name, path in cases:
            f.write(f"## {name}\n\n")
            f.write(JUDGE_RUBRIC.format(content=doc_of(open(path).read())))
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
    lines = doc_of(open(path).read()).splitlines()
    return {
        "review_header": check_header(lines),
        "verdict_valid": check_verdict(lines),
        "issues_well_formed": check_issues(lines),
        "ac_assessment_valid": check_ac_assessment(lines),
        "verdict_consistent": check_verdict_consistent(lines),
    }


def main():
    write_prompts = "--write-judge-prompts" in sys.argv
    paths = [a for a in sys.argv[1:] if not a.startswith("--")]
    if paths:
        cases = [(os.path.splitext(os.path.basename(p))[0], p) for p in paths]
    else:
        cases = find_cases()
    if not cases:
        sys.exit(f"No cases found under {OUTPUTS_DIR}/*/review.yaml "
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

    out = os.path.join(HERE, "eval_results_review.json")
    with open(out, "w") as f:
        json.dump({k: {c: {"pass": ok, "detail": d} for c, (ok, d) in v.items()}
                   for k, v in results.items()}, f, indent=2)
    print(f"Machine-readable results written to {out}")


if __name__ == "__main__":
    main()
