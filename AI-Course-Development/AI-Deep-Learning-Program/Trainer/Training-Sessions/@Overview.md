# Training Sessions — Overview
*6 × 4-Hour Trainer-Led Sessions Across 12 Weeks*

---

## Purpose

The Trainer delivers structured group sessions that introduce techniques, establish shared vocabulary, and build skills that the Embedded Engineer then reinforces in daily work. Sessions land at the start of each 2-week block, just before the Embedded Engineer begins that role's focused coaching work.

**All participants attend all 6 sessions regardless of role.** Product/Process, Dev, and Testing roles are always present together. The role-focus label indicates which role's primary artifact is the session's demonstration vehicle — not who the session is "for."

---

## Session Sequence

### Loop 1 — Building the SDLC Skeleton Pipeline (Weeks 1–6)

| Session | Week | Role Focus | Content | What Participants Leave With |
|---------|------|-----------|---------|------------------------------|
| 1 | 1 | Product/Process | **Prompt/Harness/Model + SDLC skeleton skills introduced + Epics & Stories Generation** — build out the `epics-and-stories` skeleton skill | Working `epics-and-stories` skill (RTCC, `disable-model-invocation: true`) with written Evaluation Criteria (EC) |
| 2 | 3 | Development | **The Development Loop** — build out `plan-story` and `implement-story` skeleton skills; Plan → Code | `plan-story` and `implement-story` skills built out with EC; Plan → Code chain run on a real story |
| 3 | 5 | Testing | **Review Implementation** — build out the `review-implementation` skeleton skill | `review-implementation` skill built out with EC; full Loop 1 SDLC pipeline assembled |

### Loop 2 — Deepening the Discipline (Weeks 7–12)

| Session | Week | Role Focus | Content | What Participants Leave With |
|---------|------|-----------|---------|------------------------------|
| 4 | 7 | Product/Process | **EDD with Python Evaluations + LLM Judges** | Python evaluation script with LLM judge for their primary skill; first documented iteration cycle |
| 5 | 9 | Development | **Model Invocation + Adversarial Agent Prompts** | A skill with model invocation enabled (or gap document); at least one adversarial prompt committed |
| 6 | 11 | Testing | **Bounded Agents, Custom Harness Demo & Stage 4 Preview** (bounded agent lab + instructor demo + IIOS stage framework + program close) | Bounded agent run + commitment statement for what continues after program ends |

---

## Design Principles

1. **Value from Session 1, Day 1.** Participants leave each session with something they can use with the Embedded Engineer the next morning — not a concept, an artifact.
2. **All roles, always.** Every session benefits every role. The SDLC pipeline only works if everyone understands it.
3. **Artifacts over notes.** Every session ends with committed files. Notes don't count.
4. **Loop 1 builds the pipeline; Loop 2 makes it rigorous.** The first 3 sessions build out the SDLC skeleton pipeline (epics-and-stories → plan-story → implement-story → review-implementation). The next 3 sessions introduce Python evaluation, adversarial agents, and custom harnesses.
5. **End goal is trajectory, not completion.** The program ends with participants owning evaluated, iterated artifacts and understanding the path to continued adoption of the core DLP skills — not with a fully integrated system.
6. **Prompt/Harness/Model is the foundational framework.** Introduced in Session 1, referenced throughout. The harness controls invocation, not the model. Skills with `disable-model-invocation: true` are the starting point; enabling model invocation is a graduated decision in Session 5; custom harnesses are demoed in Session 6 as the endpoint of the automation spectrum — building one is the work of a future Stage 4 Deep Learning Program.

---

## Deck Files

Decks are generated from `.deck.md` prompt files by a specialized design harness. PPTX files are generated from `.deck.md` files and committed to the repository for instructor use. Each session has:
- `Session-N.md` — authoritative content source
- `Session-N.deck.md` — deck structure prompt for the design harness

The design harness reads both and generates the actual slides as a derived artifact. Decks are generated using Claude Design (or equivalent design tool).

---

## Session Files
- [Session-1](Session-1.md) — Prompt/Harness/Model + SDLC Skeleton Skills + Epics & Stories Generation (Loop 1, Week 1)
- [Session-2](Session-2.md) — The Development Loop: plan-story + implement-story (Loop 1, Week 3)
- [Session-3](Session-3.md) — Review Implementation: review-implementation (Loop 1, Week 5)
- [Session-4](Session-4.md) — EDD with Python Evaluations + LLM Judges (Loop 2, Week 7)
- [Session-5](Session-5.md) — Model Invocation + Adversarial Agent Prompts (Loop 2, Week 9)
- [Session-6](Session-6.md) — Bounded Agents, Custom Harness Demo & Stage 4 Preview (Loop 2, Week 11)