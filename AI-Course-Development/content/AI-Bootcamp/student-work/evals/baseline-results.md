# Baseline Results — trend-identification eval (Red state)

Date: 2026-10-12
Script: `eval_trends.py` — run with `python3 eval_trends.py`
Judge: Devin (verdicts in `judge_verdicts.json`; regenerate prompts via `--write-judge-prompts`)

## Checks in the script

| Check | Type | EC it encodes |
|-------|------|----------------|
| `topic_count_in_range` | deterministic | numbered list of 5–8 topics |
| `hashtags_per_topic` | deterministic | 3–5 hashtags in #format per topic (counted on the Hashtags line) |
| `rationale_per_topic` | deterministic | one "why trending" explanation per topic |
| `platform_per_topic` | deterministic | each topic names its platform |
| `llm_judge_quality` | LLM judge | trends specific to subject AND AI; no reworded duplicates; current within ~2 months |

## Scores

| Test | Checks passed | Result | What failed |
|------|---------------|--------|-------------|
| test-1-ai-ux-design | 5/5 | PASS | — |
| test-2-ai-music | 5/5 | PASS | — |
| test-3-ai-nfl | 5/5 | PASS | — |
| test-4-ai-food | 4/5 | **FAIL** | `llm_judge_quality`: topic 5 (Gen Z food trends on social media) isn't about AI |
| test-5-ai-minecraft | 5/5 | PASS | — |

**Overall: 4/5 cases fully passed.**

## Notes vs. the manual table

The automated eval is stricter than the hand-graded results in
`../trend-identification-tests.md`, which marked test-4 as PASS. On closer
inspection that output has three borderline issues: topic 5 isn't AI-specific
(caught by the judge), topic 3's platform is TikTok rather than one of the
skill's three allowed platforms, and its rationale contains a `#Food` hashtag
in prose. The latter two are within the letter of the EC but not the spirit —
good candidates for tightening the EC next iteration.
