# Training Session 6 — Bounded Agents, Custom Harness Demo & Stage 4 Preview: Program Close

*Week 11 | 4 Hours | All Participants | Loop 2 — Role Focus: Testing*

> **Loop 2 framing:** Session 6 is the final training session. By now participants have skills, evaluation scripts with LLM judges, iteration histories, adversarial agents, and for some, skills with model invocation enabled. This session has three purposes: (1) participants **build a bounded agent** — a multi-step workflow that chains the skills they already have into a full pipeline run within the IDE harness; (2) the instructor demonstrates a **custom harness** — a Python program that orchestrates multiple model calls with clean context per step, passes artifacts between steps, and evaluates each step programmatically — so participants see what the next level of a DLP would involve; (3) we preview the **Improving Intelligence Operating System (IIOS) stage framework** — where participants are now (Stage 3), what Stage 4 looks like, and what a future Stage 4 Deep Learning Program will cover; (4) we close the program with capstone, final assessment, and commitment statements.

---

## Why This Session Comes Last

Sessions 1–3 gave participants the SDLC pipeline as skills: epics-and-stories → plan-story → implement-story → review-implementation. Session 4 gave them the discipline to know if those skills are improving — Python evaluation scripts with LLM judges. Session 5 gave them adversarial agents to find problems the evaluator missed and the model invocation decision. Session 6 has participants compose those skills into a bounded agent — running the full pipeline in the IDE — then shows them what a custom harness looks like, previews the next stage of AI maturity, and closes the program.

**A bounded agent** is a multi-step workflow that runs within the IDE's built-in harness. Participants invoke their skills in sequence, review output at each step, and run evaluation scripts and adversarial agents manually. The context window carries artifacts between steps. This is the natural composition of everything they've built — and it's something they can do right now with the skills they already have.

**A custom harness** is a Python program that orchestrates multiple model calls with clean context per step, passes artifacts between steps programmatically, evaluates each step automatically, and manages the overall workflow. The IDE's built-in harness (Claude Code, Devin, etc.) accumulates context across steps and requires manual evaluation — the bounded agent works within this limitation. The custom harness solves it. The custom harness demo is instructor-led — participants see it, they do not build it in this session. Building one is the work of a future Stage 4 program.

This session also closes the program. The capstone elements — artifact showcase, final maturity assessment, and commitment statements — happen here because this is where the whole picture is visible for the first time.

---

## Session Goals

By end of this session, every participant:
- Has built a bounded agent — chained their existing skills into a full pipeline run (epics-and-stories → plan-story → implement-story → review-implementation) within the IDE harness, with manual evaluation and adversarial review at key steps
- Understands context window discipline: why bounded agents degrade at later steps as the context window accumulates, and what strategies help within the IDE
- Has seen the instructor demo a custom harness running the full chain with clean context per step, Python evaluation at each step, and adversarial agents at key points
- Understands the difference between a bounded agent (IDE harness, context window carries artifacts, manual evaluation) and a custom harness (Python program, clean context per step, automatic evaluation gates)
- Understands the Improving Intelligence Operating System (IIOS) stage framework and where they are: Stage 3 (Task) — building evaluated, iterated, and composed skills for real work
- Has a clear picture of what Stage 4 (Workflow) looks like and what a future Stage 4 Deep Learning Program would cover — without being expected to build a custom harness in this program
- Has presented their best artifact to a peer and articulated the evaluate-iterate discipline behind it
- Has completed the final AI Adoption Maturity Assessment
- Has stated a specific, observable commitment for their next sprint

---

## Agenda

| Time | Block | Format |
|------|-------|--------|
| 0:00–0:15 | Check-in: model invocation and adversarial agents since Session 5 | Discussion |
| 0:15–0:30 | What is a bounded agent? Multi-step orchestration in the IDE | Presentation + Discussion |
| 0:30–1:00 | Lab: Build a bounded agent — full pipeline run in the IDE | Lab |
| 1:00–1:30 | Context window discipline: why bounded agents degrade and what to do about it | Presentation + Discussion |
| 1:30–1:45 | Break | |
| 1:45–2:30 | Instructor demo: the full chain as a custom harness (requires API key) | Demo |
| 2:30–2:50 | The Improving Intelligence Operating System: Where You Are (Stage 3) and What Comes Next (Stage 4) | Presentation |
| 2:50–3:20 | Capstone: artifact showcase (pairs) | Peer Review |
| 3:20–3:35 | Final AI Adoption Maturity Assessment | Individual |
| 3:35–4:00 | Commitment statements and program close | Discussion |

---

## Detailed Block Notes

### Check-in (15 min)

Two questions:
1. *"Did anyone enable model invocation on a skill since Session 5? What happened?"*
2. *"Did anyone run their adversarial agent against real work? What did it catch?"*

**Embedded Engineer shares one real observation:** Either a successful model invocation from the Dev team (Weeks 9–10), or an adversarial agent that caught a significant problem the evaluator missed. Either story anchors the session's starting point.

**Transition:** "You've been building individual skills, evaluating them, and challenging them. Today you'll compose them into a bounded agent — running the full pipeline right here in your IDE. Then I'll show you what a custom harness looks like — the next level. And we'll close the program by looking at where you are and what comes next."

---

### What Is a Bounded Agent? Multi-Step Orchestration in the IDE (15 min)

**Reconnecting to Session 1:** In Session 1, we defined Prompt, Harness, Model. The model can only do what the harness allows. Sessions 1–5 used the IDE's built-in harness (Claude Code, Devin, etc.) — you invoke a skill, the harness runs the model, you get output. The IDE harness is single-step: one skill invocation, one model call, one output.

**But you can chain those single-step interactions together.** A bounded agent is a multi-step workflow that runs within the IDE's built-in harness. You invoke a skill, review the output, invoke the next skill, review that output, and so on. The context window carries the artifacts between steps — the output of epics-and-stories is in context when you invoke plan-story, and the plan is in context when you invoke implement-story.

This is not a new tool. It's not a Python program. It's not API calls. It's you, in your IDE, running the skills you've already built, in sequence, with your evaluation script and adversarial agent available at each step. The bounded agent is the natural composition of everything you've built in this program.

**What a bounded agent can do:**
- Run the full SDLC pipeline: epics-and-stories → plan-story → implement-story → review-implementation, all within one session
- Run the evaluation script after each step (you invoke it manually, but it runs)
- Run the adversarial agent after key steps (same — you invoke it, it runs)
- Produce a final artifact that includes all step outputs, all evaluation scores, and all adversarial findings

**What a bounded agent cannot do (and why custom harnesses exist):**
- It can't give each step its own clean context — the context window accumulates, and output quality may degrade at later steps
- It can't evaluate automatically at each step — you have to run the evaluation script manually
- It can't handle failures programmatically — if step 2 fails its evaluation, you decide what to do, not the harness
- It can't run unattended — you're in the loop at every step

**The bounded agent is real and useful.** For many workflows, it's sufficient. Running the full pipeline in one session with manual evaluation at each step is a genuine capability — it's what a Stage 3 practitioner does. The custom harness is what you build when you outgrow it.

**The v2 automation spectrum (where we are):**
```
Skills (invocation disabled) — Sessions 1–3
  → Skills (invocation enabled) — Session 5
    → Adversarial Agents — Session 5
      → Bounded Agents (multi-step in the IDE) — Session 6 (today, you build this)
        → Custom Harnesses (Python with API calls) — Stage 4 program (demo today, build later)
```

Each step extends what you can trust AI to do. Each step requires earning the right to the next one through evaluation evidence. **Bounded agents** are something you can build today with what you have. **Custom harnesses** are the next horizon, demoed today but built in a future Stage 4 program.

**Discussion:** Who has already run something like a bounded agent in their work — multiple skills in sequence, reviewing output at each step? What worked? Where did the context window accumulation cause problems?

---

### Lab: Build a Bounded Agent — Full Pipeline Run (30 min)

Participants build a bounded agent by running the full SDLC pipeline in a single IDE session. This is not a new artifact to create — it's the composition of skills they already have.

**Lab steps:**
1. Open a fresh session in your IDE (Claude Code, Devin, etc.)
2. Start with a sample story from `sample-stories/` in the workspace
3. Invoke the epics-and-stories skill — review the output (stories with AC)
4. Run the evaluation script from `evaluations/` against the AC output — note the EC scores
5. Invoke the plan-story skill with the story + AC in context — review the plan
6. Run the evaluation script against the plan output — note the EC scores
7. Invoke the implement-story skill with the plan in context — review the code
8. Run the adversarial agent from `adversarial-agents/` against the code output — note findings
9. Invoke the review-implementation skill with the story + AC + plan + code in context — review the review
10. Save the full session output as your bounded agent artifact

**What to watch for:** As you progress through the steps, notice how the context window fills. By step 4 (review-implementation), the model has the story, AC, plan, code, and adversarial findings all in context. Does the review quality differ from when you ran review-implementation in Session 3 with a clean context? This is the context window discipline question — and we'll discuss it next.

**Done when:** You've run all four SDLC skills in sequence in a single IDE session, with evaluation and adversarial review at key steps, and you can point to where the context window accumulation affected later steps. You've built a bounded agent — the full pipeline, orchestrated by you, in the IDE harness you already have.

---

### Context Window Discipline in a Bounded Agent (30 min)

**Why this matters:** You just ran the full pipeline in your bounded agent lab. You likely noticed something: the later steps didn't produce output as sharp as the earlier ones. That's not a model problem — it's a context window problem.

**The degradation pattern (what you just experienced):**
- Step 1 (epics-and-stories) had a clean context window: good output
- Step 2 (plan-story) had Step 1's output in context: still good, slightly constrained
- Step 3 (implement-story) had Steps 1 and 2 in context: noticeable quality difference in complex cases
- Step 4 (review-implementation) had everything in context: often where quality falls off a cliff in complex inputs

**Why this happens:** The model's attention is spread across the entire accumulated context. Earlier steps had a clean window — the model focused on the task. Later steps have the full history — the model has to navigate everything at once. The IDE harness doesn't manage this for you; the context window just grows.

**What you can do about it within the IDE:**
- Keep each step's output compact — verbose output crowds the next step even more
- Run evaluation at each step — catch quality degradation early, before it compounds
- If a step's output degrades, start a fresh session with only the prior artifact pasted in — a manual "clean context" workaround
- Accept that the bounded agent has a ceiling: for long pipelines, the context window will fill, and quality will degrade

This is the bounded agent's fundamental limitation. You can manage it, but you can't eliminate it within the IDE harness. The custom harness solves this by giving each step its own clean context — which is what you're about to see demonstrated.

**Discussion:** Where in your own workflows have you seen AI output quality drop mid-session? That experience — the IDE harness accumulating context — is the problem you just felt. What strategies have you tried?

---

### Instructor Demo: The Full Chain as a Custom Harness (45 min, requires API key)

The instructor demonstrates a custom harness that implements the full SDLC pipeline. This is a live demo — the instructor runs the harness and shows the output at each step. Participants observe; they do not build this in the session.

**What the harness does:**

The harness orchestrates YAML files between steps — each step reads upstream YAML artifacts and writes its own, so artifacts are passed structurally rather than through context window carryover.

1. **Story input** — The harness starts with a sample story from `sample-stories/` in the workspace
2. **epics-and-stories** — Calls the epics-and-stories skill from `skills/` with the story input. Captures the output (stories with AC). **Writes `stories.yaml`.**
3. **Evaluate AC output** — Runs the Python evaluation script from `evaluations/` against the stories + AC. Shows the EC scores. (This is the same evaluation pattern from Session 4.)
4. **plan-story** — Calls the plan-story skill from `skills/` with the story + AC. Captures the plan. **Reads `stories.yaml`, writes `plan.yaml`.**
5. **Evaluate plan output** — Runs the evaluation script against the plan. Shows the EC scores.
6. **implement-story** — Calls the implement-story skill from `skills/` with the plan. Captures the code. **Reads `plan.yaml`.**
7. **Adversarial agent on code** — Runs the adversarial prompt from `adversarial-agents/` against the code output. (This is the same adversarial pattern from Session 5.) Shows what the adversarial agent finds.
8. **review-implementation** — Calls the review-implementation skill from `skills/` with the story + AC + plan + code. Captures the review. **Reads `stories.yaml` + `plan.yaml` + code, writes `review.yaml`, and updates `stories.yaml` (sets `review_status` and `review_notes`).** This is the feedback loop from Session 3 — the review flows back to update the original story artifact.
9. **Final artifact** — The harness produces a complete package: `stories.yaml`, `plan.yaml`, code, `review.yaml`, and evaluation scores at each step. The final artifact is a document showing the full chain with quality scores at every step. The YAML artifacts carry the pipeline state.

**What to focus on during the demo:**
- Notice how the harness gives each step its own clean context — the context window accumulation you just experienced in the bounded agent lab doesn't happen here
- Notice how evaluation happens at each step, not just at the end — failures are caught early, not after downstream steps have built on bad output
- Notice how the adversarial agent at the code step catches things the code evaluator missed — the same complementary pairing from Session 5
- Notice that this is the same skills, the same evaluation scripts, and the same adversarial agents the participants have been building in the workspace all program — the harness just orchestrates them

**The key insight:** The custom harness doesn't replace the skills. It composes them. Everything participants have built in the workspace — the skills in `skills/`, the EC, the evaluation scripts in `evaluations/`, the adversarial agents in `adversarial-agents/` — becomes the building blocks. The harness is how you put them together into a production workflow. The full pipeline chain is described in the pipeline diagram below:

```
sample-stories/ ──► epics-and-stories ──► stories.yaml ──► plan-story ──► plan.yaml ──► implement-story ──► code ──► review-implementation ──► review.yaml
                                                          │                                                                  │
                                                          └──────────────────────────────────────────────────────────────────┘
                                                                          stories.yaml updated (review_status, review_notes)
```

---

### The IIOS Stage Framework: Where You Are (Stage 3) and What Comes Next (Stage 4) (35 min)

This block introduces the **Improving Intelligence Operating System (IIOS)** — Improving's framework for building, certifying, and operating AI capability. The IIOS defines stages of AI maturity with artifact-based certification criteria. This framework puts what you've built in this program into a larger context: where you are now, and what's ahead.

**The stage framework (power-law progression):**

| Stage | Name | What It Means | Median Effort |
|-------|------|---------------|---------------|
| 2 | Off the Shelf | Using AI tools as-is (Copilot, ChatGPT, Claude Code). Producing with AI but not measuring impact. | — |
| 3 | Task | Giving AI a defined task with real context. Crafting prompts deliberately, setting constraints, measuring improvement. | 18h |
| 4 | Workflow | Chaining multiple AI steps into a repeatable process with deterministic validation, adversarial agents, governance rules, and human punch-out points. | 172h (~10x Stage 3) |

**Where you are now: Stage 3 (Task)**

By completing this program, you should be at Stage 3. Stage 3 means:
- You give AI a defined task with real context, not ad-hoc prompting
- You craft skills deliberately using RTCC (WHO/WHAT/WHY/HOW)
- You measure improvement from prompt changes with Python evaluation scripts and LLM judges
- You iterate with evidence (3+ documented cycles), not opinion
- You can build adversarial agents that challenge your skills' output
- You make deliberate model invocation decisions (enable or document the gap)
- You can compose skills into bounded agents — multi-step workflows that chain skills in the IDE with manual evaluation at each step

The artifacts you've committed — skills in `skills/`, evaluation scripts in `evaluations/`, adversarial agents in `adversarial-agents/`, iteration histories, bounded agent runs — are Stage 3 artifacts. You own them. You can explain them. You can reproduce the quality. That is Stage 3.

**The Stage 3 ceiling:**

Stage 3 is powerful, but it has a ceiling. Everything is still personal — each person's skills reflect their own standards. Reviewing is still done by a human, one piece at a time. To compound, the team has to reconcile personal agents into shared workflows and move checking out of human heads and into systems. That's Stage 4.

**What Stage 4 (Workflow) looks like:**

Stage 4 is where the custom harness demo you just saw becomes real. At Stage 4:
- Multiple Stage 3 agents are wired into an end-to-end workflow with handoffs and branching logic
- An **automated harness or runner script** executes the workflow — not a human typing each step
- **Guardrails** run automatically between steps: adversarial review agents AND deterministic hooks that validate structure, content, and format
- **Human punch-out points** are explicitly defined and tested — places where a human must sign off regardless of what the agent can technically do
- An **end-to-end success rate** is measured — not just per-step accuracy, but the composite (at 95% per-step accuracy, a 20-step pipeline completes correctly only ~36% of the time)
- An **audit trail** traces any failure to its origin step, with per-step model and token/cost data

**What Stage 4 requires that Stage 3 doesn't:**

- **Team coordination with IT oversight** — Stage 4 is a team event, not an individual one. Personal agents must be reconciled into shared workflows. IT is pulled in because gates and pipelines live in shared infrastructure.
- **~10x the effort of Stage 3** — Stage 4 median effort is ~172h vs Stage 3's ~18h. This is not a small step. It's a different kind of work.
- **Solid Stage 3 foundations** — Weak foundations at Stage 3 accumulate as expensive back-work at Stage 4. A Stage 4 workflow built on unreliable Stage 3 agents is not faster; it is a "slop cannon" — errors compound through every connected step.

**Why we don't build a custom harness in this program:**

The jump from Stage 3 to Stage 4 is large — approximately 10x the effort, requiring team coordination, IT infrastructure, API access, and a different set of skills (orchestration, governance, audit trails). The custom harness demo shows you what the destination looks like so you can see the trajectory. But building one is the work of a future **Stage 4 Deep Learning Program** — a separate course designed for teams who have solid Stage 3 foundations and are ready to invest in production workflow integration.

**What the Stage 4 Deep Learning Program would cover:**

- Building and iterating a custom harness (Python program orchestrating multi-step workflows with API calls)
- Designing guardrails: deterministic hooks + adversarial review agents between every step
- Defining and testing human punch-out points (including bypass testing)
- Measuring end-to-end success rates and understanding compounding error math
- Building audit trails with per-step model, token, and cost data
- Reconciling personal Stage 3 skills into shared team workflows
- IT coordination for shared infrastructure (pipelines, gates, deployment)

**The key takeaway:** You leave this program at Stage 3. That is a real, significant achievement — you can build, evaluate, iterate, and adopt AI skills for your real work. Stage 4 is the next horizon, not the next session. When your team is ready, the Stage 4 Deep Learning Program will take you there.

---

### Capstone: Artifact Showcase (30 min)

In pairs, each participant presents three things from the workspace:

1. **Their most-used skill** — what it does, how it's structured using RTCC (WHO/WHAT/WHY/HOW), what the evaluation script showed, one improvement cycle they documented
2. **Their evaluation script + adversarial agent** — what the EC are, how many iterations the evaluator tracked, one thing they learned from the scores that surprised them, what the adversarial agent caught that the evaluator missed
3. **Their model invocation decision, adversarial agent, or their bounded agent run** — what it does, what the invocation boundary is, or where context window degradation showed up during the pipeline run

Partners ask one question each: *"What would you do differently if you started this over?"*

This is peer learning, not a formal presentation. The purpose is articulation: if you can't explain what you built and why it's better than where you started, you don't own it yet. The act of explaining to a peer is itself a diagnostic.

**Trainer and Embedded Engineer circulate:** Listen for participants who describe their work in terms of outputs ("it generates stories") rather than discipline ("I iterated it 4 times and the evaluator showed EC 3 was the hardest to satisfy"). The discipline framing is DLP Completion; the output framing is Basic Prompting.

---

### Final AI Adoption Maturity Assessment (20 min)

Participants complete the AI Adoption Maturity Assessment for the third time. This is the same 7-dimension, 21-question instrument used at Week 1 (baseline) and Week 7 (midpoint).

- Complete individually and honestly
- Not graded. The value is comparison with prior administrations, not the score in isolation
- DLP Completion signal: Dimensions 1–4 averaging 3.0+ per question

**Reflection questions** (written, not shared unless participant chooses):
- What's the hardest part of DLP Completion that you still don't have as a default behavior?
- What will you still be doing differently in 6 months that you weren't doing before this program?

The Embedded Engineer collects and cross-references against the Week 1 and Week 7 administrations, and against the Program Completion Rubric conversation in Week 12. Participants keep their own copy.

---

### Commitment Statements and Program Close (20 min)

Each participant states — out loud, to the group — one specific commitment:

> *"In my next sprint, I will [specific behavior change] that I could not or did not do before this program. I'll know I've done it when [specific artifact or outcome]."*

Not aspirations. Not "I'll use AI more." Specific, observable, next-sprint actions that can be checked.

**Trainer writes them down.** The Embedded Engineer also captures them. In Week 12, the Embedded Engineer will follow up with each participant individually on their commitment.

**Program close:** The Trainer summarizes what the group has built collectively — not generically, but specifically: the skills in `skills/`, evaluation scripts in `evaluations/`, adversarial agents in `adversarial-agents/`, and iterations that now live in the workspace. The Embedded Engineer acknowledges what they observed change in the team over 11 weeks (genuine and specific, not ceremonial). The Trainer previews what comes next: the Stage 4 Deep Learning Program for teams ready to move from individual skills to production workflows. Next steps: Week 12 wrap-up sessions, Program Completion Rubric, final artifact review.

---

## Session Artifacts

Each participant commits before leaving:

- [ ] **Bounded agent run** — the full pipeline session output (all 4 SDLC skills run in sequence with evaluation and adversarial review at key steps)
- [ ] **Capstone presentation notes** — the three artifacts presented to a peer, with the "what would you do differently" answer noted
- [ ] **Completed final AI Adoption Maturity Assessment** (7-dimension, 21-question instrument)
- [ ] **Written commitment statement** — specific, observable, next-sprint behavior change

---

## Trainer Notes

- **This session has a lab and a demo.** The bounded agent lab (30 min) is the hands-on portion — participants build something real with the skills they already have. The custom harness demo (45 min) is the centerpiece — it shows participants what the next level looks like. The custom harness is demonstrated, not assigned. Building one is the work of a future Stage 4 program.
- **The bounded agent lab is the payoff of the entire program.** Participants have been building individual skills for 10 weeks. The bounded agent lab is where they compose those skills into a multi-step workflow for the first time. Make this connection explicit — it's the moment everything connects.
- **The Prompt/Harness/Model arc from Session 1 closes here.** Session 1 defined the three terms and said the model can only do what the harness allows. Sessions 1–5 used the IDE's built-in harness. The bounded agent extends what the IDE harness can do. The custom harness demo reveals what's beyond it. Make this connection explicit — it's the conceptual payoff of the entire program.
- **The context window discipline concept should be taught after the bounded agent lab, not before.** Participants who just ran the full pipeline and felt the context window degrade at later steps will understand why context window discipline matters. Teaching it abstractly before the lab doesn't land. The experienced degradation makes the principle stick. Then the custom harness demo shows the solution.
- **The session flow is: build → feel the problem → see the solution.** Bounded agent lab (build) → context window discipline (feel the problem) → custom harness demo (see the solution). This sequence makes the demo the answer to a problem participants just experienced, not an abstract concept.
- **The IIOS stage framework block is a preview, not a sales pitch.** The purpose is to give participants a clear picture of where they are (Stage 3) and what's next (Stage 4) so they can make informed decisions about continued growth. Don't oversell Stage 4 — the 10x effort multiplier is real, and not every team needs it. But every team should know it exists and what it requires.
- **The Stage 3 ceiling discussion is important.** Some participants will feel like they've only scratched the surface. That's correct — Stage 3 has a ceiling (personal, one-at-a-time review). Naming the ceiling is not diminishing the achievement; it's being honest about what Stage 3 can and cannot do. The custom harness demo shows what breaking through that ceiling looks like.
- **The artifact showcase is intentionally peer-to-peer, not trainer-evaluated.** Resist the urge to add your evaluation. The goal is forcing participants to own and explain their work to a peer. Your job in this block is to circulate and listen for the discipline framing vs. output framing distinction.
- **The commitment statements are the most important output of this session.** Push for specificity ruthlessly. If a participant says "I'll keep using my skill every sprint," ask: "For which task? How often? How will you know it's getting better?" Keep pushing until the commitment is observable by someone other than the participant.
- **The Embedded Engineer's closing acknowledgment is not a performance.** It should name specific things that changed in specific people — things only the Embedded Engineer could know from 11 weeks of embedded work. A generic "you've all grown a lot" is a missed opportunity and participants will read it as hollow. Prepare it honestly. If the Embedded Engineer can't point to real changes they observed, the acknowledgment will ring false and undercut the program's close.

**EE Transfer Model:** Between sessions, the EE helps participants transfer skills from the workspace to their real codebase. The workspace is the training ground; the real codebase is the application. All labs and demos work against the shared workspace — the EE coaches the transfer.