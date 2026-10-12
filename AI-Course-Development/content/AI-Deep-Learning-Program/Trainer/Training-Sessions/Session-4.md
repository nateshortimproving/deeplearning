# Training Session 4 — EDD Formalization with Python Evaluations

*Week 7 | 4 Hours | All Participants | Loop 2 — Role Focus: Product/Process*

> **Loop 2 framing:** This session deepens craft for every participant regardless of role. The role-focus label indicates which workflow is used as the primary demonstration vehicle — epics-and-stories output — but EDD applies to every skill, every prompt, and every artifact built by every person in this room. The discipline you've been practicing informally since Session 1 now gets a name, a tool, and a rigorous structure.

---

## Why This Session Exists

After 6 weeks, participants have been running their skills in real sprints — both in the shared student workspace and (with the EE's help) against their real codebase. Some are improving their prompts. Most are *changing* them — adjusting language, tweaking wording, trying different phrasing — but without a systematic way to know if the output actually got better.

That's not iteration. That's drift.

This session formalizes the Evaluation-Driven Development discipline: write the test first, measure against it, treat changes as hypotheses. It also introduces the tooling that makes this discipline mechanical rather than manual: **Python evaluation scripts**.

**Two types of evaluation, used in sequence:**

1. **Deterministic checks** (fast, free, definitive) — Python code that checks structural properties: schema validation, field counts, format patterns, YAML structure. These run first, are instant, and catch quantitative issues. A schema check on `stories.yaml` can verify every story has 3-8 AC without calling any model.

2. **LLM judge checks** (slower, costs money, handles qualitative judgment) — for criteria that require understanding meaning: "Is this AC specific enough for a developer to plan from?" or "Does at least one AC cover a failure or edge case?" The LLM judge receives the output and the EC, and returns structured judgment.

**The discipline: deterministic first, LLM judge second.** Start with what you can check with code. Only escalate to an LLM judge for criteria that genuinely require judgment. This is faster, cheaper, more consistent, and it sharpens your EC — if you find yourself using an LLM judge for something that could be a regex, your EC needs refinement.

**No Python prerequisite.** Participants do not write Python from scratch. The AI writes the evaluation scripts. Participants direct the AI — "write a script that checks my skill's output against these EC, use deterministic checks where possible and LLM judges where needed" — then read and review the generated code. The models carry the coding load. The skill being taught is "directing AI to produce evaluation code," not "writing Python."

**No prior introduction needed.** Session 4 is the first encounter with Python evaluation. There is no pre-teaching in Week 6. The approach is fully AI-coded from the start.

EDD is not a new idea in this program — participants wrote Evaluation Criteria (EC) before building their first skill in Session 1. What changes today is the rigor: documented baseline, version-controlled improvement cycles, hypothesis-driven changes, and tooling that makes measurement fast enough to be habitual.

---

## Session Goals

By end of this session, every participant:
- Can articulate EDD: Red (baseline), Green (make it pass), Refactor (remove dead instructions) applied to skills
- Has a Python evaluation script running against a skill they own — with deterministic checks AND LLM judge checks
- Understands the two types of evaluation: deterministic (fast, free, structural) and LLM judge (slower, qualitative, for criteria requiring judgment)
- Understands the LLM judge pattern: send skill output + EC to a model, receive structured judgment (pass/fail, score, reasoning per EC)
- Has run a documented improvement cycle: hypothesis → change → measure → conclude
- Has applied the Refactor step: used the evaluator to identify and remove dead instructions
- Can articulate why evaluation is a non-negotiable DLP Completion criterion
- Has completed the midpoint AI Adoption Maturity Assessment

---

## Agenda

| Time | Block | Format |
|------|-------|--------|
| 0:00–0:15 | Check-in: 6 weeks in — what's working, what's drifting? | Discussion |
| 0:15–0:45 | EDD: Red, Green, Refactor for skills | Presentation |
| 0:45–1:15 | Python evaluations + LLM judges — demonstration | Demo |
| 1:15–1:30 | Break | |
| 1:30–2:15 | Lab 1: Have the AI write an evaluation script for your skill | Hands-on |
| 2:15–2:50 | Lab 2: Run the baseline; form hypotheses; iterate | Hands-on |
| 2:50–3:05 | Break | |
| 3:05–3:35 | Lab 3: Document one improvement cycle and apply the Refactor step | Hands-on |
| 3:35–3:50 | Midpoint AI Adoption Maturity Assessment | Individual |
| 3:50–4:00 | Wrap-up and next two weeks | Closeout |

---

## Detailed Block Notes

### Check-in (15 min)

Open with a direct question: *"In the past 6 weeks, did you change a skill? How do you know if the change made it better?"*

Let 3–4 participants answer honestly. Expected range:
- "I just tried it and it seemed better" → common and honest
- "I compared outputs side by side" → good instinct, no rigor
- "I evaluated it against my EC" → good — this is the baseline we're building on
- "I didn't really change my skill" → also useful — why not? Was it already good enough?

Embedded Engineer shares one real observation: a participant (anonymized) who changed their skill and couldn't tell whether it improved or regressed. Not a critique — a shared reality check.

**Trainer cue:** This check-in should create low-level productive discomfort. The goal is for participants to recognize that informal evaluation is not systematic evaluation. Frame it as universal: "This is how everyone starts. Today we make it rigorous."

---

### EDD: Red, Green, Refactor for Skills (30 min)

**The analogy to TDD is precise, not approximate:**

| TDD | EDD |
|-----|-----|
| Write a failing test (Red) | Write your Evaluation Criteria and baseline them against your current skill. Some EC should fail. |
| Write code to make the test pass (Green) | Add instructions to the skill until all EC pass |
| Refactor: remove code that isn't needed (Refactor) | Remove any instruction that — when deleted — causes no EC to fail. Dead instructions are noise. |

**Red:** Before making any change to a skill, establish the baseline. Run your current skill against 3–5 inputs from `sample-stories/`. Score each output against your Evaluation Criteria. Record the score. This is Red — even if your current skill is pretty good, you need to know exactly where it stands before you change it.

**Green:** Form a hypothesis: "I believe EC X is failing because the skill lacks instruction Y." Make one change. Re-run against the same inputs. Score again. Did EC X improve? Did anything else change?

**Refactor:** When all EC are passing, read every instruction in the skill. For each one: remove it mentally and ask which EC would now fail. If no EC would fail, the instruction is dead weight. Remove it and run the evaluator to confirm nothing drops. A skill where every instruction is load-bearing is a tighter, more reliable skill.

**The most important rule: one change per iteration.** Changing multiple instructions at once makes it impossible to know which change produced which effect. The discipline is to know, not to guess.

**Why EDD matters more than intuition:**
- Skills are not code — you cannot read them and know with certainty how the model interprets them
- A change that improves one EC often degrades another — you won't see this without measurement
- Skills interact with context in non-obvious ways; what works for one input may not work for another
- Without EDD, the best-case outcome is lucky drift. The worst case is confident regression.

---

### Python Evaluations + LLM Judges — Demonstration (30 min)

The evaluation tool is a **Python evaluation script**. It runs your skill against a set of test inputs, checks deterministic properties with Python code, and uses an LLM judge only for criteria that require judgment.

**No Python prerequisite.** The AI writes the evaluation script. The participant directs: "Write a Python script that takes my skill's output, checks these EC, uses deterministic checks where possible and LLM judges where needed" The participant reads and reviews the generated code. The models carry the coding load.

**Two types of evaluation in the script:**

1. **Deterministic checks** — Python code that checks structural properties without calling any model. These are fast, free, and definitive. Examples for `stories.yaml`:
   - Every story has 3-8 AC (count check)
   - Every AC uses Given/When/Then format (regex or pattern match)
   - story.id is unique (set comparison)
   - At least one AC per story has type: "negative" or "edge_case" (filter check)
   - YAML schema validation (structure check)

2. **LLM judge checks** — for criteria that require understanding meaning. These are slower and cost money but handle qualitative judgment:
   - "Does at least one AC cover a failure or edge case?" (semantic, not just the type field)
   - "Are the AC specific enough for a developer to plan from?"
   - "Does any AC describe implementation detail?"

**The LLM judge pattern:**
The LLM judge is the core evaluation mechanism for criteria that require judgment. The pattern:
1. Take the skill's output
2. Take the Evaluation Criteria (EC) — the same EC the participant wrote in Sessions 1–3
3. Send both to a model: "Here is the output. Here are the Evaluation Criteria. For each criterion, judge whether the output passes or fails, provide a score, and explain your reasoning."
4. The model returns structured judgment: JSON with pass/fail, score, and reasoning per EC

This is how production AI systems measure quality. Teaching this pattern directly gives participants a deeper understanding of how evaluation works and how to build it.

**Demonstration steps (live):**

1. Trainer asks the AI to write a Python evaluation script for the epics-and-stories skill in the workspace's `skills/` directory
2. The AI generates a script that:
   - Loads the skill's output (`stories.yaml` — stories with AC)
   - Runs **deterministic checks first**: AC count per story (3–8), Given/When/Then format check, story format check, unique ID check, YAML schema validation
   - Runs **LLM judge checks second**: "Does at least one AC cover a failure or edge case?", "Are the AC specific enough for a developer to plan from?", "Does any AC describe implementation detail?"
   - Returns a structured report: per-EC pass/fail, score, reasoning — clearly separating deterministic results from LLM judge results
3. **Run the deterministic-only baseline first.** Show which EC pass/fail with zero model calls. This is fast and free.
4. **Then run the full script with LLM judges.** Compare: what did deterministic checks catch? What needed the LLM judge?
5. Walk through the generated Python code — participants read it, understand what it checks
6. Form a specific hypothesis: "EC X fails because the skill lacks instruction Y"
7. Make one change to the skill
8. Re-run the evaluation. Compare scores. Did the target EC improve? Did anything regress?

**Key concept — structured output from LLM judges:** The judge returns JSON with per-EC judgments. This makes the evaluation script programmable — you can count passes, track scores over time, compare across iterations. The structure makes it mechanical, not subjective.

**What the participant does vs. what the AI does:**
- The participant writes the EC (already done in Sessions 1–3)
- The participant directs: "Write a script that checks my output against these EC, uses an LLM judge for judgment-based criteria, and returns structured results"
- The AI writes the Python code
- The participant reads the code, understands what it checks, and commits it
- The participant runs the evaluator, reads the results, and makes decisions

---

### Lab 1: Have the AI Write an Evaluation Script for Your Skill (45 min)

Participants work individually or in pairs on a skill they have actually used in the past 6 weeks from the workspace's `skills/` directory.

**Instructions:**
1. Choose the skill you've run most frequently from `skills/`. Use your epics-and-stories skill if unsure.
2. Open the EC you wrote for this skill in Sessions 1–3.
3. Ask the AI to write a Python evaluation script that:
   - Loads the skill's output (`stories.yaml` or `plan.yaml`)
   - Runs **deterministic checks first** for EC that can be code-checked (count, format, structure, schema validation)
   - Runs **LLM judge checks second** for EC that require judgment (specificity, coverage, quality)
   - Returns structured results: per-EC pass/fail, score, reasoning — with deterministic and LLM judge results clearly separated
4. Read the generated Python code. Make sure you understand what it checks and why.
5. Select 3 test inputs from `sample-stories/` — the sample epics and stories everyone shares
6. Run the baseline. Record your scores per EC per input.
7. Commit the evaluation script to `evaluations/`

**Embedded Engineer coaching during lab:**
- Watch for EC that are too permissive — an LLM judge that passes trivially means the EC text isn't specific enough
- If someone can't find 4 meaningful EC, their skill may not be specific enough — the evaluation exercise is revealing that the skill needs more definition before it can be measured
- Push for real inputs from `sample-stories/`, not constructed ones
- Help participants who are uncomfortable reading Python: "You don't need to write it, but you need to understand what it's checking. Ask the AI to explain any part you don't follow."

#### Stretch Goals (for advanced users)

Write evaluation checks that validate TypeScript type definitions in the skill output. Add a deterministic check that verifies the skill output includes proper Express route definitions (e.g., checking for `app.get`/`app.post` patterns). Add an LLM judge criterion that evaluates whether the generated code follows ShadCN/Tailwind conventions.

---

### Lab 2: Run the Baseline, Form Hypotheses, Iterate (35 min)

Participants use their evaluation script to run one full EDD iteration cycle.

**Instructions:**
1. Review the baseline scores. Identify the EC that scored lowest.
2. Form a hypothesis: "I believe this EC fails because the skill lacks ___. I predict that adding ___ will cause this EC to pass."
3. Make one change to the skill. One change only.
4. Re-run the evaluation script against all 3 test inputs from `sample-stories/`.
5. Compare scores. Record: did the target EC improve? Did anything else change?

**What to look for:**
- Did the targeted EC improve? ✓
- Did other EC change? (Better or worse?) ✓
- Was the effect consistent across all 3 test inputs, or only some? ✓

Most participants will find that their "improvement" helped one EC and had no effect — or a negative effect — on another. This is expected and valuable: it's the discovery that skills are a system. You can't tune one variable in isolation.

---

### Lab 3: Document One Improvement Cycle and Apply the Refactor Step (30 min)

**Part 1 — Document the improvement cycle (20 min):**

Participants write up their iteration in a format they commit.

```
Skill: [name]
Evaluation Criteria (EC): [list]
Baseline score: [x/y EC passing across N inputs]
Hypothesis: [what change, why]
Change made: [exact instruction diff]
Result: [new score + EC-by-EC comparison]
Conclusion: [did the hypothesis hold? what was unexpected?]
Next hypothesis: [what you'd test next, and why]
```

Commit this document to `evaluations/`. A skill without an improvement log is Basic Prompting behavior. A skill with a documented improvement cycle is DLP Completion.

**Part 2 — Refactor step (10 min):**

Run the EDD Refactor on your skill. For each instruction, remove it and re-run the evaluation script (or check mentally if you know the EC mappings). If no EC score drops, remove the instruction from the skill. Commit the leaner skill to `skills/`.

**Using the evaluator to find dead instructions:** The evaluation script makes the Refactor step mechanical. Run the evaluator with the full skill. Then remove an instruction, re-run, and compare scores. If nothing drops, the instruction was dead weight. This is the same Load-Bearing Rule from Sessions 1–3, now backed by automated measurement.

---

### Midpoint AI Adoption Maturity Assessment (15 min)

Participants complete the AI Adoption Maturity Assessment for the second time. This is the same 7-dimension, 21-question instrument used at Week 1 (baseline).

- Complete individually and honestly
- Not graded. The value is comparison with the Week 1 baseline, not the score in isolation
- DLP Completion signal: Dimensions 1–4 averaging 3.0+ per question
- The Embedded Engineer collects and cross-references against the Week 1 baseline to identify movement

**Reflection question** (written, not shared unless participant chooses):
- What's different about how you're working with AI now compared to Week 1?

---

### Wrap-up and Next Two Weeks (10 min)

**Before Session 5 (Week 9):**
- Run your evaluation script at least once more against a real work artifact
- Log at least one more iteration cycle (hypothesis → change → score)
- Bring your evaluation script, improvement log, and the skill it evaluates to Session 5

Embedded Engineer: in the next two weeks, "What does your evaluator say?" and "Have you run your evaluation script?" should become normal coaching questions alongside the model invocation and adversarial agent questions coming in Session 5.

---

## Session Artifacts

Each participant commits before leaving:

- [ ] **Python evaluation script** — AI-generated, reviewed by participant, includes deterministic checks AND LLM judge checks, committed to `evaluations/`
- [ ] **Baseline scores documented** — per-EC pass/fail across 3 test inputs from `sample-stories/`
- [ ] **One documented improvement cycle** — hypothesis, skill diff, evaluation scores, conclusion
- [ ] **Next hypothesis** — written, even if not yet tested
- [ ] **Refactor applied** — leaner skill committed to `skills/` with confirmed load-bearing instructions only, verified by the evaluator
- [ ] **Completed midpoint AI Adoption Maturity Assessment** (7-dimension, 21-question instrument)

---

## Trainer Notes

- **The EDD framing is not new — participants have been doing informal versions of this since Session 1.** The key message is: today we make it systematic and measurable. Don't introduce it as "a new concept" — introduce it as "the discipline you've already been practicing, now with real tooling."
- **The "no Python prerequisite" message is critical.** Many participants — especially Product/Process and Testing roles — will hear "Python evaluation script" and feel excluded. Make it explicit from the first mention: "The AI writes the code. You direct and review. You will not write Python from scratch." Repeat this throughout the session.
- **Participants with strong software testing backgrounds will recognize TDD immediately.** Let them articulate the parallel — peer articulation is more persuasive than trainer explanation.
- **The Refactor step is consistently under-emphasized.** Most participants stop at Green (all EC passing) and don't audit for dead instructions. Require the Refactor in Lab 3 and name it explicitly as the third step. The evaluator makes it mechanical — use it.
- **Embedded Engineer: share a personal evaluation script and improvement log from your own prior work if you have one.** A real example from someone they trust closes the gap between "training content" and "real practice."
- **The LLM judge pattern is the conceptual core of this session.** Make sure participants understand: the judge receives the skill output and the EC, and returns structured judgment. This is not a black box — it's a prompt that asks a model to evaluate against written criteria. The EC the participant wrote in Sessions 1–3 are the same EC the judge uses. This connection should be made explicit.
- **Participants who have been mostly hands-off with their skills (running them but not changing them) will feel less immediately engaged.** Reframe: if you haven't changed it, your evaluation baseline will tell you whether you should. Absence of change is also a finding — and if the scores are all passing, your load-bearing audit might still find dead instructions.

**EE Transfer Model:** Between sessions, the EE helps participants transfer skills from the workspace to their real codebase. The workspace is the training ground; the real codebase is the application. All labs and demos work against the shared workspace — the EE coaches the transfer.

**Trainer repo push (before Session 4):** Push `evaluations/example-eval-script.py` — a sample Python evaluation script with LLM judge pattern (for participants to study before writing their own).