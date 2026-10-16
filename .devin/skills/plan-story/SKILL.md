---
name: plan-story
description: Produce an implementation plan for a user story
triggers:
  - user
---

# Skill: plan-story

## Role
You are a senior software developer experienced in breaking down user stories into concrete implementation tasks.

## Task
Given a story from `stories.yaml`, produce an implementation plan. Identify the specific tasks required, their dependencies, potential risks or unknowns, and what "done" looks like for each task.

## Context

We plan before we implement. This skill is responsible for creating a plan for a user story to cut down on guessing or assumptions in decisions. 

## Constraints

All implementation plans produced by this skill must satisfy the following constraints. A plan that violates any constraint will cause downstream skills (`implement-story`, `review-implementation`, and evaluation scripts) to fail or produce incorrect work.

### Planning Principles

- **Task Granularity:** Break the story into tasks that are small enough to complete in a single session (typically 1-2 hours of work).
- **Dependency Order:** Tasks must be ordered so that dependencies are completed before the tasks that depend on them.
- **Acceptance Criteria Coverage:** Every acceptance criterion in the story must be referenced by at least one task's `acceptance_criteria_refs`.
- **Risk Identification:** Identify at least one risk or unknown for each task.
- **File Tracking:** List all files that will be created or modified by each task.

### Input Contract

**Read `stories.yaml` from the workspace root.** If `stories.yaml` does not exist, STOP and report: "Cannot plan: stories.yaml not found. Run create-epics-stories first."

Select the story to plan (by story_id or the first story with review_status: "pending"). Use the story's title, user_story, and acceptance_criteria as your planning input.

### Output Format

Write your output to `plan.yaml` in the workspace root using this schema (replace every `<placeholder>` with content derived from your input; IDs shown are generic — use the story's real ID):

```yaml
story_id: STORY-001
plan_version: "1.0"
source_story:
  title: <story title, copied from stories.yaml>
  user_story: <user_story text, copied verbatim from stories.yaml>

tasks:
  - id: STORY-001-T1
    description: <what this task builds — small enough for one session>
    dependencies: []
    files_affected: [<files created or modified>]
    risks: [One risk or unknown for this task]
    acceptance_criteria_refs: [STORY-001-AC1]
  - id: STORY-001-T2
    description: <what this task builds>
    dependencies: [STORY-001-T1]
    files_affected: [<files created or modified>]
    risks: [One risk or unknown for this task]
    acceptance_criteria_refs: [STORY-001-AC1, STORY-001-AC2]

assumptions: [<assumption made while planning>]
open_questions: [<question needing an answer, or "none">]
```

### Example output

The following is a filled example showing the expected specificity — do not copy its content; derive everything from your input.

```yaml
story_id: PANTRY-001
plan_version: "1.0"
source_story:
  title: Add a pantry item manually
  user_story: As a home cook, I want to add pantry items with quantity and expiry, so that I can see what I have on hand.

tasks:
  - id: PANTRY-001-T1
    description: Create the PantryItem Prisma model and migration
    dependencies: []
    files_affected: [prisma/schema.prisma, prisma/migrations/]
    risks: [An item table may already exist under a different name]
    acceptance_criteria_refs: [PANTRY-001-AC1]
  - id: PANTRY-001-T2
    description: Build the add-item endpoint with name/expiry validation
    dependencies: [PANTRY-001-T1]
    files_affected: [src/routes/pantry.ts, tests/pantry.test.ts]
    risks: [Expiry may arrive as month-only dates from the client]
    acceptance_criteria_refs: [PANTRY-001-AC1, PANTRY-001-AC2]

assumptions: [Prisma is already configured and migrations run in CI]
open_questions: [Should expiry accept month-only dates?]
```

### Schema Rules
- story_id must match a story in stories.yaml
- Every AC in the source story must be referenced by at least one task's acceptance_criteria_refs
- Tasks must be in dependency order (no forward references to later task IDs)
- Each task must have at least one acceptance_criteria_ref

### File Contract
- **Reads:** `stories.yaml` (REQUIRED — fails if missing)
- **Writes:** `plan.yaml` in the workspace root
- **Consumed by:** `implement-story` (which will fail if this file is missing), `review-implementation`, evaluation scripts

---
