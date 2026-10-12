# Week 5 — Loop 1: Testing Team
*Training Session 3 occurs this week*

---

## Focus
Embedded Engineer transitions to the Testing team. All participants attend Training Session 3 on Review Implementation. Testing team begins using the `review-implementation` skeleton skill to review implementations against story + AC + plan. Session 3 teaches in the shared student workspace; the EE coaches the transfer to the team's real codebase.

---

## Training Session This Week
**Session-3 — Review Implementation: `review-implementation`** (4 hours, all participants)
- What review-implementation is: reviewing the implementation against the story + Acceptance Criteria + plan, not an isolated test planning exercise
- Building out the `review-implementation` skeleton skill: add Context (WHY we review implementation against the story + plan, what a review catches that coding misses) and Constraints (HOW the review should be structured, what to check, what to flag)
- EDD: write Evaluation Criteria (EC) before building out the skill
- RTCC structure — WHO, WHAT, WHY, HOW
- Lab: build out `review-implementation` with EC, load-bearing audit
- Lab: generate reviews on real implementations; evaluate against EC
- The plan and code output from Session 2 is the input to `review-implementation` — the chain completes
- The full Loop 1 chain assembled: epics-and-stories → plan-story → implement-story → review-implementation
- Entering Loop 2 preview: Python evaluations + LLM judges coming in Session 4

---

## Embedded Engineer Focus (Testing Team)

- **Day 1:** Orient with the Testing team. Understand current review/testing practice — how do they decide what to test, at what level, in what sequence? What's the highest-friction step? You're learning the real testing workflow so you can help transfer the workspace-built skill to it.
- **Day 2:** Introduce the review-implementation concept. Show the chain: epics-and-stories → plan-story → implement-story → review-implementation. The review uses all upstream artifacts — story, AC, plan, and code. The Testing team builds out the skill in the workspace against sample stories, plans, and code.
- **Days 3–4:** Transfer the skill to real work. Build out the `review-implementation` skill with the Testing team using RTCC and real stories + plans + code from the sprint (not workspace samples). Write EC first — before running anything. Add Context (WHY) and Constraints (HOW) that reflect the team's real review standards and codebase.
- **Day 5:** Run the skill on 2–3 real stories from the sprint. Evaluate the output against the EC together. What passes? What fails? What's the most common gap? If the skill works on workspace samples but fails on real stories, adjust Context or Constraints.

**Key Embedded Engineer priority this week:** Establish the full artifact chain (epics-and-stories → plan-story → implement-story → review-implementation) as visible and real to the Testing team. The SDLC skeleton pipeline is complete. The Testing team builds the skill in the workspace, then transfers it to real reviews.

---

## Participant Activities (Testing Team)
- Attend Training Session 3
- Examine existing stories + AC + plans + code from the past 2 weeks
- Write Evaluation Criteria (EC) for review-implementation output before building out the skill
- Build out `review-implementation` skill using RTCC; apply the load-bearing audit after first successful run

## Participant Activities (All)
- Attend Training Session 3
- Review their primary skill and the EC they wrote in Sessions 1 or 2
- Prepare for evaluation formalization: bring your skill and your EC to Session 4

---

## Artifacts Due by End of Week 5
- [ ] All participants: written EC for their primary skill (if not already done in Sessions 1–2)
- [ ] Testing team: `review-implementation` skill built out (RTCC, EC-first, load-bearing audit) — committed
- [ ] Testing team: reviews generated from 1–2 real stories with EC scores noted

---

## Embedded Engineer Coaching Notes

- Session 3 closes Loop 1. The Embedded Engineer should reinforce this framing explicitly during the week: "You now have skills across all three workflow areas of the SDLC pipeline. The next step is making the evaluation of those skills systematic."
- The Testing team will often have a strong existing review methodology. Respect it — the goal is to make that methodology faster and more thorough, not to replace it. The skill's Context section should encode their existing standards.
- Watch for participants who write EC after building out the skill rather than before. If this happens, have them scrap the EC and write them fresh against a blank slate. The value of EC-first is that the model hasn't influenced the expectations yet.
- The Loop 2 preview in Session 3 mentions Python evaluations + LLM judges coming in Session 4. This is the first time participants will encounter automated evaluation — Session 4 is where they'll learn it. The EE does NOT pre-teach Python evaluation in Week 6.
- The SDLC skeleton pipeline is now complete: all 7 skeleton skills were introduced in Session 1, and `epics-and-stories`, `plan-story`, `implement-story`, and `review-implementation` have been built out across Sessions 1-3.
- **Transfer model note:** The `review-implementation` skill is built in the workspace against sample stories, plans, and code. The Testing team's real codebase has different review standards, different code patterns, and different risk areas. The transfer coaching this week is about adapting the skill's Context and Constraints from the sample domain to the team's real review process. Don't expect the workspace-built skill to know the team's testing standards — those need to be encoded in Context and Constraints during transfer.