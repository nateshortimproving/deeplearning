# AI Course Development

**© 2025 Improving Enterprises, Inc. All rights reserved.**

This repository contains proprietary training content developed by [Improving](https://improving.com). All materials — including course curricula, exercise descriptions, program guides, evaluation frameworks, product descriptions, kata specifications, and all other documents — are the exclusive intellectual property of Improving Enterprises, Inc. and are protected by copyright law. Unauthorized reproduction, distribution, modification, or use outside of authorized Improving engagements is strictly prohibited.

---

## What This Repository Contains

This repository houses three distinct but related AI training programs. Each is designed for a different audience and delivery context, but all three share the same foundational discipline: Evaluation-Driven Development (EDD), RTCC prompt structure, and a skills-first approach to AI-assisted work.

---

### AI Bootcamp

**Audience:** Senior and Principal-level engineers being prepared to serve as Embedded Engineers in Deep Learning Program (DLP) engagements.

**Delivery:** Instructor-led, in-person, 4 weeks full-time.

**What it covers:** The Bootcamp is an intensive prerequisite program. Candidates enter using AI tools off-the-shelf and exit having demonstrated the full skill set required for a DLP engagement: EDD discipline, RTCC prompt structure, Promptfoo-measured iteration, load-bearing audits, skill and hook development, and the player-coach coaching model.

**Structure:**
- Week 1 — EDD and RTCC foundations via a social media content pipeline
- Week 2 — SDLC command development with pre-built starter stubs and Promptfoo iteration
- Week 3 — Skills, hooks, sentinel files, and governed multi-step workflows
- Week 4 — Coaching readiness, resistance scenarios, artifact handoff, and certification gate

**Entry point:** [`AI-Bootcamp/@Overview.md`](AI-Bootcamp/@Overview.md)

---

### AI Deep Learning Program

**Audience:** Engineering teams at client organizations, delivered over a 12-week engagement by a trained Embedded Engineer (EE) and supported by an Account Manager or Executive Coach.

**Delivery:** Embedded, on-site or remote, over 12 weeks. The Embedded Engineer works alongside the client team doing real work, not exercises.

**What it covers:** The DLP takes a client team from Basic Prompting — AI present but not structurally embedded in their workflow — to DLP Completion across four dimensions: Craft, Evaluate, Iterate, and Adopt. The program produces durable artifacts committed to the client's codebase that survive the EE's departure.

**Structure:**
- 12-week embedded engineer curriculum with weekly milestones
- Account Manager and Executive Coach guidance for stakeholder management and program governance
- Trainer-facing session guides and deck prompt files for the six training sessions
- Evaluation framework, completion rubric, and maturity assessments
- SDLC skeleton skills for use within the client's AI-assisted development workflow
- Sustainment guides for team members, managers, and executive sponsors after program completion

**Session Content (v2):**

The program runs two 6-week loops (Foundation, Deepening) across six training sessions. Each session produces committed artifacts, not notes:

| Session | Week | Content |
|---------|------|---------|
| 1 | 1 | **Prompt/Harness/Model** conceptual foundation + SDLC skeleton skills introduced + build out the **epics-and-stories** skill (skills with `disable-model-invocation: true`) |
| 2 | 3 | **The Development Loop**: build out **plan-story** and **implement-story** skeleton skills (Plan → Code two-step approach) |
| 3 | 5 | Build out the **review-implementation** skeleton skill (testing/review step) |
| 4 | 7 | **EDD with Python evaluations + LLM judges** — AI-generated evaluation scripts that measure skill output against Evaluation Criteria (EC) |
| 5 | 9 | **Model invocation of skills** + **Adversarial agent prompts** — enabling auto-invocation and AI challenges that find problems the evaluation scripts missed |
| 6 | 11 | **Custom harnesses** — instructor demo of a Python program that orchestrates multiple model calls, passes artifacts between steps, and evaluates each step programmatically |

**Deck format:** Each session has a `.deck.md` deck prompt file (not PPTX files) that describes the structure and content of the deck. These prompts are consumed by a design harness that generates the actual slide decks.

**Key terminology:**
- **Evaluation Criteria (EC)** — the quality bar for a skill's output. Participants write EC before building or iterating on a skill.
- **Acceptance Criteria (AC)** — the product artifact: what a story must satisfy to be considered done.
- **Skills** — every artifact participants build is a skill file. Skills with `disable-model-invocation: true` are invoked via slash command; skills with invocation enabled can be auto-invoked by the model.
- **Python evaluation scripts with LLM judges** — the primary evaluation mechanism. Participants write (with AI assistance) Python scripts that evaluate skill outputs against EC.
- **Adversarial agents** — AI prompts that challenge and critique the output of primary skills, catching semantic failures that deterministic checks cannot.
- **Custom harnesses** — Python programs that orchestrate multiple model calls, pass artifacts between steps, evaluate each step, and manage multi-step workflows.

**Entry point:** [`AI-Deep-Learning-Program/@Overview.md`](AI-Deep-Learning-Program/@Overview.md)

---

### AI Self-Directed Learning

**Audience:** Engineers who want to develop the same skills taught in the AI Bootcamp but without an instructor present — working independently at their own pace.

**Delivery:** Self-paced. Participants need an active AI subscription (Windsurf, Claude, or GitHub Copilot) and access to Promptfoo. Promptfoo is configured to run through the participant's existing CLI tools using wrapper scripts from [github.com/improving/promptfoo](https://github.com/improving/promptfoo) — no separate API key required.

**What it covers:** A structured sequence of 21 exercises across 6 modules that builds the same skills as the AI Bootcamp: EDD, RTCC, Promptfoo, load-bearing audits, skills, hooks, sentinel files, and governed workflows. Module 6 extends the program indefinitely with 14 development katas that serve as ongoing stress tests for the SDLC tooling built in earlier modules.

**Structure:**
- Module 1 — EDD and RTCC Foundations (6–8 hours)
- Module 2 — Social Media Content Pipeline (10–14 hours)
- Module 3 — SDLC Commands (14–18 hours)
- Module 4 — Skills, Hooks, and Governed Flows (10–14 hours)
- Module 5 — Completion and Self-Assessment (3–4 hours)
- Module 6 — Development Katas (ongoing)

**Entry point:** [`AI-Self-Directed-Learning/@Overview.md`](AI-Self-Directed-Learning/@Overview.md)

---

## How These Programs Relate

```
AI Self-Directed Learning  ──►  AI Bootcamp  ──►  AI Deep Learning Program
(individual, self-paced)         (cohort, 4 weeks)    (team, 12 weeks embedded)
```

The SDL program and the Bootcamp teach the same skills in different formats. The SDL is for individuals building foundational competency on their own timeline. The Bootcamp is the accelerated, instructor-led path that gates entry to DLP engagements. The DLP is the client-facing product — what Improving delivers to engineering organizations.

An engineer completing the SDL program has built the same artifact set required at the Bootcamp certification gate. An engineer completing the Bootcamp is cleared to serve as an Embedded Engineer in a DLP engagement.

---

## Shared Foundational Concepts

All three programs are built on the same disciplines. These concepts are not program-specific — they are the core of how Improving approaches AI-assisted development:

**Evaluation-Driven Development (EDD):** Write the Evaluation Criteria (EC) before the skill. Define the quality bar before building. Every instruction in a skill must be load-bearing — provably changing the output in a measurable way.

**RTCC Prompt Structure:** Role (WHO), Task (WHAT), Context (WHY), Constraints (HOW). The four-part structure that turns ad-hoc prompting into repeatable, improvable skills. Context is the intent behind the task — why we want it done. Constraints absorb the data, rules, and specifications the model needs.

**The Load-Bearing Rule:** If removing an instruction does not cause an Evaluation Criterion (EC) to fail, the instruction is not earning its place. Skills are not documentation — every word must do work that can be proven.

**Acceptance Criteria (AC) vs. Evaluation Criteria (EC):** AC is the product artifact — what a story must satisfy to be considered done. EC is the quality bar — what a skill's output must satisfy to be considered good. Two distinct concepts, two distinct abbreviations, no overlap.

**Prompt / Harness / Model:** The three-part mental model for understanding AI-assisted work. The **Prompt** is the instruction you give the model. The **Harness** is the software environment that mediates between you and the model — it determines what the model can actually do on your machine. The **Model** is the AI itself. The harness is the capability boundary; the model is the intelligence; the prompt is the instruction.

**Skills-First Discipline:** Every artifact is a skill file using the skill format. Skills with `disable-model-invocation: true` are invoked via slash command; skills with invocation enabled can be auto-invoked by the model. Move to model invocation only when the team has evaluation evidence, documented in writing with test cases, about when and how the skill should trigger.

**Upstream Quality Dependency:** Quality problems in a multi-step pipeline trace back to their source. Adding constraints to a downstream skill rarely fixes a problem that originates upstream.

---

## Repository Structure

```
AI-Course-Development/
├── AI-Bootcamp/
│   ├── @Overview.md
│   ├── Week-1.md               # EDD + RTCC + Social Media Pipeline
│   ├── Week-2.md               # SDLC Commands + Promptfoo Iteration
│   ├── Week-3.md               # Skills, Hooks, Sentinel Files
│   └── Week-4.md               # Coaching Readiness + Certification Gate
│
├── AI-Deep-Learning-Program/
│   ├── @Overview.md
│   ├── DLPv2-Plan.md            # DLP v2 major changes plan
│   ├── Embedded Engineer/
│   │   ├── 12-Week-Curriculum/ # Week-by-week EE curriculum
│   │   └── EE-Implementation-Guide.md
│   ├── Trainer/
│   │   ├── Training-Sessions/  # Six session guides + deck prompt files (.deck.md)
│   │   └── Trainer-Implementation-Guide.md
│   ├── Account Manager or Executive Coach/
│   │   └── AM-EC-Executive-Guidance.md
│   └── Resources/
│       ├── SDLC-Commands/      # SDLC skeleton skills for client codebases
│       ├── Measures-and-Assessments/
│       └── Sustainment/        # Post-program guidance by role
│
└── AI-Self-Directed-Learning/
    ├── @Overview.md
    ├── Module-1-EDD-and-RTCC/
    ├── Module-2-Content-Pipeline/
    ├── Module-3-SDLC-Commands/
    ├── Module-4-Skills-Hooks-Governance/
    ├── Module-5-Completion/
    ├── Module-6-Development-Katas/
    └── Resources/
```

---

## Copyright and Licensing

**© 2025 Improving Enterprises, Inc. All rights reserved.**

All content in this repository is proprietary to Improving Enterprises, Inc. ([improving.com](https://improving.com)). This includes but is not limited to:

- Course curricula, module structures, and learning objectives
- Exercise descriptions, kata specifications, and product descriptions
- Evaluation frameworks, rubrics, and assessment instruments
- Implementation guides, trainer notes, and coaching materials
- All associated slide deck prompts, templates, and supporting resources

**This content may not be:**
- Reproduced or distributed outside of authorized Improving engagements
- Modified and represented as independent work
- Used to deliver training, coaching, or consulting services without express written authorization from Improving Enterprises, Inc.
- Incorporated into products, services, or other training materials without a licensing agreement

For licensing inquiries or questions about authorized use, contact Improving at [improving.com](https://improving.com).