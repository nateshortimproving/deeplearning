# LOG-PASS-0 — plan-story baseline eval

Date: 2026-10-16
Evaluator: `.devin/skills/plan-story/eval_plan.py`
Criteria: `.devin/skills/plan-story/eval-criteria.md`
Artifact under test: `.devin/skills/plan-story/SKILL.md`
Command: `python3 eval_plan.py SKILL.md`
LLM judge: Devin (verdict in `judge_verdicts.json` beside this log)

## Result: 2/6 checks passed — RED

| Check | EC | Verdict | Detail |
|-------|----|---------|--------|
| plan_header | EC 1 | PASS (GREEN) | all plan header fields present |
| tasks_min_2 | EC 2 | FAIL (RED) | 1 tasks found (need >= 2) |
| refs_and_files_nonempty | EC 3 | PASS (GREEN) | all tasks have non-empty AC refs and files_affected |
| deps_backward_only | EC 4 | FAIL (RED) | <string> depends on unknown/later <string> |
| risk_per_task | EC 5 | FAIL (RED) | tasks with empty risks: <string> |
| llm_judge_specificity | judge | FAIL (RED) | YAML schema with <string> placeholders and a single example task - structure is defined but no concrete tasks, dependencies, risks, or assumptions to grade |

## Notes

The eval inspected the fenced `yaml` template inside SKILL.md. The plan
schema is structurally complete (all header and task fields) but carries a
single placeholder task, so count, dependency-order, and risk checks have
nothing real to verify — same instance-level gap as create-epics-stories.

Baseline for EDD iteration: converting the schema block into a worked
example (2+ concrete tasks with real ids, backward-only dependencies,
non-empty risks and AC refs) should turn all checks green.
