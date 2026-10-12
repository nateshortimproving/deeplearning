# Trainer Implementation Guide
*Trainer Operational Playbook — Deep Learning Program (DLP) Engagement*

> **You own the 6 sessions. The Embedded Engineer owns the 12 weeks.** Your job is to deliver training that lands in the real work context participants are living — and to be a steady mentor to the Embedded Engineer who is embedded there every day.

---

## Before Session 1: Preparation Checklist

Allow at least one week before Session 1 for preparation. Do not show up cold.

### Know the Client Context

- [ ] Get a briefing from the Account Manager or Executive Coach — what is this client's business, why are they doing the DLP, what's the executive sponsor's framing?
- [ ] Understand which client teams are participating (e.g., Website team, CRM team) — these are teams of mixed roles, not role-based groups
- [ ] Know the approved AI tooling: what tools do participants have access to? What is blocked or restricted?
- [ ] Confirm API keys are available for Python evaluation scripts and LLM judges (the Account Manager / Executive Coach handles provisioning)
- [ ] Know the approximate distribution of roles among participants: how many Product/Process people, developers, Quality Assurance staff? (This affects your examples, not your session structure — all roles attend all sessions)
- [ ] Identify any known sensitivities or concerns the Account Manager or Executive Coach has flagged

### Coordinate with Your Embedded Engineer

- [ ] Receive the Embedded Engineer's artifact environment briefing: where are artifacts stored, what templates exist, who has access?
- [ ] Confirm the SDLC skeleton skills are available in the repository (all 7 with `disable-model-invocation: true`)
- [ ] Align on what "ready to work with the Embedded Engineer immediately after Session 1" means for this cohort
- [ ] Confirm Session 1 logistics: location, time, room setup, participant list
- [ ] Establish your standing weekly touchpoint (Embedded Engineer will send the invite — confirm receipt and accept it)
- [ ] Get the Embedded Engineer's honest assessment of where participants are starting: pre-Basic Prompting? Basic Prompting? Any outliers?

### Session 1 Material Preparation

- [ ] Customize your examples for this client's tech stack and domain
- [ ] Prepare the skill template for the `epics-and-stories` skeleton skill (or confirm the Embedded Engineer has it ready)
- [ ] Prepare demo outputs for `create-prd`, `create-architecture`, and `create-ux` (pre-generated so participants see the full pipeline)
- [ ] Prepare 2–3 "before and after" epics-and-stories examples using language relevant to this client
- [ ] Prepare your Prompt/Harness/Model conceptual block — this is new in v2 and foundational
- [ ] Know your Session 1 outcome: participants leave with a working `epics-and-stories` skill (with `disable-model-invocation: true`) they have personally tried, not just watched
- [ ] Confirm deck prompt file (`Session-1.deck.md`) is ready for the design harness to generate slides

### Your Own Calibration

- [ ] Review the DLP Completion criteria: Craft, Evaluate, Iterate, Adopt
- [ ] Remind yourself: **participant target is Basic Prompting → DLP Completion**
- [ ] Review what Loop 1 sessions are doing (building out the SDLC skeleton pipeline) vs. Loop 2 sessions (deepening discipline with Python evaluation, adversarial agents, and custom harnesses)
- [ ] Familiarize yourself with the 21-question, 7-dimension self-assessment instrument — you should be able to explain all 7 dimensions and their score ranges to participants
- [ ] Understand the Prompt/Harness/Model framework — you teach it in Session 1 and reference it throughout
- [ ] Understand the RTCC structure: WHO (Role) → WHAT (Task) → WHY (Context) → HOW (Constraints)
- [ ] Understand the EC/AC distinction and be ready to enforce it from Session 1

---

## Session Delivery Standards

### The All-Roles-Present Principle

Every participant attends every session — Product/Process, developers, and Quality Assurance alike. This is not optional and is not a mistake.

**Why it matters:** DLP Completion requires understanding how AI-assisted work connects across a delivery pipeline. A developer who has never seen how epics-and-stories are generated, and a Product Manager who has never seen how plans and code are generated from those stories, are both weaker for it. Shared language across roles is a program outcome, not a side effect.

**How to honor it in delivery:** Do not teach to only one role's perspective. When you deliver Session 2 (The Development Loop), the developers are doing primary hands-on work — but you are also showing Product/Process people and Quality Assurance participants why this matters and how it connects to their work.

### Artifact-First Design

Sessions are not lectures about AI. Sessions are working sessions where participants produce artifacts.

**What this means in practice:**
- At least 50% of session time should be hands-on, not instruction
- Every session ends with a committed artifact (or a draft committed before the next session)
- Concepts are introduced *just in time* — explain the thing participants are about to do, not everything that could ever be said about it
- Do not front-load theory. Show the artifact first, then explain why it's built that way

### What Makes a Good Session

| Quality | What it looks like |
|---------|--------------------|
| **Grounded in this client's reality** | Examples use their terminology, their stack, their actual work context — not generic lorem ipsum examples |
| **Participants do the work** | You facilitate; they produce |
| **Artifacts leave the room** | Not notes, not slides — an actual committed artifact |
| **Confusion is surfaced, not papered over** | When something doesn't land, name it and address it |
| **DLP Completion criteria visible throughout** | Participants should hear "Craft / Evaluate / Iterate / Adopt" across all 6 sessions, not just at the end |

### Session Pacing

Each session is 4 hours. Rough structure:

| Time | Block |
|------|-------|
| 0:00–0:30 | Opening: connect to prior work; what we're doing today and why |
| 0:30–1:30 | Concept + demo: introduce the technique with a real example |
| 1:30–2:00 | Break |
| 2:00–3:30 | Hands-on: participants work, you and Embedded Engineer circulate and support |
| 3:30–4:00 | Debrief + commit: review what was produced; commit or assign commit; preview next session |

Adjust as needed, but protect the hands-on block. If you run long on concept, cut from the opening — not from the work time.

### Deck Files

Decks are generated from `.deck.md` prompt files by a design harness. There are no PPTX files in the repository — the deck prompt files are the source for slide generation. Before each session, confirm the deck prompt file is ready and the design harness has generated the slides.

---

## Weekly Embedded Engineer Touchpoint

The Embedded Engineer owns scheduling this. You should have a standing 30-minute weekly invite on your calendar for the full 12 weeks. Accept it and keep it.

### What the Embedded Engineer Will Bring

Expect the Embedded Engineer to come with:
- Participant progress observations (specific, not general)
- A coaching challenge they're facing
- Questions from participants that came up during the week
- An artifact example for review
- Prep questions if a session is coming up

### What to Listen For

| Signal | What it means |
|--------|--------------|
| Embedded Engineer is doing more showing than asking | Embedded Engineer may be rescuing participants instead of coaching — gently redirect |
| Participants aren't committing artifacts | Either the Embedded Engineer isn't holding the expectation or something is blocking adoption — dig in |
| Same coaching challenge for 3+ weeks | The Embedded Engineer needs a different technique; what you've offered isn't working — try something else |
| Manager resistance showing up | Do not try to solve this in the touchpoint; flag it to Account Manager or Executive Coach (or confirm Embedded Engineer has already done so) |
| "Everything is fine" with no specifics | Push for specifics; a touchpoint with no problems is usually a touchpoint where problems are hidden |

### How to Mentor vs. Escalate

**Mentor in the touchpoint:**
- Coaching technique questions ("How do I get this participant to stop depending on me for every skill decision?")
- Artifact quality questions ("Is this Python evaluation approach rigorous enough?")
- Embedded Engineer confidence issues ("I'm not sure I know enough to coach adversarial agents")
- Participant-level resistance and disengagement

**Escalate after the touchpoint (notify Account Manager or Executive Coach):**
- Manager blocking participation
- Participation rates falling without explanation
- Embedded Engineer reports a situation that sounds like a client relationship problem, not a coaching problem
- Anything that requires changing the engagement structure or scope

### Capturing Program Design Feedback

If the Embedded Engineer flags something that isn't working about the program design itself — a concept that isn't landing, a session sequence that doesn't match participant readiness, an artifact template that doesn't fit this client — capture it explicitly.

In your own session prep notes, use a `[PROGRAM FEEDBACK]` tag for these items. After the engagement, compile them for a program design debrief.

---

## Between Sessions: What You Do in the 2 Weeks Between

Sessions are approximately every two weeks. The weeks between sessions are not idle weeks.

### Week After Each Session

- [ ] Review artifacts committed during the session and in the days immediately after
- [ ] Send the Embedded Engineer any observations from session delivery that they should know: "I noticed participant X struggled with Python evaluation — watch for that in coaching this week"
- [ ] Note what landed and what didn't; start the revision list for next session

### Week Before Each Session

- [ ] Attend (or review notes from) your weekly Embedded Engineer touchpoint with extra attention to field observations
- [ ] Pull 1–2 real artifacts from the engagement to use as examples in the next session — with participant permission
- [ ] Adapt your next session plan based on what the Embedded Engineer has reported: if participants are stuck on a specific concept, that becomes the center of the next session, not a footnote
- [ ] Prepare any new templates or worked examples that reflect what you've learned from the field
- [ ] Confirm the deck prompt file for the next session is ready for the design harness

### The Most Important Between-Session Practice

**Use real artifacts from this engagement in the next session.**

Not hypothetical examples. Not examples from a previous client (unless anonymized and genuinely relevant). Artifacts that participants in this cohort actually produced. This does two things: it validates their work, and it sharpens everyone's ability to evaluate what "good" looks like for *their* context.

Get the Embedded Engineer to identify the best 1–2 artifacts from each two-week cycle. Use those in the next session's worked examples.

---

## Sessions 1–3 Posture (Loop 1): Building the SDLC Skeleton Pipeline

Loop 1 is about giving participants the language, the mechanics, and their first real artifacts. They are starting from Basic Prompting — they use AI off-the-shelf, but they have not built skills, used evaluators, or changed their default workflow behaviors. The SDLC skeleton skills are introduced in Session 1 and built out across Sessions 1–3.

### Session 1 (Week 1) — Prompt/Harness/Model + SDLC Skeleton Skills + Epics & Stories Generation

**Participant starting point:** They may have used AI for informal tasks, but they have not used it systematically for epics-and-stories generation. Many will be skeptical it can improve their existing process.

**Your job:** Leave every participant with a working `epics-and-stories` skill they have personally tested on a real story. Not a template they copied — a skill they actually ran and got output from. The skill has `disable-model-invocation: true` and uses RTCC structure.

**New content in v2:**
- **Prompt/Harness/Model** — teach this early, before RTCC. It's the foundational conceptual framework that makes the rest of the program make sense. Prompt = instructions. Harness = software environment that mediates between you and the model. Model = the AI. The harness controls invocation, not the model. This is why we set `disable-model-invocation: true`.
- **SDLC skeleton skills introduced** — walk through all 7 in pipeline order. Show demo outputs for `create-prd`, `create-architecture`, `create-ux`. The primary build-out target is `epics-and-stories`.
- **EC/AC disambiguation** — participants build a skill that generates Acceptance Criteria (AC) and simultaneously write Evaluation Criteria (EC) for that skill. Enforce the distinction from the start.

**Tone:** Curious and practical. "Let's find out what this can do for your actual work." Not evangelical. Not "AI is going to change everything." Show, don't tell.

**Calibration cues:**
- If participants' skills are producing usable output on the first try, they're ahead of baseline — move faster
- If participants are confused about what a "skill" even is, slow down and do more live demonstration
- Never assume Basic Prompting means the same thing across all participants

### Session 2 (Week 3) — The Development Loop: `plan-story` + `implement-story`

**Participant starting point:** They've had 2 weeks with the Embedded Engineer on `epics-and-stories` generation. Some will have committed artifacts; some will not. The Embedded Engineer will have told you which.

**Your job:** Connect Session 2 content back to Session 1 artifacts. The epics-and-stories → plan-story → implement-story chain should be visible. Participants should understand they're building out the SDLC skeleton pipeline, even at this early stage. The `plan-story` and `implement-story` skills are the primary build-out targets.

**Key lesson:** Plan quality determines code quality. A vague plan produces vague code; a specific plan produces specific code. This is the upstream quality dependency lesson — more universal than v1's AC → Test dependency.

**For non-developers in the room:** Make the Plan → Code connection to their work explicit. Quality Assurance participants are not just watching a developer session — they are seeing how review-implementation (Session 3) will integrate with what developers are generating.

**Watch for:** Participants who skip the plan step and go straight to code generation. The discipline is: plan first, evaluate the plan, then generate code from the plan.

### Session 3 (Week 5) — Review Implementation: `review-implementation`

**Participant starting point:** They have 4 weeks of artifacts. They have attended 2 sessions. By now, the participants who are engaged are starting to see the pipeline. Those who aren't engaged are clearer to identify.

**Your job:** Complete the Loop 1 pipeline — participants now have artifact experience in all three role-focus areas (epics-and-stories, plan-story/implement-story, review-implementation). The Loop 1 story should be visible in the debrief: "You now have skills across the whole SDLC skeleton pipeline."

**Set up Loop 2:** In the Session 3 debrief, explicitly preview what Loop 2 is about — not more techniques, but deeper discipline. The question for the second half of the program is not "can you use AI for this?" but "are you actually using it, and is it getting better?" Preview Python evaluations + LLM judges coming in Session 4.

---

## Sessions 4–6 Posture (Loop 2): Deepening the Discipline

By Session 4, participants have 6 weeks of lived experience and a set of real artifacts. Loop 2 sessions are not introductions — they are reckonings. Participants are being asked to evaluate whether they've actually changed, not just whether they've tried.

### Session 4 (Week 7) — EDD with Python Evaluations + LLM Judges

**Participant starting point:** They have 6 weeks of skills built out from the SDLC skeleton pipeline. The Embedded Engineer did NOT pre-teach Python evaluation in Week 6 — participants have been evaluating informally against EC written in Sessions 1–3. Most have been iterating intuitively ("I changed it and it seems better") without structured measurement.

**Your job:** Introduce Python evaluation scripts with LLM judges as the measurement tool. EDD is Red/Green/Refactor applied to skills: write EC before building, run a baseline, make the EC pass, then audit for dead instructions. The AI writes the evaluation code — participants direct and evaluate. No Python prerequisite. Make the Red step concrete: "Write 4–6 EC that your current skill fails. Now fix it." This framing — EC first, not intuition first — is the discipline shift.

**The LLM judge pattern:** Send skill output + EC to a model, receive structured judgment (pass/fail, score, reasoning). This is how production AI systems measure quality. Teaching this pattern directly gives participants a deeper understanding of evaluation.

**The resistance you will encounter:** "This feels like overhead." Address it directly: "The overhead is front-loaded. Once your Python evaluation script exists, improving the skill takes minutes, not guesswork. You've been doing the guesswork version for 6 weeks."

**Session outcome:** Every participant has a Python evaluation script for one of their existing skills — with at least one documented iteration cycle from this session.

### Session 5 (Week 9) — Model Invocation + Adversarial Agent Prompts

**Participant starting point:** They have skills — some well-validated with Python evaluation iterations, others still rough. All have `disable-model-invocation: true`. They have not yet considered which ones could be invoked automatically by the model.

**Part A: Enabling Model Invocation (~60 min)**
Revisit the `disable-model-invocation` flag from Session 1. The question is: "Which of your skills is ready for the model to invoke automatically?" The three graduation criteria (exact trigger inputs, output specification, 3+ verified trigger test cases) apply — but now they're about flipping a config flag on an existing, well-evaluated skill. Lab: evaluate one skill against the three criteria.

**Part B: Adversarial Agent Prompts (~75 min)**
An adversarial agent is a prompt that receives the output of another skill and attempts to find problems — missing requirements, logical errors, edge cases the primary skill missed, quality gaps the evaluation script didn't catch. It's AI-native (a prompt, not code), accessible to all roles. It complements the Python evaluation script: evaluation measures against EC; adversarial agents find problems the EC didn't anticipate. Lab: write an adversarial prompt for one skill. Run it against real outputs.

**The real work of Session 5:** Have participants apply the three graduation criteria to their most-used skill AND build an adversarial agent. For model invocation: does it pass? What specifically is missing? For adversarial agents: what does it find that the evaluation script missed?

**Watch for:** Participants who want to enable model invocation on skills with fewer than 3 Python evaluation iteration cycles. The prerequisite is EDD-validated skills — not popular ones. Check the history before agreeing.

### Session 6 (Week 11) — Bounded Agents, Custom Harness Demo & Stage 4 Preview

**Participant starting point:** They are 10 weeks into the program. They have skills (some with model invocation enabled), Python evaluation scripts, and adversarial agents. The Embedded Engineer has been working toward a full-chain demonstration this week.

**Your job:** Complete the Prompt/Harness/Model conceptual arc from Session 1. Sessions 1–5 used the IDE's built-in harness. The bounded agent extends what the IDE harness can do — chaining skills into multi-step workflows. The custom harness demo reveals what's beyond it — Python programmatic orchestration with clean context per step.

**Session 6 has a lab and a demo:**
- **Bounded agent lab (hands-on, no API key required):** Participants run the full SDLC pipeline (epics-and-stories → plan-story → implement-story → review-implementation) in a single IDE session, with manual evaluation and adversarial review at key steps. The context window carries artifacts between steps.
- **Context window discipline (discussion):** Participants experience context window degradation at later steps in the bounded agent lab, then discuss why it happens and what strategies help within the IDE.
- **Instructor demo (requires API key):** Demonstrate a custom harness implementing the full chain — Story → AC → Plan → Code → Review. Each step gets clean context, evaluated with a Python evaluation script + LLM judge. An adversarial agent runs against the code output. Final artifact with evaluation scores at each step. The custom harness is demonstrated, not assigned — building one is the work of a future Stage 4 program.
- **IIOS stage framework preview:** Where participants are (Stage 3: Task) and what comes next (Stage 4: Workflow, ~10x effort).

**Session 6 tone:** Celebratory but honest. Participants have done real work across 12 weeks. The capstone artifact showcase (peer pairs presenting their most-used skill, its RTCC structure, Python evaluation history, and one specific thing they learned from the scores) is the evidence of that. Name what they've built before asking them to look forward.

**Self-assessment and close:** Administer the final AI Adoption Maturity Assessment (7 dimensions, 21 questions) in session. Commitment statements follow: specific, observable, next-sprint behavior changes. Explain that the 7-dimension instrument gives participants a structured way to see where they've grown. Participants scoring in the 43–58 range have reached DLP Completion; those approaching 59+ are deepening their practice. This framing helps them approach the final assessment as a learning tool, not just a checkbox.

---

## Program Completion: Week 12

### Rubric Co-Assessment with the Embedded Engineer

The Program Completion Rubric is completed jointly with the Embedded Engineer. Complete your independent assessment before the joint review, then align.

**DLP Completion Criteria:**

| Criterion | What you're assessing |
|-----------|----------------------|
| **Craft** | Has the participant built at least one skill and adversarial agent in their actual work context? |
| **Evaluate** | Has the participant used Python evaluation scripts with LLM judges — demonstrably, not just by report? |
| **Iterate** | Is there documented evidence of hypothesis → result → improvement on at least one artifact? |
| **Adopt** | Is new AI-assisted behavior the participant's default behavior, not a special-occasion behavior? |

**Rating:** Met / Partial / Not Met with one line of evidence per criterion per participant.

**Self-assessment corroboration:** Cross-reference rubric ratings against participants' Week 12 self-assessment scores from the 21-question, 7-dimension instrument. Participants who have achieved DLP Completion should score 3.0+ averages on Dimensions 1–4 (Prompt Engineering & AI Interaction, Task Agents & Single-Box Automation, Workflow Orchestration & Coordination, and Output Evaluation & Quality Judgment), with a total score in the 43–58 range. Significant gaps between your rubric ratings and a participant's self-assessment scores are useful conversation starters in the joint Embedded Engineer review.

**Disagreements between you and the Embedded Engineer are useful data.** If you rate a participant differently, that means one of you has information the other doesn't. Work it out — the final rubric should represent a shared, honest assessment.

### Final Debrief

After Week 12, conduct a full program debrief. This is not a client-facing meeting — it is an internal Improving conversation.

**Who participates:** You, the Embedded Engineer, the Account Manager or Executive Coach.

**Agenda:**
1. Participant outcomes summary — rubric results, notable wins, risks
2. What the program design got right for this cohort
3. What the program design got wrong or needed adjustment
4. Embedded Engineer performance feedback (honest — this feeds Embedded Engineer development)
5. Recommendations for the next cohort

**[PROGRAM FEEDBACK] items:** Compile all tagged program design feedback from your session notes and the Embedded Engineer's field notes. These go to whoever owns the program design improvement cycle.

### What You Leave Behind

When the engagement closes, these materials should exist:

- [ ] Completed Program Completion Rubric (joint, signed off by you and Embedded Engineer)
- [ ] Your session delivery notes (6 sessions, including what you adjusted and why)
- [ ] Compiled `[PROGRAM FEEDBACK]` items
- [ ] 1–2 artifact examples from this cohort that could be anonymized and used in future sessions as exemplars

---

*This guide is a working document. If the program design doesn't match what you're encountering in the field, tag it, surface it in your next Embedded Engineer touchpoint, and escalate to the program design owner.*