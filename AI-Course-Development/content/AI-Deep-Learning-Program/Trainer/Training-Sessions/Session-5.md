# Training Session 5 — Model Invocation & Adversarial Agents

*Week 9 | 4 Hours | All Participants | Loop 2 — Role Focus: Development*

> **Loop 2 framing:** Session 4 gave participants a discipline for measuring output quality — retrospectively, after the fact, with Python evaluation scripts and LLM judges. Session 5 asks two next questions: (1) Should the model invoke your skills automatically? (2) Can AI challenge AI to find problems the evaluator missed? Part A covers model invocation — revisiting the `disable-model-invocation: true` flag from Session 1. Part B covers adversarial agents — prompts that receive another skill's output and attempt to find problems.

---

## Why This Session Exists

Session 4 ended with participants running Python evaluation scripts against their skills — a baseline, a hypothesis, a change, a measurement. That discipline is real progress. But evaluation is retrospective: you run it on past output and hope the next invocation follows the same pattern.

This session adds two capabilities:

1. **Model invocation** — Participants have been using skills with `disable-model-invocation: true` for 8 weeks. They have evaluation evidence. They understand the Prompt/Harness/Model distinction from Session 1. They're ready to ask: "Should the model invoke this skill automatically?" The answer requires the three graduation criteria.

2. **Adversarial agents** — An adversarial agent is a prompt that receives the output of another skill and attempts to find problems with it — missing requirements, logical errors, edge cases the primary skill missed, quality gaps the evaluation script didn't catch. The evaluator (Session 4) measures against criteria; the adversarial agent (Session 5) finds problems the criteria didn't anticipate. The two are complementary: the evaluator measures, the adversarial agent attacks.

The progression is: **Python evaluation (Session 4, retrospective) → adversarial agents (Session 5, proactive).** Both are needed for a complete quality strategy.

---

## Session Goals

By end of this session, every participant:
- Understands the model invocation decision and can evaluate a skill against the three graduation criteria
- Has either enabled model invocation on a skill (with test cases) or documented the gap preventing it
- Understands what an adversarial agent is and how it differs from an evaluation script
- Has written an adversarial prompt for one of their existing skills and run it against real outputs
- Can connect the evaluator (Session 4, retrospective) and adversarial agent (Session 5, proactive) as complementary quality strategies
- References back to the Prompt/Harness/Model framework from Session 1: the harness controls invocation

---

## Agenda

| Time | Block | Format |
|------|-------|--------|
| 0:00–0:15 | Check-in: What has evaluation taught you about your skills? | Discussion |
| 0:15–0:45 | Part A: Model invocation — the `disable-model-invocation` flag revisited | Presentation |
| 0:45–1:15 | Lab 1: Evaluate one skill against the three graduation criteria | Hands-on |
| 1:15–1:30 | Break | |
| 1:30–2:05 | Part B: Adversarial agents — AI challenges AI | Presentation + Demo |
| 2:05–2:45 | Lab 2: Write an adversarial prompt for one of your skills | Hands-on |
| 2:45–3:00 | Break | |
| 3:00–3:30 | Lab 3: Run the adversarial agent; compare with evaluation results | Hands-on |
| 3:30–3:50 | Discussion: Retrospective evaluation vs. proactive challenge | Discussion |
| 3:50–4:00 | Wrap-up and next two weeks | Closeout |

---

## Detailed Block Notes

### Check-in (15 min)

Open with a targeted question: *"In the two weeks since Session 4, what has running your evaluation script against your skills taught you that you didn't know before?"*

Let 3–4 participants answer. The range will include:
- "I found out an instruction I thought was essential isn't" — the Load-Bearing Rule in action
- "The output is less consistent than I assumed" — the baseline problem
- "I haven't run it yet" — this is fine; acknowledge and move on

**The bridge to Part A:** *"Since Session 1, every skill you've built has had `disable-model-invocation: true` — you invoke it via slash command. Today we ask: should the model invoke any of your skills automatically? And what would it take to trust that?"*

**The bridge to Part B:** *"Your evaluation script measures output against criteria you wrote. But what about problems your criteria didn't anticipate? What if AI could challenge AI to find gaps the evaluator missed?"*

---

### Part A: Model Invocation — The `disable-model-invocation` Flag Revisited (30 min)

**Reconnecting to Session 1:** In Session 1, we defined Prompt, Harness, Model. The harness controls invocation, not the model. Every skill in this program has `disable-model-invocation: true` — the harness only runs the skill when you explicitly invoke it via slash command. The model cannot auto-invoke it based on context.

**The question for today:** Should any of your skills have model invocation enabled?

By Week 9, participants have been using skills with invocation disabled for 8 weeks. They have evaluation evidence from Session 4. They understand the invocation boundary concept. They're ready to make this decision.

**Why this is a configuration decision, not a format migration:** In v2, there is no "commands to skills" conversion. Everything is already a skill. The only change is flipping a configuration flag: `disable-model-invocation: true` → `false` (or unset). The question is whether the skill is ready for the model to invoke automatically based on context.

**The three graduation criteria** — a skill is ready for model invocation when the team has agreed, in writing, on:

1. **Exact trigger inputs** — What specific input conditions should cause the model to invoke this skill? Not "when it seems relevant" — specific, describable input conditions. The evaluation baseline from Session 4 teaches you exactly which inputs produce good output (candidate trigger conditions).

2. **Output specification** — What does the skill do when triggered? What output does it produce? This must be specific enough that you can verify the skill triggered correctly.

3. **At least 3 verified trigger test cases** — At least 3 specific scenarios where the skill SHOULD invoke, verified to confirm that (a) the model actually does invoke it when those conditions are present, and (b) the output it produces meets the specification from criterion 2. This is positive case testing — the primary question is "does the skill fire when it's supposed to, and does it produce the right output?" If you can't name three specific scenarios where the skill should trigger and verify both invocation and output quality, you don't understand the invocation conditions well enough to automate it. This difficulty is the signal — it means you need more evaluation, not less. The evaluation script from Session 4 is the verification tool — the same EC that measure output quality can verify that the skill produced the right kind of output when auto-invoked.

**The most important criterion is #3.** If you can't name three specific scenarios where the skill should invoke and verify that it does — and that the output is correct — you don't understand the invocation conditions well enough to enable model invocation. The evaluation evidence from Session 4 is the prerequisite — it tells you which inputs produce good output.

**Reference back to Prompt/Harness/Model:** The harness controls invocation. Enabling model invocation means telling the harness: "the model can decide to run this skill based on context." The model still can't do anything the harness doesn't allow — but now the harness allows the model to make the invocation decision for this specific skill.

---

### Lab 1: Evaluate One Skill Against the Three Graduation Criteria (30 min)

Participants work individually. Select the skill with the most evaluation history from the workspace's `skills/` directory — ideally the one they ran the evaluation script against in Session 4.

**Apply the three graduation criteria.** For each criterion, write it down. If you can't write it, you don't have consensus — you have an opinion.

1. Exact trigger inputs: write the specific input conditions
2. Output specification: write what the skill produces
3. Verified trigger test cases: write at least 3 specific scenarios where the skill SHOULD invoke, then verify the model actually invokes it when those conditions are present and the output meets the specification

**Checkpoint:** Every participant leaves Lab 1 with one of:
- "This skill is ready for model invocation. Here are my three criteria and test cases." → Enable `disable-model-invocation: false`, commit to `skills/`, and note the test cases for the Embedded Engineer to validate in Weeks 9–10.
- "This skill is not ready. Here is the specific gap." → Document the gap. The skill stays at `disable-model-invocation: true` in `skills/`. The gap document is the coaching agenda for the next two weeks.

Both are valid outcomes. The committed decision (enable or document gap) is the artifact.

**Embedded Engineer coaching:** Watch for invocation criteria written as "when the model thinks it should." Push for specific, describable conditions. If someone can't name 3 verified trigger test cases, that's the lab's work — not a shortcut to skip. The EDD-validated prerequisite applies: skills should have 3+ documented iteration cycles before model invocation is enabled.

#### Stretch Goals (for advanced users)

For participants who have already enabled model invocation on a skill: write an adversarial agent that specifically targets the TypeScript type safety of generated code. Challenge the skill to produce code that compiles without errors under strict TypeScript settings.

---

### Part B: Adversarial Agents — AI Challenges AI (35 min)

This is the session's main content block. Spend the time here.

**What an adversarial agent is:**
An adversarial agent is a prompt that receives the output of another skill and attempts to find problems with it — missing requirements, logical errors, edge cases the primary skill missed, quality gaps the evaluation script didn't catch.

**How it differs from an evaluation script (Session 4):**
- The evaluation script measures output against written EC — it checks whether the output meets the defined quality bar
- The adversarial agent challenges the output without pre-defined criteria — it looks for problems the EC didn't anticipate
- The evaluation script is retrospective: you run it after the fact, against criteria you wrote
- The adversarial agent is proactive: it attacks the output looking for anything wrong, not just what the criteria cover

**How it differs from deterministic hooks (v1, retired):**
- Hooks are deterministic code that check structural properties (is the field present? does the schema validate?)
- Adversarial agents are AI-based — they check meaning, not just structure
- A hook can check whether a required field is present. An adversarial agent can check whether the field's content is actually correct, whether the reasoning is sound, and whether the output misses something the criteria didn't anticipate

**Why adversarial agents are AI-native, not code-native:**
An adversarial agent is a prompt. Every participant in the program can write one — no coding required. This makes proactive quality challenge accessible to all roles, not just developers.

**The two-prompt problem — you now have two prompts to vet:**

When you use an adversarial agent, you introduce a second prompt into your quality pipeline: the adversarial prompt itself. You now have:
1. **The worker prompt** (your skill) — the prompt that produces the output
2. **The evaluator prompt** (the adversarial agent) — the prompt that checks the output

Both can have bugs. Both need evaluation. An adversarial agent that produces false positives is just as harmful as one that misses real issues — it wastes time and erodes trust in the quality process. The mindset for "prompt to check the work" differs from "prompt to do the work":
- The worker prompt is optimized for producing good output
- The adversarial prompt is optimized for finding problems — it needs a different persona, different EC, and different tuning
- A common failure: adversarial agents that are too permissive ("looks good") or too aggressive (every output has "problems" that aren't real)

**Adversarial agents are one form of verification — not the only form.**

This session teaches AI-based quality challenge. For deterministic verification (schema checks, format validation, field presence), your Python evaluation script from Session 4 already handles that. Adversarial agents complement deterministic checks — they don't replace them. A complete quality strategy uses both: deterministic checks for quantitative judgment (fast, free), adversarial agents for qualitative challenge (finds what the criteria didn't anticipate). Beyond DLP, teams may add deterministic hooks or sentinel files for automated gates — that's the next step after this program, not part of it.

**The complementary pairing:**
- **Evaluator (Session 4):** measures against EC — "Does this output meet the defined quality bar?"
- **Adversarial agent (Session 5):** challenges without EC — "What's wrong with this output that the EC didn't catch?"

Both are needed. The evaluator gives you a scorecard. The adversarial agent gives you a red team. A skill that passes its evaluator but fails its adversarial agent has a gap in the EC — which is itself a finding.

**Demonstration:**

1. Take a real output from the epics-and-stories skill in `skills/` (stories with AC from a `sample-stories/` input)
2. Show the evaluation script results — which EC pass, which fail
3. Now run an adversarial prompt against the same output: "You are a senior product manager reviewing these stories and their AC. Find as many problems as you can: missing requirements, ambiguous AC, edge cases not covered, AC that can't be tested, dependencies not identified. For each problem, explain why it's a problem and what should be done about it."
4. Compare: what did the evaluator catch? What did the adversarial agent catch that the evaluator missed?
5. The adversarial agent will find things the EC didn't cover — this is the value. Each finding is either a gap in the skill (fix the skill) or a gap in the EC (add the EC to the evaluator)

**What makes a good adversarial prompt:**
- Specific role: "You are a [senior QA engineer / security reviewer / product manager] reviewing this output."
- Clear mission: "Find as many problems as you can. For each, explain why it's a problem."
- Receives the full output as input: the adversarial agent sees what the primary skill produced
- Structured response: "List each problem with: what's wrong, why it matters, recommended fix."
- Not constrained by the original EC: the adversarial agent doesn't know the EC — it looks for anything wrong
- **Calibrated severity**: each finding should have a severity level (blocker, major, minor, nit) — an agent that labels everything as a blocker needs tuning
- **Actionable findings**: every finding should include a specific recommendation, not just "this is wrong" — vague findings are false positives in disguise
- **Domain expertise in the role**: "You are a senior QA engineer" produces different findings than "you are a product manager." Choose the reviewer role that is the natural critic of the skill's output. The best adversarial agent comes from the perspective the primary skill's author is least likely to have.

---

### Lab 2: Write an Adversarial Prompt for One of Your Skills (40 min)

Participants work individually or in pairs.

**Instructions:**
1. Choose one of your existing skills from `skills/` — ideally one you've been evaluating with the Python evaluation script from Session 4
2. Write an adversarial prompt that:
   - Assigns a specific reviewer role (senior engineer, QA lead, product manager — whichever is the natural critic for this skill's output)
   - Receives the skill's output as input
   - Challenges the output to find problems: missing requirements, logical errors, edge cases, quality gaps
   - Returns structured findings: problem, why it matters, recommended fix
3. Run the adversarial prompt against 2–3 real outputs from your skill (use `sample-stories/` inputs)
4. Compare: what did the adversarial agent find that your evaluation script missed?

**What to look for:**
- Did the adversarial agent find problems the EC didn't cover? → These are gaps in your EC. Add them to your evaluation script.
- Did the adversarial agent find problems that are actually skill bugs? → These are gaps in your skill. Fix them.
- Did the adversarial agent produce false positives? → Tune the prompt to be more specific about what counts as a problem.

**Commit the adversarial prompt to `adversarial-agents/`.** It's an artifact — a reusable quality tool that complements the evaluation script.

#### Stretch Goals (for advanced users)

Write adversarial agents for both the backend (Express API) and frontend (React/ShadCN) aspects of the pantry tracker skills. Compare what each adversarial agent catches — backend adversarial agents may find different issues than frontend ones.

---

### Lab 3: Run the Adversarial Agent; Compare with Evaluation Results (30 min)

This lab closes the loop between Session 4 and Session 5.

**Instructions:**
1. Open your evaluation script from `evaluations/` (Session 4) and your adversarial prompt from `adversarial-agents/` (Lab 2)
2. Run both against the same 2–3 real outputs (use `sample-stories/` inputs)
3. Document the comparison:
   - What did the evaluator catch?
   - What did the adversarial agent catch that the evaluator missed?
   - What did the evaluator catch that the adversarial agent missed?
   - What does this tell you about gaps in your EC?
4. For each finding the adversarial agent produced that the evaluator missed:
   - Is it a real problem? If yes → add a corresponding EC to your evaluation script in `evaluations/`
   - Is it a false positive? If yes → tune the adversarial prompt in `adversarial-agents/`
5. Commit the comparison document to `adversarial-agents/`

**The output:** A short document (committed) mapping evaluation findings to adversarial findings, with the delta noted. This document is the starting point for the Embedded Engineer's coaching conversations in Weeks 9–10.

---

### Discussion: Retrospective Evaluation vs. Proactive Challenge (20 min)

Open discussion — trainer facilitates.

Prompt questions:
- "What did your adversarial agent find that surprised you?"
- "Did it find problems you would have caught manually but your evaluator didn't?"
- "Which findings were gaps in your skill vs. gaps in your EC?"
- "How would you use the evaluator and the adversarial agent together in your weekly workflow?"

**Common revelations to surface:**
- The evaluator measures what you thought to check. The adversarial agent finds what you didn't think to check.
- Most participants will find that their EC cover the obvious quality dimensions but miss domain-specific risks that the adversarial agent (especially with a well-chosen reviewer role) catches.
- The two tools are complementary, not competing. A complete quality strategy uses both: evaluate against EC to track improvement, then run an adversarial agent to find what you missed.

---

### Wrap-up and Next Two Weeks (10 min)

**Before Session 6 (Week 11):**
- Model invocation decision completed for at least one skill — enabled or documented gap
- Adversarial prompt committed for at least one skill
- Comparison document (evaluator findings vs. adversarial findings) committed
- If the adversarial agent has been active for any work: note what it caught, and whether any findings led to skill or EC changes

**Embedded Engineer in the next two weeks:**
- Reference the adversarial prompt in every coaching conversation about skill quality
- Watch for adversarial agents that are too permissive — if the agent never finds problems, the prompt isn't specific enough about the reviewer role and mission
- The Testing team work in Weeks 11–12 will draw on adversarial agents as a foundation for custom harness governance

---

## Session Artifacts

Each participant commits before leaving:

- [ ] **Model invocation decision** — either enabled with three graduation criteria + test cases (committed to `skills/`), or gap document with specific gap noted (committed to `adversarial-agents/`)
- [ ] **Adversarial prompt** — committed to `adversarial-agents/`, targeting one skill's output, with specific reviewer role and structured findings format
- [ ] **Adversarial agent results** — run against 2–3 real outputs (from `sample-stories/` inputs), findings documented
- [ ] **Evaluator-to-adversarial comparison** — document connecting evaluation findings to adversarial findings, with delta noted, committed to `adversarial-agents/`

---

## Trainer Notes

- **The model invocation discussion is shorter than participants might expect.** The graduation criteria are not new — they're the same criteria from v1, now applied to a configuration flag on an existing skill. Don't over-teach the mechanics. The lab is where the learning happens: participants discover whether they can actually name the trigger inputs and verify trigger test cases. If they can't, that's the finding.
- **The "3 verified trigger test cases" criterion is the most important.** If a participant can't name three scenarios where the skill should invoke and verify that the model actually does invoke it — and that the output is correct — they don't understand the invocation conditions. Don't let them enable model invocation without it. The difficulty is the signal — it means they need more evaluation, not less.
- **The adversarial agent is the main event of this session.** Spend the time on Part B. The conceptual load is: evaluation measures against criteria; adversarial agents find problems the criteria didn't anticipate. Participants who understand this deeply will build adversarial prompts that actually catch problems. Those who don't will write prompts that just say "looks good."
- **The reviewer role in the adversarial prompt matters enormously.** "You are a senior QA engineer" produces different findings than "you are a product manager." Encourage participants to choose the reviewer role that is the natural critic of their skill's output. The best adversarial agent comes from the perspective the primary skill's author is least likely to have.
- **Lab 3's comparison is high-value.** The mapping exercise forces participants to confront the gap between what they evaluate and what they challenge. Most will find they're evaluating things the adversarial agent also catches — and the adversarial agent catches additional things the evaluator missed. Don't skip it to save time.
- **The Development role focus is right for this session** because model invocation and adversarial agents integrate into the development workflow naturally. But every role has skills whose output can be challenged adversarially. Push participants from all roles to find their adversarial angle.
- **Reference back to Prompt/Harness/Model from Session 1 throughout.** The harness controls invocation. Enabling model invocation is a harness configuration decision. The adversarial agent works because the harness gives it access to the primary skill's output. The conceptual framework from Session 1 makes both concepts click.

**EE Transfer Model:** Between sessions, the EE helps participants transfer skills from the workspace to their real codebase. The workspace is the training ground; the real codebase is the application. All labs and demos work against the shared workspace — the EE coaches the transfer.

**Trainer repo push (before Session 5):** Push `adversarial-agents/example-adversarial-prompt.skill.md` — a sample adversarial agent skill (for participants to study).