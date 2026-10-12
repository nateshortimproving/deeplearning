# Deep Learning Program (DLP) — Execution Plan
*DLP: Execution Framework & Curriculum*

---

## Program Summary

The Deep Learning Program (DLP) is a **12-week embedded client engagement** designed to move development team participants from **Basic Prompting** to **DLP Completion** — the point at which participants have achieved tangible, measurable outcomes in their AI-assisted work.

It runs as **two 6-week loops** — each loop cycles through three functional teams in sequence:
1. **Product / Process team** — focus: Epics & Stories generation (build out the `epics-and-stories` SDLC skeleton skill)
2. **Development team** — focus: The Development Loop (build out `plan-story` and `implement-story` skeleton skills)
3. **Testing team** — focus: Review Implementation (build out the `review-implementation` skeleton skill)

The program is staffed by two distinct roles:
- **Trainer** — delivers 6 structured training sessions (4 hours each, one every ~2 weeks) across all 12 weeks
- **Embedded Engineer** — works with client teams continuously for all 12 weeks as a player-coach

---

## Program Progression: Basic Prompting → DLP Completion

**Basic Prompting** is where participants start. They use AI tools off-the-shelf — present as a tool, not yet embedded in structured work. No repeatability, no evaluation, no craft.

### The Prompt/Harness/Model Framework

The foundational conceptual framework, introduced in Session 1:

- **Prompt** — The instructions you give to a model. What you want it to do, how you want it done, what constraints it must follow.
- **Harness** — The software environment that mediates between you and the model. The harness determines what the model can actually do: read files, run commands, access tools. Claude Code, Devin, Copilot, and ChatGPT web are all different harnesses with different boundaries.
- **Model** — The AI itself. The model generates text based on its training and the prompt. But the model cannot do anything on your machine that the harness does not allow. The harness is the capability boundary; the model is the intelligence; the prompt is the instruction.

This framework explains why skills use `disable-model-invocation: true` (the harness controls invocation), why Session 5 discusses enabling model invocation (a configuration decision), and why Session 6 demos custom harnesses (when the IDE harness isn't enough, you build your own — but building one is the work of a future Stage 4 Deep Learning Program, not this program).

### RTCC Prompt Structure

- **R — Role:** WHO the model should act as — a specific, credentialed persona
- **T — Task:** WHAT they should do — verb-first, unambiguous
- **C — Context:** WHY we want this done — the intent behind the task
- **C — Constraints:** HOW — the data, rules, and specifications the model needs

### EC vs. AC Terminology

- **Evaluation Criteria (EC)** — the quality bar for a skill's output. What a participant writes before building or iterating on a skill, used to measure whether the skill is producing good results. Never "success criteria" or bare "criteria."
- **Acceptance Criteria (AC)** — the product artifact. What a story must satisfy for it to be considered done. These are what the `epics-and-stories` skill produces.

### DLP Completion — The Program Target

DLP Completion is achieved when participants demonstrate **four tangible outcomes**:

1. **Iterative refinement of Skills and Adversarial Agents** — the participant has built and iteratively improved AI skills and adversarial agents for their real work
2. **Deliberate usage of evaluation frameworks to codify performance** — the participant uses Python evaluation scripts with LLM judges to *know* whether changes improve skills vs. merely change them
3. **At least 1 core human workflow step developed to 95%+ accuracy** — the participant has identified at least one real workflow step and developed an AI skill to the point where it produces results at 95% or higher accuracy
4. **Changed human behavior to use high-reliability skills in place of manual work** — the participant has actually changed their default behavior, using their high-reliability AI skill instead of "just doing it myself"

These outcomes are assessed through four behavioral criteria — **Craft, Evaluate, Iterate, Adopt** — which map directly to the outcomes above:

a) **Craft** — ability to create skills and adversarial agents (within IDE/agentic context)
b) **Evaluate** — use of Python evaluation scripts with LLM judges to know if changes *improve* skills vs. merely *change* them
c) **Iterate** — iterative improvement of skills/adversarial agents for one or more real workflow pieces
d) **Adopt** — actual behavior change: the new skills are the *default* behavior for that workflow

**Measurement:** DLP Completion is assessed using the 21-question, 7-dimension AI maturity self-assessment. Participants who have reached DLP Completion will score consistently at 3.0+ averages across Dimensions 1–4 (Prompt Engineering & AI Interaction, Task Agents & Single-Box Automation, Workflow Orchestration & Coordination, and Output Evaluation & Quality Judgment). Total scores in the 43–58 range indicate program completion.

### Why Prompt Evaluation is Non-Negotiable
Without evaluation frameworks, you don't know if you're improving skills — you're just changing them. The same engineering discipline that makes tests mandatory for code quality makes evaluators mandatory for prompt quality. In DLP v2, evaluation is done through Python evaluation scripts — the AI writes the evaluation code, participants direct and evaluate. No Python prerequisite.

**Why Python (not Promptfoo)?** DLP v2 uses Python evaluation scripts rather than Promptfoo because corporate security teams typically approve custom Python without friction, while third-party tools like Promptfoo can face approval challenges in enterprise environments. Python scripts are also more flexible — they can combine deterministic checks (fast, free, structural) with LLM judge calls (qualitative judgment) in a single script.

**Deterministic first, LLM judge second.** The evaluation discipline starts with deterministic checks (schema validation, field counts, format patterns) that run without any model call. Only escalate to an LLM judge for criteria that genuinely require qualitative judgment. This is faster, cheaper, more consistent, and sharpens your EC — if you find yourself using an LLM judge for something that could be a regex, your EC needs refinement.

By teaching evaluation in the context of personal workflow, participants develop the rigor they will apply to any prompting context throughout their careers.

---

## Program Structure

```
Week  1–6  | Loop 1 — Building the SDLC Skeleton Pipeline
  Week 1–2 | Product/Process team — Build out `epics-and-stories` skeleton skill
  Week 3–4 | Development team — Build out `plan-story` and `implement-story` skeleton skills (The Development Loop)
  Week 5–6 | Testing team — Build out `review-implementation` skeleton skill

Week  7–12 | Loop 2 (deepens the same sequence with new tooling)
  Week 7–8 | Product/Process team — Python evaluations + LLM judges, harder cases
  Week 9–10| Development team — Model invocation + adversarial agents
  Week 11–12| Bounded agents, custom harness demo, IIOS stage framework, full chain integration, DLP Completion
```

### The v2 Automation Spectrum

```
Skills (invocation disabled)
  → Skills (invocation enabled)
    → Adversarial Agents (AI challenges AI)
      → Bounded Agents (multi-step orchestration in the IDE)
        → Custom Harnesses (programmatic multi-step orchestration — demoed in Session 6, built in future Stage 4 DLP)
```

Each step extends what you can trust AI to do. Each step requires earning the right to the next one through evaluation evidence.

### The SDLC Pipeline (Structured Data Flow)

The 7 SDLC skeleton skills communicate through structured YAML files. Each skill writes to a specific file that the next skill reads — making the pipeline tangible and the handoffs explicit.

![SDLC Pipeline](images/sdlc-pipeline.svg)

See `student-workspace/schemas/README.md` for the complete YAML schema definitions.

---

## Roles

### Trainer
- Delivers 6 training sessions (4 hours each) — approximately one per 2 weeks
- Responsible for structured curriculum, concept introduction, and skill-building exercises
- Assesses participant progress against DLP Completion criteria

### Embedded Engineer
- Present with client teams continuously for all 12 weeks
- Player-coach: works in the actual codebase alongside developers
- Produces committed artifacts (skills, Python evaluation scripts, adversarial agents)
- Candidates must have achieved **DLP Completion** before engagement begins (the AI Bootcamp 4-week program targets this)

### Trainer and Embedded Engineer Coordination

The two roles operate on a **introduce → reinforce** cadence. Each Training Session lands at the start of a 2-week block (weeks 1, 3, 5, 7, 9, 11). Participants leave each session with a working artifact — a skill, an evaluation script, an adversarial agent — that they begin using with the Embedded Engineer the following day. The Embedded Engineer then spends the next two weeks reinforcing, deepening, and applying what the Trainer introduced, working in the client's actual codebase.

All participants attend all 6 Training Sessions regardless of role. The Trainer and Embedded Engineer jointly complete the Program Completion Rubric at Week 12, which is the only formal co-assessment point in the program.

---

## File Structure

```
AI-Deep-Learning-Program/
├── @Overview.md                                          ← This file
├── DLPv2-Plan.md                                          ← v2 changes plan
├── images/                                               ← Mermaid source + SVG diagrams
│   ├── README.md                                          ← Diagram standard
│   └── sdlc-pipeline.mmd / .svg                          ← Pipeline data flow diagram
├── Account Manager or Executive Coach/
│   └── AM-EC-Executive-Guidance.md
├── Embedded Engineer/
│   ├── EE-Implementation-Guide.md
│   ├── EE-Playbook.md                                     ← Field-tested coaching plays
│   └── 12-Week-Curriculum/                               ← Week-by-week EE + participant activities
│       ├── @Overview.md
│       └── Week-01.md through Week-12.md
├── Resources/
│   ├── Program-Evaluation-Framework.md
│   ├── SDLC-Commands/                                     ← RT-only skeleton skills for SDLC pipeline (introduced Session 1)
│   │   ├── @Overview.md
│   │   ├── create-prd.skill.md
│   │   ├── create-architecture.skill.md
│   │   ├── create-ux.skill.md
│   │   ├── create-epics-stories.skill.md
│   │   ├── plan-story.skill.md
│   │   ├── implement-story.skill.md
│   │   └── review-implementation.skill.md
│   ├── Measures-and-Assessments/                         ← Evaluations, self-assessments, deliverables
│   │   ├── @Overview.md
│   │   ├── AI-Adoption-Maturity-Assessment.md
│   │   ├── EE-Participant-Feedback.md
│   │   └── Program-Completion-Rubric.md
│   └── Sustainment/
│       ├── Executive-Sponsors.md
│       ├── Managers.md
│       └── Team-Members.md
└── Trainer/
    ├── Trainer-Implementation-Guide.md
    └── Training-Sessions/                                ← 6 × 4-hour Trainer-led sessions
        ├── @Overview.md
        ├── AGENTS.md                                      ← Deck generation workflow instructions
        ├── Session-1.md through Session-6.md
        └── Session-1.deck.md through Session-6.deck.md    ← Deck prompt files for design harness
```

---

## Key Design Principles

1. **Prompt/Harness/Model** — the foundational conceptual framework, introduced in Session 1 and referenced throughout
2. **Skills with `disable-model-invocation: true`** — every artifact participants build is a skill file; the difference is a configuration flag, not a format migration
3. **EC, not "success criteria"** — Evaluation Criteria (EC) is the exclusive term for skill evaluation criteria; Acceptance Criteria (AC) is exclusively the product artifact
4. **Measure don't guess** — every skill development activity has an evaluation mechanism (Python evaluation scripts with deterministic checks and LLM judges)
5. **Deterministic first, LLM judge second** — use deterministic checks (schema, count, format) for quantitative judgment and LLM judges for qualitative judgment. Deterministic checks are faster, cheaper, and more consistent
6. **Artifacts over advice** — every session and week produces something committed and usable
7. **Real work not exercises** — the Embedded Engineer works in the client's actual codebase, not synthetic scenarios
8. **AI writes the code** — participants direct AI to produce evaluation scripts; no Python prerequisite; the models carry the coding load
9. **Behavior change is the bar** — the target is new default behavior, not awareness or completion

---

## Assessment Structure

| Assessment | Who completes | When |
|-----------|--------------|------|
| AI Adoption Maturity Assessment (21-question, 7-dimension instrument) | Participants | Week 1 (baseline), Week 6–8 (midpoint), Week 12 |
| Embedded Engineer Participant Feedback | Participants (about their Embedded Engineer) | Week 6, Week 12 |
| Program Completion Rubric | Embedded Engineer + Trainer jointly | Week 12 |
| Embedded Engineer Certification Gate | Program manager review | End of AI Bootcamp Week 4 |

---

## Related Documents
- [AI Bootcamp](../AI-Bootcamp/@Overview.md) — 4-week Embedded Engineer readiness program; prerequisite for DLP engagement
- AI Maturity Model — Maturity model definition
- DLP-EE-Candidate-Readiness — Embedded Engineer bench and candidate materials
- DLP-EE-Opt-In-Communication — Embedded Engineer opt-in and role description