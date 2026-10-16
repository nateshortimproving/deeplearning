#!/usr/bin/env python3
"""
Evaluation script for the create-epics-stories skill.

Reads each stories.yaml output (or a SKILL.md containing a fenced
```yaml template) and applies the EC from eval-criteria.md:

DETERMINISTIC CHECKS (pure Python, no model call, line-based YAML scan):
  1. required_structure     - top-level `epic:` and `stories:` keys exist;
       epic has name, description, source_prd (EC 1)
  2. stories_min_2          - at least two stories, each with id, title,
       user_story, acceptance_criteria, review_status, review_notes
       (EC 1, EC 2)
  3. ac_per_story           - every story has >= 2 acceptance criteria,
       each with id, given, when, then, type (EC 3)
  4. negative_or_edge_ac    - at least one AC has type "negative" or
       "edge_case" (EC 4)
  5. review_status_pending  - every story's review_status is "pending"
       (EC 5)

LLM JUDGE CHECK (qualitative EC from eval-criteria.md):
  6. llm_judge_specificity  - a model grades whether stories are
       independently deliverable, AC are testable observable behavior
       (no implementation detail), personas/roles are real, and there
       is no duplication. Reads verdicts from judge_verdicts.json; run
       with --write-judge-prompts to emit judge_prompts.md.

Usage:
  python3 eval_stories.py                            # eval all cases in outputs/*/stories.yaml
  python3 eval_stories.py path/to/file [...]         # eval specific files (yaml or SKILL.md)
  python3 eval_stories.py --write-judge-prompts      # emit judge_prompts.md
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
MIN_STORIES = 2
MIN_AC_PER_STORY = 2

EPIC_FIELDS = ["name", "description", "source_prd"]
STORY_FIELDS = ["id", "title", "user_story", "acceptance_criteria",
                "review_status", "review_notes"]
AC_FIELDS = ["id", "given", "when", "then", "type"]

JUDGE_RUBRIC = """You are grading output from a "create-epics-stories" skill that breaks a
feature into epics and user stories (stories.yaml).

Grade the stories.yaml content below against these criteria:
1. INDEPENDENTLY DELIVERABLE: each story can be built, tested, and shipped
   on its own - no story's AC depends on another story being done first.
2. TESTABLE AC: each acceptance criterion describes observable behavior a
   reviewer could verify without seeing code - Given/When/Then is specific,
   not vague ("works correctly").
3. NO IMPLEMENTATION DETAIL: no story or AC names technologies, endpoints,
   database tables, or code structure.
4. REAL USER VALUE: each story names a real role and a concrete benefit;
   no two stories deliver the same capability.
5. FAILURE COVERAGE: at least one story or AC covers a failure path
   (invalid input, missing data, unavailable dependency).
6. SPECIFICITY: content is concrete, not placeholder or boilerplate.

Respond with exactly this JSON on one line:
{{"pass": true/false, "independent": true/false, "testable_ac": true/false, "no_impl_detail": true/false, "user_value": true/false, "failure_coverage": true/false, "specific": true/false, "notes": "one sentence"}}

--- BEGIN stories.yaml ---
{content}
--- END stories.yaml ---
"""


def find_cases():
    cases = []
    if os.path.isdir(OUTPUTS_DIR):
        for name in sorted(os.listdir(OUTPUTS_DIR)):
            path = os.path.join(OUTPUTS_DIR, name, "stories.yaml")
            if os.path.isfile(path):
                cases.append((name, path))
    return cases


def doc_of(content):
    """Return the fenced yaml block if present, else the whole file."""
    m = YAML_FENCE_RE.search(content)
    return m.group(1) if m else content


def indent_of(line):
    return len(line) - len(line.lstrip())


def collect_block(lines, start):
    """Lines after `start` until a non-empty line at indent <= its key."""
    base = indent_of(lines[start])
    out = []
    for l in lines[start + 1:]:
        if l.strip() and indent_of(l) <= base:
            break
        out.append(l)
    return out


def top_key(lines, name):
    """Index of a top-level 'name:' line, or None."""
    for i, l in enumerate(lines):
        if re.match(rf"^{re.escape(name)}\s*:", l):
            return i
    return None


def split_items(block_lines):
    """Split a yaml list block into per-item chunks at '- key:' markers
    at the shallowest list indent (so nested lists are not split)."""
    items = [(i, indent_of(l)) for i, l in enumerate(block_lines)
             if re.match(r"^\s*-\s*\S+\s*:", l)]
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


def check_required_structure(lines):
    problems = []
    ei = top_key(lines, "epic")
    if ei is None:
        problems.append("no epic: block")
    else:
        epic = "\n".join(collect_block(lines, ei))
        missing = [f for f in EPIC_FIELDS if not has_field(epic, f)]
        if missing:
            problems.append("epic missing: " + ", ".join(missing))
    if top_key(lines, "stories") is None:
        problems.append("no stories: key")
    ok = not problems
    return ok, ("epic + stories present with required fields" if ok
                else "; ".join(problems))


def story_chunks(lines):
    si = top_key(lines, "stories")
    if si is None:
        return []
    return split_items(collect_block(lines, si))


def check_stories(lines):
    chunks = story_chunks(lines)
    n = len(chunks)
    if n < MIN_STORIES:
        return False, f"{n} stories found (need >= {MIN_STORIES})"
    incomplete = []
    for c in chunks:
        sid = re.search(r"id\s*:\s*(\S+)", c)
        label = sid.group(1) if sid else "?"
        missing = [f for f in STORY_FIELDS if not has_field(c, f)]
        if missing:
            incomplete.append(f"{label} (no {', '.join(missing)})")
    if incomplete:
        return False, "incomplete stories: " + "; ".join(incomplete)
    return True, f"{n} stories, each with all required fields"


def check_ac_per_story(lines):
    bad = []
    total = 0
    for c in story_chunks(lines):
        sid = re.search(r"id\s*:\s*(\S+)", c)
        label = sid.group(1) if sid else "?"
        cl = c.splitlines()
        aci = next((i for i, l in enumerate(cl)
                    if re.match(r"^\s*acceptance_criteria\s*:", l)), None)
        if aci is None:
            bad.append(f"{label} (no acceptance_criteria)")
            continue
        acs = split_items(collect_block(cl, aci))
        total += len(acs)
        issues = []
        if len(acs) < MIN_AC_PER_STORY:
            issues.append(f"{len(acs)} AC")
        for ac in acs:
            missing = [f for f in AC_FIELDS if not has_field(ac, f)]
            if missing:
                issues.append("AC missing " + ",".join(missing))
        if issues:
            bad.append(f"{label} ({'; '.join(issues)})")
    if bad:
        return False, "AC problems: " + "; ".join(bad)
    return True, f"{total} AC across stories, each fully fielded"


def check_negative_or_edge(lines):
    doc = "\n".join(lines)
    ok = bool(re.search(r'type\s*:\s*"?(negative|edge_case)"?', doc))
    return ok, ("found AC with type negative or edge_case" if ok
                else "no negative or edge_case AC found")


def check_review_status(lines):
    vals = re.findall(r'review_status\s*:\s*"?([\w<]+)', "\n".join(lines))
    if not vals:
        return False, "no review_status fields found"
    bad = [v for v in vals if v != "pending"]
    ok = not bad
    return ok, (f"all {len(vals)} review_status values are 'pending'" if ok
                else "non-pending review_status: " + ", ".join(bad))


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
        "required_structure": check_required_structure(lines),
        "stories_min_2": check_stories(lines),
        "ac_per_story": check_ac_per_story(lines),
        "negative_or_edge_ac": check_negative_or_edge(lines),
        "review_status_pending": check_review_status(lines),
    }


def main():
    write_prompts = "--write-judge-prompts" in sys.argv
    paths = [a for a in sys.argv[1:] if not a.startswith("--")]
    if paths:
        cases = [(os.path.splitext(os.path.basename(p))[0], p) for p in paths]
    else:
        cases = find_cases()
    if not cases:
        sys.exit(f"No cases found under {OUTPUTS_DIR}/*/stories.yaml "
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

    out = os.path.join(HERE, "eval_results_stories.json")
    with open(out, "w") as f:
        json.dump({k: {c: {"pass": ok, "detail": d} for c, (ok, d) in v.items()}
                   for k, v in results.items()}, f, indent=2)
    print(f"Machine-readable results written to {out}")


if __name__ == "__main__":
    main()
