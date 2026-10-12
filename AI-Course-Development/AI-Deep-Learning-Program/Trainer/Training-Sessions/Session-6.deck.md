# Session 6 Deck Prompt — Bounded Agents, Custom Harness Demo & Stage 4 Preview (v3)
*Week 11 | Loop 2 | Role Focus: Testing*

---

## Intro Slide

**Title:** Bounded Agents, Custom Harness Demo & Stage 4 Preview
**Week:** 11 | **Loop:** 2 | **Role Focus:** Testing
**Framing:** In Session 1 we defined Prompt, Harness, and Model. You've been using your IDE's built-in harness for 10 weeks. Today you'll build a bounded agent — a multi-step workflow that chains the skills you already have into a full pipeline run, right in your IDE. Then the instructor demos what a custom harness looks like — a Python program that orchestrates multiple model calls with clean context and evaluation at each step, showing you what the next level of a DLP would involve. You'll also see where you are in the Improving Intelligence Operating System (Stage 3) and what comes next (Stage 4). Then we close the program.

---

## Check-In Slide

**Question:** Did anyone enable model invocation on a skill since Session 5? What happened — did the model invoke when it should? Did it stay silent when it shouldn't? And: what's the skill you've run most across the full program? Could you describe its invocation boundary?

*This question connects Session 5's model invocation and adversarial agent work to Session 6's bounded agent concept. Skills with enabled invocation are the building blocks of a bounded agent workflow.*

---

## Session Goals Slide

**Goal 1: Build a bounded agent — chain your existing skills into a multi-step workflow in the IDE**
- **Product/Process:** You'll run the full SDLC pipeline — epics-and-stories → plan-story → implement-story → review-implementation — in a single IDE session, with the context window carrying artifacts between steps. This is the natural composition of everything you've built.
- **Development:** You'll use a workflow prompt to tie together the skills you've already created, running each in sequence and reviewing output at each step. You'll run your evaluation script and adversarial agent manually at key points. This is what a Stage 3 practitioner does.
- **Testing:** You'll run the review-implementation skill as the final step, consuming all prior outputs. You'll experience how the context window accumulates across the full chain — and see why later steps may degrade.

**Goal 2: See a custom harness demonstrated — the full chain with clean context and evaluation at each step**
- **Product/Process:** You'll see your epics-and-stories skill running inside a custom harness, with its output evaluated by a Python script and LLM judge before being passed to the next step. This is the next horizon — what your skills look like in production.
- **Development:** You'll see plan-story → implement-story running inside the harness, with adversarial agents challenging the output at each step. Your skills are the building blocks; the harness is the composition.
- **Testing:** You'll see the review-implementation skill consuming the output of every prior step, evaluated by its own Python script. The full chain, orchestrated and measured. This is the destination.

**Goal 3: Understand the IIOS stage framework — where you are (Stage 3) and what comes next (Stage 4)**
- **Product/Process:** You are at Stage 3 (Task) — you can build, evaluate, and iterate skills for real work. Stage 4 (Workflow) is where those skills connect into shared, governed workflows. A future Stage 4 Deep Learning Program takes you there.
- **Development:** Stage 3 is individual: your skills, your evaluation, your iteration. Stage 4 is team + IT: shared workflows, automated guardrails, audit trails, end-to-end success rates. The effort scales ~10x.
- **Testing:** Stage 3 means you review output one piece at a time, by hand. Stage 4 means the quality gates are automated between steps. The review-implementation skill you built is Stage 3; wrapping it in a harness with guardrails is Stage 4.

**Goal 4: Complete the capstone, final assessment, and commitment statements**
- **Product/Process:** You'll present your best skill to a peer — its RTCC structure, your Python evaluator, your improvement cycles, and one thing you learned from the scores.
- **Development:** You'll present your Plan or implement-story skill (or adversarial agent) with the same discipline framing — not "it generates code" but "I iterated it 4 times and the evaluator showed EC 3 was the hardest to satisfy."
- **Testing:** You'll present your review-implementation skill with evaluation history and iteration evidence. And you'll state a specific, observable commitment for your next sprint.

---

## Lecture Slide — Bounded Agents: Multi-Step Orchestration in the IDE

**Content to teach:**

Before we look at custom harnesses, let's talk about what you can build right now with the IDE harness you've been using for 10 weeks.

A **bounded agent** is a multi-step workflow that runs within the IDE's built-in harness. You invoke a skill, review the output, invoke the next skill, review that output, and so on. The context window carries the artifacts between steps.

What a bounded agent can do:
- Run the full SDLC pipeline: epics-and-stories → plan-story → implement-story → review-implementation, all within one session
- Run the evaluation script after each step (you invoke it manually)
- Run the adversarial agent after key steps (same — you invoke it)
- Produce a final artifact with all step outputs, evaluation scores, and adversarial findings

What a bounded agent cannot do (and why custom harnesses exist):
- Clean context per step — the context window accumulates, output quality may degrade
- Automatic evaluation at each step — you run the evaluation script manually
- Programmatic failure handling — you decide what to do, not the harness
- Unattended execution — you're in the loop at every step

The bounded agent is real and useful. For many workflows, it's sufficient. The custom harness is what you build when you outgrow it.

---

## Exercise Slide — Build a Bounded Agent: Full Pipeline Run

**Lab Name:** Bounded Agent — Full SDLC Pipeline in the IDE
**Lab Timing:** 30 minutes
**Lab Steps:**
1. Open a fresh session in your IDE (Claude Code, Devin, etc.)
2. Start with a sample story from `sample-stories/` in the workspace
3. Invoke your epics-and-stories skill — review the output (stories with AC)
4. Run your evaluation script from `evaluations/` against the AC output — note the EC scores
5. Invoke your plan-story skill with the story + AC in context — review the plan
6. Run your evaluation script against the plan output — note the EC scores
7. Invoke your implement-story skill with the plan in context — review the code
8. Run your adversarial agent from `adversarial-agents/` against the code output — note findings
9. Invoke your review-implementation skill with the story + AC + plan + code in context — review the review
10. Save the full session output as your bounded agent artifact

**You'll know when you're done because...** you've run all four SDLC skills in sequence in a single IDE session, with evaluation and adversarial review at key steps, and you can point to where the context window accumulation affected later steps. You've built a bounded agent — the full pipeline, orchestrated by you, in the IDE harness you already have.

---

## Lecture Slide — Context Window Discipline in a Bounded Agent

**Content to teach:**

You just ran the full pipeline in one session. You likely noticed something: the later steps didn't produce output as sharp as the earlier ones. That's not a model problem — it's a context window problem.

The degradation pattern in a single long context:
- Step 1 has a clean context window: good output
- Step 2 has Step 1's output in context: slightly constrained
- Step 3 has Steps 1 and 2 in context: noticeable quality loss
- Step 4+: quality falls off a cliff in complex inputs

Why this happens: the model's attention is spread across the entire accumulated context. Earlier steps had a clean window — the model focused on the task. Later steps have the full history — the model has to navigate everything at once.

What you can do about it within the IDE:
- Keep each step's output compact — verbose output crowds the next step even more
- Run evaluation at each step — catch quality degradation early, before it compounds
- If a step's output degrades, start a fresh session with only the prior artifact pasted in — a manual "clean context" workaround
- Accept that the bounded agent has a ceiling: for long pipelines, the context window will fill, and quality will degrade

This is the bounded agent's fundamental limitation. You can manage it, but you can't eliminate it within the IDE harness. The custom harness solves this by giving each step its own clean context — which is what you're about to see demonstrated.

---

## Lecture Slide — From Bounded Agent to Custom Harness

**Content to teach:**

From Session 1: the model can only do what the harness allows. Your IDE's built-in harness is designed for single-step interactions: you invoke a skill, the model produces output, you review it. A bounded agent chains these single-step interactions together — but the IDE harness still manages each step, and the context window accumulates.

When you need more than the bounded agent provides — clean context per step, automatic evaluation gates, programmatic failure handling, unattended execution — you build a **custom harness**: a Python program that:
1. Calls the model API directly (not through the IDE)
2. Passes artifacts between steps (the AC output becomes the Plan input)
3. Runs Python evaluation scripts at each step (from Session 4)
4. Runs adversarial agents at key points (from Session 5)
5. Handles failures (if evaluation fails at step 2, does it retry? halt? notify a human?)
6. Produces a final artifact with evaluation scores at each step

This is the natural extension of what participants have been building:
- Session 4: Python evaluation scripts that call the model API → custom harnesses call the model API
- Session 5: Adversarial agents that receive another skill's output → custom harnesses pass output between steps
- Session 6: the harness ties it all together — you see it demonstrated today

The custom harness doesn't replace your bounded agent. It's what you build when you outgrow it. The bounded agent is Stage 3 — real, useful, buildable today. The custom harness is Stage 4 — the next horizon, demoed now but built in a future program.

---

## Demo Slide — Custom Harness: The Full Chain

**Description:** The instructor demonstrates a custom harness (Python program) that implements the full chain: Story → epics-and-stories → plan-story → implement-story → review-implementation. The harness calls the model API at each step, runs a Python evaluation script (from Session 4) after each step, runs an adversarial agent (from Session 5) at key points, and produces a final artifact with evaluation scores at each step. This demo requires an API key and is instructor-led — participants observe, they do not build this in the session.

**What to focus on:** As the demo runs, notice how each step is a separate API call with its own clean context — the problem you just experienced in the bounded agent lab doesn't happen here. Watch how the evaluation script runs after each step — if a step's evaluation score is below threshold, the harness can retry or flag for human review. See how the adversarial agent challenges the output before it's passed to the next step. The harness orchestrates YAML files between steps — stories.yaml, plan.yaml, review.yaml — each step's output is written to a YAML artifact that the next step reads as input, making the pipeline's data flow explicit and inspectable. Notice the final artifact: it contains all step outputs, all evaluation scores, and all adversarial findings in a single document. This is what production AI workflow integration looks like.

---

## Compare/Contrast Slide — IDE Single-Step vs. Bounded Agent vs. Custom Harness

| IDE Harness (Sessions 1-5) | Bounded Agent (Session 6 Lab) | Custom Harness (Session 6 Demo) |
|---|---|---|
| Single-step: you invoke a skill, get output | Multi-step: you chain skills in sequence, review at each step | Multi-step: harness orchestrates the full chain |
| Clean context per invocation | Context accumulates across the session — quality degrades | Each step gets a clean context — no accumulation |
| Evaluation runs when you decide to run it | Evaluation runs when you decide to run it | Evaluation runs automatically at each step |
| You manually pass output to the next skill | Context window carries artifacts between steps | Harness passes artifacts between steps automatically |
| No programmatic failure handling | You decide what to do at each failure | Harness can retry, halt, or notify on evaluation failure |
| You're in the loop at every step | You're in the loop at every step | Unattended execution possible |

---

## Lecture Slide — The Intelligence OS: Stage 3 (Where You Are)

**Content to teach:**

The Improving Intelligence Operating System (IIOS) is Improving's framework for AI maturity. It defines stages with artifact-based certification criteria.

**Stage 2: Off the Shelf** — Using AI tools as-is (Copilot, ChatGPT, Claude Code). Producing with AI but not measuring. No structured prompt framework.

**Stage 3: Task** — Giving AI a defined task with real context. Crafting prompts deliberately. Measuring improvement from prompt changes. This is where you are.

You are at Stage 3 because you can:
- Build skills using RTCC (WHO/WHAT/WHY/HOW) — not ad-hoc prompting
- Write Evaluation Criteria (EC) before building — not subjective "looks good"
- Run Python evaluation scripts with LLM judges — not guessing at quality
- Iterate with 3+ documented cycles — not one-and-done
- Build adversarial agents that challenge output — not rubber-stamping
- Make deliberate model invocation decisions — not auto-invoking everything
- Build bounded agents that chain skills into multi-step workflows — not just single-step interactions

The artifacts in your workspace — skills, evaluation scripts, adversarial agents, iteration histories, bounded agent runs — are Stage 3 artifacts. You own them. You can explain them. You can reproduce the quality.

**The Stage 3 ceiling:** Everything is still personal. Each person's skills reflect their own standards. Reviewing is done by a human, one piece at a time. To compound, the team has to reconcile personal agents into shared workflows — that's Stage 4.

---

## Lecture Slide — Stage 4 (What Comes Next)

**Content to teach:**

Stage 4: Workflow — chaining multiple AI steps into a repeatable process with deterministic validation, adversarial agents, governance rules, and human punch-out points. The custom harness demo you just saw is what Stage 4 looks like in practice.

What Stage 4 requires that Stage 3 doesn't:
- **Automated harness or runner script** — a program that executes the workflow end-to-end. A human typing each step is Stage 2, not Stage 4.
- **Guardrails between steps** — adversarial review agents AND deterministic hooks that validate structure, content, and format. Not just "is the file present" — real validation.
- **Human punch-out points** — explicitly defined, tested for bypass. Places where a human must sign off regardless of what the agent can technically do.
- **End-to-end success rate** — not just per-step accuracy. At 95% per-step, a 20-step pipeline completes correctly only ~36% of the time. You must know your composite number.
- **Audit trail** — every failure traceable to its origin step, with per-step model and token/cost data.
- **Team coordination with IT oversight** — Stage 4 is a team event. Personal agents reconciled into shared workflows. IT pulled in for infrastructure.

The effort scales ~10x from Stage 3 (~18h) to Stage 4 (~172h). This is not a small step. It is a different kind of work.

**Why we don't build a custom harness in this program:** The jump is too large for a single session. Building a custom harness is the work of a future **Stage 4 Deep Learning Program** — a separate course for teams with solid Stage 3 foundations who are ready to invest in production workflow integration.

What the Stage 4 DLP would cover:
- Building and iterating a custom harness (Python, API calls, orchestration)
- Designing guardrails: deterministic hooks + adversarial review agents between every step
- Defining and testing human punch-out points (including bypass testing)
- Measuring end-to-end success rates and compounding error math
- Building audit trails with per-step model, token, and cost data
- Reconciling personal Stage 3 skills into shared team workflows
- IT coordination for shared infrastructure

**The key takeaway:** You leave this program at Stage 3. That is a real, significant achievement. Stage 4 is the next horizon, not the next session.

---

## Lecture Slide — Capstone: Artifact Showcase

**Content to teach:**

In pairs, each participant presents three things to their partner:

1. **Their most-used skill** — what it does, how it's structured using RTCC, what the Python evaluator showed, one improvement cycle they documented
2. **Their evaluator** — what the EC are, how many iterations it's tracked, one thing they learned from the scores that surprised them
3. **One skill with model invocation enabled, an adversarial agent, or their bounded agent run** — what it does, what the invocation boundary or scope is, where context window constraints showed up

Partners ask one question each: "What would you do differently if you started this over?"

This is peer learning, not a formal presentation. The purpose is articulation: if you can't explain what you built and why it's better than where you started, you don't own it yet.

---

## Exercise Slide — Capstone Showcase

**Lab Name:** Capstone Artifact Showcase (Peer Pairs)
**Lab Timing:** 30 minutes
**Lab Steps:**
1. Pair up with another participant
2. Present your most-used skill: RTCC structure, Python evaluator, one improvement cycle
3. Present your evaluator: EC, iteration count, one surprising finding from the scores
4. Present one of: a skill with model invocation enabled, an adversarial agent, or your bounded agent run
5. Your partner asks: "What would you do differently if you started this over?"
6. Switch roles

**You'll know when you're done because...** you've presented your work to a peer with discipline framing (not just "it generates X" but "I iterated it N times and the evaluator showed..."), and you've heard your partner's presentation and asked them the question.

---

## Lecture Slide — Final Assessment + Commitment Statements

**Content to teach:**

**Final AI Adoption Maturity Assessment:** 21 questions, 7 dimensions. Same instrument as Week 1 and Week 7. Complete individually and honestly. Not graded — the value is comparison with prior administrations. DLP Completion signal: Dimensions 1-4 averaging 3.0+ per question.

**Commitment statements:** Each participant states — out loud, to the group — one specific commitment:

"In my next sprint, I will [specific behavior change] that I could not or did not do before this program. I'll know I've done it when [specific artifact or outcome]."

Not aspirations. Not "I'll use AI more." Specific, observable, next-sprint actions that can be checked.

The Embedded Engineer will follow up on your commitment in Week 12.

---

## Closing Slide

**Goal 1: Build a bounded agent**
- **Product/Process:** You've run the full SDLC pipeline in your IDE — epics-and-stories → plan-story → implement-story → review-implementation — with evaluation and adversarial review at key steps. This is the composition of everything you've built.
- **Development:** You've used a workflow prompt to chain your skills in sequence and experienced the context window accumulation firsthand. You know what a bounded agent can do and where it hits its ceiling.
- **Testing:** You've run the review-implementation skill as the final step, consuming all prior outputs. You've felt the context window degradation and know why it happens. This is Stage 3 composition.

**Goal 2: See a custom harness demonstrated**
- **Product/Process:** You've seen the full chain running in a custom harness with clean context and evaluation at each step. Your epics-and-stories skill is step 1. This is the trajectory — what production looks like when your skills are the building blocks.
- **Development:** You've seen plan-story → implement-story running inside the harness with adversarial agents challenging output. Your skills are production-ready when they're in a harness.
- **Testing:** You've seen the review-implementation skill as the final step, consuming all prior output and producing a complete, evaluated review. The full chain, automated and measured.

**Goal 3: Understand the IIOS stage framework**
- **Product/Process:** You are at Stage 3 (Task) — you can build, evaluate, iterate, and compose skills. Stage 4 (Workflow) is where those skills connect into shared, governed workflows. A future Stage 4 Deep Learning Program takes you there.
- **Development:** Stage 3 is individual: your skills, your evaluation, your iteration. Stage 4 is team + IT: shared workflows, automated guardrails, audit trails. The effort scales ~10x. You know what's ahead.
- **Testing:** Stage 3 means you review output one piece at a time. Stage 4 means quality gates are automated between steps. You know the ceiling and you know what breaking through it looks like.

**Goal 4: Capstone, assessment, and commitment**
- **Product/Process:** You've presented your epics-and-stories skill with discipline framing and completed your final assessment. You've committed to a specific next-sprint behavior change.
- **Development:** You've presented your Plan or implement-story skill with iteration evidence and adversarial agent findings. You've committed to continuing the discipline.
- **Testing:** You've presented your review-implementation skill with evaluation history. You've committed to extending the chain. The program ends here; the work continues.