# LOG-PASS-2 — create-epics-stories template/example split

Date: 2026-10-16
Evaluator: `.devin/skills/create-epics-stories/eval_stories.py`
Criteria: `.devin/skills/create-epics-stories/eval-criteria.md`
Artifact under test: `.devin/skills/create-epics-stories/SKILL.md`
Command: `python3 eval_stories.py SKILL.md`
LLM judge: Devin (verdict in `judge_verdicts.json` beside this log)
Previous: `../LOG-PASS-1/log.md` (6/6)

## Result: 6/6 checks passed — GREEN

| Check | EC | Verdict | Detail |
|-------|----|---------|--------|
| required_structure | EC 1 | PASS (GREEN) | epic fields + stories list present |
| stories_min_2 | EC 2 | PASS (GREEN) | 2 stories, each with all required fields |
| ac_per_story | EC 3 | PASS (GREEN) | 4 AC across stories, each fully fielded |
| negative_or_edge_ac | EC 4 | PASS (GREEN) | found AC with type negative or edge_case |
| review_status_pending | EC 5 | PASS (GREEN) | all 2 review_status values are 'pending' |
| llm_judge_specificity | judge | PASS (GREEN) | worked example retains concrete specificity |

## Changes since LOG-PASS-1

### Hypothesis 1 — reusability vs. specificity tension
*The pantry worked example made the judge green but risked domain
anchoring; a placeholder schema in the first yaml fence plus a labeled
`### Example output` in a second fence should preserve the score while
making the skill reusable for any domain.*

**Change:** replaced the pantry stories.yaml in the Output Format fence
with `<placeholder>` stubs (2 generic STORY-xxx stories, each with a
positive + negative/edge AC and `review_status: pending`) and moved the
pantry content into a labeled `### Example output` section marked "do not
copy its content." The eval's `doc_of` takes the *first* fenced yaml
block, so deterministic checks grade the template while the judge sees
the example.
**Result:** PASS (GREEN) — 6/6 retained.

## Notes

6/6 -> 6/6 through the refactor. Generic `STORY-xxx` IDs replace the
pantry prefix in the template; the pantry threading remains as the
worked example chain-wide.
