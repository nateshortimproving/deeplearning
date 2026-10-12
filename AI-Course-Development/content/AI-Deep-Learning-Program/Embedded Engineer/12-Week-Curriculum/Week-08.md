# Week 8 — Loop 2: EDD with Python Evaluations
*No training session this week*

---

## Focus
Product/Process team deepens epics-and-stories generation practice using EDD with Python evaluations. Begins exploring adversarial thinking against their skill output. Python evaluation discipline should be habitual by end of this week.

---

## Embedded Engineer Focus (Product/Process Team)

- **Days 1–2:** Deepen the evaluation cycle. The team should be running their Python evaluation script regularly and documenting iteration cycles. Push for at least 2 documented cycles this week: hypothesis → change → evaluation run → conclusion. Each cycle changes one thing.
- **Day 3:** Introduce the adversarial thinking preview in more depth. Have participants write an ad-hoc adversarial prompt — a prompt that tries to find problems with their `epics-and-stories` output. What does it find that the evaluation script missed? This is preparation for Session 5.
- **Day 4:** Address the hardest case in the sprint backlog. What story has the team been avoiding running through the skill because they don't trust it? Do that one — with the Python evaluation script measuring the result.
- **Day 5:** Cross-team sync — Product/Process team reviews their best epics-and-stories with the Dev team. Is it actually producing good plans? Close the feedback loop with evaluation evidence, not just opinions.

**Key Embedded Engineer priority this week:** Independence. The Product/Process team should be able to run their epics-and-stories workflow without the Embedded Engineer present by end of this week — and Python evaluation results should be the thing that drives their skill changes, not gut feel.

---

## Independence Check (End of Week 8)
The Embedded Engineer should be able to step out for a half-day and the Product/Process team continues generating epics-and-stories without degradation. If this isn't true, identify why and address it in the remaining 4 weeks.

---

## Participant Activities (Product/Process Team)
- Run epics-and-stories workflow independently on at least one full sprint's worth of stories
- Run Python evaluation script on at least one skill variation — one documented hypothesis and result
- Write an ad-hoc adversarial prompt against their skill output; note what it finds that the evaluation script missed
- Cross-team review: share best epics-and-stories output with Dev team, gather feedback

## Participant Activities (All)
- Continue iterating on their primary skill using Python evaluation scripts
- Begin thinking about the model invocation question: is any skill ready for the model to invoke automatically? (Preview — Session 5 covers this formally)

---

## Artifacts Due by End of Week 8
- [ ] Product/Process team: `epics-and-stories` skill demonstrably used independently (Embedded Engineer not present)
- [ ] Product/Process team: at least one documented Python evaluation iteration cycle since Session 4
- [ ] Product/Process team: cross-team feedback captured from Dev team on epics-and-stories quality

---

## Embedded Engineer Coaching Notes

- The independence check is critical. It's easy for participants to perform competence when the Embedded Engineer is present. The test is what happens when they're not.
- If a participant can't run their workflow independently, diagnose: is it a skill quality gap, a confidence gap, or an evaluation script problem? Each has a different fix.
- The cross-team feedback loop is often neglected. Facilitate it explicitly — put a calendar hold on a 30-minute slot for Product and Dev to review epics-and-stories together. Ask them to bring evaluation results, not just opinions.
- Start planting the model invocation question this week, ahead of Session 5. "Is there a skill you've been running for 6+ weeks that you'd trust the model to invoke automatically based on context?" This primes the Session 5 conversation.
- The adversarial prompt preview this week is informal — just a prompt that challenges the output. Session 5 formalizes this into adversarial agents. The preview helps participants see the gap between evaluation (measuring against EC) and adversarial challenge (finding problems the EC didn't anticipate).
- **Transfer model note:** By Week 8, both the skills and the evaluation scripts should be running against real stories from the backlog, not just workspace samples. The transfer from workspace to real codebase should be complete for the Product/Process team. The independence check this week is: can the team run their full workflow (skills + evaluation) on real stories without the EE present? If they can only do it in the workspace, the transfer isn't done yet.