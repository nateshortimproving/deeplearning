# EDD Iteration Log — Development Skill

Timeline of the baseline and each iteration cycle run against the `development-tests.md` criteria. Every entry: hypothesis written *before* the run, one change, one run, measured outcome.

Evaluator: `content/AI-Bootcamp/student-work/evals/eval_development.py`
Outputs under test: `content/AI-Bootcamp/student-work/development-outputs/test-*/post.md`
Skill under test: `content/AI-Bootcamp/student-work/development.skill.md`

---

## Baseline — bare prompt, no skill

Posts generated with no skill constraints in context ("Write a social media post for [platform] based on this trend"), then scored:

| Case | Score | Failing checks |
|------|-------|----------------|
| test-1-linkedin-ux | 2/5 | hashtag_count_in_range (8, need 3–5), cta_present, llm_judge_quality (salesy tone, no CTA) |
| test-2-x-minecraft | 1/5 | length_in_range (353 chars), hashtag_count_in_range (6, need 1–2), cta_present, llm_judge_quality |
| test-3-instagram-meal-planning | 3/5 | imagery_when_appropriate (no visual), llm_judge_quality (no platform CTA) |
| test-4-linkedin-nfl | 5/5 | — |
| test-5-x-minecraft-npcs | 1/5 | length_in_range (391 chars), hashtag_count_in_range (6, need 1–2), cta_present, llm_judge_quality |

**1/5 cases passed.** Dominant failure mode: platform limits ignored (length, hashtag count) and posts end without a CTA.

---

## Iteration 1 — Apply the skill

**Target EC:** All platform-format checks (length, hashtag count, CTA).

**Hypothesis:** *I believe the baseline fails because the bare prompt had no platform rules. I predict that generating posts under `development.skill.md`'s constraints (per-platform length ranges, hashtag counts, mandatory closing CTA) will move length, hashtag, and CTA checks to green.*

**Change:** Regenerated all 5 posts following the skill — the skill itself is the single change vs. baseline.

**Result:**

| Case | Score | Notes |
|------|-------|-------|
| test-1-linkedin-ux | 5/5 | all checks pass |
| test-2-x-minecraft | 5/5 | 260 chars, 2 hashtags, question CTA |
| test-3-instagram-meal-planning | 5/5 | includes `Visual:` suggestion; save/tag CTA |
| test-4-linkedin-nfl | 5/5 | all checks pass |
| test-5-x-minecraft-npcs | 5/5 | 174 chars, 1 hashtag, "Tried one yet?" CTA |

**Conclusion:** Hypothesis held — platform constraints took all cases to 5/5. All-green now means the *current* EC can't see remaining defects; next iterations probe EC gaps, not output gaps.


## Iteration 2 — CTA tightening

**Target EC:** "Clear call to action" (currently accepts a bare `?` in the last 3 lines).

**Hypothesis:** *I believe the current `cta_present` check accepts a rhetorical question or a question that isn't a directive as a CTA. I predict tightening the check to require an explicit CTA phrase (e.g., "have you tried", "try it", "save this", "tag a friend") will produce a real red state on at least one case.*

**Change:** Tightened `CTA_RE` in `eval_development.py`. Removed the bare `?` wildcard and required an explicit directive phrase (e.g., "have you tried", "try it", "save this", "tag a friend", "check it out", "share your", "let me know") in the last 3 lines.

**Result:**

| Case | Score | Notes |
|------|-------|-------|
| test-1-linkedin-ux | 4/5 | `cta_present` fails — "Where have you seen...?" is question-only, no directive phrase |
| test-2-x-minecraft | 5/5 | "Have you tried..." matches explicit phrase |
| test-3-instagram-meal-planning | 5/5 | "Save this" and "tag the friend" match explicit phrases |
| test-4-linkedin-nfl | 4/5 | `cta_present` fails — "What AI applications are you seeing...?" is question-only |
| test-5-x-minecraft-npcs | 4/5 | `cta_present` fails — "Tried one yet?" is too terse, no directive phrase |

**Conclusion:** Hypothesis held. The original check's bare `?` wildcard was masking three question-only closers. Two posts still pass because they include explicit directive language; the other three read as genuine discussion questions but don't actually ask the reader to do anything specific. The skill's constraint "end with a clear call to action" needs to be tightened so the model outputs directive CTAs, not just closing questions.


## Iteration 3 — Tighten the skill's CTA instruction

**Target EC:** Clear, directive call to action (fixing the gap exposed in Iteration 2 where bare questions passed the check).

**Hypothesis:** *I believe the three Iteration 2 failures happened because the skill told the model to "end with a clear call to action" but never defined what a directive CTA looks like. I predict adding explicit reader-action language and platform-specific CTA examples to the skill constraints will bring all cases back to 5/5 under the tightened evaluator.*

**Change:** Updated the CTA constraints in `development.skill.md`: replaced the vague "clear call to action" rule with a requirement for directive reader-action language, plus platform-specific examples for LinkedIn, X/Twitter, and Instagram.

**Result:**

| Case | Score | Notes |
|------|-------|-------|
| test-1-linkedin-ux | 5/5 | CTA now ends with "Drop your example below" |
| test-2-x-minecraft | 5/5 | "Have you tried..." still passes |
| test-3-instagram-meal-planning | 5/5 | "Save this... tag the friend" still passes |
| test-4-linkedin-nfl | 5/5 | CTA now ends with "Share an example in the comments" |
| test-5-x-minecraft-npcs | 5/5 | CTA now ends with "Reply and let me know" |

**Conclusion:** Hypothesis held. Tightening the skill's CTA instruction restored all cases to 5/5 against the stricter evaluator. The loop is complete: Iteration 2 found an EC gap, and Iteration 3 fixed it at the skill level. This gives 3 documented iterations past baseline, satisfying the lab exit criteria. 