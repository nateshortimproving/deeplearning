# Week 10 — Loop 2: Model Invocation + Adversarial Agents
*No training session this week*

---

## Focus
Development team deepens model invocation work and adversarial agent practice. Model invocation decisions made in Week 9 are validated in production use. Adversarial agents are refined and run against harder cases. Evaluation discipline should be fully habitual. Independence check applies.

---

## Embedded Engineer Focus (Development Team)

- **Days 1–2:** Continue model invocation validation. Run invocation validation on any skills with model invocation enabled — did they invoke when they should? Did they stay silent when they shouldn't? Address any over-invocation or under-invocation immediately, before it becomes a habit.
- **Day 3:** Adversarial agent refinement. Take the adversarial prompts from Week 9 and run them against harder outputs — complex stories, edge cases, unusual inputs. What does the adversarial agent find now? Update the adversarial prompt based on what it missed.
- **Day 4:** Evaluation maturity check. Is the Python evaluation script being used as a real feedback mechanism on both skills and adversarial agents, or was it a one-time setup? Run a documented iteration cycle together on the current state of `implement-story` or the highest-use skill.
- **Day 5:** Independence session — the Embedded Engineer observes without coaching. The Dev team runs their full workflow independently. Embedded Engineer takes notes but does not intervene unless there's a genuine blocker.

**Key Embedded Engineer priority this week:** Dev team runs their full workflow — skills, model invocation, Python evaluation, adversarial agents — independently. Embedded Engineer observes, doesn't drive.

---

## Independence Check (End of Week 10)
The Dev team runs their Plan → Code workflow (skills with or without model invocation + evaluation + adversarial checks) without Embedded Engineer involvement on at least one real sprint story. If this isn't working, the Embedded Engineer needs to understand why and make it the top priority for the remaining 2 weeks.

---

## Participant Activities (Development Team)
- Run invocation validation on any skills with model invocation enabled; document results
- Refine adversarial prompts; run against harder outputs; document findings
- Run full workflow independently on 3+ real sprint stories
- Update Python evaluation scripts based on results from harder stories
- Cross-team review: share skill output with Testing team, gather feedback on coverage gaps

## Participant Activities (All)
- Begin preparing capstone artifact for Session 6: most-used skill (with RTCC structure, Python evaluation history, iteration log) and any adversarial agents
- Continue using and iterating their primary skill with Python evaluation scripts

---

## Artifacts Due by End of Week 10
- [ ] Development team: invocation validation results for any skills with model invocation enabled
- [ ] Development team: refined adversarial prompts with findings against harder outputs
- [ ] Development team: workflow run independently on 3+ real stories (Embedded Engineer observing, not coaching)
- [ ] Development team: Python evaluation script updated with harder test cases
- [ ] Cross-team feedback from Testing team captured

---

## Embedded Engineer Coaching Notes

- By Week 10, participants who are going to achieve DLP Completion are on a clear trajectory. Those who aren't will show it here. Be direct with any participant who is at risk — name it, give them a specific path, and give them the two remaining weeks to close the gap.
- Over-invocation of skills with model invocation enabled is the most common problem at this stage. A skill that runs when it shouldn't may produce output that gets committed or acted on before anyone notices. Treat over-invocation incidents as urgent — add the failing case as a negative invocation test and update the skill's boundary.
- Adversarial agents should be finding real problems by now. If the adversarial prompt only finds things the evaluation script already catches, it's not adding value. Push for adversarial prompts that find gaps the EC didn't anticipate — that's the whole point.
- The cross-team feedback loop between Dev and Testing is often where the most interesting conversations happen. Facilitate the overlap — testing teams often see coverage gaps that developers don't.
- At this point, if any participant has not run a Python evaluation iteration since they first set it up, that's a red flag. Evaluation without iteration is box-checking. Address it directly.
- Start the conversation about Session 6 artifacts. What skill, adversarial agent, or bounded agent run will each participant present in the capstone? The best capstone presentations are built on a real iteration history, not assembled in a hurry.
- **Transfer model note:** By Week 10, all skills, evaluation scripts, and adversarial agents should be running against real codebase inputs. The workspace was the training ground; the real codebase is where the value is produced. The independence check this week should be against real sprint stories — if the Dev team can only run their workflow independently in the workspace but not on the real codebase, the transfer isn't complete. Push for at least one real sprint story to go through the full workflow (skills + evaluation + adversarial) without EE involvement.