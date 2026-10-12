# Session 3 Deck Prompt — Review Implementation (v2)
*Week 5 | Loop 1 | Role Focus: Testing*

---

## Intro Slide

**Title:** Review Implementation
**Week:** 5 | **Loop:** 1 | **Role Focus:** Testing
**Framing:** You now have epics-and-stories and Plan → Code skills. Today we close Loop 1 by building the final skill in the SDLC pipeline: review-implementation. This is where the full chain comes together — story, plan, code, and review, each building on the last.

---

## Check-In Slide

**Question:** How has the Development Loop been working? What did your EC scores show for plan-story and implement-story? Did you notice the quality dependency — where vague plans produced vague code?

*This connects Session 2's Development Loop to Session 3's review skill. The review consumes the output of every prior step.*

---

## Session Goals Slide

**Goal 1: Build out the review-implementation skill from the SDLC skeleton**
- **Product/Process:** You need to see how reviews validate your stories. If the review can't verify a story's AC, the story is incomplete.
- **Development:** You need to see how reviews validate your Plan → Code output. Reviews reveal what the plan missed.
- **Testing:** This is your primary artifact. You own the review-implementation skill and will iterate on it for the rest of the program.

**Goal 2: Write EC for the review skill before building it**
- **Product/Process:** Your EC for reviews defines what good review coverage looks like. This tells you what story quality means downstream.
- **Development:** You'll see how EC for reviews reveals gaps in plans and code — the EC-first discipline surfaces what matters.
- **Testing:** Your EC defines the quality bar for your reviews. You own this standard.

**Goal 3: See the full Loop 1 chain assembled — epics-and-stories → plan-story → implement-story → review-implementation**
- **Product/Process:** You'll see how your story quality ripples through the entire chain. If the review has gaps, trace it upstream.
- **Development:** You'll see your Plan → Code output validated by review. The chain is a system, not isolated skills.
- **Testing:** You'll see your review skill consume the output of every other role's skills. This is where the chain comes together.

**Goal 4: Understand what a review covers that code and tests don't**
- **Product/Process:** Reviews cover correctness, edge cases, maintainability, and missing tests — things the story alone can't guarantee.
- **Development:** Reviews reveal gaps your Plan → Code skills didn't address.
- **Testing:** Reviews are your domain. You decide what matters — AI accelerates the review, you prioritize the findings.

---

## Lecture Slide — What a Review Covers (and What AI Can and Can't Do)

**Content to teach:**

The review-implementation skill reads `stories.yaml` + `plan.yaml` + the code as inputs, writes `review.yaml` with its findings, and updates `stories.yaml` — setting `review_status` and `review_notes` on the reviewed story so the feedback loop flows back to the original artifact.

A review covers: correctness issues, edge cases not handled, readability/maintainability concerns, missing tests, and anything that would prevent merging.

The human role in reviewing: deciding which issues matter most. AI can enumerate issues but can't prioritize by business risk without context.

What AI can do: dramatically accelerate issue identification, pattern detection, and review documentation.

What AI gets wrong: over-flagging low-severity issues, missing business-context risks, conflating style preferences with correctness problems.

---

## Lecture Slide — Review-Implementation RTCC Structure

**Content to teach:**

RTCC for the review-implementation skill — four elements, each answering a different question:
- **R — Role (WHO):** A senior software developer conducting a thorough code review
- **T — Task (WHAT):** Review the implementation against the story, AC, and plan. Identify correctness issues, edge cases, maintainability concerns, missing tests, and merge blockers
- **C — Context (WHY):** Why we review — to catch what planning and coding missed, to ensure the implementation satisfies the story's AC, to prevent regressions, and to maintain code quality as a team standard
- **C — Constraints (HOW):** Story + AC + plan + code as inputs. For each issue: explain why it matters and suggest a specific improvement. Severity levels required. Must reference which AC item is affected.

---

## Compare/Contrast Slide — Code vs. Review

| Code (Session 2) | Review (Session 3) |
|---|---|
| Generates implementation from the plan | Validates implementation against story + plan |
| Answers: "Does it implement the plan?" | Answers: "Does it satisfy the story?" |
| Developer-owned | Testing-owned (with input from all roles) |
| Covers the "how" | Covers the "did we get it right?" |
| Output: working code | Output: issues found, severity, recommendations |

---

## Demo Slide — Review on a Real Story

**Description:** The instructor takes a sample story from sample-stories/ + AC + Plan → Code output from the past two weeks and runs the review-implementation skill against it. The demo shows how the review consumes all upstream artifacts and what the output looks like. It connects to learning goals by making the full chain visible for the first time.

**What to focus on:** As the demo runs, notice how the review references specific AC items and plan steps. Watch what the AI gets wrong — does it over-flag style issues? Does it miss business-context risks? See how the human needs to prioritize which issues matter.

---

## Exercise Slide — Lab 1: Write EC for Your Review Skill

**Lab Name:** Write Evaluation Criteria for Your Review-Implementation Skill
**Lab Timing:** 15 minutes
**Lab Steps:**
1. Write 4-6 EC for review output before building anything
2. Suggested starting EC: "Every AC item is checked in the review" / "At least one edge case not handled is identified" / "Each issue includes why it matters and a specific improvement" / "Severity level is assigned to each issue" / "Review references which AC item is affected"
3. Commit your EC

**You'll know when you're done because...** you have 4-6 written EC for your review-implementation skill, each specific and measurable, committed before building the skill.

---

## Exercise Slide — Lab 2: Build Out the Review-Implementation Skill

**Lab Name:** Build the Review-Implementation Skill
**Lab Timing:** 45 minutes
**Lab Steps:**
1. Open the review-implementation.skill.md skeleton — Role and Task defined, Context and Constraints empty
2. Fill in Context (WHY: why we review against story + plan, what a review catches that coding misses) and Constraints (HOW: review format, what inputs to use, what to check, what to flag)
3. The skill has `disable-model-invocation: true` — invoke via slash command
4. Apply the Load-Bearing Rule: each instruction must map to at least one EC
5. Test it on 1-2 sample stories from sample-stories/ using the Plan → Code output from this sprint
6. Write `review.yaml` with the review findings (issues, severity, recommendations) and update `stories.yaml` — setting `review_status` and `review_notes` on the reviewed story
7. Evaluate the review output against your EC
8. Commit the skill

**You'll know when you're done because...** you have a committed review-implementation skill with RTCC structure that reviews real implementations against story + AC + plan, with output evaluated against your EC.

**Stretch goal:** write the review skill to check both Express backend and React frontend aspects of the implementation.

---

## Exercise Slide — Lab 3: Load-Bearing Audit and the Full Chain

**Lab Name:** Load-Bearing Audit + Full Pipeline Assembly
**Lab Timing:** 30 minutes
**Lab Steps:**
1. Review each instruction in your review skill: which EC would fail if you removed it?
2. Remove any instruction that corresponds to no EC; verify scores don't drop
3. Commit the audited skill
4. Walk through one complete story as a group: demo PRD → epics-and-stories → plan-story → implement-story → review-implementation
5. Notice the feedback loop: the review writes `review.yaml` and updates the original `stories.yaml` (setting `review_status` and `review_notes`), so review findings flow back to the story artifact itself
6. Evaluate each step's output: what quality did it produce? Where did upstream decisions affect downstream output?

**You'll know when you're done because...** your review-implementation skill has been load-bearing audited, and you've seen the full Loop 1 SDLC pipeline run end-to-end on a sample story from sample-stories/ with quality evaluated at each step.

**Stretch goal:** run the review on a complete full-stack implementation from the pantry tracker.

---

## Lecture Slide — Loop 1 Retrospective

**Content to teach:**

Complete this sentence: "In Week 1 I couldn't [blank]. Now I can [blank]."

What's the one thing you'd change about your epics-and-stories skill now, having used it for 5 weeks?

This is the transition into Loop 2: you've built the foundation. Now we make it rigorous.

Session 4: EDD with Python evaluations and LLM judges — formalizing the evaluation discipline you've been practicing informally
Session 5: Model invocation and Adversarial Agents — when to trust AI to invoke skills automatically, and how to challenge AI output with AI
Session 6: Bounded Agents, Custom Harness Demo & Stage 4 Preview — participants build a bounded agent, instructor demos a custom harness

The program's end goal: not full integration, but every participant owning evaluated, iterated skills with a clear path to continued adoption.

---

## Closing Slide

**Goal 1: Build the review-implementation skill**
- **Product/Process:** You've seen how reviews validate your stories. If a review can't verify an AC item, the story is incomplete — that's your signal.
- **Development:** You've seen how reviews validate your Plan → Code output. Coverage gaps trace back to the plan.
- **Testing:** You own this skill. You'll iterate on it for the rest of the program. This is your primary artifact.

**Goal 2: Write EC before building**
- **Product/Process:** Your EC for reviews reveals what story quality means downstream. Use it to hold your stories accountable.
- **Development:** You've seen how EC for reviews surfaces gaps in plans and code. The EC-first discipline works across the chain.
- **Testing:** You own the quality standard for reviews. Your EC defines what good review coverage looks like for your team.

**Goal 3: See the full Loop 1 chain**
- **Product/Process:** You've seen epics-and-stories → Plan → Code → Review as a connected system. Your story quality ripples through everything.
- **Development:** You've seen your Plan → Code output validated by review. The chain is a system, not isolated skills.
- **Testing:** You've seen your review skill consume every other role's output. This is where the chain comes together — and where you'll deepen it in Loop 2.

**Goal 4: Understand what reviews cover**
- **Product/Process:** Reviews cover issues that stories alone can't prevent. Your stories should enable review, not constrain it.
- **Development:** Reviews reveal gaps your Plan → Code skills missed. Use them to improve your planning.
- **Testing:** Reviews are your domain. You decide what matters. AI accelerates; you prioritize.