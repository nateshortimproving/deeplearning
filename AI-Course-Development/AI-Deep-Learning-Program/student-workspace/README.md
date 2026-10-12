# DLP Student Workspace

This is your working directory for the Deep Learning Program. Clone this repo (or the class-specific repo created from it) and you're ready to go.

## Structure

```
student-workspace/
├── skills/              ← The 7 SDLC skeleton skills (RT-only stubs)
├── demo-outputs/        ← Pre-generated PRD, Architecture, UX outputs for Session 1
├── sample-stories/      ← Sample stories/epics for use in labs
├── schemas/             ← YAML schema definitions for pipeline artifacts
├── evaluations/         ← Your Python evaluation scripts (Session 4+)
├── adversarial-agents/  ← Your adversarial agent prompts (Session 5+)
├── harness-specs/       ← Custom harness specifications (future Stage 4 DLP)
├── stories.yaml         ← Output of create-epics-stories (Session 1+)
├── plan.yaml            ← Output of plan-story (Session 2+)
└── review.yaml          ← Output of review-implementation (Session 3+)
```

## The Pipeline Data Flow

Skills communicate through structured YAML files. Each skill writes to a specific file, and the next skill reads that file as input. This makes the pipeline tangible — you can see the artifacts flowing between steps.

```
create-epics-stories → stories.yaml
                           ↓
plan-story reads stories.yaml (FAILS if not found)
plan-story → plan.yaml
                           ↓
implement-story reads plan.yaml (FAILS if not found)
implement-story → code
                           ↓
review-implementation reads stories.yaml + plan.yaml + code
review-implementation → review.yaml
review-implementation updates stories.yaml (review_status, review_notes)
```

See `schemas/README.md` for the complete YAML schema definitions.

## How to Use This Workspace

1. Clone this repo to your local machine
2. Open it in your agentic IDE (Claude Code, Devin, GitHub Copilot, etc.)
3. Your trainer will guide you through each session, building skills in the `skills/` directory
4. Between sessions, your Embedded Engineer will help you apply what you learned here to your real codebase

## What Lives Where

- **skills/** — The 7 SDLC skeleton skills start as RT-only stubs (Role and Task defined, Context and Constraints empty). You'll build them out across Sessions 1-3 by adding Context (WHY) and Constraints (HOW) using EDD discipline. Each skill specifies its input and output file contracts.
- **demo-outputs/** — Pre-generated outputs showing what the RT-only stubs produce. These are intentionally generic — the gaps are the lesson.
- **sample-stories/** — Sample stories and epics for use in labs and demos. Everyone in the class uses the same inputs so demos and labs are consistent. The sample stories cover the Pantry Tracker PWA domain:
  - `pantry-inventory.md` and `shopping-list.md` — **Good** stories with clear, testable AC (Given/When/Then format, edge cases covered, no implementation detail). These are the primary lab inputs.
  - `vague-pantry-stories.md` — **Bad** stories: plausible-sounding but untestable, missing AC detail, no edge cases, no definition of "done." Used as the contrast example in the Session 1 good/bad/AI-generated demo.
  - `ai-generated-pantry-stories.md` — **AI-generated without care**: polished-sounding but AC describe implementation detail (PostgreSQL, JWT, Redux, Firebase, WebSocket, OpenAI API), epics are too large, edge cases missing. Used as the AI-without-care example in the Session 1 demo.
  
  The Pantry Tracker is a TypeScript/Node.js backend with a React/ShadCN/Tailwind PWA frontend.
- **schemas/** — YAML schema definitions for stories.yaml, plan.yaml, and review.yaml. These define the structured format that flows between pipeline skills.
- **evaluations/** — Empty at start. You'll commit Python evaluation scripts here starting in Session 4.
- **adversarial-agents/** — Empty at start. You'll commit adversarial agent prompts here starting in Session 5.
- **harness-specs/** — Empty at start. Custom harness specifications would be committed here in a future Stage 4 Deep Learning Program. In the current DLP, custom harnesses are demoed by the instructor in Session 6 but not built by participants.

## Session Progression

| Session | What You Build | Where | Pipeline Artifact |
|---------|---------------|-------|-------------------|
| 1 (Week 1) | create-epics-stories skill | skills/ | stories.yaml |
| 2 (Week 3) | plan-story + implement-story skills | skills/ | plan.yaml + code |
| 3 (Week 5) | review-implementation skill | skills/ | review.yaml (updates stories.yaml) |
| 4 (Week 7) | Python evaluation scripts + LLM judges | evaluations/ | Reads stories.yaml, plan.yaml |
| 5 (Week 9) | Adversarial agent prompts | adversarial-agents/ | Reads stories.yaml, plan.yaml |
|| 6 (Week 11) | Custom harness specifications (future Stage 4 DLP) | harness-specs/ | Orchestrates all YAMLs |