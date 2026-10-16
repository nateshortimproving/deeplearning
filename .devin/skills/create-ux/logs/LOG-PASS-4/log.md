# LOG-PASS-4 — create-ux template/example split

Date: 2026-10-16
Evaluator: `.devin/skills/create-ux/eval_ux.py`
Criteria: `.devin/skills/create-ux/eval-criteria.md`
Artifact under test: `.devin/skills/create-ux/SKILL.md`
Command: `python3 eval_ux.py SKILL.md`
LLM judge: Devin (verdict in `judge_verdicts.json` beside this log)
Previous: `../LOG-PASS-3/log.md` (6/6)

## Result: 6/6 checks passed — GREEN

| Check | EC | Verdict | Detail |
|-------|----|---------|--------|
| required_sections_present | EC 1 | PASS (GREEN) | all 5 required sections present and non-empty |
| personas_min_2 | EC 2 | PASS (GREEN) | 2 personas, each with Role/Goals/Pain Points |
| flows_min_2 | EC 3 | PASS (GREEN) | 2 flows, each with >= 3 steps, Decision Point, and Error Risk |
| error_table_min_2 | EC 4 | PASS (GREEN) | 2 error-state rows with >= 3 filled cells |
| design_covers_a11y_responsive | EC 5 | PASS (GREEN) | covers accessibility and responsiveness |
| llm_judge_specificity | judge | PASS (GREEN) | worked example retains concrete specificity |

## Changes since LOG-PASS-3

### Hypothesis 1 — reusability vs. specificity tension
*The pantry worked example made the judge green but risked domain
anchoring; splitting into a placeholder template plus a labeled
`### Example output` should preserve the score while making the skill
reusable for any input domain.*

**Change:** replaced the worked example inside the Output Format fence with
instructive placeholders (2 persona stubs with Role/Goals/Pain Points,
2 flow stubs with steps + Decision Point + Error Risk, a 2-row error table
shell, a11y + responsiveness placeholder bullets) and moved the pantry
content into a labeled `### Example output` section marked "do not copy
its content."
**Result:** PASS (GREEN) — all 5 deterministic checks pass on the
placeholder structure alone; judge grades the example.

## Notes

6/6 -> 6/6 through the refactor. The template now specifies *shape* and the
example specifies *quality bar* — a downstream model can produce UX
guidance for any domain without pantry anchoring.
