# Training Session 2 — The Development Loop: Plan → Code

*Week 3 | 4 Hours | All Participants | Loop 1 — Role Focus: Development*

> **All-roles framing:** Every participant attends. The primary artifact focus is the Development Loop — building out the **plan-story** and **implement-story** skills from the SDLC skeleton. Product/Process role participants see how their epics-and-stories output directly shapes the quality of plans and code. Testing role participants see the implementation artifacts that the review-implementation skill (Session 3) will evaluate.

---

> **⚠️ Pipeline Transition — Read This First**
>
> Your Session 1 output (`stories.yaml`) is the **INPUT** to Session 2. This transition is vital — plan quality depends on story quality. **Garbage in, garbage out.** The `plan-story` skill reads `stories.yaml` from the workspace root; if it's missing or poorly written, every downstream artifact suffers.

---

## Why This Session Is Here

By Week 3, participants have two weeks of working with the epics-and-stories skill against the shared student workspace behind them. The Dev role has been receiving those stories with AC and working with them. This session takes the next step in the chain: using story + AC as the specification for an implementation plan, then using that plan as the specification for code.

The key design insight: **the quality of the plan determines the quality of the code.** This is the Plan quality dependency, and it's the same lesson as the upstream quality dependency from Session 1 — but now it's tangible because participants can see a vague plan produce vague code and a specific plan produce specific code.

This session is framed as **"The Development Loop"** — the inner loop of development: plan, code, evaluate, iterate. The plan-story and implement-story skeleton skills are its articulation.

---

## Session Goals

By end of this session, every participant:
- Understands the Development Loop: Plan → Code as a two-step skill workflow
- Has built out the **plan-story** skill from its SDLC skeleton — adding Context (WHY) and Constraints (HOW) using EDD discipline
- Has built out the **implement-story** skill from its SDLC skeleton — adding Context and Constraints using EDD discipline
- Has written Evaluation Criteria (EC) for both skills before building them
- Knows the most common failure modes in AI-generated plans (vague plans, missing edge cases, over-constrained implementations) and how plan quality determines code quality
- Can apply the Load-Bearing Rule to audit both skills against their EC
- Understands the Plan quality dependency concretely — upstream quality determines downstream quality
- Connects back to Session 1: the epics-and-stories output is the input to plan-story
- Is ready to work with the Embedded Engineer on plan-and-implement work this week, transferring skills from the workspace to their real codebase

---

## Agenda

| Time | Block | Format |
|------|-------|--------|
| 0:00–0:15 | Check-in: what happened in Weeks 1–2? | Discussion |
| 0:15–0:40 | The Development Loop: Plan → Code — and how AI gets it wrong | Presentation |
| 0:40–1:10 | Plan → Code generation — structured prompting demo | Demonstration |
| 1:10–1:30 | Break | |
| 1:30–1:45 | EDD: write your EC for plan-story and implement-story before building | Exercise |
| 1:45–2:30 | Lab 1: Build out the plan-story skill | Hands-on Lab |
| 2:30–3:00 | Lab 2: Build out the implement-story skill | Hands-on Lab |
| 3:00–3:15 | Break | |
| 3:15–3:35 | The Plan quality dependency — group analysis | Discussion |
| 3:35–3:50 | Load-Bearing Audit on both skills | Analysis |
| 3:50–4:00 | Wrap-up: what to expect from the Embedded Engineer this week | Discussion |

---

## Detailed Block Notes

### Block 1: Check-in (15 min)

- Who used their epics-and-stories skill since Session 1? What output did you get from the `sample-stories/` inputs? Did you evaluate it against the EC you wrote?
- Embedded Engineer shares one real observation from Weeks 1–2 — something that worked, something that didn't, what the EC scores showed (anonymized) — drawn from either workspace work or the transfer to the real codebase
- Transition: "You've been generating stories with AC from the workspace. Now we find out if they're actually useful for planning and coding."

### Block 2: The Development Loop — Plan → Code (25 min)

**The Development Loop** is the inner loop of development:
1. **Plan** — Given a story + AC, generate an implementation plan (approach, key decisions, edge cases, file changes)
2. **Code** — Given the implementation plan, generate the code

The loop is: plan, code, evaluate, iterate. You don't ask AI to "write the code" — you plan first, then generate code from the plan.

**Why two steps instead of one:**
- A plan is an artifact that can be evaluated: Is it specific? Does it cover edge cases? Does it reference the AC?
- Code generated from a plan can be evaluated against the plan — a two-layer evaluation surface
- The Plan step is where human judgment and AI assistance interact most productively
- This is the discipline that separates DLP Completion from Basic Prompting

**How AI gets planning wrong:**
- **Vague plans**: "Implement the user registration feature" — no approach, no decisions, no edge cases
- **Missing edge cases**: plan covers the happy path but doesn't address what happens when validation fails, when the database is unavailable, when concurrent requests collide
- **Over-constrained plans**: plan dictates implementation so specifically that the code skill has no room to make reasonable choices
- **Disconnected from AC**: plan doesn't reference the Acceptance Criteria, so the code may not satisfy them

**How plan quality determines code quality:**
- A vague plan produces vague code — the code skill has nothing specific to work from
- A plan that misses edge cases produces code that misses edge cases
- A plan that references the AC produces code that satisfies the AC
- The plan is the specification for the code; the story + AC is the specification for the plan

**The chain so far:**
- Session 1: epics-and-stories → stories with AC
- Session 2 (today): story + AC → plan-story → implementation plan → implement-story → code
- The epics-and-stories output from Session 1 is the input to plan-story — the chain continues

### Block 3: Plan → Code Generation — Structured Prompting Demo (30 min)

**Demonstration:** Trainer takes a sample story + AC from `sample-stories/` (ideally generated by the epics-and-stories skill in Session 1) and demonstrates the two-step workflow live using RTCC-structured skills.

**Step 1 — Plan generation (plan-story):**
- **The plan-story skill reads `stories.yaml` from the workspace root — if the file is missing, the skill fails immediately with a clear error.** This enforces the pipeline contract: no stories, no plans.
- Walk through the RTCC elements for plan-story:
  - R: A senior engineer in the specific language and framework
  - T: Given a story and its Acceptance Criteria (from `stories.yaml`), generate an implementation plan
  - C (WHY): We need a plan specific enough that a code generation step can produce working code from it. The purpose is to separate thinking about approach from writing code — so that the code step has a clear specification to follow.
  - C (HOW): Language, framework, codebase conventions, relevant dependencies. Plan must include: approach summary, key decisions, edge cases, file changes. Plan must reference each AC. Plan must not over-constrain implementation detail.
- Show what changes when the skill is structured vs. ad hoc
- Walk through the generated plan: what's useful, what requires human judgment to complete

**Step 2 — Code generation (implement-story):**
- **The implement-story skill reads `plan.yaml` from the workspace root** — the plan-story skill writes to this file, and implement-story picks it up as its input. This is the next link in the YAML pipeline.
- Walk through the RTCC elements for implement-story:
  - R: A senior engineer in the specific language and framework
  - T: Given an implementation plan (from `plan.yaml`), generate the code
  - C (WHY): We generate code from the plan, not directly from the story, because the plan is where approach decisions are made. The code step executes the plan — it doesn't re-plan.
  - C (HOW): Language, framework, test runner, codebase conventions. Code must implement every item in the plan. Code must satisfy every AC referenced in the plan. Code must include error handling for edge cases identified in the plan.
- Show the generated code: does it satisfy the AC? Does it follow the plan?
- One targeted adjustment: identify the weakest part of the plan, form a hypothesis about the plan-story skill, change it, regenerate the plan, then regenerate the code. Show how improving the plan improves the code.

### EDD Exercise: Write Your EC Before Building (15 min)

Before building either skill, participants write Evaluation Criteria for both. Same discipline as Session 1.

**EC for plan-story (suggested starting criteria):**
- Every AC from the story is referenced in the plan (measurable: yes/no per AC)
- Plan includes at least one edge case or failure mode (measurable: yes/no)
- Plan identifies specific files to change or create (measurable: yes/no)
- Plan does not over-constrain implementation with unnecessary detail (measurable: yes/no — requires judgment)
- Plan is specific enough that another developer could code from it (measurable: yes/no)

**EC for implement-story (suggested starting criteria):**
- Code implements every item in the plan (measurable: yes/no per plan item)
- Code satisfies every AC referenced in the plan (measurable: yes/no per AC)
- Code handles edge cases identified in the plan (measurable: yes/no)
- Code would compile and run in the project's framework (measurable: yes/no)
- Code does not introduce functionality beyond the plan scope (measurable: yes/no)

Participants may add criteria specific to their project's standards (naming conventions, code organization, test coverage requirements, etc.).

These EC become the evaluation standard for Labs 1 and 2.

### Lab 1: Build Out the plan-story Skill (45 min)

- Each participant builds out the plan-story skeleton skill in the workspace's `skills/` directory
- The skill reads `stories.yaml` from the workspace root as its input — the same file Session 1 produced
- **The skill must write its output to `plan.yaml` in the workspace root** — this is the YAML pipeline artifact that implement-story will read next
- Use the RTCC elements from Block 3 as the template; populate with Context (WHY: what a good plan enables) and Constraints (HOW: language, framework, conventions, required plan structure — the EE provides common conventions for the sample stories (TypeScript/Node.js backend, React/ShadCN/Tailwind frontend))
- Apply the Load-Bearing Rule as you build: for each instruction, identify which EC it corresponds to. If no EC would fail without it, don't add it.
- Dev participants: build this with your real language/framework conventions in Constraints (the EE can help you adapt)
- Product/Process and Testing participants: build it too — understanding what a plan looks like improves your upstream work (better stories produce better plans)
- Use stories with AC from Session 1's epics-and-stories output (run against `sample-stories/` epics) as input
- Commit the skill to `skills/`

#### Stretch Goals (for advanced users)

Add Context and Constraints specific to the Pantry Tracker PWA tech stack (TypeScript, Express, React, ShadCN). Include framework-specific plan structure requirements (e.g., API route definitions, component hierarchy, ShadCN component selection).

### Lab 2: Build Out the implement-story Skill (30 min)

- Each participant builds out the implement-story skeleton skill in the workspace's `skills/` directory
- Use the RTCC elements from Block 3 as the template; populate with Context (WHY: why we code from the plan, not the story) and Constraints (HOW: language, framework, test runner, conventions, required code structure — the EE provides common conventions)
- Apply the Load-Bearing Rule as you build
- The plan-story output from Lab 1 is the input to implement-story — run the chain end-to-end on a `sample-stories/` story
- Commit the skill to `skills/`

#### Stretch Goals (for advanced users)

Generate code that includes both the Express API endpoint AND the React component. Include ShadCN component imports and Tailwind class structure. Include TypeScript types for the pantry item model.

### Block 4: The Plan Quality Dependency (20 min)

Group analysis: what happened when the plan was strong vs. weak?

- **Live example:** Take one vague plan (missing edge cases, no AC references) generated from a `sample-stories/` input and generate code from it — the code will be vague too. Now take the improved version of the same plan and regenerate the code. Show the difference.
- Key question for Product/Process participants: "What would you change about your epics-and-stories skill right now, based on what you just saw happen to the plan?"
- Key question for Dev participants: "What do you need from the plan to generate good code?"
- Key question for Testing participants: "What gaps in the plan would make the code hardest to review?"
- Key insight: **plan quality is partially determined upstream.** The story + AC quality (Session 1, from `sample-stories/`) shapes the plan quality, which shapes the code quality. This is not abstract — it's visible in the EC scores at each step.

### Block 5: Load-Bearing Audit on Both Skills (15 min)

Participants review both skills — plan-story and implement-story.

**For each instruction in each skill:**
- Which EC would fail if this instruction were removed?
- If no EC would fail, flag the instruction for removal
- Check the RTCC structure: is background data sitting in Context (WHY) instead of Constraints (HOW)? Is intent sitting in Constraints instead of Context? Move it.
- Remove flagged instructions and re-run to confirm no scores drop

Commit both audited skills to `skills/`.

### Block 6: Wrap-up (10 min)

- What the Embedded Engineer will be doing this week: embedded with the whole team, primary focus on plan-story and implement-story work with Dev role members
- What participants should do before Week 2: use both skills on at least 3 sample stories from `sample-stories/`; evaluate each output against the EC they wrote today
- What to bring to the Embedded Engineer: the plan output, the code output, the EC scores, the failure modes
- Preview of Session 3: "Next session we build the review-implementation skill — the piece that closes Loop 1 and makes the full chain visible."

---

## Session Artifacts

Each participant leaves with:
- [ ] Written Evaluation Criteria (EC) for plan-story output (4+ criteria, written before building)
- [ ] Written Evaluation Criteria (EC) for implement-story output (4+ criteria, written before building)
- [ ] Committed plan-story skill in `skills/` (skill file format, `disable-model-invocation: true`, RTCC structure, load-bearing audit completed)
- [ ] Committed implement-story skill in `skills/` (skill file format, `disable-model-invocation: true`, RTCC structure, load-bearing audit completed)
- [ ] `plan.yaml` committed to the workspace root (the pipeline artifact for Session 3)
- [ ] Plans generated from 2–3 sample stories with EC scores noted
- [ ] Code generated from those plans with EC scores noted
- [ ] Written: most common failure mode in plan output and a hypothesis about why

---

## Trainer Notes

- **The "Development Loop" framing is the conceptual spine of this session.** Plan → Code is the inner loop of development. Don't let participants treat the two skills as independent — they're a loop. The plan-story skill produces the input to the implement-story skill. Make the chain visible in every block.
- **The plan failure modes discussion is the highest-value moment for experienced developers.** Give it time — don't rush to the lab. The vague-plan / missing-edge-case / over-constrained-plan patterns are things participants will recognize from their own work. Naming them is the first step to fixing them.
- **The EDD exercise before Labs 1 and 2 is essential.** Participants who skip writing EC first will produce skills that feel good but aren't evaluatable. Enforce the sequence: EC for plan-story, then build plan-story, then EC for implement-story, then build implement-story.
- **Product/Process and Testing participants may feel "this isn't my skill to build."** Push back: everyone needs to understand what a plan looks like and what code-from-a-plan looks like. Building the skills is how you understand the downstream consequences of your upstream work.
- **The Plan quality dependency block often produces the most honest cross-role conversation.** Facilitate it openly — this is where the teams start seeing the chain.
- **The chain connection to Session 1 is critical.** Remind participants throughout: the epics-and-stories output from Session 1 (run against `sample-stories/`) is the input to plan-story today. The quality of those stories with AC directly shapes the quality of the plans. Use stories from `sample-stories/` as the input in the demo and labs.
- Embedded Engineer should come with 1–2 real examples from Weeks 1–2 of epics-and-stories output (from the workspace or the transfer to the real codebase) that worked well for planning and output that didn't. Concrete beats abstract.

**EE Transfer Model:** Between sessions, the EE helps participants transfer skills from the workspace to their real codebase. The workspace is the training ground; the real codebase is the application. All labs and demos work against the shared workspace — the EE coaches the transfer.

**Trainer repo push (after Session 2):** Nothing additional to push — the plan-story and implement-story skeletons are already in `skills/`.