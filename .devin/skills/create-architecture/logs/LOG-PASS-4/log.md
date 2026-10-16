# LOG-PASS-4 — create-architecture template/example split

Date: 2026-10-16
Evaluator: `.devin/skills/create-architecture/eval_architecture.py`
Criteria: `.devin/skills/create-architecture/eval-criteria.md`
Artifact under test: `.devin/skills/create-architecture/SKILL.md`
Command: `python3 eval_architecture.py SKILL.md`
LLM judge: Devin (verdict in `judge_verdicts.json` beside this log)
Previous: `../LOG-PASS-3-DELTA/log.md` (delta study), `../LOG-PASS-2/log.md` (6/6)

## Result: 6/6 checks passed — GREEN

| Check | EC | Verdict | Detail |
|-------|----|---------|--------|
| required_sections_present | EC 1 | PASS (GREEN) | all 5 required sections present and non-empty |
| components_min_3 | EC 2 | PASS (GREEN) | 3 components, each with a Responsibility entry |
| decisions_table_min_2 | EC 3 | PASS (GREEN) | 2 decision rows with >= 3 filled cells |
| constraints_min_2 | EC 4 | PASS (GREEN) | 3 constraint items |
| no_orphan_components | EC 5 | PASS (GREEN) | all components referenced in Data Flow |
| llm_judge_specificity | judge | PASS (GREEN) | worked example retains concrete specificity |

## Changes since LOG-PASS-2

### Hypothesis 1 — reusability vs. specificity tension
*The worked example made the judge green but risked domain anchoring;
splitting into a placeholder template (format spec) plus a labeled
`### Example output` (quality bar) should preserve the score while making
the skill reusable for any input domain.*

**Change:** restored bracketed placeholders inside the Output Format fence
and moved the Notification Service worked example into a labeled
`### Example output` section marked "do not copy its content."
**Result:** PASS (GREEN) — eval still 6/6; judge grades the example.

### Hypothesis 2 — parser robustness (regression caught)
*Duplicating the doc structure could break first-match section binding.*

**Change:** the `component` pattern had matched the H1 title
`# Architecture: [Feature or Component Name]` and bound the whole doc as
the Components section; anchored the eval pattern to `^components?\b`.
Also made the template's Data Flow placeholder name the placeholder
components explicitly (`[Component 1 Name]` etc.) so the orphan check and
the naming discipline both hold.
**Result:** PASS (GREEN) — regression fixed in `eval_architecture.py`;
the same H1-title trap now cannot fire on any doc whose title mentions
"component."

## Notes

6/6 -> 6/6 through a structural refactor, with one real eval bug found and
fixed. Template/example split is the chain-wide convention.
