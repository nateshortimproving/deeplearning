# LOG-PASS-0 — create-epics-stories baseline eval

Date: 2026-10-16
Evaluator: `.devin/skills/create-epics-stories/eval_stories.py`
Criteria: `.devin/skills/create-epics-stories/eval-criteria.md`
Artifact under test: `.devin/skills/create-epics-stories/SKILL.md`
Command: `python3 eval_stories.py SKILL.md`
LLM judge: Devin (verdict in `judge_verdicts.json` beside this log)

## Result: 1/6 checks passed — RED

| Check | EC | Verdict | Detail |
|-------|----|---------|--------|
| required_structure | EC 1 | PASS (GREEN) | epic + stories present with required fields |
| stories_min_2 | EC 1, EC 2 | FAIL (RED) | 1 stories found (need >= 2) |
| ac_per_story | EC 3 | FAIL (RED) | AC problems: <string> (1 AC) |
| negative_or_edge_ac | EC 4 | FAIL (RED) | no negative or edge_case AC found |
| review_status_pending | EC 5 | FAIL (RED) | non-pending review_status: <string |
| llm_judge_specificity | judge | FAIL (RED) | YAML schema with <string> placeholders - defines structure but contains no concrete stories, real AC, or negative/edge_case coverage to judge |

## Notes

The eval inspected the fenced `yaml` template inside SKILL.md. Unlike the
markdown-template skills, the schema is structurally complete (epic block,
all story/AC fields) — its failures are all *instance-level*: one example
story instead of two, one AC instead of two+, no negative/edge_case example,
and `<string>` placeholder values throughout.

Baseline for EDD iteration: converting the schema block into a worked
example (2 concrete stories, >= 2 AC each incl. a negative/edge_case, real
ids and review_status values) should take all six checks green in one pass.
