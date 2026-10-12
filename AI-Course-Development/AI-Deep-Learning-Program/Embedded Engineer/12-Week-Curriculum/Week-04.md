# Week 4 — Loop 1: Development Team
*No training session this week*

---

## Focus
Development team iterates on the `plan-story` and `implement-story` skeleton skills using EDD, refining Context and Constraints that are demonstrably load-bearing. The Plan → Code chain is applied to real sprint work — the skills were built in the workspace, now they're transferred to real stories. Evaluation Criteria (EC) written before building drive the iteration.

---

## Embedded Engineer Focus (Development Team)

- **Days 1–2:** EDD iteration on `plan-story` and `implement-story`. For each skill the team wants to improve, have them: (1) write EC before changing anything, (2) run the current skill against a real story (transferred from the workspace to the real codebase), (3) add or refine Context that addresses the failure modes they observed in Week 3, (4) run again and check which EC now pass. One change per iteration — document the hypothesis each time.
- **Day 3:** Pair with one developer to build a proper `implement-story` skill tailored to their real codebase, language, and framework. The skill was built in the workspace against sample stories; now adapt it for the real codebase. RTCC structure, EC written first, load-bearing audit after first successful run. Commit it.
- **Day 4:** Broader adoption — get the Plan → Code chain used by at least 2 developers on their own stories. Embedded Engineer coaches the transfer, doesn't take over.
- **Day 5:** Identify the most common failure mode in the generated plans and code. This becomes the input for Session 4's EDD work. Ask developers to write it down — not just observe it.

**Key Embedded Engineer priority this week:** Real Plan → Code generation on real sprint work, and real EDD iteration on the `plan-story` and `implement-story` skills. Not demos, not exercises — plans and code that get committed to the codebase, and skills that are measurably better than the RT-only stubs. The transfer from workspace to real codebase should be producing measurable results by now.

---

## Skill Iteration This Week

The goal is that by end of Week 4, `plan-story` and `implement-story` have been iterated beyond their RT-only stubs using EDD:

1. **For each skill to iterate:** Write EC first. What would good output look like? What are the 3–5 most important properties the output must have?
2. **Run the current version.** Score it against the EC. This is Red state — some EC should fail.
3. **Add or refine Context (first pass).** What is the WHY — the intent behind the task? What problem are we trying to solve? Run again. Record the delta.
4. **Add or refine Constraints (second pass).** What data does the model need? What rules must the output follow? What should it never do? What format is required? Run again. Check that each Constraint is load-bearing.
5. **Load-Bearing Audit.** Remove each instruction one at a time; if no EC fails, remove it.

The team does not need to perfect both skills this week. Well-iterated skills beat partially-improved ones.

---

## Participant Activities (Development Team)
- Use the Plan → Code chain on at least 3 real stories with Acceptance Criteria
- Evaluate each generated plan against EC: does it cover the AC? Does it identify edge cases? Does it reference file changes?
- Evaluate each generated code against EC: does it follow the plan? Does it adhere to conventions? Is it testable?
- Iterate at least one of `plan-story` or `implement-story` using EDD (EC written first, Context refined, Constraints refined, load-bearing audit completed)
- Identify the most common failure mode in plan or code generation output — write it down

## Participant Activities (Product/Process Team)
- Review developer feedback on epics-and-stories quality
- Update `epics-and-stories` skill to address specific gaps developers identified
- Run the updated skill on 5+ stories and compare EC scores to the previous version

---

## Artifacts Due by End of Week 4
- [ ] Development team: `plan-story` skill iterated (EC written, Context and Constraints refined, load-bearing audit) — committed
- [ ] Development team: `implement-story` skill iterated (EC written, Context and Constraints refined, load-bearing audit) — committed
- [ ] Development team: Plan → Code chain run on at least 3 real stories with EC scores
- [ ] Development team: failure mode documentation (what the plan or code generation gets wrong most often, written down)
- [ ] Product/Process team: updated `epics-and-stories` skill with EC score comparison (before/after update)

---

## Embedded Engineer Coaching Notes

- The EDD discipline on the skeleton skills is as important as the Plan → Code work. Watch for participants who add Context and Constraints without writing EC first — they're guessing at improvement rather than measuring it. Enforce the EC-first sequence every time.
- "Committed code" is the bar for code generation, not "generated code." Code that gets generated and deleted because it's wrong is a signal that the skill needs work — document this as a failure mode, don't hide it.
- The failure mode assessment directly feeds Session 4 (EDD formalization with Python evaluations). Ask developers to write down the failure mode they see most, not just to observe it. Written documentation of failures is the prerequisite for forming evaluation hypotheses.
- Check in with the Product/Process team mid-week. The epics-and-stories quality conversation is ongoing and the Dev team feedback should flow back continuously.
- Watch for developers who are running the skills but not reading the output carefully. The gaps in output are subtle — they require attention, not just execution. Slow them down and ask: "What did the model assume here that we didn't tell it?"
- Remember the RTCC structure: Context is WHY (intent), Constraints are HOW (data/rules). If participants put background data in Context, redirect them to Constraints. If they put intent in Constraints, redirect them to Context.
- **Transfer model note:** By Week 4, the skills built in the workspace should be producing real results on the real codebase. If the transfer hasn't happened yet — if developers are still only running skills on workspace sample stories — that's a red flag. The workspace is the training ground; the real codebase is where the value is. Push for at least one real story to go through the full Plan → Code chain this week.