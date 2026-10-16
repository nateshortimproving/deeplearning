#!/usr/bin/env python3
"""
Evaluation script for the plan-story skill.

Reads each plan.yaml output (or a SKILL.md containing a fenced
```yaml template) and applies the EC from eval-criteria.md:

DETERMINISTIC CHECKS (pure Python, no model call, line-based YAML scan):
  1. plan_header            - story_id, plan_version, source_story
       (with title + user_story), tasks, assumptions, open_questions
       all present (EC 1)
  2. tasks_min_2            - at least two tasks, each with id,
       description, dependencies, files_affected, risks,
       acceptance_criteria_refs (EC 2)
  3. refs_and_files_nonempty - every task's acceptance_criteria_refs
       and files_affected lists are non-empty (EC 3)
  4. deps_backward_only     - task dependencies reference only task ids
       that appear earlier in the list (EC 4)
  5. risk_per_task          - every task lists at least one risk or an
       explicit "none" entry (EC 5)

LLM JUDGE CHECK (qualitative EC from eval-criteria.md):
  6. llm_judge_specificity  - a model grades task granularity, real
       dependency ordering, AC coverage, and whether risks/open
       questions are honest. Reads verdicts from judge_verdicts.json;
       run with --write-judge-prompts to emit judge_prompts.md.

Usage:
  python3 eval_plan.py                            # eval all cases in outputs/*/plan.yaml
  python3 eval_plan.py path/to/file [...]         # eval specific files (yaml or SKILL.md)
  python3 eval_plan.py --write-judge-prompts      # emit judge_prompts.md
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
MIN_TASKS = 2

HEADER_FIELDS = ["story_id", "plan_version", "source_story",
                 "tasks", "assumptions", "open_questions"]
SOURCE_STORY_FIELDS = ["title", "user_story"]
TASK_FIELDS = ["id", "description", "dependencies", "files_affected",
               "risks", "acceptance_criteria_refs"]

JUDGE_RUBRIC = """You are grading output from a "plan-story" skill that turns a user story
into an implementation plan (plan.yaml).

Grade the plan.yaml content below against these criteria:
1. TASK GRANULARITY: each task is small enough to complete in a single
   session (~1-2 hours) - not "build the whole feature".
2. DEPENDENCY SANITY: task ordering reflects real dependencies; nothing
   depends on later work.
3. AC COVERAGE: every acceptance criterion from the source story is
   claimed by at least one task; no task is decoupled from all AC.
4. REAL RISKS: risks are plausible unknowns for this work, not filler
   ("things could go wrong").
5. HONEST UNKNOWNS: assumptions and open_questions state real unknowns
   or are explicitly empty - not invented certainty.
6. SPECIFICITY: descriptions are verb-first and concrete; files_affected
   names plausible paths.

Respond with exactly this JSON on one line:
{{"pass": true/false, "granular": true/false, "deps_sane": true/false, "ac_covered": true/false, "real_risks": true/false, "honest_unknowns": true/false, "specific": true/false, "notes": "one sentence"}}

--- BEGIN plan.yaml ---
{content}
--- END plan.yaml ---
"""


def find_cases():
    cases = []
    if os.path.isdir(OUTPUTS_DIR):
        for name in sorted(os.listdir(OUTPUTS_DIR)):
            path = os.path.join(OUTPUTS_DIR, name, "plan.yaml")
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
             if re.match(r"^\s*-\s*\S+\s*:", l) or
             re.match(r"^\s*-\s+\S", l)]
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


def list_values(text, field):
    """Return list item values for 'field: [a, b]' or a block list."""
    m = re.search(rf"^\s*-?\s*{re.escape(field)}\s*:\s*\[([^\]]*)\]",
                  text, re.M)
    if m:
        return [v.strip().strip('"\'') for v in m.group(1).split(",")
                if v.strip()]
    m = re.search(rf"^\s*-?\s*{re.escape(field)}\s*:\s*$", text, re.M)
    if m:
        start = text[:m.end()].count("\n")
        lines = text.splitlines()
        vals = []
        base = indent_of(lines[start - 1]) if start else 0
        for l in lines[start:]:
            if not l.strip():
                continue
            if indent_of(l) <= base:
                break
            mm = re.match(r"^\s*-\s+(\S.*)$", l)
            if mm:
                vals.append(mm.group(1).strip().strip('"\''))
        return vals
    m = re.search(rf"^\s*-?\s*{re.escape(field)}\s*:\s*(.+?)\s*(?:#|$)",
                  text, re.M)
    if m and m.group(1).strip():
        return [m.group(1).strip().strip('"\'')]
    return []


def check_header(lines):
    missing = [f for f in HEADER_FIELDS if top_key(lines, f) is None]
    if missing:
        return False, "missing plan fields: " + ", ".join(missing)
    si = top_key(lines, "source_story")
    src = "\n".join(collect_block(lines, si))
    sm = [f for f in SOURCE_STORY_FIELDS if not has_field(src, f)]
    if sm:
        return False, "source_story missing: " + ", ".join(sm)
    return True, "all plan header fields present"


def task_chunks(lines):
    ti = top_key(lines, "tasks")
    if ti is None:
        return []
    return split_items(collect_block(lines, ti))


def task_id(chunk):
    m = re.search(r"^\s*-?\s*id\s*:\s*(\S+)", chunk, re.M)
    return m.group(1) if m else None


def check_tasks(lines):
    chunks = task_chunks(lines)
    if len(chunks) < MIN_TASKS:
        return False, f"{len(chunks)} tasks found (need >= {MIN_TASKS})"
    incomplete = []
    for c in chunks:
        missing = [f for f in TASK_FIELDS if not has_field(c, f)]
        if missing:
            incomplete.append(f"{task_id(c) or '?'} "
                              f"(no {', '.join(missing)})")
    if incomplete:
        return False, "incomplete tasks: " + "; ".join(incomplete)
    return True, f"{len(chunks)} tasks, each with all required fields"


def check_refs_and_files(lines):
    bad = []
    for c in task_chunks(lines):
        tid = task_id(c) or "?"
        if not list_values(c, "acceptance_criteria_refs"):
            bad.append(f"{tid} (empty acceptance_criteria_refs)")
        if not list_values(c, "files_affected"):
            bad.append(f"{tid} (empty files_affected)")
    if bad:
        return False, "; ".join(bad)
    return True, "all tasks have non-empty AC refs and files_affected"


def check_deps_backward(lines):
    chunks = task_chunks(lines)
    seen = []
    bad = []
    for c in chunks:
        tid = task_id(c) or "?"
        for dep in list_values(c, "dependencies"):
            if dep not in seen:
                bad.append(f"{tid} depends on unknown/later {dep}")
        seen.append(tid)
    if bad:
        return False, "; ".join(bad)
    return True, "all dependencies point to earlier tasks"


def check_risks(lines):
    bad = []
    for c in task_chunks(lines):
        tid = task_id(c) or "?"
        vals = list_values(c, "risks")
        if not vals or (len(vals) == 1 and
                        not re.search(r"none", vals[0], re.I) and
                        vals[0].startswith("<")):
            bad.append(tid)
    if bad:
        return False, "tasks with empty risks: " + ", ".join(bad)
    return True, "every task lists a risk or explicit none"


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
        "plan_header": check_header(lines),
        "tasks_min_2": check_tasks(lines),
        "refs_and_files_nonempty": check_refs_and_files(lines),
        "deps_backward_only": check_deps_backward(lines),
        "risk_per_task": check_risks(lines),
    }


def main():
    write_prompts = "--write-judge-prompts" in sys.argv
    paths = [a for a in sys.argv[1:] if not a.startswith("--")]
    if paths:
        cases = [(os.path.splitext(os.path.basename(p))[0], p) for p in paths]
    else:
        cases = find_cases()
    if not cases:
        sys.exit(f"No cases found under {OUTPUTS_DIR}/*/plan.yaml "
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

    out = os.path.join(HERE, "eval_results_plan.json")
    with open(out, "w") as f:
        json.dump({k: {c: {"pass": ok, "detail": d} for c, (ok, d) in v.items()}
                   for k, v in results.items()}, f, indent=2)
    print(f"Machine-readable results written to {out}")


if __name__ == "__main__":
    main()
