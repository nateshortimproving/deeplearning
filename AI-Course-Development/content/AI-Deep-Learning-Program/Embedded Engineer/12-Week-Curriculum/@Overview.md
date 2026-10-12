# 12-Week Curriculum — Overview

---

## Program Structure

The Deep Learning Program (DLP) is a 12-week embedded engagement. Every week, an **Embedded Engineer** is present with actual client teams — teams like the Website team, CRM team, or Platform team. Each of those teams contains people in Product/Process, Dev, and Testing **roles**.

The Embedded Engineer coaches the whole team throughout all 12 weeks. The loop structure below describes which **role's workflow** is the Embedded Engineer's *primary coaching focus* during that 2-week block — not who they spend time with.

A **Trainer** delivers 6 structured training sessions (4 hours each, approximately every 2 weeks). **All participants attend all training sessions regardless of role.**

---

## Loop Structure

| Loop | Weeks | Primary Role Focus | Core Technique |
|------|-------|--------------------|----------------|
| **Loop 1** | Weeks 1–2 | Product/Process | Epics & Stories generation — introduce and apply (build out the `epics-and-stories` SDLC skeleton skill) |
| **Loop 1** | Weeks 3–4 | Development | The Development Loop — build out `plan-story` and `implement-story` SDLC skeleton skills |
| **Loop 1** | Weeks 5–6 | Testing | Review Implementation — build out the `review-implementation` SDLC skeleton skill |
| **Loop 2** | Weeks 7–8 | EDD with Python Evaluations | Deterministic checks + LLM judges — all roles deepen together |
| **Loop 2** | Weeks 9–10 | Model Invocation + Adversarial Agents | All roles deepen together — no team focus |
| Loop 2 | Weeks 11–12 | Bounded Agents, Custom Harness Demo & Stage 4 Preview | The path to continued adoption — all roles deepen together |

**Loop 1** = Foundation. Each 2-week block introduces and builds out one SDLC skeleton skill. The sessions are organized around the SDLC pipeline: Session 1 introduces all 7 skeleton skills and builds out `epics-and-stories`; Session 2 builds out `plan-story` and `implement-story` (The Development Loop); Session 3 builds out `review-implementation`.

**Loop 2** = Deepening. All roles deepen together — the technique is the focus, not the team. Loop 1 uses team-focused language to scaffold the SDLC pipeline one role at a time. Loop 2 intentionally removes team labels because Loop 2 is about cross-team deepening: the same evaluation, adversarial, and harness skills apply to every role's work.

---

## Training Session Alignment

| Session | Week | Primary Role Focus | Content | SDLC Skeleton Skill |
|---------|------|--------------------|---------|---------------------|
| Session 1 | Week 1 | Product/Process | Prompt/Harness/Model + SDLC skeleton skills introduced + build out `epics-and-stories` | epics-and-stories |
| Session 2 | Week 3 | Development | The Development Loop — build out `plan-story` and `implement-story` | plan-story, implement-story |
| Session 3 | Week 5 | Testing | Build out `review-implementation` — testing/review step | review-implementation |
| Session 4 | Week 7 | All roles | EDD with Python evaluations (deterministic + LLM judges) | — |
| Session 5 | Week 9 | All roles | Model invocation + Adversarial Agent prompts | — |
| Session 6 | Week 11 | All roles | Bounded Agents, Custom Harness Demo & Stage 4 Preview (bounded agent lab + instructor demo + IIOS stage framework + program close) | Bounded agent run + commitment statement |

All participants attend all sessions. Loop 1 sessions build out the SDLC skeleton pipeline one skill at a time. Loop 2 sessions deepen everyone's craft regardless of role.

---

## The Student Workspace and the Transfer Model

All training sessions use a **shared student workspace** — a single repo that contains everything participants need for the class: the 7 SDLC skeleton skills (`skills/`), pre-generated demo outputs (`demo-outputs/`), sample stories for labs (`sample-stories/`), and directories for the artifacts participants will commit over the program (`evaluations/`, `adversarial-agents/`, `harness-specs/`). Cloning the workspace is the only setup required for Session 1. Every lab, demo, and exercise works against this shared workspace, not the participant's real codebase.

This gives the coaching model a clean split:

- **During sessions:** The Trainer teaches skills in the workspace. Every participant works with the same sample stories, the same skeleton skills, and the same demo outputs. Labs are consistent and predictable.
- **Between sessions:** The Embedded Engineer's job is **transfer** — helping participants take the skills they built in the workspace and apply them to the client's actual codebase. The workspace is the training ground; the real codebase is the application.

The weekly coaching notes below reflect this transfer model. Sessions teach in the workspace; the EE coaches the transfer to real work.

---

## Session-to-Skeleton Mapping

The 7 SDLC skeleton skills are introduced in Session 1 as the structural backbone of the program. Each is a skill with `disable-model-invocation: true` — participants invoke them via slash command. The Role and Task are pre-defined; participants add Context (WHY) and Constraints (HOW) using EDD discipline.

The pipeline skills communicate through structured YAML files — each skill writes to a specific file that the next skill reads. See the [SDLC Pipeline diagram](../../images/sdlc-pipeline.svg) and `student-workspace/schemas/README.md` for the complete YAML schema definitions.

- **Session 1** → `epics-and-stories` (primary build-out target). Demo outputs for `create-prd`, `create-architecture`, and `create-ux` are pre-generated so participants see the full pipeline.
- **Session 2** → `plan-story` and `implement-story` (The Development Loop). The epics-and-stories output feeds into plan-story.
- **Session 3** → `review-implementation` (the testing/review step). The plan and code output feeds into review-implementation.

The remaining skeletons (`create-prd`, `create-architecture`, `create-ux`) are introduced in Session 1 with demo outputs but are not the primary iteration targets until later.

---

## Program Outcome

The end goal is **NOT** full workflow integration. The end goal is:

> Every participant owns at least one **evaluated, iterated artifact** — and can see the road to continued adoption of the core DLP skills.

Participants exit the program at **DLP Completion**: they have craft, they can evaluate, they have evidence of iteration, at least one workflow step is at 95%+ accuracy, and AI-assisted work has become their default behavior.

---

## Assessment Cadence

| Assessment | Who | When |
|-----------|-----|------|
| AI Adoption Maturity Assessment (7 dimensions, 21 questions) | All participants | Week 1 (baseline), Week 7 (midpoint), Week 12 (final) |
| Embedded Engineer Participant Feedback | Participants (about their Embedded Engineer) | Week 6, Week 12 |
| Program Completion Rubric | Embedded Engineer + Trainer jointly | Week 12 |

---

## How to Read the Weekly Files

Each weekly file covers:
- **Role focus** — which role's workflow is the Embedded Engineer's primary coaching focus this week
- **Training session** — if a session occurs this week, what it covers
- **Embedded Engineer coaching priorities** — what the Embedded Engineer should accomplish day-to-day
- **Participant activities by role** — what participants across all roles should be doing
- **Artifacts due** — what should be committed by end of week
- **Embedded Engineer coaching notes** — what to watch for, common failure modes

---

## Weekly Files

- [Week-01](Week-01.md) | [Week-02](Week-02.md) — Loop 1: Product/Process Role Focus — Epics & Stories Generation (build out `epics-and-stories` skeleton skill)
- [Week-03](Week-03.md) | [Week-04](Week-04.md) — Loop 1: Development Role Focus — The Development Loop (build out `plan-story` and `implement-story` skeleton skills)
- [Week-05](Week-05.md) | [Week-06](Week-06.md) — Loop 1: Testing Role Focus — Review Implementation (build out `review-implementation` skeleton skill)
- [Week-07](Week-07.md) | [Week-08](Week-08.md) — Loop 2: EDD with Python Evaluations (deterministic checks + LLM judges, all roles deepen together)
- [Week-09](Week-09.md) | [Week-10](Week-10.md) — Loop 2: Model Invocation + Adversarial Agents (all roles deepen together)
- [Week-11](Week-11.md) | [Week-12](Week-12.md) — Loop 2: Bounded Agents, Custom Harness Demo & Stage 4 Preview (the path to continued adoption, all roles deepen together)