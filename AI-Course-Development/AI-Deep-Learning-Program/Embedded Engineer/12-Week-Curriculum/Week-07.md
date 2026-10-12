# Week 7 — Loop 2: EDD with Python Evaluations
*Training Session 4 occurs this week*

---

## Focus
Loop 2 begins. Embedded Engineer returns to the Product/Process team with higher expectations — Loop 2 deepens and extends Loop 1 work. All participants attend Training Session 4 on Evaluation-Driven Development (EDD) with Python evaluations and LLM judges. Session 4 teaches in the shared student workspace; the EE coaches the transfer of evaluation skills to the real codebase. Before this session, the trainer pushes `evaluations/example-eval-script.py` to the student workspace.

---

## Training Session This Week
**Session-4 — EDD with Python Evaluations + LLM Judges** (4 hours, all participants)
- EDD: Red/Green/Refactor applied to skills
- Python evaluation scripts as the measurement tool — not a YAML config, but code participants own and adapt
- The LLM judge pattern: send skill output + Evaluation Criteria (EC) to a model, receive structured judgment (pass/fail, score, reasoning)
- Writing evaluation scripts in Python: load skill output, run deterministic checks (count, format, structure), run LLM judge checks (quality, coverage, specificity)
- Structured output from LLM judges: JSON responses with pass/fail, score, reasoning per criterion
- AI writes the evaluation code — participants direct and evaluate. No Python prerequisite.
- Lab: write a Python evaluation script for your most-used skill (with AI assistance)
- Lab: run the baseline, form hypotheses, iterate
- Lab: document one improvement cycle; apply the Refactor step (load-bearing audit)
- Discussion: what EDD reveals that informal evaluation doesn't

---

## Embedded Engineer Focus (Product/Process Team)

- **Day 1:** Re-engage the Product/Process team. Don't start from zero — review their Loop 1 skills together. What's working on the real codebase? What do the developers say about the epics-and-stories quality? What did participants' EC-based evaluations from Loop 1 show? In Session 4, participants wrote Python evaluation scripts against workspace skills; now the transfer work is to apply those evaluation scripts to skills running on real stories.
- **Days 2–3:** Harder cases. In Loop 1, the team likely stuck to straightforward stories. In Loop 2, tackle the harder ones: stories with complex business rules, stories with multiple edge cases, stories where the domain is ambiguous. Run the Python evaluation script on these harder inputs (transferred from workspace to real stories) and compare to baseline.
- **Day 4:** Introduce adversarial thinking. Can the `epics-and-stories` skill output be challenged? What would an adversarial prompt find — missing requirements, logical errors, edge cases the skill missed? Explore together — but the formal adversarial agent work comes in Session 5. For now, plant the seed.
- **Day 5:** Focus on evaluation maturity. Are participants running Python evaluation scripts and documenting improvement cycles on real stories, or was the Session 4 script a one-time exercise in the workspace? Run a documented cycle together — the evaluation script built in the workspace needs to transfer to evaluating real skill output.

**Key Embedded Engineer priority this week:** Raise the bar. Loop 2 is not a repeat of Loop 1 — it's deeper, harder, and expects more independence from participants. Python evaluation results should be driving decisions, not intuition. The evaluation skills from the workspace need to transfer to the real codebase.

---

## Participant Activities (Product/Process Team)
- Attend Training Session 4
- Apply `epics-and-stories` skill to 3+ harder/more complex stories
- Update Python evaluation script with new EC for harder story cases
- Run at least one documented iteration cycle: hypothesis → evaluation run → conclusion

## Participant Activities (All)
- Attend Training Session 4
- Complete midpoint AI Adoption Maturity Assessment (7 dimensions, 21 questions)

---

## Artifacts Due by End of Week 7
- [ ] Product/Process team: Python evaluation script updated with harder story test cases
- [ ] Product/Process team: `epics-and-stories` skill — one documented iteration cycle driven by Python evaluation results
- [ ] All participants: midpoint AI Adoption Maturity Assessment (7 dimensions, 21 questions)

---

## Embedded Engineer Coaching Notes

- Loop 2 is when the Embedded Engineer starts reducing their scaffolding. In Loop 1, the Embedded Engineer was often the driver. In Loop 2, participants should be driving and the Embedded Engineer is the coach.
- Session 4's EDD formalization with Python evaluations is important for the Product/Process team specifically — they have been generating epics-and-stories for 6 weeks and likely have intuitions about what works. Python evaluation scripts make those intuitions testable. Use this as motivation for harder work in Loop 2.
- The AI writes the evaluation code. Participants direct the AI: "Write a Python script that checks my skill output against these EC." Then they read and review the output. The skill being taught is "directing AI to produce evaluation code," not "writing Python from scratch." Every role — including non-technical — can succeed at this.
- Participants who are performing well will find Loop 2 energizing. Those who are struggling will find it exposing. Diagnose which is which and adjust accordingly — struggling participants may need the EDD discipline broken down further; strong participants may need harder challenges.
- The adversarial thinking on Day 4 is a preview, not the main event. Don't build full adversarial agents yet — Session 5 covers that. The seed is: "What would a prompt that tries to find problems with your output look like?"
- **Transfer model note:** The Python evaluation scripts are built in Session 4 against workspace skills and sample stories. The transfer work this week is to run those same evaluation scripts against skill output on real stories from the backlog. The evaluation script itself doesn't need to change — but the skill output it's evaluating will be different on real stories. That's where the evaluation reveals real gaps. The `evaluations/example-eval-script.py` pushed to the workspace before Session 4 is a reference — participants study it, then write their own.