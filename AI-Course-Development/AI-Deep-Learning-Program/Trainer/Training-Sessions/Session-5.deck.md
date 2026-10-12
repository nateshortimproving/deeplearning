# Session 5 Deck Prompt — Model Invocation + Adversarial Agents (v2)
*Week 9 | Loop 2 | Role Focus: Development*

---

## Intro Slide

**Title:** Model Invocation + Adversarial Agents
**Week:** 9 | **Loop:** 2 | **Role Focus:** Development
**Framing:** Session 4 gave you retrospective evaluation — measuring output quality after the fact. Today we ask two new questions: When should the model invoke a skill automatically instead of waiting for your slash command? And: How do you challenge AI output with AI to find problems your evaluator missed?

---

## Check-In Slide

**Question:** In the two weeks since Session 4, what has running your Python evaluator taught you about your skills that you didn't know before? Did any of your instructions turn out to be dead weight?

*This question connects Session 4's evaluation discipline to Session 5's two topics. Evaluation is retrospective; model invocation and adversarial agents are the next steps — proactive and challenging.*

---

## Session Goals Slide

**Goal 1: Evaluate a skill for model invocation readiness using the three graduation criteria**
- **Product/Process:** Your epics-and-stories skill has been invoked via slash command for 8 weeks. Is it ready for the model to invoke automatically? The three criteria tell you.
- **Development:** Your Plan and Code skills are candidates too. This is where you decide what to trust the model to trigger on its own.
- **Testing:** Your review-implementation skill may also be a candidate. But if the invocation boundary isn't clear, don't enable it — that's the signal.

**Goal 2: Enable model invocation on at least one skill (or document the gap)**
- **Product/Process:** If your epics-and-stories skill passes the three criteria, enable model invocation. If not, write down exactly what's missing.
- **Development:** Same for Plan and Code skills. The decision is evidence-based, not preference-based.
- **Testing:** Same for the review-implementation skill. Both outcomes (enable or document gap) are valid.

**Goal 3: Write an adversarial agent prompt that challenges another skill's output**
- **Product/Process:** An adversarial agent can challenge your epics-and-stories output — finding missing edge cases, vague AC, or untestable statements your evaluator didn't catch.
- **Development:** An adversarial agent can challenge your Plan → Code output — finding implementation gaps, missing edge cases, or architectural issues the plan didn't address.
- **Testing:** An adversarial agent can challenge your review-implementation output — finding missing issues, overlooked edge cases, or severity misclassifications your evaluator didn't catch.

**Goal 4: Understand how adversarial agents complement Python evaluation**
- **Product/Process:** Your Python evaluator measures against known EC. Your adversarial agent finds problems the EC didn't anticipate. Both are needed.
- **Development:** Same — the evaluator says "does it meet the plan?" and the adversarial agent says "what did the plan miss?"
- **Testing:** Same — the evaluator checks coverage against EC; the adversarial agent finds risks the EC didn't define.

---

## Lecture Slide — Model Invocation: Flipping the Switch

**Content to teach:**

Since Session 1, every skill has had `disable-model-invocation: true`. The skill only runs when you invoke it via slash command. The model never triggers it automatically.

Now we ask: which skills are ready for the model to invoke on its own?

The three graduation criteria — a skill is ready for model invocation when the team has agreed, in writing, on:

1. **Exact inputs that should trigger the skill** — what specific context should cause the model to invoke this skill automatically?
2. **What the skill does when triggered** — the output specification
3. **At least 3 verified trigger test cases** — scenarios where the skill SHOULD invoke, verified to confirm (a) the model actually invokes it when those conditions are present, and (b) the output meets the specification from criterion 2. This is positive case testing — the primary question is "does the skill fire when it's supposed to, and does it produce the right output?" If you can't name 3 scenarios where the skill should trigger and verify both invocation and output, you don't understand the invocation conditions.

The most important criterion is #3. Verified trigger test cases define the invocation boundary. A skill that doesn't invoke when it should means the trigger conditions aren't clear enough.

Remember from Session 1: the harness controls invocation, not the model. Enabling model invocation means telling the harness: "you may trigger this skill when the context matches these conditions."

---

## Lecture Slide — Adversarial Agents: AI Challenges AI

**Content to teach:**

An adversarial agent is a prompt that receives the output of another skill and attempts to find problems with it — missing requirements, logical errors, edge cases the primary skill missed, quality gaps the evaluator didn't catch.

**The two-prompt problem:** When you use an adversarial agent, you now have TWO prompts to vet — the worker prompt (your skill) and the evaluator prompt (the adversarial agent). Both can have bugs. The mindset for "prompt to check the work" differs from "prompt to do the work." Your adversarial agent's prompt needs its own evaluation: does it find real issues, or does it hallucinate problems? Does it miss issues it should catch? Vet the vetted.

How it differs from Python evaluation (Session 4):
- Python evaluation measures against known EC — it tells you if the output meets the Evaluation Criteria you wrote
- Adversarial agents find problems the EC didn't anticipate — they challenge the output from perspectives the criteria didn't cover
- Python evaluation is deterministic + LLM judge (both code and AI); adversarial agents are fully AI-based
- Python evaluation answers "does it meet the EC?" — adversarial agents answer "what did the EC miss?"

The adversarial agent pattern:
1. Take the output of a primary skill (e.g., AC generation, Plan, Code, Review)
2. Give it to a model with an adversarial prompt: "You are a senior product manager reviewing these stories and their AC. Find as many problems as you can: missing requirements, ambiguous AC, edge cases not covered, AC that can't be tested, dependencies not identified. For each problem, explain why it's a problem and what should be done about it."
3. The adversarial agent returns: issues found, severity, and specific recommendations
4. The participant reviews the adversarial findings and decides what to fix
5. Calibrated severity and actionable findings: every issue should have a severity level (blocker, major, minor, nit) and a specific, actionable recommendation — not "this is weak" but "AC #3 is untestable because X; rewrite as Y"

Adversarial agents are AI-native — they're prompts, not code. Every participant can write one, regardless of role or coding ability.

**Note:** Adversarial agents are one form of verification — not the only form. Deterministic checks from Session 4 handle structural validation. Beyond DLP, teams may add deterministic hooks or sentinel files.

---

## Lecture Slide — How Adversarial Agents Relate to the Prompt/Harness/Model Framework

**Content to teach:**

From Session 1: the harness mediates between you and the model. The model can only do what the harness allows.

An adversarial agent is a prompt running through a harness that has access to the output of another skill. The harness makes the connection — it passes the primary skill's output to the adversarial agent. The model provides the judgment.

In your IDE: the adversarial agent can be a skill with `disable-model-invocation: true` that you invoke after running the primary skill. The harness passes the primary output as context.

In a custom harness (Session 6): the adversarial agent runs automatically after each step, with the harness orchestrating the handoff.

This is why understanding Prompt/Harness/Model matters — the adversarial agent is just a prompt, but it needs the harness to give it the primary skill's output. The model provides the judgment; the harness provides the connection.

---

## Compare/Contrast Slide — Evaluation vs. Adversarial Agents

| Python Evaluation (Session 4) | Adversarial Agents (Session 5) |
|---|---|
| Measures against known EC | Finds problems the EC didn't anticipate |
| Retrospective — runs after the fact | Proactive — challenges output before it's used |
| Deterministic + LLM judge | Fully AI-based |
| Answers: "Does it meet the criteria?" | Answers: "What did the criteria miss?" |
| Owned by the skill author | Can be written by anyone — even a different team member |

---

## Exercise Slide — Lab 1: Evaluate a Skill for Model Invocation

**Lab Name:** Graduation Criteria for Model Invocation
**Lab Timing:** 30 minutes
**Lab Steps:**
1. Select the skill you've used most and have the most evaluation evidence for
2. Apply the three graduation criteria. For each criterion, write it down. If you can't write it, you don't have consensus — you have an opinion.
3. For criterion 3 (verified trigger test cases): write at least 3 specific scenarios where the skill SHOULD invoke, then verify the model actually invokes it when those conditions are present and the output meets the specification. If you can't name 3, that's the lab's work — not a shortcut to skip.
4. Decision: either enable model invocation (with test cases committed) or document the specific gap

**You'll know when you're done because...** you have either a skill with `disable-model-invocation` set to false (or removed) with 5 invocation test cases committed (3 verified positive trigger cases, 2 quality), or a gap document with the specific gap identified.

**Stretch goal:** write an adversarial agent that targets TypeScript type safety of generated code under strict settings.

---

## Exercise Slide — Lab 2: Write an Adversarial Agent Prompt

**Lab Name:** Write an Adversarial Agent for One of Your Skills
**Lab Timing:** 40 minutes
**Lab Steps:**
1. Choose one of your existing skills (AC, Plan, Code, or Review)
2. Write an adversarial prompt as a new skill with `disable-model-invocation: true`
3. The adversarial skill receives the primary skill's output and attempts to find: missing requirements, logical errors, edge cases, quality gaps the evaluator didn't catch
4. Run the adversarial agent against 2-3 real outputs from the primary skill
5. Document: what does the adversarial agent find that your Python evaluator (from Session 4) didn't?
6. Commit the adversarial skill and findings

**You'll know when you're done because...** you have a committed adversarial skill that challenges another skill's output, and you've documented at least one issue the adversarial agent found that your Session 4 evaluator missed.

**Stretch goal:** write adversarial agents for both Express backend and React/ShadCN frontend aspects of the pantry tracker skills.

---

## Exercise Slide — Lab 3: Connect Your Evaluator and Your Adversarial Agent

**Lab Name:** Evaluator + Adversarial Agent — Closing the Loop
**Lab Timing:** 30 minutes
**Lab Steps:**
1. Open your Python evaluation script from Session 4
2. Open your adversarial agent from Lab 2
3. For each EC in your evaluator: does the adversarial agent also check it? If not, consider whether the EC is something the adversarial agent should challenge
4. For each issue the adversarial agent found: should it become a new EC in your evaluator?
5. Document the delta: what does evaluation catch that the adversarial agent doesn't? What does the adversarial agent catch that evaluation doesn't?

**You'll know when you're done because...** you have a committed document mapping your evaluation criteria to your adversarial agent's findings, with the delta noted — what each catches that the other doesn't.

---

## Closing Slide

**Goal 1: Evaluate a skill for model invocation**
- **Product/Process:** You've applied the three criteria to your epics-and-stories skill. If it's ready, the model can invoke it automatically. If not, you know exactly what's missing.
- **Development:** You've done the same for your Plan and Code skills. The decision is evidence-based.
- **Testing:** You've evaluated your review-implementation skill the same way. If the invocation boundary isn't clear, you've documented why — and that's the right call.

**Goal 2: Enable model invocation (or document the gap)**
- **Product/Process:** Your epics-and-stories skill may now auto-invoke when the context matches. Or you've written down exactly what needs to happen first.
- **Development:** Same for Plan and Code. Both outcomes are valid; vague "it's not ready" without specifics is not.
- **Testing:** Same for the review-implementation skill. The discipline is in the documentation.

**Goal 3: Write an adversarial agent prompt**
- **Product/Process:** You have an adversarial skill that challenges your epics-and-stories output — finding what your evaluator missed. This is your proactive quality layer.
- **Development:** You have an adversarial skill that challenges your Plan → Code output. It finds gaps the plan didn't address.
- **Testing:** You have an adversarial skill that challenges your review-implementation output. It finds issues your EC didn't define.

**Goal 4: Understand how they complement each other**
- **Product/Process:** Your Python evaluator says "does the epics-and-stories output meet the EC?" Your adversarial agent says "what did the EC miss?" Both are needed.
- **Development:** Your evaluator measures Plan → Code quality. Your adversarial agent finds what the plan missed. Together they're a complete quality strategy.
- **Testing:** Your evaluator checks review coverage. Your adversarial agent finds issues the coverage didn't anticipate. Together they make your reviews stronger.