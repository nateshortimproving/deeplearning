# Week 1 — Loop 1: Product/Process Role Focus
*Training Session 1 occurs this week*

---

## Role Focus This Week
**Product/Process** — The Embedded Engineer's primary coaching energy this week is on the Product/Process role's workflow: how stories and Acceptance Criteria (AC) are currently written, what friction exists, and what epics-and-stories generation can unlock. The Embedded Engineer is present with the whole client team and available to everyone, but the core coaching work is focused on this role's artifacts.

---

## Training Session 1 — Prompt/Harness/Model + SDLC Skeleton Skills + Epics & Stories Generation
*(4 hours, all participants attend regardless of role)*

**Content:**
- Program overview — where we are, where we're going, what DLP Completion actually means
- **Prompt/Harness/Model** — the foundational conceptual framework:
  - **Prompt** — the instructions you give to a model; what you want it to do, how, and what constraints it must follow
  - **Harness** — the software environment that mediates between you and the model; determines what the model can actually do (read files, run commands, access tools). Claude Code, Devin, Copilot, ChatGPT web — all different harnesses with different boundaries
  - **Model** — the AI itself; generates text based on training and prompt. Can only do what the harness allows
  - Why this matters: skills need `disable-model-invocation: true` because the harness controls invocation, not the model
- Basic Prompting vs. DLP Completion — the difference between using AI off-the-shelf and building craft
- IDE agentic tool setup and configuration
- **SDLC skeleton skills introduced** — all 7 skeleton skills in pipeline order:
  - `create-prd` → `create-architecture` → `create-ux` → `epics-and-stories` → `plan-story` → `implement-story` → `review-implementation`
  - Demo outputs pre-generated for `create-prd`, `create-architecture`, and `create-ux` so participants see the full pipeline and what feeds into `epics-and-stories`
  - All skeleton skills are skills with `disable-model-invocation: true` — invoked via slash command
  - Each has Role and Task defined; Context and Constraints are intentionally left empty
- RTCC prompt structure — Role (WHO), Task (WHAT), Context (WHY — intent), Constraints (HOW — data/rules)
- EDD discipline — define Evaluation Criteria (EC) before building any skill
- **Build out the `epics-and-stories` skeleton skill** — the primary iteration target:
  - Participants add Context (WHY we need good stories, what makes a story actionable) and Constraints (HOW stories should be formatted, what data the model needs)
  - The demo PRD/Architecture/UX outputs are the input that `epics-and-stories` consumes — the chain is visible from day one
  - Evaluation Criteria (EC) for the skill's output written before building — what makes good epics-and-stories output?
  - **AC vs. EC disambiguation**: participants build a skill that generates Acceptance Criteria (AC) from stories, and simultaneously write Evaluation Criteria (EC) to evaluate that skill's output. AC = the product artifact. EC = the quality bar for the skill's output. Never confuse the two.
- Load-Bearing Rule — auditing every instruction against an Evaluation Criterion: "which EC would fail if I removed this instruction?"
- Baseline AI Adoption Maturity Assessment (7 dimensions, 21 questions)

**Goal:** Participants leave Session 1 with a working tool environment, an understanding of Prompt/Harness/Model, the SDLC skeleton skills introduced, a committed `epics-and-stories` skill built out using RTCC with `disable-model-invocation: true`, written Evaluation Criteria (EC) for its output, and enough understanding to apply EDD discipline with Embedded Engineer support this week.

---

## Embedded Engineer Coaching Priorities

- **Day 1:** Orient. Meet the whole team. Understand who is in which role. Ask questions about their current workflow — story writing, backlog refinement, who writes Acceptance Criteria and how. Observe ceremonies if happening. Don't introduce AI. **Help every participant clone the shared student workspace repo and set up their IDE against it.** This is the only setup required — the workspace contains all 7 SDLC skeleton skills, demo outputs, and sample stories. No per-participant environment debugging.
- **Day 2:** Shadow the Product/Process role members specifically. Understand the highest-friction point in their current Acceptance Criteria process. What takes longest? What gets rewritten? What are the most common sprint-time surprises about unclear requirements? This is context you'll need for the transfer work — you're learning what their real codebase workflow looks like so you can help them map workspace skills onto it.
- **Day 3:** Training Session 1 occurs. Be present and engaged — the Embedded Engineer's enthusiasm and credibility are set here. Participants work in the workspace during the session.
- **Day 4:** Post-session, begin the transfer work. Participants built out the `epics-and-stories` skill in the workspace during Session 1 using sample stories. Now sit with a Product/Process role member and help them apply that same skill to one real story from their actual backlog. The skill lives in the workspace; the real story comes from their real codebase. Evaluate the output against the EC written in session. Commit the result to the workspace.
- **Day 5:** Reflect with the team. What did they notice? What felt awkward? What surprised them? Don't over-coach — listen. The key question for the transfer model: did the skill that worked on a sample story in the workspace also work on a real story from their backlog? If not, what needs to change — the skill's Context/Constraints, or the story format?

**Key Embedded Engineer priority this week:** Trust before tools, and workspace before codebase. The team needs to see the Embedded Engineer as a peer who understands their real work before they'll engage with change. Credibility is earned by being genuinely helpful on actual work, not by running demos. The workspace is the training ground; your job between sessions is to help participants transfer what they learned in the workspace to their real codebase.

---

## Participant Activities

### Product/Process Role
- Attend Training Session 1
- Complete baseline AI Adoption Maturity Assessment (7 dimensions, 21 questions)
- Clone the shared student workspace and configure agentic IDE tool against it
- Commit a first rules file for the real project
- Build out the `epics-and-stories` skeleton skill in the workspace: add Context (WHY) and Constraints (HOW) using RTCC, with `disable-model-invocation: true`
- Write Evaluation Criteria (EC) for the skill's output before running it
- Try `epics-and-stories` on at least one sample story in the workspace, then transfer to one real story from the actual backlog with Embedded Engineer support; evaluate against the EC written in session

### Development Role
- Attend Training Session 1
- Complete baseline AI Adoption Maturity Assessment (7 dimensions, 21 questions)
- Clone the shared student workspace and configure agentic IDE tool against it
- Commit a first rules file for the real project
- Build out a skeleton skill in the workspace for a real personal coding task (RTCC structure, `disable-model-invocation: true`)

### Testing Role
- Attend Training Session 1
- Complete baseline AI Adoption Maturity Assessment (7 dimensions, 21 questions)
- Clone the shared student workspace and configure agentic IDE tool against it
- Commit a first rules file for the real project
- Build out a skeleton skill in the workspace for a real personal testing task (RTCC structure, `disable-model-invocation: true`)

---

## Artifacts Due by End of Week 1
- [ ] Baseline AI Adoption Maturity Assessment (7 dimensions, 21 questions) — all participants
- [ ] Student workspace cloned and IDE configured against it — all participants
- [ ] Rules file committed — all participants
- [ ] First skill committed (RTCC structure, `disable-model-invocation: true`) — all participants
- [ ] Written Evaluation Criteria (EC) for their skill (4+ criteria, written before running) — all participants
- [ ] `epics-and-stories` skill built out with Context and Constraints added in the workspace — Product/Process role members (with Embedded Engineer support)
- [ ] Epics & stories generation attempt on one sample story in the workspace, then transfer to one real story — Product/Process role members
- [ ] Embedded Engineer observation notes: current story/AC process, friction points, team dynamics (internal, not submitted)

---

## Embedded Engineer Coaching Notes

**On resistance:** Expect two flavors — "this won't work for our stories" (skepticism) and "this is going to solve everything" (over-excitement). Both derail learning. Defer to the actual work. The story either produces good epics-and-stories output or it doesn't. Let the artifact be the judge.

**On skills vs. ad-hoc prompts:** If participants conflate these, use this framing: an ad-hoc prompt is a sticky note — useful, personal, not transferable. A skill is a procedure — RTCC-structured, repeatable, committable, shareable with the team, with `disable-model-invocation: true` so it runs when you explicitly invoke it via slash command.

**On AC vs. EC confusion:** This is the most common Session 1 confusion. Participants are building a skill that generates Acceptance Criteria (AC) from stories, and simultaneously writing Evaluation Criteria (EC) to evaluate that skill's output. If someone says "criteria" without specifying which kind, stop and ask: "Do you mean Acceptance Criteria — what the story must satisfy? Or Evaluation Criteria — what the skill's output must satisfy?" Enforce the distinction from day one.

**On EDD:** Watch for participants who generate output and then write EC to match what they got. That inverts EDD entirely — the EC should be written before the skill runs, when the model hasn't yet shaped expectations. If you see this, name it directly and ask them to write the EC fresh, before the next run.

**On Prompt/Harness/Model:** If participants struggle with the concept, anchor on the harness: "Your IDE is the harness. The model can only do what the harness allows. When we set `disable-model-invocation: true`, we're telling the harness not to auto-invoke the skill — we invoke it ourselves via slash command. Later in the program, we'll discuss when to let the harness invoke skills automatically."

**On the AI Adoption Maturity Assessment:** Some participants will rate themselves higher than they are (optimism) and some lower (imposter syndrome). Don't correct them yet. The value of the baseline is comparison at Week 7 and Week 12, not accuracy at Week 1.

**On tool setup friction:** Some participants will arrive at Session 1 with tool setup issues. Don't let this block anyone from the conceptual content. Setup can be finished the next morning — RTCC and EDD understanding shouldn't wait. The shared student workspace eliminates most setup friction: clone the repo, open it in the IDE, and everything is there. If a participant's environment has issues, it's likely their IDE configuration, not the workspace.

**On the transfer model:** The workspace is the training ground; the real codebase is the application. Session 1 teaches in the workspace using sample stories. Your job starting Day 4 is to help participants transfer the skill to a real story from their actual backlog. If the skill works on a sample story but not on a real one, that's not a failure — it's the signal for what Context or Constraints need to change. The transfer is where the real learning happens.