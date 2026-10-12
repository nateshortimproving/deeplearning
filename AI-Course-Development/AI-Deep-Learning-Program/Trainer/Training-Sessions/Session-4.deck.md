# Session 4 Deck Prompt — EDD with Python Evaluations (v2)
*Week 7 | Loop 2 | Role Focus: Product/Process*

---

## Intro Slide

**Title:** Evaluation-Driven Development with Python Evaluations
**Week:** 7 | **Loop:** 2 | **Role Focus:** Product/Process
**Framing:** You've been evaluating your skills informally for 6 weeks — checking output against EC you wrote by hand. Today we make evaluation systematic, automated, and repeatable. There are two types of evaluation: deterministic checks first (fast, free, structural — schema validation, field counts, format patterns), then LLM judges second (qualitative judgment for criteria that require understanding, not just pattern matching). We write Python evaluation scripts that use both — and we use them to drive iteration.

---

## Check-In Slide

**Question:** In the past 6 weeks, did you change a skill? How do you know if the change made it better — or just different?

*This question surfaces the gap between informal evaluation (intuition) and systematic evaluation (EDD). Most participants have been changing skills without measurement. This session fixes that.*

---

## Session Goals Slide

**Goal 1: Articulate EDD — Red/Green/Refactor applied to skills**
- **Product/Process:** Your AC generation skill has been changing for 6 weeks. EDD tells you whether those changes improved it or just changed it. This is your discipline now.
- **Development:** Your Plan and Code skills have been iterating too. EDD gives you the measurement tool to know if your iteration is working.
- **Testing:** Your review-implementation skill benefits from EDD the same way — but you'll also see how LLM judges can evaluate review quality, not just code.

**Goal 2: Write a Python evaluation script with an LLM judge for your most-used skill**
- **Product/Process:** You'll build a Python evaluation script that checks your AC skill's output against your EC. The LLM judge evaluates quality; deterministic checks validate structure.
- **Development:** You'll apply the same pattern to your Plan and Code skills. The evaluation script is an artifact you own and can adapt.
- **Testing:** You'll see how LLM judges can evaluate review-implementation output — coverage, risk identification, and non-duplication with unit tests.

**Goal 3: Run a documented improvement cycle — hypothesis → change → measure → conclude**
- **Product/Process:** You'll form a hypothesis about your AC skill, make one change, run the evaluator, and document whether the change improved the score.
- **Development:** Same discipline for Plan and Code skills. One change per iteration. Document everything.
- **Testing:** Same for review-implementation skills. The improvement cycle is universal across all skills.

**Goal 4: Apply the Refactor step — remove dead instructions using your evaluator**
- **Product/Process:** Your AC skill may have instructions that don't affect output quality. The evaluator proves it. Remove them.
- **Development:** Your Plan and Code skills have the same risk. The evaluator finds dead weight.
- **Testing:** Your review-implementation skill too. A leaner skill is a more reliable skill.

---

## Lecture Slide — EDD: Red, Green, Refactor for Skills

**Content to teach:**

The TDD analogy is precise:

| TDD | EDD |
|-----|-----|
| Write a failing test (Red) | Write your EC and baseline them against your current skill. Some EC should fail. |
| Write code to make the test pass (Green) | Add instructions to the skill until all EC pass |
| Refactor: remove code that isn't needed | Remove any instruction that, when deleted, causes no EC to fail. Dead instructions are noise. |

**Red:** Run your current skill against 3-5 sample stories from sample-stories/. Score each output against your EC using your Python evaluation script. Record the score. Some EC should fail — that's the baseline.

**Green:** Form a hypothesis: "I believe EC X is failing because the skill lacks instruction Y." Make one change. Re-run the evaluator. Did EC X improve? Did anything else change?

**Refactor:** When all EC are passing, read every instruction in the skill. For each: remove it and re-run the evaluator. If no EC score drops, the instruction is dead weight. Remove it.

**The most important rule: one change per iteration.** Changing multiple instructions at once makes it impossible to know which change produced which effect.

---

## Lecture Slide — The LLM Judge Pattern

**Content to teach:**

Deterministic checks come first. Before invoking any LLM judge, run the fast, free, structural checks: schema validation (does the output have the required fields?), field counts (are there 3-8 AC items?), format patterns (does each AC start with Given/When/Then?). These checks catch the obvious failures instantly and cost nothing. Only use LLM judges for criteria that require genuine judgment — semantic quality, coverage of edge cases, specificity of recommendations. An LLM judge is a Python script that sends your skill's output and your EC to a model and receives a structured judgment: pass/fail, score, and reasoning per criterion.

The pattern:
1. Load the skill's output
2. Load the EC (the same EC you wrote before building the skill)
3. Construct a prompt: "Given this output and these evaluation criteria, evaluate whether the output meets each criterion. Return JSON with: criterion, pass (boolean), score (1-5), reasoning (string)."
4. Call the model API
5. Parse the structured response
6. Aggregate scores across criteria and inputs

**Why LLM judges instead of string matching:**
- Most EC require judgment, not just string matching ("does the output cover at least one edge case?" requires understanding what counts as an edge case)
- LLM judges can evaluate semantic quality, not just structural properties
- The judge uses the same EC the participant wrote — creating a direct feedback loop between intent and measurement

**Why Python instead of a YAML config tool:**
- Python is universal — every participant's environment has it
- Python can do anything: count, parse, call APIs, compare across runs, run subprocesses
- The evaluation script is itself an artifact participants own and can adapt
- No tool-specific configuration format to learn

---

## Lecture Slide — Structured Output from LLM Judges

**Content to teach:**

The LLM judge returns structured JSON, not free-form text. This makes the evaluation programmatically consumable:

```json
{
  "criteria": [
    {
      "criterion": "Every AC item starts with Given/When/Then or testable behavior statement",
      "pass": true,
      "score": 4,
      "reasoning": "All 5 AC items use Given/When/Then format"
    },
    {
      "criterion": "At least one AC covers a failure or edge case",
      "pass": false,
      "score": 2,
      "reasoning": "No edge cases identified; all AC cover happy path only"
    }
  ],
  "overall_score": 3.0
}
```

The evaluation script can:
- Run across multiple test inputs
- Aggregate scores across inputs and criteria
- Track scores over time (iteration history)
- Compare scores before and after a change
- Generate a report for the improvement cycle documentation

---

## Compare/Contrast Slide — Informal Evaluation vs. EDD with Deterministic Checks + LLM Judges

| Informal Evaluation | EDD with Deterministic Checks + LLM Judges |
|---|---|
| "It seemed better" | Documented scores per EC per input |
| No baseline; can't tell if improving or regressing | Baseline recorded; every change measured against it |
| One change might fix one thing and break another | One change per iteration; evaluator catches regressions |
| No committed evidence of iteration | Python eval script + improvement log committed to repo |
| Intuition-driven | Hypothesis-driven with measurement |

---

## Demo Slide — Python Evaluation with LLM Judge

**Description:** The instructor demonstrates a Python evaluation script that evaluates an AC generation skill's output. The script loads the skill output, runs deterministic checks (count AC items, check format), runs an LLM judge for quality criteria, and produces a structured report with scores per EC. The demo connects to the learning goals by making the evaluation pattern concrete — participants will build the same thing in Lab 1.

**What to focus on:** As the demo runs, notice how the LLM judge evaluates semantic quality (does each AC cover an edge case?) while the Python code checks structural properties (are there 3-8 AC items?). Watch the JSON output — it's structured, not free-form. See how the overall score is computed and how it compares to the baseline.

---

## Exercise Slide — Lab 1: Write a Python Evaluation Script with LLM Judge

**Lab Name:** Write a Python Evaluation Script for Your Most-Used Skill
**Lab Timing:** 45 minutes
**Lab Steps:**
1. Choose the skill you've used most frequently (AC, Plan, Code, or Review)
2. Open or create a Python evaluation script
3. Define 4-6 EC as code: deterministic checks (count, format, structure) and LLM judge calls (quality, coverage, specificity)
4. Select 3 real test inputs from the student workspace
5. Run the deterministic-only baseline first. Record scores per EC per input.
6. Then add the LLM judge checks. What does each type of evaluation catch that the other doesn't?
7. Commit the evaluation script

**You'll know when you're done because...** you have a committed Python evaluation script that checks your skill's output against 4-6 EC using both deterministic checks and LLM judges, with baseline scores documented for 3 sample stories from sample-stories/.

**Stretch goal:** write deterministic checks that validate TypeScript types and Express route patterns in the skill output. Add an LLM judge criterion for ShadCN/Tailwind convention compliance.

---

## Exercise Slide — Lab 2: Run the Baseline and Iterate

**Lab Name:** Baseline, Hypothesize, Iterate
**Lab Timing:** 35 minutes
**Lab Steps:**
1. Review the baseline scores. Identify the EC that scored lowest.
2. Form a hypothesis: "I believe this EC fails because the skill lacks ___. I predict that adding ___ will cause this EC to pass."
3. Make one change to the skill. One change only.
4. Re-run the evaluation script against all 3 test inputs.
5. Compare scores. Record: did the target EC improve? Did anything else change? Was the effect consistent across inputs?

**You'll know when you're done because...** you've run one documented EDD iteration cycle with a written hypothesis, a single skill change, evaluator scores before and after, and a conclusion about whether the hypothesis held.

---

## Exercise Slide — Lab 3: Document the Improvement Cycle and Refactor

**Lab Name:** Document the Cycle and Apply the Refactor Step
**Lab Timing:** 30 minutes
**Lab Steps:**
1. Write up your iteration in a committed document: skill name, EC list, baseline score, hypothesis, change made, result (new score + EC-by-EC comparison), conclusion, next hypothesis
2. Apply the Refactor step: for each instruction in your skill, remove it and re-run the evaluator. If no EC score drops, remove the instruction permanently.
3. Commit the improvement log and the leaner skill

**You'll know when you're done because...** you have a committed improvement cycle document with hypothesis, change, scores, and conclusion — plus a leaner skill where every instruction is provably load-bearing according to your evaluator.

---

## Closing Slide

**Goal 1: Articulate EDD**
- **Product/Process:** You now have the discipline to know whether your AC skill changes are improvements or just changes. This is non-negotiable for the rest of the program.
- **Development:** Your Plan and Code skills now have the same measurement rigor. No more guessing.
- **Testing:** Your review-implementation skill is measurable now too. Same discipline, same Python pattern.

**Goal 2: Write a Python evaluation script with LLM judge**
- **Product/Process:** You own an evaluation script for your AC skill. You can run it anytime, against any input, and get a structured score.
- **Development:** You own evaluation scripts for your Plan and Code skills. These are artifacts you'll maintain and adapt.
- **Testing:** You've seen how LLM judges evaluate review quality — coverage, risk identification, non-duplication. You can build the same for your review-implementation skill.

**Goal 3: Run a documented improvement cycle**
- **Product/Process:** You've proven that one change, measured, is worth more than ten changes guessed. This is the iteration discipline.
- **Development:** Same. Your Plan and Code skills now have evidence-driven iteration, not intuition-driven drift.
- **Testing:** Same. Your review-implementation skill's iteration is now documented and measurable.

**Goal 4: Apply the Refactor step**
- **Product/Process:** Your AC skill is leaner — every instruction is load-bearing. Dead weight removed, proven by the evaluator.
- **Development:** Your Plan and Code skills are leaner too. The evaluator found the dead weight.
- **Testing:** Your review-implementation skill is leaner. A leaner skill is more reliable and easier to maintain.