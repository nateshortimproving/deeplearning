# Training Session 1 — The SDLC Pipeline & Epics-and-Stories Skill

*Week 1 | 4 Hours | All Participants | Loop 1 — Role Focus: Product/Process*

> **All-roles framing:** Every participant attends this session — Product/Process, Dev, and Testing roles alike. The primary artifact focus is the **epics-and-stories** skill, but every role benefits from understanding how stories with Acceptance Criteria (AC) are created: developers need AC to plan implementations, testers need AC to build reviews and test plans. This is the foundation of the full chain.

---

## Why This Session Comes First

The program starts here because the quality of every artifact downstream depends on the quality of the stories and their AC. If the stories are vague, the plans will be vague. If the plans are vague, the code will be vague. Starting with epics-and-stories means starting with leverage.

This session also introduces the three conceptual terms that frame the entire program — **Prompt, Harness, Model** — and the 7 SDLC skeleton skills that form the structural backbone of the next 12 weeks. Participants see the full pipeline on day one, then build out their first piece of it: the epics-and-stories skill.

More importantly: participants need to leave this session with something they can use with the Embedded Engineer starting the next morning. No orientation, no warm-up period, no "we'll get to the real work soon." The real work starts now.

---

## Session Goals

By end of this session, every participant:
- Understands the **Prompt / Harness / Model** distinction and can articulate why the model can only do what the harness allows
- Has seen all 7 SDLC skeleton skills in pipeline order and understands what each produces and what it consumes
- Has seen pre-generated demo outputs for create-prd, create-architecture, and create-ux (RT-only, not iterated this session)
- Used the RTCC structure (Role=WHO, Task=WHAT, Context=WHY, Constraints=HOW) to build out the epics-and-stories skill
- Understands the **AC/EC disambiguation**: the skill produces stories with Acceptance Criteria (AC); the participant writes Evaluation Criteria (EC) to evaluate the skill's output
- Has written Evaluation Criteria (EC) for the epics-and-stories skill before building it (EDD discipline)
- Has built a working epics-and-stories skill using the skill file format with `disable-model-invocation: true`
- Has generated stories with AC from sample-stories/ inputs and evaluated the output against written EC
- Can apply the **Load-Bearing Rule**: audit each instruction in a skill against its EC
- Is ready to work with the Embedded Engineer tomorrow — the EE will help transfer epics-and-stories skills from the workspace to the real codebase

---

## Agenda

| Time | Block | Format |
|------|-------|--------|
| 0:00–0:20 | Prompt, Harness, Model — the foundational framework | Presentation |
| 0:20–0:45 | The SDLC skeleton skills — walking the full pipeline | Presentation + Demo |
| 0:45–1:05 | IDE setup + rules file | Hands-on Lab |
| 1:05–1:25 | RTCC: WHO / WHAT / WHY / HOW — the structure every skill uses | Presentation + Exercise |
| 1:25–1:45 | EDD: define your Evaluation Criteria before you build | Presentation + Exercise |
| 1:45–2:00 | Break | |
| 2:00–2:45 | Build out the epics-and-stories skill | Hands-on Lab |
| 2:45–3:10 | Use it: generate stories with AC from sample epics | Hands-on Lab |
| 3:10–3:25 | Break | |
| 3:25–3:45 | Evaluate the output and apply the Load-Bearing Rule | Discussion + Analysis |
| 3:45–4:00 | Baseline AI Adoption Maturity Assessment + Wrap-up | Individual + Discussion |

---

## Detailed Block Notes

### Block 1: Prompt, Harness, Model — The Foundational Framework (20 min)

This block introduces the three terms that frame the entire program. Everything that follows — skills, evaluation, adversarial agents, custom harnesses — is grounded in this distinction.

**Prompt** — The instructions you give to a model. What you want it to do, how you want it done, what constraints it must follow. This is what participants spend the program learning to write well.

- **Harness** — The software environment that mediates between you and the model. The harness determines what the model can actually do on your machine. It decides what files the model can read, what commands it can run, what tools it has access to, and how its output reaches you. Claude Code, Devin, GitHub Copilot, and the ChatGPT web interface are all different harnesses with different capabilities and different boundaries.

**Model** — The AI itself. The model generates text based on its training and the prompt it receives. But the model cannot do anything on your box that the harness does not offer or allow it to. A model without a harness is a chat interface. A model with a harness can read files, run commands, and produce artifacts. The harness is the capability boundary; the model is the intelligence; the prompt is the instruction.

**Why this matters for the rest of the program:**
- Why skills need `disable-model-invocation: true` — the harness controls invocation, not the model. We choose to start with explicit (slash-command) invocation.
- Why Session 6 demos a custom harness — the IDE's built-in harness supports single-step interactions. Multi-step workflow integration requires a custom harness with API access.
- Why adversarial agents work (Session 5) — an adversarial agent is a prompt running through a harness that has access to the output of another prompt. The harness makes the connection; the model provides the judgment.

Don't linger here too long — the work is the teacher — but make sure participants can state the three terms and the relationship before moving on.

### Block 2: The SDLC Skeleton Skills — Walking the Full Pipeline (25 min)

This block introduces the structural backbone of the program: 7 SDLC skeleton skills in pipeline order.

**The 7 skeleton skills (pipeline order):**
1. **create-prd** — generates a Product Requirements Document from a product vision
2. **create-architecture** — generates an architecture design from a PRD
3. **create-ux** — generates UX wireframes/flows from a PRD + architecture
4. **epics-and-stories** — generates epics with stories (each story has AC) from a PRD + architecture + UX, and outputs to `stories.yaml`
5. **plan-story** — generates an implementation plan from a story + AC
6. **implement-story** — generates code from an implementation plan
7. **review-implementation** — generates a review of the implementation against the story + AC + plan + code

**The YAML pipeline:** Each skill in the pipeline writes its output to a specific file that the next skill reads as input. This creates a deterministic, auditable chain — you can inspect the intermediate artifact at every step. The pipeline flows as structured YAML from skill to skill:

![SDLC Pipeline](../images/sdlc-pipeline-simple.svg)

Each skeleton skill is an RT-only stub: Role and Task are pre-defined, but Context and Constraints are empty. Over the next three sessions, participants build out specific skeleton skills by adding Context (WHY) and Constraints (HOW) using EDD discipline.

**Demo outputs (pre-generated, RT-only — show but don't iterate this session):**
- Show a demo PRD produced by create-prd
- Show a demo Architecture produced by create-architecture
- Show a demo UX output produced by create-ux
- These are committed artifacts that participants can reference. They exist to show what good upstream artifacts look like and to serve as the input that the epics-and-stories skill consumes.

**Good/Bad/AI-Generated story demo:** The workspace `sample-stories/` directory contains three contrast examples for the quality-bar demo:
- `pantry-inventory.md` and `shopping-list.md` — **Good** stories with clear, testable AC in Given/When/Then format, edge cases covered, no implementation detail
- `vague-pantry-stories.md` — **Bad** stories: plausible-sounding but untestable, missing AC detail, no edge cases, no definition of "done"
- `ai-generated-pantry-stories.md` — **AI-generated without care**: polished-sounding but AC describe implementation detail (PostgreSQL, JWT, Redux, Firebase, WebSocket, OpenAI API), epics are too large, edge cases missing, some AC are untestable

**Key framing:** The epics-and-stories skill takes a PRD + architecture + UX as input and produces epics with stories, where each story has Acceptance Criteria (AC). This is where the program's primary iteration target for Session 1 lives.

**The `disable-model-invocation: true` flag:** Every skill in this program starts with `disable-model-invocation: true`. This means the skill only runs when explicitly invoked via slash command — the model will not auto-invoke it based on context. The harness controls invocation; we start with explicit invocation. Later (Session 5), participants will evaluate whether to enable model invocation on specific skills.

### Lab 1: IDE Setup + Rules File (20 min)

- Every participant clones the shared student workspace repo and opens it in their agentic tool of choice (Claude Code, Devin, GitHub Copilot, or equivalent)
- Minimum: a project-level rules file that gives the AI context about the workspace structure, the SDLC skeleton skills in `skills/`, the demo outputs in `demo-outputs/`, and the sample stories in `sample-stories/`
- Verify that participants can invoke skills via slash command — this is the harness-level interaction they'll use all program
- Trainer and Embedded Engineer circulate and unblock. Don't let setup failures persist — move to pair-debugging immediately.
- Checkpoint: everyone has a running tool with the workspace cloned and a committed rules file before moving on

**Stretch Goals (for advanced users):**
- Configure a custom rules file with project-specific conventions for the Pantry Tracker PWA — e.g., TypeScript strict mode, React component naming patterns, ShadCN/Tailwind usage guidelines, and Express route naming conventions. Go beyond the minimum workspace-structure rules and document real conventions the AI should follow when generating code.

### Block 3: RTCC — WHO / WHAT / WHY / HOW (20 min)

Every skill built in this program uses the same four-part structure. Learning it once means participants never start from blank when building a new skill.

**RTCC:**
- **R — Role (WHO):** Who the model should act as — a specific, credentialed persona that changes tone, vocabulary, and default assumptions
- **T — Task (WHAT):** What they should do — verb-first, unambiguous, the specific action to perform
- **C — Context (WHY):** Why we want this done — the intent behind the task. What outcome are we trying to achieve? What problem are we solving? Why does this matter? Context is the purpose that shapes how the model interprets its Role and Task.
- **C — Constraints (HOW):** The data, rules, and specifications the model needs. What background information is relevant? What codebase, standards, or domain knowledge applies? What rules must the output follow? What should it never do? What format is required? Constraints absorb the data, background, and specification elements.

**Why this order matters:** WHO and WHAT define the basic contract. WHY gives it purpose. HOW provides the data and rules. Adding data before establishing purpose produces outputs that have information but miss the intent.

**Example for epics-and-stories:**
> **Context (WHY):** We need stories with Acceptance Criteria that are specific enough for developers to write implementation plans from and testers to build reviews from. The purpose is to eliminate the back-and-forth between Product, Dev, and Testing that happens when stories arrive with vague or untestable criteria. Every story that enters the sprint should have AC that any role can read and know what "done" means.
>
> **Constraints (HOW):** Stories are written in the standard format: "As a [role], I want [capability], so that [benefit]." Stories are stored in Azure DevOps. The team works in .NET 8 with xUnit. Output must include 3–8 AC per story using Given/When/Then format. At least one AC must cover a failure or edge case. No AC should describe implementation detail.

The Context section answers: why are we generating stories with AC, and what makes them good for this team? The Constraints section answers: what data does the model need, and what rules must the output follow?

**Exercise (5 min):** For the epics-and-stories skill they're about to build, participants write down answers to each element before opening any file:
- R: Who should be generating these stories?
- T: What exactly are they doing?
- C (WHY): What outcome are we trying to achieve? Why does this matter?
- C (HOW): What data does the model need? What rules must the output follow?

This pre-work becomes the raw material for Lab 2.

### Block 4: EDD — Define Your Evaluation Criteria Before You Build (20 min)

Before writing a single line of the skill, participants write their Evaluation Criteria (EC). This is the most important habit in the program.

**The AC/EC disambiguation (critical for this session):**
- **Acceptance Criteria (AC)** — the product artifact. What a story must satisfy for it to be considered done. These are what the epics-and-stories skill *produces*.
- **Evaluation Criteria (EC)** — the quality bar for a skill's output. What the participant writes to measure whether the skill is producing good results. These are what the participant writes *before* building the skill.

When the instructor says "write your EC," participants should know exactly which kind of criteria they're writing: the EC for the epics-and-stories skill, not the AC that the skill generates.

**The EDD discipline:**
> Before building a skill, define what good output looks like — specifically, in writing — so that you can evaluate whether the skill is producing it.

**Why this matters:** If you define EC after seeing the output, the model has already shaped your expectations. You'll tend to see the output as good because it's what the model produced. Writing EC first forces an honest definition of the target before you see whether it was hit.

**Exercise (10 min):** For the epics-and-stories skill, participants write 4–6 specific Evaluation Criteria before building anything. Each criterion should be answerable as yes/no or countable.

**Examples of weak EC:** "It sounds like good stories."
**Examples of strong EC:** "Every story includes 3–8 Acceptance Criteria in Given/When/Then format. At least one AC per story covers a failure or edge case. No AC describes implementation detail. Every story follows the 'As a [role], I want [capability], so that [benefit]' format. Each epic contains 3–7 stories."

These EC become the evaluation standard used after Lab 3.

### Lab 2: Build Out the Epics-and-Stories Skill (45 min)

A skill is not a saved prompt. It's a transferable, intentional instruction set another developer could use. It uses RTCC structure. Every instruction should correspond to at least one of the EC written in Block 4.

**Build the skill using the RTCC pre-work:**
- R: Your Role element — the specific persona
- T: Your Task element — what the skill does, verb-first
- C (WHY): Your Context element — the intent behind the task
- C (HOW): Your Constraints element — the data, rules, and specifications

**Skill file format:** Use the skill file format with `disable-model-invocation: true`. The skill is invoked via slash command. The RTCC structure lives inside the skill file.

**Apply the Load-Bearing Rule as you build:** For each instruction you write, ask: which Evaluation Criterion from Block 4 would fail if I removed this instruction? If no EC would fail, don't add the instruction. A skill instruction that corresponds to no Evaluation Criterion is either testing something you haven't written down, or it's not doing anything at all.

- In your breakout room, pair up as you build: would your partner's skill produce useful stories with AC for the sample epics?
- Use the demo PRD/Architecture/UX outputs in `demo-outputs/` as input — the epics-and-stories skill consumes these artifacts
- Build the skill in the workspace's `skills/` directory
- Commit the skill file before the next lab

**Stretch Goals (for advanced users):**
- Add model invocation criteria to your skill — write 3+ positive trigger test cases describing specific scenarios where the skill SHOULD invoke (e.g., "invoke when the input is a PRD with feature requirements and architecture artifacts" or "invoke when a user story needs acceptance criteria generated"). This prepares you for Session 5, where you'll evaluate enabling `disable-model-invocation: false` and letting the model decide when to trigger the skill automatically.

### Lab 3: Use It — Generate Stories with AC from Sample Epics (25 min)

- Each participant runs their epics-and-stories skill on the sample epics in `sample-stories/` (pantry-inventory.md and shopping-list.md — the EE has additional examples ready if needed)
- Dev and Testing role participants: run it on the sample stories you'll be planning or reviewing in Session 2 — this is your upstream material
- **Output should be written to `stories.yaml` in the workspace root** — this is the YAML pipeline artifact that Session 2's plan-story skill will read as input
- Generate, review, evaluate each output against the EC from Block 4
- Record: which EC does the output pass? Which does it fail? What's the most common failure?

**Stretch Goals (for advanced users):**
- In addition to the sample stories, run your epics-and-stories skill on a real story from your own backlog or project. Compare the output quality against the sample-story runs — does the skill generalize, or does it overfit to the Pantry Tracker PWA domain? Note any EC that pass on samples but fail on your real story.

### Block 5: Evaluate the Output and Apply the Load-Bearing Rule (20 min)

Group evaluation and audit.

**Part 1 — Group evaluation (10 min):**
- Share outputs across the room — anonymized if preferred
- Group scores each output on the EC from Block 4
- What's the most common failure pattern in this group's output?
- Key question for Dev and Testing roles: "Could you write an implementation plan from these stories and their AC?" If not, why not? Name it.

**Part 2 — Load-Bearing Audit (10 min):**
Participants review their own skill. For each instruction:
- Which of your Evaluation Criteria would fail if you removed this instruction?
- If no EC would fail, the instruction is dead weight — flag it for removal
- Also check: is the instruction in the right RTCC section? Background data in Context (WHY) should be moved to Constraints (HOW). Intent in Constraints should be moved to Context.
- Run the skill again after removing flagged instructions and verify the EC scores don't drop

This is the Refactor step. A skill with no dead instructions is a cleaner, more reliable skill.

### Block 6: Baseline AI Adoption Maturity Assessment + Wrap-up (15 min)

**Baseline Assessment (10 min):**
- Participants complete the AI Adoption Maturity Assessment individually — this is the Week 1 baseline
- The assessment covers 7 dimensions: Prompt Engineering & AI Interaction, Task Agents & Single-Box Automation, Workflow Orchestration & Coordination, Output Evaluation & Quality Judgment, Governance/Trust & Safety Nets, Trust & Working Identity, and Team & Organizational Practices
- 21 questions total; each answered A through D (1–4 points). Total score range is 21–84.
- Not graded. The only instruction is honesty.

**Wrap-up (5 min):**
- What the Embedded Engineer will be doing this week: embedded with the whole team, primary focus on epics-and-stories generation with Product/Process role members
- What participants should do before Week 2: use their epics-and-stories skill on at least 3 more sample stories from `sample-stories/`; evaluate each output against the EC they wrote today
- What to bring to the Embedded Engineer: the output, the EC scores, the failure modes

---

## Session Artifacts

Each participant leaves with:
- [ ] Committed rules file for the student workspace
- [ ] Committed epics-and-stories skill in `skills/` (skill file format, `disable-model-invocation: true`, RTCC structure, load-bearing audit completed)
- [ ] Written Evaluation Criteria (EC) — 4–6 specific, measurable criteria for epics-and-stories output
- [ ] Stories with AC generated from sample stories in `sample-stories/` with EC scores noted
- [ ] `stories.yaml` committed to the workspace root (the pipeline artifact for Session 2)
- [ ] Completed baseline AI Adoption Maturity Assessment (7-dimension, 21-question instrument)

---

## Trainer Notes

- **The Prompt/Harness/Model block is not optional and is not just theory.** It is the conceptual foundation for Sessions 5 and 6. Participants who don't internalize it will struggle to understand why skills have `disable-model-invocation: true`, why adversarial agents work, and why custom harnesses are the endpoint of the program. Make sure participants can state the three terms before moving on.
- **The AC/EC disambiguation is the most important conceptual moment of this session.** Participants are building a skill that *produces* Acceptance Criteria (AC) while simultaneously writing Evaluation Criteria (EC) to evaluate that skill. If both are called "criteria," confusion is guaranteed. Use the full terms — "Acceptance Criteria" and "Evaluation Criteria" — and the abbreviations "AC" and "EC" consistently from the first mention.
- **The RTCC block with the WHO/WHAT/WHY/HOW framing is critical.** Context is WHY (intent), not "background information." Constraints are HOW (data/rules). This distinction gives participants a structural diagnostic for the Load-Bearing Audit: if background data is sitting in Context, it's in the wrong place.
- **The EDD block is the most important habit.** If participants leave without internalizing "define EC before you build," the evaluation work in Session 4 will feel like a new idea instead of a deeper application of something they already know.
- **The Load-Bearing Rule should be introduced gently but firmly.** Participants will find it uncomfortable to audit their own skill and discover dead instructions. That discomfort is the learning.
- **Dev and Testing participants may feel like this session isn't for them.** It is. Make the downstream dependency explicit early and return to it throughout: developers plan from stories + AC, testers review against stories + AC.
- **The demo PRD/Architecture/UX outputs are show-and-tell, not iteration targets.** Show them (from `demo-outputs/` in the workspace) so participants see the full pipeline and understand what feeds into epics-and-stories. Don't spend time iterating them this session.
- **The good/bad/AI-generated story demo uses three contrast files in `sample-stories/`.** The good stories (`pantry-inventory.md` and `shopping-list.md`) have clear, testable AC. The vague stories (`vague-pantry-stories.md`) sound plausible but are untestable — missing AC detail, no edge cases, no definition of "done." The AI-generated-without-care stories (`ai-generated-pantry-stories.md`) sound polished but AC describe implementation detail (PostgreSQL, JWT, Redux, Firebase, WebSocket, OpenAI API), epics are too large, and edge cases are missing. Walk through all three so participants see what the skill should produce and what it shouldn't.
- **Workspace setup is the only Session 1 setup.** Participants clone the student workspace repo and open it in their IDE. No per-participant environment debugging — the workspace is self-contained. The EE's job between sessions is to help participants transfer skills from the workspace to their real codebase.
- The Embedded Engineer should be active in Labs 1–3, not observing. They're establishing their coaching presence from day one.

**EE Transfer Model:** Between sessions, the EE helps participants transfer skills from the workspace to their real codebase. The workspace is the training ground; the real codebase is the application. All labs and demos work against the shared workspace — the EE coaches the transfer.

**Trainer repo push (after Session 1):** The workspace is complete for Session 1, including the good/bad/AI-generated story demo files in `sample-stories/`.