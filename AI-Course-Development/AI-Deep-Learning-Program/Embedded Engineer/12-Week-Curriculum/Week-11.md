# Week 11 — Loop 2: Bounded Agents & Custom Harnesses
*Training Session 6 occurs this week*

---

## Focus
Embedded Engineer moves to the Testing team for the final loop. All participants attend Training Session 6 on Bounded Agents, Custom Harness Demo & Stage 4 Preview. Testing team builds `review-implementation` to Loop 2 depth. Session 6 has participants build a bounded agent (full pipeline run in the IDE) and the instructor demos a custom harness (Python program with clean context per step and evaluation at each step). The EE coaches the transfer of bounded agent and harness concepts to the real codebase. Session 6 also introduces the IIOS stage framework — where participants are (Stage 3) and what comes next (Stage 4). Session 6 closes with the capstone showcase, final maturity assessment, and commitment statements.

---

## Training Session This Week
**Session-6 — Bounded Agents, Custom Harness Demo & Stage 4 Preview** (4 hours, all participants)
- The Prompt/Harness/Model arc completes: Sessions 1–5 used the IDE's built-in harness. The bounded agent extends what the IDE harness can do — chaining skills into multi-step workflows. The custom harness demo reveals what's beyond it — Python programmatic orchestration with clean context per step.
- Bounded agent lab: participants run the full SDLC pipeline (epics-and-stories → plan-story → implement-story → review-implementation) in a single IDE session, with manual evaluation and adversarial review at key steps. The context window carries artifacts between steps.
- Context window discipline: participants experience context window degradation at later steps in the bounded agent lab, then discuss why it happens and what strategies help within the IDE.
- What a custom harness is: a Python program that orchestrates multiple model calls with clean context per step, passes artifacts between steps programmatically, evaluates each step automatically, and manages the overall workflow
- Instructor demo (requires API key): a custom harness implementing the full chain — Story → AC → Plan → Code → Review. The harness calls each skill with clean context, evaluates each output with a Python evaluation script + LLM judge, runs an adversarial agent against the code output, and produces a final artifact with evaluation scores at each step. The custom harness is demonstrated, not assigned — building one is the work of a future Stage 4 program.
- IIOS stage framework preview: where participants are (Stage 3: Task), what Stage 4 (Workflow) looks like, and what a future Stage 4 Deep Learning Program would cover.
- Capstone: artifact showcase (peer pairs)
- Final AI Adoption Maturity Assessment (7 dimensions, 21 questions)
- Commitment statements and program close

---

## Embedded Engineer Focus (Testing Team)

- **Day 1:** Re-engage the Testing team. Review their Loop 1 `review-implementation` skill — what's been used, what's been shelved, what's changed since Loop 1? Review Python evaluation iteration history.
- **Days 2–3:** Harder stories. In Loop 2, the `review-implementation` skill should be applied to complex, multi-risk scenarios from the real codebase. Build toward an integrated workflow: story → AC → plan → code → review. Write EC for the full chain first. Run adversarial agents against the review output.
- **Day 4:** Evaluation and iteration. The `review-implementation` skill's Python evaluation script should be running and informing changes on real stories. If it isn't, address this directly before Session 6.
- **Day 5:** Full chain run. Take one real story all the way from story input → epics-and-stories → plan-story → implement-story → review-implementation, using skills transferred from the workspace to the real codebase. Evaluate each step with Python evaluation scripts. Run adversarial agents against key outputs. This is the live demonstration of everything the program has built.

**Key Embedded Engineer priority this week:** The full chain should be visible and working. Every team's artifacts connect. The custom harness demo in Session 6 shows what the next step looks like — but the full chain run on Day 5 shows what participants have already built.

---

## Full Chain Demonstration (End of Week 11 or Start of Week 12)
The Embedded Engineer facilitates a walkthrough of the complete artifact chain with representatives from all three teams:
1. Product/Process team runs their `epics-and-stories` skill on a real story
2. Dev team takes that output and runs `plan-story` then `implement-story`
3. Testing team takes the story + AC + plan + code and runs `review-implementation`
4. Each step is evaluated with Python evaluation scripts — not just "it works" but "what's the quality score?"
5. Adversarial agents are run against key outputs to find gaps the evaluation scripts missed

This is the clearest evidence of what the 12-week program has built. Document it and, where appropriate, share it with the client stakeholder.

---

## Participant Activities (Testing Team)
- Attend Training Session 6
- Extend `review-implementation` skill to handle complex, multi-risk stories
- Run full chain with at least one real story end-to-end; evaluate with Python evaluation scripts
- Run adversarial agents against review output
- Complete capstone artifact showcase prep

## Participant Activities (All)
- Attend Training Session 6
- Build a bounded agent: run the full SDLC pipeline in the IDE with manual evaluation and adversarial review at key steps
- Complete AI Adoption Maturity Assessment (7 dimensions, 21 questions) — final assessment (administered in session)
- Write commitment statement (in session)
- Prepare artifact showcase for a peer: most-used skill + RTCC structure + Python evaluation history + one iteration cycle

---

## Artifacts Due by End of Week 11
- [ ] All participants: bounded agent run (full pipeline session output with evaluation and adversarial review at key steps)
- [ ] Testing team: updated `review-implementation` skill for complex stories (Python evaluation history showing iteration)
- [ ] Testing team: full chain run evaluated with Python evaluation scripts, each step scored
- [ ] All participants: completed AI Adoption Maturity Assessment (7 dimensions, 21 questions) — final
- [ ] All participants: written commitment statement (specific, observable, next-sprint behavior change)
- [ ] Full chain walkthrough conducted and documented (Embedded Engineer)

---

## Embedded Engineer Coaching Notes

- Session 6's commitment statements are only valuable if the Embedded Engineer follows up on them in Week 12. Capture each commitment in writing during the session. Schedule a brief individual check-in at the start of Week 12 for each participant.
- The bounded agent lab is a significant moment — participants compose the skills they've been building for 10 weeks into a full pipeline run in their IDE. This is the payoff of the program. Help participants see the connection: their individual skills are now working together as a multi-step workflow. The context window degradation they'll experience at later steps is the teaching moment for the custom harness demo that follows.
- The custom harness demo is a significant moment — it shows participants what the next level looks like. The instructor demonstrates the full chain automated through a Python program with API calls, clean context per step, evaluation at each step, and adversarial agents. Participants see where their skills fit into a production workflow. They do not build a harness in this session — the IIOS stage framework block explains that building one is the work of a future Stage 4 Deep Learning Program.
- The IIOS stage framework preview is important context for participants. They need to understand that completing this program puts them at Stage 3 (Task), which is a real achievement. Stage 4 (Workflow) is a ~10x effort jump requiring team coordination and IT infrastructure. The preview gives them a clear trajectory without overwhelming them.
- The full chain demonstration is a significant moment for the client. If a stakeholder can attend or observe, arrange it. Visible outcomes build continued support for the program.
- Some participants will feel they haven't done enough by Week 11. Review their Python evaluation iteration histories and name what they've actually built — the evidence is usually better than their self-assessment. Others will feel they've done enough and are coasting. Push them: "What would your evaluation scores look like if you ran your evaluator on the hardest story in the current sprint?"
- The capstone preparation matters. A participant who can walk a peer through their skill's RTCC structure, their Evaluation Criteria, their Python evaluation improvement history, and one specific thing they learned from the scores — that participant owns their artifact. One who can only say "I ran it a bunch and it's pretty good" does not.