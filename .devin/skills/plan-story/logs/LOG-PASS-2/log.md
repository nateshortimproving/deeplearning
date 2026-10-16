# LOG-PASS-2 — plan-story template/example split

Date: 2026-10-16
Evaluator: `.devin/skills/plan-story/eval_plan.py`
Criteria: `.devin/skills/plan-story/eval-criteria.md`
Artifact under test: `.devin/skills/plan-story/SKILL.md`
Command: `python3 eval_plan.py SKILL.md`
LLM judge: Devin (verdict in `judge_verdicts.json` beside this log)
Previous: `../LOG-PASS-1/log.md` (6/6)

## Result: 6/6 checks passed — GREEN

| Check | EC | Verdict | Detail |
|-------|----|---------|--------|
| plan_header | EC 1 | PASS (GREEN) | all plan fields present |
| tasks_min_2 | EC 2 | PASS (GREEN) | 2 tasks, each with all required fields |
| refs_and_files_nonempty | EC 3 | PASS (GREEN) | all tasks have non-empty AC refs and files_affected |
| deps_backward_only | EC 4 | PASS (GREEN) | all dependencies point to earlier tasks |
| risk_per_task | EC 5 | PASS (GREEN) | every task lists a risk or explicit none |
| llm_judge_specificity | judge | PASS (GREEN) | worked example retains concrete specificity |

## Changes since LOG-PASS-1

### Hypothesis 1 — reusability vs. specificity tension
*Same chain-wide refactor: placeholder schema in the first yaml fence,
labeled pantry example in a second fence under `### Example output`.*

**Change:** replaced pantry content in the Output Format fence with
`<placeholder>` stubs (STORY-001 tasks with generic risks/files/refs)
and moved the pantry plan into `### Example output`. Two iterations on
the template: `risks: [<risk or unknown>]` counted as empty (the eval
treats `<...>` values as placeholders) — switched to a plain-text
placeholder `risks: [One risk or unknown for this task]`.
**Result:** PASS (GREEN) — 6/6 retained after the placeholder-wording fix.

## Notes

6/6 -> 6/6. Lesson recorded for the chain: list-field checks treat
`<angle-bracket>` items as empty placeholders — instructive placeholders
must be plain text.
