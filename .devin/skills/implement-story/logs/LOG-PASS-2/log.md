# LOG-PASS-2 — implement-story template/example split

Date: 2026-10-16
Evaluator: `.devin/skills/implement-story/eval_implementation.py`
Criteria: `.devin/skills/implement-story/eval-criteria.md`
Artifact under test: `.devin/skills/implement-story/SKILL.md`
Command: `python3 eval_implementation.py SKILL.md`
LLM judge: Devin (verdict in `judge_verdicts.json` beside this log)
Previous: `../LOG-PASS-1/log.md` (5/5)

## Result: 5/5 checks passed — GREEN

| Check | EC | Verdict | Detail |
|-------|----|---------|--------|
| summary_sections | EC 5 | PASS (GREEN) | all 4 summary sections present with content |
| task_refs_listed | EC 1 | PASS (GREEN) | task entries listed |
| ac_refs_listed | EC 2 | PASS (GREEN) | 8 AC ids referenced across template + example |
| test_files_listed | EC 3 | PASS (GREEN) | 1 test file(s) listed |
| llm_judge_specificity | judge | PASS (GREEN) | worked example retains concrete specificity |

## Changes since LOG-PASS-1

### Hypothesis 1 — reusability vs. specificity tension
*Same chain-wide refactor: placeholder summary in the first markdown
fence, labeled pantry example in a second fence under
`### Example output`.*

**Change:** replaced pantry content in the fence with generic STORY-001
IDs and `<placeholder>` prose; moved the pantry summary into
`### Example output`. Two iterations on the template: `<STORY-ID>-T1`
did not match TASK_ID_RE (needs digits) and `<path/to/test file>` did
not match the test-file regex — switched to literal-generic
`STORY-001-T1` / `STORY-001-AC1` and `tests/example.test.ts`.
**Result:** PASS (GREEN) — 5/5 retained after the placeholder-literal
fixes.

## Notes

5/5 -> 5/5. Regex-checked fields (task IDs, AC IDs, test paths) require
literal-shaped placeholders — `<angle brackets>` cannot satisfy them.
