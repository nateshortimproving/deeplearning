# Manual Test File — Development Skill

Bare prompt under test: "Write a social media post for [platform] based on this trend"

Written before the skill exists. These Expected Outputs are my Evaluation Criteria (EC).

## For all tests
- **Pass if:**
* The post is {appropriate platform length}.
* The post contains {appropriate platform length} hashtags in #format.
* The post ends with a clear call to action {appropriate platform context}.
* The post is self-contained: someone who never saw the trend entry understands the angle.
* THe post provides imagery if appropriate for the platform.

- **Fail if:**
* Tone sounds like a salesman, or obvious AI.
* First line doesn't hook into the trend.

## Test 1
- **Input:** "Write a LinkedIn post based on this trend: AI co-pilots for UX design"

## Test 2
- **Input:** "Write an X/Twitter post based on this trend: AI use in Minecraft"

## Test 3
- **Input:** "Write an Instagram post based on this trend: AI-powered personalized meal planning"

## Test 4
- **Input:** "Write a LinkedIn post based on this trend: AI-powered player performance analytics in the NFL.

## Test 5
- **Input:** "Write an X/Twitter post based on this trend: AI NPC companions in Minecraft servers.


---

## Baseline results (bare prompt — fill in after running)

| Test | Result (pass/fail) | Which criteria failed? |
|------|--------------------|------------------------|
| 1    | FAIL               | hashtag_count (8, need 3–5); no CTA at end; judge: salesy/AI tone, no CTA |
| 2    | FAIL               | length (353 chars, need ≤280); hashtag_count (6, need 1–2); no CTA; judge: hype tone, no CTA |
| 3    | FAIL               | no visual suggestion for Instagram; judge: no platform CTA |
| 4    | PASS               | — |
| 5    | FAIL               | length (391 chars, need ≤280); hashtag_count (6, need 1–2); no CTA; judge: no CTA |

## Skill results (development.skill.md — after building)

| Test | Result (pass/fail) | Notes |
|------|--------------------|-------|
| 1    |                    |       |
| 2    |                    |       |
| 3    |                    |       |
| 4    |                    |       |
| 5    |                    |       |
