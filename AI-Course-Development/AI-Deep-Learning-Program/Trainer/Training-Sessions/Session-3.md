# Training Session 3 — Review Implementation: Closing Loop 1

*Week 5 | 4 Hours | All Participants | Loop 1 — Role Focus: Testing*

> **All-roles framing:** Every participant attends. The primary artifact focus is the **review-implementation** skill — the testing/review step of the SDLC pipeline. This session closes Loop 1: the full pipeline from epics-and-stories → plan-story → implement-story → review-implementation is now built out. Product/Process and Dev participants see their upstream work assembled into a review — and for the first time, the entire chain is visible end-to-end.

---

## Why This Session Closes Loop 1

By Week 5, the full chain exists in practice: stories have AC (Session 1, from `sample-stories/`), AC has been used to generate plans (Session 2), plans have been used to generate code (Session 2). This session builds the final piece — the review-implementation skill that reviews the implementation against the story + AC + plan + code — and then assembles the whole chain.

For the Testing role, this is their primary skill-building session. For Product/Process and Dev, this session answers the question: "Did our upstream work actually support what came after it?"

The review-implementation skill consumes everything produced upstream — story + AC + plan + code — and produces a review. This is the artifact that closes the loop: it tells you whether the implementation satisfies the story, whether the plan was followed, and what the gaps are.

---

## Session Goals

By end of this session, every participant:
- Has built out the **review-implementation** skill from its SDLC skeleton, adding Context (WHY) and Constraints (HOW) using EDD discipline
- Has written Evaluation Criteria (EC) for the review skill before building it
- Understands what a review covers that code generation misses: gaps between AC and implementation, plan-vs-code divergence, missing edge cases, untested failure modes
- Has seen the full Loop 1 chain assembled: epics-and-stories → plan-story → implement-story → review-implementation
- Can assess review quality: coverage completeness, risk identification, traceability back to AC
- Has applied the Load-Bearing Audit to the review-implementation skill
- Is ready to work with the Embedded Engineer on review work this week, transferring skills from the workspace to their real codebase

---

## Agenda

| Time | Block | Format |
|------|-------|--------|
| 0:00–0:15 | Check-in: what happened in Weeks 3–4? | Discussion |
| 0:15–0:40 | What a review covers — and what AI can and can't do | Presentation |
| 0:40–1:10 | Review generation — structured prompting demo | Demonstration |
| 1:10–1:30 | Break | |
| 1:30–1:45 | EDD: write your EC for review-implementation before building | Exercise |
| 1:45–2:30 | Lab 1: Build out the review-implementation skill | Hands-on Lab |
| 2:30–3:00 | Lab 2: Generate reviews; evaluate and audit | Hands-on Lab |
| 3:00–3:15 | Break | |
| 3:15–3:45 | The full chain — Loop 1 assembled | Group Discussion |
| 3:45–3:55 | Loop 1 retrospective | Reflection |
| 3:55–4:00 | Entering Loop 2 | Discussion |

---

## Detailed Block Notes

### Block 1: Check-in (15 min)

- Who used their plan-story and implement-story skills in Weeks 3–4? What EC scores did you see on the `sample-stories/` inputs?
- Embedded Engineer shares one real cross-role observation: how has the story + AC quality (from the workspace or the transfer to the real codebase) affected the plans and code? (anonymized)
- Transition: "Today we close the loop. The review-implementation skill is the last piece."

### Block 2: What a Review Covers — and What AI Can and Can't Do (25 min)

**What the review-implementation skill does:**
Given `stories.yaml` + `plan.yaml` + code, the review-implementation skill reads the upstream YAML artifacts and code, writes `review.yaml` (the review output), and **updates `stories.yaml`** — setting `review_status` and `review_notes` on the story being reviewed. This is the feedback loop: the review doesn't just produce a separate artifact; it flows back to update the original story artifact with review status and notes, so the story carries its own review state. The review identifies:
- Gaps between AC and implementation — which AC are satisfied, which are not, which are partially covered
- Plan-vs-code divergence — where the code deviates from the plan, and whether the deviation is justified
- Missing edge cases — edge cases identified in the plan but not handled in the code
- Untested failure modes — failure paths that exist in the AC but are not exercised
- Quality concerns — code structure, naming, error handling, anything that would fail a code review

**What a review covers that code generation misses:**
- Code generation produces code that *should* satisfy the AC; the review verifies whether it *actually* does
- Code generation follows the plan; the review checks whether the plan was correct
- The review is the feedback loop — it tells you where the chain broke down

**The human role in reviewing:**
- Deciding what risks matter most — AI can enumerate gaps but can't prioritize by business risk without context
- Determining whether a deviation from the plan is acceptable or a problem
- Making the call: does this implementation pass review, or does it go back?

**What AI can do:**
- Dramatically accelerate gap analysis, coverage checking, and review documentation
- Trace each AC to specific code locations and flag missing coverage
- Compare plan items to code and identify divergence

**What AI gets wrong:**
- Flagging false positives — identifying "gaps" that are actually handled differently but correctly
- Missing business-context risks that require domain knowledge
- Conflating code style preferences with actual quality issues

**The structure of a useful review:**
- AC coverage map: each AC → satisfied / partially / not satisfied, with evidence
- Plan compliance: each plan item → implemented / deviated / missing
- Risk areas: integration scenarios, failure modes, non-functional concerns
- Verdict: pass, pass with notes, or fail with specific remediation items

### Block 3: Review Generation — Structured Prompting Demo (30 min)

**Demonstration:** Trainer takes a sample story + AC + plan + code from `sample-stories/` pipeline outputs (from Sessions 1–2 work) and generates a review live using a RTCC-structured skill.

**Walk through the RTCC elements for review-implementation:**
- R: A senior engineer or QA lead with context about the system
- T: Given a story, its AC, the implementation plan, and the code, generate a review
- C (WHY): We need to verify that the implementation actually satisfies the story's AC and follows the plan. The review is the feedback loop that tells us whether the chain worked — and where it broke down. Without it, we're trusting that code generation produced correct output without checking.
- C (HOW): The system context, testing standards, risk areas to consider. Output must include: an AC coverage map (each AC mapped to satisfied/partially/not satisfied with evidence), a plan compliance check, identified risk areas, and a verdict. Must not duplicate line-by-line code review — focus on AC satisfaction and plan compliance.

**Walk through the output:**
- What's useful, what requires human judgment to complete
- One targeted adjustment: identify a gap the AI missed (e.g., an AC that's marked "satisfied" but the evidence is weak), add it to the skill's Constraints, regenerate

### EDD Exercise: Write Your EC Before Building (15 min)

Participants write Evaluation Criteria for review-implementation output before touching the skill.

**Suggested starting criteria:**
- Every AC from the story is addressed in the review (measurable: yes/no per AC)
- Each AC verdict includes evidence (code reference, test reference, or explanation) (measurable: yes/no per AC)
- At least one risk area is identified that code generation didn't address (measurable: yes/no)
- Plan compliance is checked: each plan item is marked as implemented, deviated, or missing (measurable: yes/no)
- The review does not duplicate line-by-line code review — it focuses on AC satisfaction and plan compliance (measurable: yes/no — requires judgment)
- A verdict is provided: pass, pass with notes, or fail with remediation (measurable: yes/no)

Participants may add criteria specific to their team's review standards.

### Lab 1: Build Out the review-implementation Skill (45 min)

- Each participant builds out the review-implementation skeleton skill in the workspace's `skills/` directory
- Use the RTCC elements from Block 3 as the template; populate with Context (WHY: why reviews matter, what a review enables) and Constraints (HOW: system context, testing standards, review format, what to include, what not to duplicate — the EE provides common conventions)
- Apply the Load-Bearing Rule as you build: for each instruction, identify which EC it corresponds to. If no EC would fail without it, don't add it.
- Testing participants: build this with your real review conventions in Constraints (the EE can help you adapt)
- Product/Process and Dev participants: build it too — understanding the downstream review improves your upstream work
- Use the story + AC + plan + code from Sessions 1–2 (run against `sample-stories/`) as input — the skill reads `stories.yaml` + `plan.yaml` + code, writes `review.yaml`, and **updates `stories.yaml`** (sets `review_status` and `review_notes` on the reviewed story)
- Commit the skill to `skills/`

#### Stretch Goals (for advanced users)

Write the review skill to check both backend (Express/TypeScript API routes, data validation) and frontend (React component structure, ShadCN component usage, Tailwind class conventions) aspects of the implementation. Include TypeScript type checking in the review criteria.

### Lab 2: Generate Reviews, Evaluate, and Apply the Load-Bearing Audit (30 min)

**Part 1 — Generate and evaluate (20 min):**
- Each participant runs their review-implementation skill on 1–2 sample stories from `sample-stories/` using the AC, plans, and code generated in Sessions 1–2
- Evaluate each review against the EC written in the EDD exercise
- Identify the most common gap in their output
- Key question: "Could you make a pass/fail decision from this review?" If not, what's missing?

**Part 2 — Load-Bearing Audit (10 min):**
- Review each instruction in the skill
- For each: which EC would fail if this instruction were removed?
- Check RTCC structure: background data in Context (WHY) should be in Constraints (HOW); intent in Constraints should be in Context
- Remove any instruction that corresponds to no EC; verify scores don't drop
- Commit the audited skill to `skills/`

#### Stretch Goals (for advanced users)

Run the review skill on a complete full-stack implementation (API + React component) from the pantry tracker. Compare the review quality when the skill sees both layers vs. only one.

### Block 4: The Full Chain — Loop 1 Assembled (30 min)

This is the moment to make the whole chain visible. This is the most important block of Loop 1.

**Walk through one complete story through the full pipeline (using a `sample-stories/` input):**
1. Story input → **epics-and-stories** skill → story with AC
2. Story + AC → **plan-story** skill → implementation plan
3. Plan → **implement-story** skill → code
4. Story + AC + plan + code → **review-implementation** skill → `review.yaml` + **updated `stories.yaml`** (review_status, review_notes)

**The feedback loop:** The review step doesn't just produce a standalone artifact. It writes `review.yaml` and **flows back to update the original `stories.yaml`** — setting `review_status` and `review_notes` on the story that was reviewed. This is what "closing the loop" means: the review feeds back into the original artifact, so the story carries its own review state. If the review finds gaps, the story's `review_status` reflects that, and the next iteration starts from the annotated artifact.

**Each step evaluated:**
- What quality did it produce? (EC scores from each session)
- Where did upstream decisions affect downstream output?
- Where did the chain break down?

**Discussion for all roles:**
- Product/Process: "Looking at the review, what would you change about how you wrote the stories and AC?"
- Dev: "What plan gaps did the review reveal? What would you change about the plan-story skill?"
- Testing: "What story/AC gaps made your review harder to generate? What plan/code gaps did the review catch?"

**This is not a blame conversation — it's a chain design conversation.** Everyone owns the whole chain. The review tells you where the chain is strong and where it's weak.

### Block 5: Loop 1 Retrospective (10 min)

Brief individual reflection: complete this sentence — "In Week 1 I couldn't [blank]. Now I can [blank]."

Share a few aloud — the Embedded Engineer captures these.

What's the one thing you'd change about your Session 1 epics-and-stories skill now, having used it for 5 weeks against the workspace and seen its output flow through the entire pipeline?

This is the transition into Loop 2: you've built the foundation — the full SDLC pipeline as skills. Now we make it rigorous.

### Block 6: Entering Loop 2 (5 min)

Preview of Loop 2: the next three sessions deepen the discipline, not add new artifacts.

- **Session 4:** Evaluation-Driven Development (EDD) formalization — you've been writing EC and evaluating outputs informally. Now we formalize: Python evaluation scripts with LLM judges. You'll have the AI write evaluation code for you — no Python prerequisite. The models carry the coding load; you direct and review.
- **Session 5:** Model invocation + adversarial agents — evaluating which skills are ready for the model to invoke automatically, and building adversarial prompts that challenge AI to find problems the evaluator missed.
- **Session 6:** Bounded agents + custom harness demo — participants build a bounded agent (full pipeline run in the IDE), the instructor demos a custom harness with clean context per step and evaluation at each step, plus a preview of the IIOS stage framework (Stage 3 vs Stage 4).

The program's end goal: not full integration, but every participant owning evaluated, iterated artifacts with a clear path to continued adoption.

---

## Session Artifacts

Each participant leaves with:
- [ ] Written Evaluation Criteria (EC) for review-implementation output (written before building)
- [ ] Committed review-implementation skill in `skills/` (skill file format, `disable-model-invocation: true`, RTCC structure, load-bearing audit completed)
- [ ] Reviews generated from 1–2 sample stories with EC scores noted
- [ ] `review.yaml` committed to the workspace for each reviewed story
- [ ] `stories.yaml` updated with `review_status` and `review_notes` on reviewed stories
- [ ] Loop 1 retrospective sentence (written)
- [ ] The full chain assembled: epics-and-stories → plan-story → implement-story → review-implementation

---

## Trainer Notes

- **The full chain assembly block is the most important moment of Loop 1.** Don't rush it or skip it. This is when participants see that the program is a coherent system, not four disconnected skills. Walk through one complete story end-to-end and evaluate quality at each step.
- **Product/Process and Testing participants who have been less engaged in Sessions 1–2 often become most engaged here** — they can finally see what their role contributes to and how the full pipeline works.
- **The EDD exercise before Lab 1 must happen before the lab — not after.** If participants built their skill in the break, push them back to EC first.
- **The retrospective should feel like a genuine reflection, not a checkbox.** If participants can't name something they've changed, push gently: "What did you do differently this sprint that you didn't do in Week 1?"
- **Loop 2 preview should generate curiosity, not anxiety.** The Python evaluation preview should emphasize: "the AI writes the evaluation code for you — you direct and review." No Python prerequisite. No mention of any specific evaluation tool — just the concept of Python evaluation scripts with LLM judges.
- **The chain connection is critical throughout this session.** The review-implementation skill consumes everything from Sessions 1–2: the story + AC from epics-and-stories, the plan from plan-story, the code from implement-story. Make the dependency visible in every block. All inputs come from `sample-stories/` pipeline outputs.
- The Embedded Engineer should come with a real example of the full chain running on a story from the engagement (from the workspace or the transfer to the real codebase) — ideally with EC scores at each step showing where the chain is strong and where it's weak.

**EE Transfer Model:** Between sessions, the EE helps participants transfer skills from the workspace to their real codebase. The workspace is the training ground; the real codebase is the application. All labs and demos work against the shared workspace — the EE coaches the transfer.

**Trainer repo push (after Session 3):** Nothing additional to push — the review-implementation skeleton is already in `skills/`.