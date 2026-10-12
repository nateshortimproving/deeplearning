# Deep Learning Program — Release Notes

*DLP v2 | Branch: `dlp-v2` | August 2026*

---

## Overview

DLP v2 is a major revision of the Deep Learning Program. It preserves the core philosophy from v1 — artifacts over advice, evaluation is non-negotiable, behavior change is the bar — while evolving the tooling, concepts, and session progression to reflect field experience and the current AI tooling landscape.

This document summarizes every change from v1 (on `main`) to v2 (on `dlp-v2`), organized by the 11 planned changes plus subsequent additions. The full rationale for each change is in `DLPv2-Plan.md`.

---

## What Stays the Same

These foundational elements are unchanged from v1:

- 12-week embedded engagement structure (Trainer + Embedded Engineer + Account Manager / Executive Coach)
- Two 6-week loops (Foundation, Deepening) cycling through Product/Process, Development, and Testing
- DLP Completion criteria: Craft, Evaluate, Iterate, Adopt
- RTCC prompt structure (Role, Task, Context, Constraints) — though the definitions of Context and Constraints have changed (see Change 9)
- EDD discipline: define criteria before building, baseline, iterate, load-bearing audit
- Load-Bearing Rule: every instruction must provably change output
- AI Adoption Maturity Assessment (21-question, 7-dimension) at Weeks 1, 7, and 12
- Program Completion Rubric (joint EE + Trainer assessment at Week 12)
- Artifact-first design: every session ends with committed artifacts
- All-roles-present principle: every participant attends every session

---

## Change 1: Prompt / Harness / Model Framework

**New in v2.** Session 1 gains a foundational conceptual block that does not exist in v1: an explicit definition of three terms and the relationship between them.

- **Prompt** — the instructions you give to a model
- **Harness** — the software environment that mediates between you and the model; determines what the model can actually do (read files, run commands, access tools)
- **Model** — the AI itself; generates text based on training and prompt, but cannot do anything the harness does not allow

This framework explains why skills use `disable-model-invocation: true` (the harness controls invocation), why Session 5 discusses enabling model invocation (a configuration decision), and why Session 6 introduces custom harnesses (when the IDE harness is not enough, you build your own). It is introduced early in Session 1, before the RTCC block.

**Affected files:** `@Overview.md`, `Session-1.md`, `Session-1.deck.md`, `Trainer-Implementation-Guide.md`, `EE-Implementation-Guide.md`

---

## Change 2: Skills from Day One with `disable-model-invocation: true`

**Replaces:** v1's commands-to-skills progression.

In v1, participants learn "commands" (explicit slash-command invocation) for 8 weeks, then "skills" (model-invoked) in Session 5. The commands-to-skills transition is a major conceptual moment.

In v2, participants learn **skills** from Session 1. Every artifact is a skill file using the skill format. All skills start with `disable-model-invocation: true`, meaning they only run when explicitly invoked via slash command. The v1 "commands vs. skills" distinction collapses — everything is a skill; the only thing that changes later is a configuration flag.

The v1 "automation spectrum" (Commands → Skills → Hooks → Governed Workflows) is replaced by:

```
Skills (invocation disabled)
  → Skills (invocation enabled)
    → Adversarial Agents
      → Custom Harnesses
```

**Affected files:** All session files, EE 12-week curriculum, Trainer Implementation Guide, Program Completion Rubric, SDLC-Commands/@Overview.md, all skeleton skill files

---

## Change 3: Session 2 — The Development Loop (Plan → Code)

**Replaces:** v1 Session 2 "Unit Test Generation."

v1 Session 2 teaches building a command that generates unit tests from story + Acceptance Criteria. v2 Session 2 teaches **Plan → Code** — a two-step approach where participants use AI to first plan an implementation, then generate code from that plan. The session builds out the `plan-story` and `implement-story` skeleton skills.

The upstream quality lesson shifts from v1's "AC → Test dependency" to "Plan quality determines code quality." Unit tests are not eliminated — testing is still a role focus in Session 3 — but the primary artifact of Session 2 is now the development loop, not test generation.

**Affected files:** `Session-2.md`, `Session-2.deck.md`, 12-Week-Curriculum/Week-03.md, `@Overview.md`

---

## Change 4: Session 4 — Python Evaluations + LLM Judges

**Replaces:** v1 Session 4 "EDD with Promptfoo."

v1 teaches EDD formalization using Promptfoo — a YAML-based assertion framework with `contains`, `icontains`, and `llm-rubric` assertions. v2 replaces this with **AI-generated Python evaluation scripts using LLM judges**. Participants have AI write Python scripts that evaluate skill outputs, using an LLM judge pattern (send skill output + Evaluation Criteria to a model, receive structured pass/fail judgment).

Key differences:
- Python evaluations are more flexible than YAML assertions
- Participants build their own evaluation tools rather than configuring someone else's
- LLM judges are the industry-standard pattern for AI output evaluation
- Removes the Promptfoo tooling dependency — Python + an API key is universal
- Aligns with the custom harness concept in Session 6 (participants already write Python that calls models)
- No Python prerequisite — the models carry the coding load; participants direct and evaluate

The EDD discipline itself (criteria first, baseline, iterate, load-bearing audit) is unchanged.

**Affected files:** `Session-4.md`, `Session-4.deck.md`, 12-Week-Curriculum/Week-06.md through Week-07.md, Program-Evaluation-Framework.md, Program-Completion-Rubric.md, EE-Implementation-Guide.md

---

## Change 5: Session 5 — Adversarial Agents + Model Invocation

**Replaces:** v1 Session 5 "Commands to Skills + Hooks & Sentinel Files."

v2 Session 5 has two focuses:

1. **Adversarial Agent Prompts** — Instead of deterministic hooks and sentinel files, participants learn to build adversarial prompts: AI prompts designed to challenge, critique, and find weaknesses in the output of their primary skills. An adversarial agent receives the output of another skill and attempts to find problems — missing requirements, logical errors, edge cases the evaluation script did not catch.

2. **Model Invocation of Skills** — Participants evaluate which of their skills are ready for the model to invoke automatically. The three graduation criteria (exact trigger inputs, output specification, 3+ verified trigger test cases) still apply, but now they are about enabling a config flag on an existing skill, not converting to a new format.

The pairing with Session 4 is complementary: the evaluation script measures (retrospective), the adversarial agent attacks (proactive).

**Affected files:** `Session-5.md`, `Session-5.deck.md`, 12-Week-Curriculum/Week-09.md through Week-10.md, Program-Completion-Rubric.md, Sustainment guides

---

## Change 6: Session 6 — Bounded Agents, Custom Harness Demo & Stage 4 Preview

**Replaces:** v1 Session 6 "Bounded Agents & Workflows."

v2 Session 6 introduces **bounded agents** (multi-step workflows chained within the IDE harness) via a hands-on lab, and **custom harnesses** (Python programs that orchestrate multiple model calls with clean context per step, pass artifacts between steps, evaluate each step automatically, and manage the overall workflow) via an instructor demo only. Building a custom harness is the work of a future **Stage 4 Deep Learning Program**, not this program.

Session 6 has a lab and a demo:
- **Bounded agent lab:** Participants run the full SDLC pipeline (epics-and-stories → plan-story → implement-story → review-implementation) in a single IDE session, with manual evaluation and adversarial review at key steps. The context window carries artifacts between steps.
- **Context window discipline:** Participants experience context window degradation at later steps in the bounded agent lab, then discuss why it happens and what strategies help within the IDE. This is taught AFTER the lab so participants feel the problem before discussing it.
- **Instructor demo:** A custom harness implementing the full chain (Story → AC → Plan → Code → Review) with clean context per step and evaluation at each step. The demo is the answer to the context window problem participants just experienced.
- **IIOS stage framework preview:** Where participants are (Stage 3: Task), what Stage 4 (Workflow) looks like, and what a future Stage 4 DLP would cover
- **No custom harness lab** — the custom harness is demonstrated, not assigned. Building one is the work of a future Stage 4 program.

The session flow is: build (bounded agent lab) → feel the problem (context window discipline) → see the solution (custom harness demo). This makes the demo the answer to a problem participants just experienced, not an abstract concept.

The capstone, final assessment, and commitment statements from v1 are preserved.

This completes the Prompt/Harness/Model conceptual arc from Session 1 and connects to participants' existing Python evaluation skills from Session 4. The bounded agent is the Stage 3 composition; the custom harness is the Stage 4 horizon.

**Affected files:** `Session-6.md`, `Session-6.deck.md`, `@Overview.md`, `Trainer/Training-Sessions/@Overview.md`, `Embedded Engineer/12-Week-Curriculum/Week-11.md`, `Week-12.md`, `Program-Completion-Rubric.md`, `EE-Participant-Feedback.md`, `AI-Adoption-Maturity-Assessment.md`, `Resources/Measures-and-Assessments/@Overview.md`, `Resources/Sustainment/Managers.md`, `Resources/Sustainment/Executive-Sponsors.md`, `Resources/Sustainment/Team-Members.md`, `student-workspace/README.md`, `student-workspace/harness-specs/README.md`

---

## Change 7: Evaluation Criteria (EC) vs. Acceptance Criteria (AC) Terminology

**Replaces:** v1's inconsistent use of "evaluation criteria," "success criteria," and bare "criteria."

In v1, the criteria participants write to evaluate their skills are referred to inconsistently. This creates documented confusion in Session 1, where participants build a skill that generates Acceptance Criteria (AC) from stories while simultaneously writing criteria to evaluate that skill's output — and both are called "criteria."

v2 standardizes:
- **Evaluation Criteria (EC)** — the quality bar for a skill's output. What a participant writes before building or iterating on a skill. Never "success criteria" or bare "criteria."
- **Acceptance Criteria (AC)** — the product artifact. What a story must satisfy for it to be considered done. Produced by the `epics-and-stories` skill.

The term "success criteria" is retired. "Criteria" is never used alone.

**Affected files:** All session files, EE 12-week curriculum, implementation guides, rubrics, assessments, sustainment guides — a full terminology sweep

---

## Change 8: Deck Prompts Replace PPTX Files

**Replaces:** All v1 PPTX and PDF files in Training-Sessions.

v1 ships PPTX slide decks for each session (Session-1 through Session-6, plus client-specific variants) and PDF exports. These binary files are difficult to diff, review, and version, and they couple content with visual design.

v2 removes all PPTX and PDF files. Each session gets a `.deck.md` prompt file — a detailed markdown file describing the deck structure and content for a design harness to generate the actual slides. The deck prompt defines slide types:

- **Required:** Intro, Check-In, Session Goals, Closing
- **Content:** Exercise, Demo, Compare/Contrast, Lecture

The `AGENTS.md` in Training-Sessions is rewritten to describe the deck prompt workflow. `Session-Template.pptx` is deleted. Client-specific variant PPTX files are deleted.

**Subsequent addition:** A `deck-template-spec.md` was added defining the general slide structure (8 slide types with required elements, rules, and constraints) separate from any session-specific content. Generated PPTX decks (Session-1 through Session-6 plus Deck-Template) were committed as derived artifacts.

**Affected files:** All `.pptx` and `.pdf` files removed; `Session-N.deck.md` files added; `AGENTS.md` rewritten; `deck-template-spec.md` added; generated `.pptx` decks added

---

## Change 9: RTCC Redefined — Context is WHY, Constraints absorb the Data

**Replaces:** v1's RTCC definitions where Context = background information and Constraints = rules.

v1 teaches RTCC as:
- **R — Role:** Who is the AI acting as?
- **T — Task:** What specific action should it perform?
- **C — Context:** What background information does it need?
- **C — Constraints:** What rules must the output follow?

v2 redefines Context and Constraints:
- **R — Role:** WHO the model should act as
- **T — Task:** WHAT they should do
- **C — Context:** WHY we want this done — the intent behind the task
- **C — Constraints:** HOW — the data, rules, and specifications the model needs

The mental model becomes WHO → WHAT → WHY → HOW. Data, background, codebase context, and domain knowledge move from Context to Constraints where they belong. Context becomes the purpose that shapes how the model interprets its role and task.

This also gives participants a structural diagnostic for the Load-Bearing Rule: "Is this instruction in the right RTCC section?" — if background data is sitting in Context, it is in the wrong place.

**Affected files:** `Session-1.md`, `Session-1.deck.md`, `Session-3.md`, `Session-3.deck.md`, all RTCC references throughout curriculum and guides, SDLC skeleton skills

---

## Change 10: SDLC Skeleton Skills Introduced in Session 1

**Replaces:** v1's Week 3 introduction of SDLC skeleton commands as a side resource.

v1 introduces the 7 SDLC skeleton commands in Week 3 as RT-only stubs for the Development team. They are a side resource, not the spine of the program.

v2 introduces the 7 SDLC skeleton **skills** in **Session 1** as the structural backbone. Each Loop 1 session focuses on building out specific skeleton skills:

- **Session 1:** Introduces the full pipeline. Pre-generates demo outputs for `create-prd`, `create-architecture`, and `create-ux`. Primary iteration target: **`epics-and-stories`** skill.
- **Session 2:** Builds out **`plan-story`** and **`implement-story`** skills — "The Development Loop."
- **Session 3:** Builds out **`review-implementation`** skill — the testing/review step.

The skeleton skills are converted from `.md` command files to `.skill.md` format with `disable-model-invocation: true`. Demo PRD, Architecture, and UX outputs are committed as artifacts so participants see what good upstream artifacts look like before building downstream ones.

**Affected files:** `SDLC-Commands/@Overview.md`, all skeleton skill files (renamed from `.md` to `.skill.md`), demo output files, Session 1-3 content and deck prompts, EE weekly curriculum

---

## Change 11: Shared Student Workspace

**New in v2.** All sessions assume a single shared student workspace — a subdirectory in the repository that contains everything participants need.

v1 has participants work against their own real codebase during labs, creating setup friction, inconsistent labs, and unpredictable demos. v2 replaces this with a shared workspace at `student-workspace/`:

- `skills/` — the 7 SDLC skeleton skills (RT-only stubs)
- `demo-outputs/` — pre-generated PRD, Architecture, and UX outputs for Session 1
- `sample-stories/` — 2 sample epics with 8 stories for common lab inputs
- `evaluations/` — placeholder for Python evaluation scripts (Session 4+)
- `adversarial-agents/` — placeholder for adversarial prompts (Session 5+)
- `harness-specs/` — placeholder for harness specifications (future Stage 4 DLP; demoed in Session 6, not built by participants)

The coaching model changes: sessions teach skills in the workspace; the EE's job is **transfer** — helping participants apply workspace skills to their real codebase between sessions. The trainer pushes additional files to the workspace progressively before Sessions 4, 5, and 6.

**Affected files:** All 6 session content files, all 6 deck prompt files, EE 12-week curriculum (Weeks 1-12), EE-Implementation-Guide.md, Trainer-Implementation-Guide.md, `student-workspace/` directory created

---

## Session-by-Session Change Summary

| Session | Week | v1 Content | v2 Content |
|---------|------|------------|------------|
| 1 | 1 | Acceptance Criteria Generation (commands, Promptfoo preview) | Prompt/Harness/Model + SDLC skeleton skills introduced + build out epics-and-stories skill |
| 2 | 3 | Unit Test Generation from story + AC | The Development Loop: build out plan-story and implement-story skeleton skills |
| 3 | 5 | Test Planning | Review Implementation: build out review-implementation skeleton skill |
| 4 | 7 | EDD with Promptfoo | EDD with Python evaluations + LLM judges (AI-coded, no Python prerequisite) |
| 5 | 9 | Commands to Skills + Hooks & Sentinel Files | Model invocation + Adversarial Agent prompts |
| 6 | 11 | Bounded Agents & Workflows | Bounded Agents, Custom Harness Demo & Stage 4 Preview (bounded agent lab + instructor demo + IIOS stage framework + program close) |

---

## Other Updates

### Assessments and Rubric
- Program Completion Rubric updated: "commands, skills, workflows, and agents" → "skills, adversarial agents, and custom harnesses"; "working evaluator with 3+ iterations" → "Python evaluation script with LLM judge, 3+ iterations documented"
- AI Adoption Maturity Assessment updated for new vocabulary
- Program Evaluation Framework version bumped from March 2026 to August 2026; references to Promptfoo replaced with Python evaluation scripts and LLM judges

### Sustainment Guides
- Executive Sponsors, Managers, and Team Members sustainment guides updated for v2 vocabulary (skills instead of commands, adversarial agents instead of hooks, custom harnesses instead of bounded agents)

### README
- "Command-first approach" → "Skills-first approach" in program descriptions

### Deck Template Specification
- `deck-template-spec.md` added to Training-Sessions — defines the 8 slide types (Intro, Check-In, Session Goals, Closing, Exercise, Demo, Compare/Contrast, Lecture) with required elements, rules, and constraints for the design harness
- Generated PPTX decks committed as derived artifacts (Session-1 through Session-6 plus Deck-Template)

---

## Commit History

| Commit | Date | Description |
|--------|------|-------------|
| `2d78799` | Aug 1, 2026 | Add plan document, replace PPTX decks with deck prompt files |
| `bd627df` | Aug 1, 2026 | Add Change 9 (RTCC Context=WHY), update deck prompts |
| `03424b8` | Aug 1, 2026 | Resolve all open questions, add Change 10 (SDLC skeleton skills) |
| `bfadcdf` | Aug 1, 2026 | Convert SDLC skeleton commands to skill format, create demo outputs |
| `796bd0a` | Aug 1, 2026 | Update assessments, evaluation framework, sustainment guides, and README |
| `4deb242` | Aug 1, 2026 | Rewrite all 6 session content files for v2 |
| `a96e639` | Aug 1, 2026 | Rewrite EE curriculum, implementation guides, and program overview |
| `ef40485` | Aug 1, 2026 | Update all 6 deck prompts for Change 10 (skeleton skills) |
| `7a62b11` | Aug 1, 2026 | Add Change 11 (student workspace), create workspace with skills, demos, sample stories |
| `b95c96c` | Aug 1, 2026 | Update deck prompts to use student workspace references |
| `368048d` | Aug 1, 2026 | Update session files to use shared student workspace |
| `eca3256` | Aug 1, 2026 | Update EE curriculum and guides for student workspace (Change 11) |
| `ce43b32` | Aug 1, 2026 | Add deck template specification (general slide structure) |
| `28fc469` | Aug 2, 2026 | Decks for DLP v2 (generated PPTX files) |
| `91b0dc6` | Aug 2, 2026 | Add RELEASE-NOTES.md covering all changes from v1 to v2 |

---

## Field Feedback Update (August 2026)

*Based on field feedback from Daniel Scheufler (Wave 1 Embedded Engineer) and additional structural improvements.*

### YAML Pipeline

All 7 SDLC skeleton skills now have Task output templates with structured YAML file contracts. The pipeline is tangible — each skill writes to a specific file that the next skill reads:

- `create-epics-stories` writes `stories.yaml` (epic, stories, acceptance_criteria, review_status)
- `plan-story` reads `stories.yaml` (fails if missing), writes `plan.yaml` (tasks, dependencies, AC refs)
- `implement-story` reads `plan.yaml` (fails if missing), writes code
- `review-implementation` reads `stories.yaml` + `plan.yaml` + code, writes `review.yaml`, and **updates `stories.yaml`** (sets review_status and review_notes — closing the feedback loop)

Schema definitions are in `student-workspace/schemas/README.md`. Sessions 1, 2, 3, and 6 updated to reference the YAML pipeline throughout.

**Affected files:** All 7 skeleton skill files (student-workspace/skills/ + Resources/SDLC-Commands/), student-workspace/README.md, student-workspace/schemas/README.md (new), Session-1.md, Session-2.md, Session-3.md, Session-6.md

### Mermaid SVG Diagrams

New `images/` directory with Mermaid source (`.mmd`) + rendered SVG. Standard: author `.mmd`, render `.svg`, reference in docs.

- `sdlc-pipeline.svg` — holistic view with YAML data flow, Loop 1/Loop 2 phases, evaluation/adversarial/harness layers. Used in @Overview.md and EE curriculum @Overview (trainer/internal reference).
- `sdlc-pipeline-simple.svg` — simplified left-to-right flow for student-facing materials. Used in Session 1 and intended for slides/student handouts/deck prompts.

**Affected files:** images/README.md (new), images/sdlc-pipeline.mmd + .svg (new), images/sdlc-pipeline-simple.mmd + .svg (new), @Overview.md, EE 12-Week-Curriculum/@Overview.md, Session-1.md

### Deterministic-First Evaluation (Session 4 Update)

Session 4 retitled from "EDD Formalization with Python Evaluations & LLM Judges" to "EDD Formalization with Python Evaluations." Added explicit framing for two types of evaluation used in sequence:

1. **Deterministic checks** (fast, free, definitive) — schema validation, field counts, format patterns, YAML structure. Run first, no model calls needed.
2. **LLM judge checks** (slower, costs money, qualitative) — for criteria requiring judgment. Run second, layered on top.

New design principle added to @Overview.md: "Deterministic first, LLM judge second." Demo restructured to show deterministic-only baseline first, then add LLM judge. Lab instructions updated.

**Affected files:** Session-4.md, @Overview.md

### Session 5: Two-Prompt Problem + Adversarial Agent Depth

Added explicit callout that adversarial agents introduce a second prompt to vet (worker + evaluator). Both can have bugs. The mindset for "prompt to check the work" differs from "prompt to do the work." Expanded "what makes a good adversarial prompt" with calibrated severity, actionable findings, and domain expertise in the role. Added note that adversarial agents are one form of verification — not the only form — and that beyond DLP, teams may add deterministic hooks or sentinel files.

**Affected files:** Session-5.md

### Loop 2: Team-Focusing Language Removed

EE curriculum Weeks 7-12 headers changed from team-focused ("Product/Process Team", "Development Team", "Testing Team") to technique-focused ("EDD with Python Evaluations", "Model Invocation + Adversarial Agents", "Custom Harnesses"). Loop 2 is about all roles deepening together — the technique is the focus, not the team. Team labels retained for Loop 1 (they serve the scaffolding purpose).

**Affected files:** EE 12-Week-Curriculum/@Overview.md, Week-07.md through Week-12.md

### EE Playbook Integration

Wave 1 EE Playbook (from Daniel Scheufler's field work) converted from `.docx` to markdown. 8 field-tested coaching plays: Rough Process Mapping, Divide and Conquer, Goals → Measures → Actions, An Exercise After Each Workshop, Build Your Own SDLC Pipeline, Everyone Gets a Turn at Show-and-Tell, One Meeting One Artifact, Cross-Pollination. Referenced in EE-Implementation-Guide.md.

**Affected files:** Embedded Engineer/EE-Playbook.md (new), Embedded Engineer/EE-Implementation-Guide.md

### @Overview.md Updates

- Added "Why Python (not Promptfoo)?" note explaining corporate security approval friction
- Added "Deterministic first, LLM judge second" design principle
- Added SDLC pipeline diagram reference (holistic SVG)
- Fixed file structure section: SDLC-Skills → SDLC-Commands, `.md` → `.skill.md` extensions, added images/ and EE-Playbook.md entries
- Updated program structure to show Loop 2 without team labels

### Other Updates

- **AGENTS.md:** Updated to reflect that PPTXs ARE committed to the repo. Deck prompts are for content maintainers; PPTXs are for instructors.
- **Week-05.md:** "Skill" terminology disambiguation — "all 7 skills" → "all 7 skeleton skills" to avoid lesson/artifact conflation.
- **Client name scrub:** All references to specific clients (NRG, Greenflag) in DLPv2-Plan.md and RELEASE-NOTES.md changed to "client-specific variants." Course files must never reference specific clients.

---

## Field Feedback Update Commit History

| Commit | Date | Description |
|--------|------|-------------|
| `a504ec3` | Aug 3, 2026 | YAML pipeline, Daniel feedback, Mermaid diagrams, EE Playbook (39 files, 1055 insertions) |
| `57b986d` | Aug 3, 2026 | Add simplified student-facing pipeline diagram |

---

## Session 6 Restructure: Bounded Agents + Custom Harness Demo + Stage 4 Preview (August 2026)

*Based on feedback from Eric Sowell (trainer) and Tim Rayburn (Global Head of AI Training). Key concern: Session 6's custom harness specification lab was too large a leap from Session 5, with predicted ~2% adoption. The specification exercise without implementation was unsatisfying. Recommendation: demo only, point to a future Stage 4 program. Subsequently refined: participants should BUILD a bounded agent (Stage 3 composition) and the custom harness should be DEMOED only (Stage 4 preview). Context window discipline is a bounded agent problem, not a custom harness problem.*

### What Changed

Session 6 was restructured from "Custom Harnesses (instructor demo + specification exercise)" to "Bounded Agents, Custom Harness Demo & Stage 4 Preview":

1. **Removed the harness specification lab** — the 45-minute specification exercise where participants wrote a harness spec is gone. Building a custom harness is now explicitly the work of a future Stage 4 Deep Learning Program, not this program.

2. **Added bounded agent lab** — a new 30-minute lab where participants build a bounded agent by running the full SDLC pipeline (epics-and-stories → plan-story → implement-story → review-implementation) in a single IDE session, with manual evaluation and adversarial review at key steps. This is the composition of skills they already have — the Stage 3 payoff.

3. **Added IIOS stage framework preview** — a lecture block introducing the Improving Intelligence Operating System (IIOS) stage framework. Participants learn where they are (Stage 3: Task — building evaluated, iterated, and composed skills) and what Stage 4 (Workflow) looks like (automated harnesses, guardrails, punch-out points, end-to-end success rates, audit trails, ~10x effort). The custom harness demo now has context: it's what Stage 4 looks like, not what participants build in this program.

4. **Retitled context window discipline** — was "Context Window Discipline: Bounded Agents vs. Custom Harnesses" (taught after the demo). Now "Context Window Discipline in a Bounded Agent" (taught after the bounded agent lab, before the demo). Participants feel the context window degradation in the lab, discuss it, then see the custom harness demo solve it. The session flow is: build → feel the problem → see the solution.

5. **Kept the instructor demo** — the 45-minute custom harness demo is retained. Participants still see the full chain running with clean context per step, evaluation at each step, and adversarial agents. The demo is now positioned as the answer to the context window problem participants just experienced.

6. **Kept capstone, final assessment, and commitment statements** — the program close elements are preserved.

7. **Updated DLP Completion criteria** — "Craft" no longer requires custom harness specifications. Completion is about skills and adversarial agents, not harness specs. The Program Completion Rubric, @Overview.md, assessments, and sustainment guides all updated to remove custom harness specifications as a participant artifact.

8. **Updated automation spectrum** — the spectrum now notes that bounded agents are "built in Session 6" and custom harnesses are "demoed in Session 6, built in future Stage 4 DLP."

9. **Updated all sustainment guides** — references to "custom harness specifications" as participant artifacts changed to "custom harness awareness" (demoed in Session 6). Next-step engagement references changed from "custom harness design" to "Stage 4 Deep Learning Program."

### What This Means for Participants

- Participants leave the program at Stage 3 (Task) of the IIOS — they can build, evaluate, iterate, and compose AI skills for real work
- They have built a bounded agent — the full pipeline run in the IDE — which is the Stage 3 composition of everything they've built
- They have seen what Stage 4 (Workflow) looks like via the custom harness demo
- They understand the trajectory: Stage 4 is a ~10x effort jump requiring team coordination and IT infrastructure
- They know a future Stage 4 Deep Learning Program exists for teams ready to make that investment
- The program close is stronger: the bounded agent lab is the payoff, the demo is the preview, and commitment statements get full time

8. **Replaced Windsurf with Devin** — Eric noted that Windsurf should be replaced with Devin as the primary example harness. All references to Windsurf across Session 1 content and deck prompt, @Overview.md, student workspace README, and EE Week-01 curriculum updated to Devin. 7 files affected.

9. **Fixed in-person language** — Eric flagged that the course assumes in-person delivery (the minority case) in various places. Fixed: "pair with the person next to you" changed to "pair with someone in your breakout room" (Session 1 deck prompt); EE Implementation Guide pairing language updated to reference breakout rooms and screen share for remote delivery.

10. **Updated Session 3 preview reference** — the Session 3 forward-looking reference to Session 6 updated to reflect the new framing (demo + IIOS stage framework preview, not harness specification exercise).

### Affected Files

| File | Change |
|------|--------|
| `Session-6.md` | Full rewrite: removed harness spec lab, added IIOS stage framework block, updated title, goals, agenda, artifacts, trainer notes |
| `Session-6.deck.md` | Full rewrite: removed harness spec exercise slide, added Stage 3 and Stage 4 lecture slides, updated intro/goals/closing |
| `Session-1.md` | Windsurf → Devin in Prompt/Harness/Model definition and lab setup instructions |
| `Session-1.deck.md` | Windsurf → Devin in Prompt/Harness/Model definition and lab setup; in-person language fix ("pair with someone in your breakout room") |
| `Session-3.md` | Updated Session 6 preview reference to reflect new demo + Stage 4 framing |
| `@Overview.md` | Updated DLP Completion criteria, Craft definition, automation spectrum annotation, Prompt/Harness/Model reference, EE artifacts, Windsurf → Devin |
| `Trainer/Training-Sessions/@Overview.md` | Updated session table, session list, design principle #6 |
| `Embedded Engineer/12-Week-Curriculum/Week-01.md` | Windsurf → Devin in Prompt/Harness/Model definition |
| `Embedded Engineer/12-Week-Curriculum/Week-11.md` | Removed harness spec from activities, artifacts, coaching notes; added IIOS stage framework references |
| `Embedded Engineer/12-Week-Curriculum/Week-12.md` | Updated handoff document and completion rubric summary |
| `Embedded Engineer/EE-Implementation-Guide.md` | Updated Craft criterion; pairing language updated for remote delivery |
| `Trainer/Trainer-Implementation-Guide.md` | Updated Craft criterion |
| `Resources/Measures-and-Assessments/Program-Completion-Rubric.md` | Removed custom harness from Craft criterion and Iterate criterion |
| `Resources/Measures-and-Assessments/EE-Participant-Feedback.md` | Removed custom harness from artifact references |
| `Resources/Measures-and-Assessments/AI-Adoption-Maturity-Assessment.md` | Updated Dimension 7 description |
| `Resources/Measures-and-Assessments/@Overview.md` | Updated custom harness definition |
| `Resources/Sustainment/Managers.md` | Updated artifact references, next-step engagement language (Stage 4 DLP) |
| `Resources/Sustainment/Executive-Sponsors.md` | Updated artifact list, trajectory, engagement options (Stage 4 DLP) |
| `Resources/Sustainment/Team-Members.md` | Updated self-audit prompt, extension path (Stage 4 DLP) |
| `student-workspace/README.md` | Updated harness-specs description and session progression table; Windsurf → Devin |
| `student-workspace/harness-specs/README.md` | Updated to reflect future Stage 4 program, not current session |

---

## Enterprise-Scale Engagement Guidance (August 2026)

*Based on the Footlocker proposal draft and Tim Rayburn's direction. These concepts apply to large enterprise engagements (5+ cohorts, 100+ participants) and are not required for standard single-cohort or small engagements.*

### What Changed

Added enterprise-scale concepts to the EC guidance and AM pricing guide — without touching any session content, deck prompts, or curriculum files. The DLP curriculum itself is unchanged; these additions cover how the DLP is scoped, sold, and managed at scale.

**Key concepts added:**

1. **Track** — A group of cohorts whose participants attend the same training session. When the EE-to-participant ratio is low (1:8), a single cohort needs 3 EEs but all 24 people can attend one training session. The Track is that grouping — multiple teams sharing one Trainer delivery. As the EE ratio drops, Tracks become necessary because a single cohort is too small to justify a Trainer alone.

2. **Wave** — One full program execution: multiple cohorts running the 12-week DLP simultaneously, preceded by a 4-week planning period. Waves run in series (not parallel). A wave typically contains 10–12 cohorts.

3. **MVP (Phase 0)** — A single-cohort pilot before committing to a full wave. Uses the same EE, same EC setup, same governance outputs — not a watered-down version. Produces the executive ROI narrative with the client's own data.

4. **Enterprise Coach** — At 5+ cohorts, the EC role becomes full-time. Starts 4 weeks before each wave for cohort composition, OCM, and governance infrastructure. This is a significantly expanded role compared to the standard EC on small engagements.

5. **Governance Infrastructure** — Spend dashboards, adoption-to-operate tracking, acceptance rate monitoring, agent promotion board, skills repository structure. Turns training into measurable operational proof. Required for enterprise-scale, overkill for small engagements.

6. **DevOps Acceleration Track (optional)** — 2 DevOps Specialists, 12–24 weeks, building CI/CD pipelines, automated testing, and AI acceptance rate instrumentation. For teams with sub-mature CI/CD where "verification debt" caps AI productivity gains.

7. **Data & Compliance Enablement (optional)** — 2 BI/Data Engineers, 16 weeks, building PCI-active agents, SOX audit trails, data classification, and governance dashboards. For clients under PCI/SOX/GDPR where passive compliance doesn't catch AI-introduced issues.

8. **ROI Framing: Capacity Recovery** — FTE capacity recovery model: breakeven = program investment / annual developer investment. At 1:8 EE ratio, in-program lift (11–18%) exceeds breakeven (~10%). Post-program compounding (20–30% at 6–12 months) is upside. The EE ratio is the single biggest cost and outcome lever.

9. **Phase-gated pricing** — MVP priced independently, subsequent waves contingent on prior wave outcomes. Reduces client risk, gives executive sponsor concrete evidence to justify each wave.

10. **Agent Repository** — Shared library of promoted agents, governed by Enterprise Coach and agent promotion board, accessible to all teams after Wave 1.

**When these concepts apply:**

| Engagement Size | Structure | Enterprise-Scale Components |
|-----------------|-----------|-----------------------------|
| 1–2 cohorts | Single engagement | None — standard guidance is sufficient |
| 3–4 cohorts | Single engagement | None — standard guidance is sufficient |
| 5+ cohorts | Multi-wave program | All enterprise-scale concepts apply |

**Key principle:** Do not over-engineer small engagements. These concepts exist because at enterprise scale, the DLP transforms from a training engagement into an operational transformation. They are not required for, and should not be sold to, clients running 1–4 cohorts.

### Affected Files

| File | Change |
|------|--------|
| `AM-EC-Executive-Guidance.md` | New "Enterprise-Scale Engagements" section: key terminology (Track, Wave, MVP, Enterprise Coach, Agent Repository), when enterprise-scale concepts apply, pre-wave planning, governance infrastructure, optional workstreams (DevOps, compliance), ROI framing (capacity recovery), MVP before full wave |
| `AM-DLP-Pricing-and-SOW-Guide.md` | New enterprise-scale components (6a–6d: Enterprise Coach, governance, DevOps track, compliance track), enterprise wave pricing structure, optional workstream pricing, phase-gated pricing, ROI framing with productivity lift scenarios and 3-year cumulative value, enterprise-scale SOW components (section 9), two new SOW pitfalls (over-engineering small engagements, under-scoping enterprise engagements), enterprise wave quick pricing reference |

---

## Domain Rework: Pantry Tracker PWA (August 2026)

*Reworked the student workspace domain from "User Notification Preferences" to a "Pantry Tracker PWA" — a Progressive Web Application for tracking pantry contents. Backend: TypeScript/Node.js/Express. Frontend: React with ShadCN/Tailwind. Also added stretch goals to every lab across all sessions for advanced users.*

### What Changed

1. **New sample stories** — Replaced `team-dashboard.md` and `user-notification-preferences.md` with `pantry-inventory.md` (managing pantry items, expiry tracking, quantities, barcode scanning) and `shopping-list.md` (building shopping lists from pantry gaps, sharing lists, marking items as purchased). Both epics have stories with Given/When/Then acceptance criteria.

2. **New demo outputs** — Rewrote all 3 demo output files (PRD, UX, Architecture) for the Pantry Tracker PWA domain. The outputs remain intentionally generic (RT-only stubs) — the pedagogical point is unchanged. The PRD covers the pantry tracking problem, the UX covers user flows for adding items and checking expiry, the architecture covers a Pantry Service / Shopping List Service / Barcode Lookup Service / React client UI.

3. **Tech stack** — The workspace now consistently references TypeScript/Node.js/Express backend and React/ShadCN/Tailwind frontend, replacing the previous domain-agnostic framing. This gives participants a concrete stack to work with when building skills.

4. **Stretch goals added to every lab** — Each lab in Sessions 1–5 now includes a "Stretch Goals (for advanced users)" subsection with 1–2 advanced challenges. Examples: configuring project-specific TypeScript conventions, adding model invocation criteria, writing full-stack code (API + React component), TypeScript type checking in evaluation scripts, adversarial agents targeting type safety. This addresses Eric Sowell's feedback about Sessions 2 and 3 being monotonous for advanced users.

5. **Remote-friendly language** — Updated "Pair up as you build" to "In your breakout room, pair up as you build" in Session 1.

6. **Updated all cross-references** — Session 1–6 content files, deck prompts, student workspace README, schemas README, and Resources/SDLC-Commands demo outputs and overview all updated to reference the new domain. Zero remaining references to the old domain.

### Affected Files

| File | Change |
|------|--------|
| `student-workspace/sample-stories/pantry-inventory.md` | New file: Pantry Inventory epic with 4 stories (add item, view inventory, edit item, expiry alerts) |
| `student-workspace/sample-stories/shopping-list.md` | New file: Shopping List epic with 4 stories (generate from pantry gaps, add manual item, mark purchased, share list) |
| `student-workspace/sample-stories/team-dashboard.md` | Deleted |
| `student-workspace/sample-stories/user-notification-preferences.md` | Deleted |
| `student-workspace/demo-outputs/demo-prd-output.md` | Rewritten for Pantry Tracker PWA |
| `student-workspace/demo-outputs/demo-ux-output.md` | Rewritten for Pantry Tracker PWA |
| `student-workspace/demo-outputs/demo-architecture-output.md` | Rewritten for Pantry Tracker PWA |
| `student-workspace/README.md` | Updated sample-stories description with pantry domain and tech stack |
| `student-workspace/schemas/README.md` | Updated schema examples to pantry domain |
| `Resources/SDLC-Commands/demo-prd-output.md` | Updated to match new demo output |
| `Resources/SDLC-Commands/demo-ux-output.md` | Updated to match new demo output |
| `Resources/SDLC-Commands/demo-architecture-output.md` | Updated to match new demo output |
| `Resources/SDLC-Commands/@Overview.md` | Updated demo description to Pantry Tracker PWA |
| `Trainer/Training-Sessions/Session-1.md` | Updated sample story references to pantry domain; added stretch goals to Labs 1, 2, 3; updated pairing language for remote |
| `Trainer/Training-Sessions/Session-1.deck.md` | Updated demo description to Pantry Tracker PWA; added stretch goals to exercise slides |
| `Trainer/Training-Sessions/Session-2.md` | Added tech stack context; added stretch goals to Labs 1, 2 |
| `Trainer/Training-Sessions/Session-2.deck.md` | Added stretch goals to exercise slides |
| `Trainer/Training-Sessions/Session-3.md` | Added stretch goals to Labs 1, 2 |
| `Trainer/Training-Sessions/Session-3.deck.md` | Added stretch goals to exercise slides |
| `Trainer/Training-Sessions/Session-4.md` | Added stretch goals to evaluation lab |
| `Trainer/Training-Sessions/Session-4.deck.md` | Added stretch goals to exercise slide |
| `Trainer/Training-Sessions/Session-5.md` | Added stretch goals to Labs 1, 2 |
| `Trainer/Training-Sessions/Session-5.deck.md` | Added stretch goals to exercise slides |

---

## IIOS Rename + Bounded Agent Reintroduction (August 2026)

*Based on Eric Sowell's feedback: (1) the "IOS" acronym collides with Apple's iOS, and (2) removing bounded agents from v2 and claiming the IDE harness can't do multi-step workflows was incredulous — bounded agents work and are a natural, buildable step.*

### What Changed

1. **Renamed IOS to IIOS** — "Intelligence Operating System (IOS)" changed to "Improving Intelligence Operating System (IIOS)" across all files. Avoids collision with Apple's iOS while preserving Devlin's framework name.

2. **Reintroduced bounded agents in Session 6** — Added a new "Bounded Agents: Multi-Step Orchestration in the IDE" block (20 min) that teaches participants what a bounded agent is, what it can do (run the full pipeline in the IDE with manual evaluation), what it can't do (clean context per step, automatic evaluation, unattended execution), and why custom harnesses exist as the next step. This addresses Eric's incredulity: bounded agents are real, useful, and buildable with what participants already have. Custom harnesses are the Stage 4 next step, not a replacement for something that doesn't work.

3. **Updated automation spectrum** — Added bounded agents as a step between adversarial agents and custom harnesses: Skills (invocation disabled) → Skills (invocation enabled) → Adversarial Agents → Bounded Agents (multi-step in the IDE) → Custom Harnesses (Python with API calls, Stage 4).

4. **Reframed Session 6 narrative** — The session now flows: bounded agent lab (what you can build today) → context window discipline (why bounded agents degrade) → custom harness demo (how custom harnesses solve it — what's next at Stage 4) → IIOS stage framework → capstone. The custom harness is no longer positioned as "the only way to do multi-step" — it's positioned as "what you build when you outgrow the bounded agent."

5. **Updated Session 6 agenda** — Adjusted timing to accommodate the bounded agent block. Custom harness section compressed from 30 min to 15 min (the bounded agent block does the conceptual groundwork). Capstone expanded slightly.

### Affected Files

| File | Change |
|------|--------|
| `Session-6.md` | Added bounded agent block, updated automation spectrum, updated session goals, agenda, and context window discipline heading; renamed IOS to IIOS |
| `Session-6.deck.md` | Added bounded agent lecture slide, reframed custom harness slide, renamed IOS to IIOS |
| `@Overview.md` | Updated automation spectrum to include bounded agents; renamed IOS to IIOS |
| `Session-3.md` | Updated Session 6 preview reference; renamed IOS to IIOS |
| `Trainer/Training-Sessions/@Overview.md` | Renamed IOS to IIOS in session table |
| `Embedded Engineer/12-Week-Curriculum/Week-11.md` | Renamed IOS to IIOS in coaching notes |
| `student-workspace/harness-specs/README.md` | Renamed IOS to IIOS |
| `RELEASE-NOTES.md` | Renamed IOS to IIOS |
| `AI-Deep-Learning-Program-Stage-4/PROPOSAL.md` | Renamed IOS to IIOS |

---

## Session 1 Demo: Good/Bad/AI-Generated Story Files

*Added August 2026 — The Session 1 deck prompt references a good/bad/AI-generated story demo, but the student workspace only contained the "good" sample stories. Added the missing vague and AI-generated-without-care contrast files.*

### What Changed

1. **Added `vague-pantry-stories.md`** — Bad example: plausible-sounding but untestable stories with missing AC detail, no edge cases, and no definition of "done."
2. **Added `ai-generated-pantry-stories.md`** — AI-generated-without-care example: polished-sounding but AC describe implementation detail (PostgreSQL, JWT, Redux, Firebase, WebSocket, OpenAI API), epics are too large, edge cases missing, some AC are untestable.
3. **Updated Session-1.md** — Added good/bad/AI-generated demo description in Block 2, added trainer notes on the contrast demo, updated trainer repo push note.
4. **Updated Session-1.deck.md** — Updated the "What Good Epics and Stories Look Like" demo slide to reference the actual filenames in `sample-stories/`.
5. **Updated student-workspace/README.md** — Expanded the `sample-stories/` description to document all four files and their roles in the demo.

### Affected Files

| File | Change |
|------|--------|
| `student-workspace/sample-stories/vague-pantry-stories.md` | New file — bad example stories |
| `student-workspace/sample-stories/ai-generated-pantry-stories.md` | New file — AI-generated-without-care stories |
| `Trainer/Training-Sessions/Session-1.md` | Added demo description, trainer notes, updated repo push note |
| `Trainer/Training-Sessions/Session-1.deck.md` | Updated demo slide with actual filenames |
| `student-workspace/README.md` | Expanded sample-stories documentation |