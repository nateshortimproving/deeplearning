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

## Context

Code is generated from the plan, not from the raw story. The plan exists because a story describes *what* the user wants, while the plan describes *how* to build it in small, sequenced, dependency-ordered tasks. Implementing directly from the story skips the design decisions, risk mitigations, and file boundaries already agreed upon in the plan. This skill honors the Development Loop discipline: the story feeds the plan, and the plan feeds the code. Any code that cannot be traced back to a task or an AC reference in the plan is out of scope.

## Constraints

All code produced by this skill must satisfy the following constraints. Violating any constraint will cause downstream review and evaluation to fail.

### Input Contract

**Read `plan.yaml` from the workspace root.** If `plan.yaml` does not exist, STOP and report: "Cannot implement: plan.yaml not found. Run plan-story first."

Use only the plan's `tasks`, `dependencies`, and `acceptance_criteria_refs` as your implementation guide. Do not read `stories.yaml` or the raw user story for scope; if the AC is not referenced in the plan, it is not in scope for this implementation. → Maps to EC6.

### Implementation Standards

- **One task, one code change:** Every task in `plan.yaml` must produce a corresponding, traceable code change in at least one file listed in its `files_affected`. → Maps to EC1.
- **AC coverage:** Every `acceptance_criteria_refs` entry in the plan must be satisfied by the code. Write code so that a reviewer can map each AC directly to the files and functions that implement it. → Maps to EC2.
- **Language and framework:** Generate TypeScript and React code for the PantryPal web client, following the architecture in `sample-docs/ARCHITECTURE.md`. Use functional components, hooks for state, and props for data flow. → Maps to EC4.
- **Testing:** Create or update at least one test file for the implemented behavior. Tests must exercise every AC referenced in the plan, including positive, negative, and edge-case paths. → Maps to EC3.
- **Dependency order:** Implement tasks in the order implied by their `dependencies`. Do not start a task until all of its dependencies are implemented and tested. → Maps to EC1 and EC2.
- **No scope creep:** Do not implement behavior for AC that are not referenced in the plan, even if they appear in the original story. → Maps to EC6.

### Output Format

Write code files as specified in the plan's `files_affected` fields. Code should be committed to the workspace.

Additionally, write an implementation summary to `IMPLEMENTATION.md` in the same directory as the primary changed component. The summary must include:
- Which plan tasks were implemented
- Any assumptions made
- Any deviations from the plan and why
- Test file locations

→ Maps to EC5.

### File Contract
- **Reads:** `plan.yaml` (REQUIRED — fails if missing)
- **Writes:** Code files as specified in plan.yaml `files_affected`, plus test files and `IMPLEMENTATION.md`
- **Consumed by:** `review-implementation` (reads the code alongside stories.yaml and plan.yaml)

---
