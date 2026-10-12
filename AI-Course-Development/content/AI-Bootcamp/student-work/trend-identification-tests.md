# Manual Test File — Trend Identification Skill

Bare prompt under test: "Identify trending topics in AI on social media"
Written before the skill exists. These Expected Outputs are my Evaluation Criteria (EC).

## Test 1
- **Input:** "Identify trending topics in AI on social media. Subject: AI in UX Design"
- **Pass if:** 

* The trends are actually current. Nothing that's been dead for over 2 months.
* The trends are specific to UX Design and AI.
* The trends are provided in a numbered list of 5–8 topics.
* Each topic notes which platform it's relevant on as its source.
* Each topic includes a brief explanation of why it's trending.
* Each topic has 3–5 hashtags in #format
* Each topic cites at least one real, named source (publication, report, platform trend tool, or credible expert) supporting the claim that it is trending.

- **Fail if:** 
* The trends are not specific to UX Design and AI.
* The trends are not provided in a numbered list of 5–8 topics.
* Each topic does not note which platform it's relevant on as its source.
* Each topic does not include a brief explanation of why it's trending.
* Each topic does not have 3–5 hashtags in #format
* Any two topics are the same thing reworded
* Any topic does not cite a real, named source supporting why it is trending

## Test 2
- **Input:** "Identify trending topics in AI on social media. Subject: AI in Music"
- **Pass if:** 
* The trends are actually current. Nothing that's been dead for over 2 months.
* The trends are specific to Music and AI.
* The trends are provided in a numbered list of 5–8 topics.
* Each topic notes which platform it's relevant on as its source.
* Each topic includes a brief explanation of why it's trending.
* Each topic has 3–5 hashtags in #format
- **Fail if:** 
* The trends are not specific to Music and AI.
* The trends are not provided in a numbered list of 5–8 topics.
* Each topic does not note which platform it's relevant on as its source.
* Each topic does not include a brief explanation of why it's trending.
* Each topic does not have 3–5 hashtags in #format
* Any two topics are the same thing reworded

## Test 3
- **Input:** "Identify trending topics in AI on social media. Subject: AI in the NFL"
- **Pass if:** 
* The trends are actually current. Nothing that's been dead for over 2 months.
* The trends are specific to NFL and AI.
* The trends are provided in a numbered list of 5–8 topics.
* Each topic notes which platform it's relevant on as its source.
* Each topic includes a brief explanation of why it's trending.
* Each topic has 3–5 hashtags in #format
- **Fail if:** 
* The trends are not specific to NFL and AI.
* The trends are not provided in a numbered list of 5–8 topics.
* Each topic does not note which platform it's relevant on as its source.
* Each topic does not include a brief explanation of why it's trending.
* Each topic does not have 3–5 hashtags in #format
* Any two topics are the same thing reworded

## Test 4
- **Input:** "Identify trending topics in AI on social media. Subject: AI in Food"
- **Pass if:**
* The trends are actually current. Nothing that's been dead for over 2 months.
* The trends are specific to Food and AI.
* The trends are provided in a numbered list of 5–8 topics.
* Each topic notes which platform it's relevant on as its source.
* Each topic includes a brief explanation of why it's trending.
* Each topic has 3–5 hashtags in #format
- **Fail if:** 
* The trends are not specific to Food and AI.
* The trends are not provided in a numbered list of 5–8 topics.
* Each topic does not note which platform it's relevant on as its source.
* Each topic does not include a brief explanation of why it's trending.
* Each topic does not have 3–5 hashtags in #format
* Any two topics are the same thing reworded

## Test 5
- **Input:** "Identify trending topics in AI on social media. Subject: AI in Minecraft"
- **Pass if:**
* The trends are actually current. Nothing that's been dead for over 2 months.
* The trends are specific to Minecraft and AI.
* The trends are provided in a numbered list of 5–8 topics.
* Each topic notes which platform it's relevant on as its source.
* Each topic includes a brief explanation of why it's trending.
* Each topic has 3–5 hashtags in #format
- **Fail if:** 
* The trends are not specific to Minecraft and AI.
* The trends are not provided in a numbered list of 5–8 topics.
* Each topic does not note which platform it's relevant on as its source.
* Each topic does not include a brief explanation of why it's trending.
* Each topic does not have 3–5 hashtags in #format
* Any two topics are the same thing reworded

---

## Baseline results (bare prompt — fill in after running)

| Test | Result (pass/fail) | Which criteria failed? |
|------|--------------------|------------------------|
| 1    | FAIL               | Not a numbered list; no platform per topic; no hashtags; explanations merged into a paragraph |
| 2    | FAIL               | No platform per topic; no hashtags; no "why trending" explanations — just a bare list |
| 3    | FAIL               | 9 topics (over the 8 max); no platform per topic; no hashtags; no explanations |
| 4    | FAIL               | Not a numbered list; no platforms; no hashtags; explanations merged into a paragraph |
| 5    | FAIL               | No platform per topic; no hashtags; no "why trending" explanations |

## Skill results (trend-identification.skill.md — after building)

| Test | Result (pass/fail) | Notes |
|------|--------------------|-------|
| 1    | FAIL               | Missing named source citations per topic |
| 2    | PASS               | 5 numbered topics, all fields present |
| 3    | PASS               | 6 topics, all fields present |
| 4    | PASS               | 5 numbered topics, all fields present |
| 5    | PASS               | 5 numbered topics, all fields present |
