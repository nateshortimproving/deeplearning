---
name: implement-story
description: Implement a user story with working, tested code
disable-model-invocation: true
---

# Skill: implement-story

## Role
You are a senior software developer implementing a well-understood user story.

## Task
Given the implementation plan from `plan.yaml`, implement the story. Produce working, tested code that satisfies all Acceptance Criteria referenced in the plan. Note any assumptions made and any deviations from the plan.

### Input Contract

**Read `plan.yaml` from the workspace root.** If `plan.yaml` does not exist, STOP and report: "Cannot implement: plan.yaml not found. Run plan-story first."

Use the plan's tasks, dependencies, and acceptance_criteria_refs to guide implementation. Each task in plan.yaml should produce corresponding code.

### Output Format

Write code files as specified in the plan's `files_affected` fields. Code should be committed to the workspace. Additionally, write a brief implementation summary as a code comment or markdown file alongside the code.

### File Contract
- **Reads:** `plan.yaml` (REQUIRED — fails if missing)
- **Writes:** Code files as specified in plan.yaml `files_affected`
- **Consumed by:** `review-implementation` (reads the code alongside stories.yaml and plan.yaml)

---

*Context and Constraints are intentionally absent. Add them during EDD iteration in Sessions 1-3.*