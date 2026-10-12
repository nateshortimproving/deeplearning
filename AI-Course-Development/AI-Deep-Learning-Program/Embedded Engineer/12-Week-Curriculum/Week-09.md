# Week 9 — Loop 2: Model Invocation + Adversarial Agents
*Training Session 5 occurs this week*

---

## Focus
Embedded Engineer returns to the Development team. All participants attend Training Session 5 on Model Invocation + Adversarial Agent Prompts. Dev team evaluates which of their skills are ready for model invocation and begins building adversarial agents that challenge their skill output. Session 5 teaches in the shared student workspace; the EE coaches the transfer of model invocation decisions and adversarial agents to the real codebase. Before this session, the trainer pushes `adversarial-agents/example-adversarial-prompt.skill.md` to the student workspace.

---

## Training Session This Week
**Session-5 — Model Invocation + Adversarial Agent Prompts** (4 hours, all participants)

**Part A: Enabling Model Invocation (~60 min)**
- Revisit the `disable-model-invocation: true` flag from Session 1
- The three graduation criteria for enabling model invocation:
  1. Exact inputs that should trigger the skill
  2. What the skill does when triggered — the output specification
  3. At least 3 verified trigger test cases where the skill SHOULD invoke, confirmed the model invokes it and output meets spec
- Lab: evaluate one skill against the three criteria. Either enable model invocation (with test cases) or document the gap.

**Part B: Adversarial Agent Prompts (~75 min)**
- What an adversarial agent is: a prompt that receives the output of another skill and attempts to find problems — missing requirements, logical errors, edge cases the primary skill missed, quality gaps the evaluation script didn't catch
- How it differs from evaluation (Session 4): evaluation measures against EC; adversarial agents find problems the EC didn't anticipate
- How it relates to Prompt/Harness/Model: an adversarial agent is a prompt running through a harness that has access to the output of another prompt. The harness makes the connection; the model provides the judgment.
- Lab: write an adversarial prompt for one of your existing skills. Run it against real outputs. What does it find that your evaluation script missed?

---

## Embedded Engineer Focus (Development Team)

- **Day 1:** Re-engage the Dev team. Review their Loop 1 `plan-story` and `implement-story` skills — what has been used consistently on the real codebase since Loop 1? What have Python evaluation scripts shown? What has atrophied?
- **Days 2–3:** Apply the Session 5 model invocation framework to the Dev team's most-used skills. These skills were built in the workspace and transferred to the real codebase in Loop 1 — now evaluate them for model invocation. For each: does it meet the three graduation criteria? Can the team write invocation test cases? Start with `implement-story` or the most-iterated skill.
- **Day 4:** For skills that pass the graduation check, enable model invocation (`disable-model-invocation: false`) with test cases committed. For skills that don't pass, document the specific gap.
- **Day 5:** Adversarial agent lab. Build an adversarial prompt against one of the Dev team's skills. Run it against real outputs from the real codebase — not just workspace sample outputs. What does it find? How does this complement the Python evaluation script?

**Key Embedded Engineer priority this week:** The Dev team makes at least one well-founded model invocation decision AND builds at least one adversarial agent. Either a skill has model invocation enabled with test cases, or the team articulates specifically why it isn't ready yet. Both outcomes are valid; vague "it's not ready" without specific criteria is not. The workspace taught the skills; the real codebase is where model invocation and adversarial agents need to work.

---

## Participant Activities (Development Team)
- Attend Training Session 5
- Apply the three graduation criteria to their most-used skill — write down all three criteria or identify specifically what's missing
- Write invocation test cases (3 verified positive trigger, 2 quality) for at least one skill
- Enable model invocation on one skill (if graduation criteria are met) or commit a specification document with the gap identified
- Write an adversarial prompt for one skill; run it against real outputs; document findings

## Participant Activities (All)
- Attend Training Session 5
- Identify a candidate skill from their own work to evaluate for model invocation
- Write the three graduation criteria or identify the gap for that skill
- Write an adversarial prompt for one of their skills

---

## Artifacts Due by End of Week 9
- [ ] Development team: graduation criteria document for at least one skill (all three criteria answered)
- [ ] Development team: invocation test cases (3 verified positive trigger, 2 quality) committed
- [ ] Development team: either a skill with model invocation enabled and test cases, or a specification document with gap identified
- [ ] Development team: at least one adversarial prompt committed, with findings documented
- [ ] All participants: candidate skill for model invocation evaluated against three criteria
- [ ] All participants: at least one adversarial prompt committed

---

## Embedded Engineer Coaching Notes

- The model invocation decision is the conceptual payoff of the `disable-model-invocation: true` approach from Session 1. Participants should feel the 8 weeks of skill-building was preparation for this decision, not a delay. Frame it that way: "You've been invoking these skills manually for 8 weeks. Now the question is: should the model invoke this automatically based on context?"
- The positive trigger test cases are the hardest part. Most participants will write trigger inputs easily but won't verify them. Push for verification — "set up the context, confirm the model actually invokes the skill, and check the output meets spec." If they can't verify invocation, the trigger conditions aren't specific enough yet.
- Developers will often want to enable model invocation on skills that are popular but not yet EDD-validated. Check the Python evaluation history before agreeing. A skill should have at least 3 documented iteration cycles before model invocation is enabled. If it doesn't have that, the prerequisite is more EDD work, not graduation.
- The adversarial agent is a new concept for participants. Anchor on the complementarity: the evaluation script (Session 4) measures against EC; the adversarial agent (Session 5) finds problems the EC didn't anticipate. Both are needed for a complete quality strategy.
- The adversarial agent is AI-native, not code-native. It's a prompt — every participant can write one. This makes the runtime verification concept accessible to all roles, not just developers.
- Don't let participants build custom harnesses this week as a workaround. Session 6 covers custom harnesses. This week is specifically about model invocation and adversarial agents.
- **Transfer model note:** The adversarial agents and model invocation decisions need to work against the real codebase, not just workspace samples. An adversarial agent that finds problems on workspace sample outputs may miss issues that only appear with real codebase inputs. Push participants to run adversarial agents against real skill output. The `adversarial-agents/example-adversarial-prompt.skill.md` pushed to the workspace before Session 5 is a reference — participants study it, then write their own.