---
name: plan-story
description: Produce an implementation plan for a user story
disable-model-invocation: true
---

# Skill: plan-story

## Role
You are a senior software developer experienced in breaking down user stories into concrete implementation tasks.

## Task
Given a story from `stories.yaml`, produce an implementation plan. Identify the specific tasks required, their dependencies, potential risks or unknowns, and what "done" looks like for each task.

### Input Contract

**Read `stories.yaml` from the workspace root.** If `stories.yaml` does not exist, STOP and report: "Cannot plan: stories.yaml not found. Run create-epics-stories first."

Select the story to plan (by story_id or the first story with review_status: "pending"). Use the story's title, user_story, and acceptance_criteria as your planning input.

### Output Format

Write your output to `plan.yaml` in the workspace root using this schema:

```yaml
story_id: <string>                   # References the story from stories.yaml
plan_version: <string>               # Semantic version or date
source_story:
  title: <string>                    # Copied from stories.yaml
  user_story: <string>               # Copied from stories.yaml

tasks:
  - id: <string>                     # Task identifier (e.g., "PANTRY-001-T1")
    description: <string>            # What to do (verb-first)
    dependencies: [<string>]         # Task IDs this depends on (empty list if none)
    files_affected: [<string>]       # Expected files to create or modify
    risks: [<string>]                # Known risks or unknowns
    acceptance_criteria_refs: [<string>]  # Which AC IDs this task addresses

assumptions: [<string>]              # Assumptions made during planning
open_questions: [<string>]           # Unresolved questions for the team
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

*Context and Constraints are intentionally absent. Add them during EDD iteration in Sessions 1-3.*