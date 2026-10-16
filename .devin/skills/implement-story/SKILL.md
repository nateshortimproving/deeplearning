---
name: implement-story
description: Implement a user story with working, tested code
triggers:
  - user
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
- **Architectural alignment:** Code must follow the architecture in `sample-docs/ARCHITECTURE.md`. If the plan includes backend tasks (API, database, services), implement them using the declared tech stack: Fastify for the API, Prisma for database access, TypeScript throughout. If the plan includes frontend tasks, use React functional components, hooks, and TypeScript. → Maps to EC4.
- **Testing:** Create or update at least one test file for the implemented behavior. Tests must exercise every AC referenced in the plan, including positive, negative, and edge-case paths. Backend tests should use a test database or mocks; frontend tests should use React Testing Library. → Maps to EC3.
- **Dependency order:** Implement tasks in the order implied by their `dependencies`. Do not start a task until all of its dependencies are implemented and tested. → Maps to EC1 and EC2.
- **No scope creep:** Do not implement behavior for AC that are not referenced in the plan, even if they appear in the original story. → Maps to EC6.

### Output Format

Write code files as specified in the plan's `files_affected` fields. Code should be committed to the workspace.

Additionally, write an implementation summary to `IMPLEMENTATION.md` in the same directory as the primary changed component. The summary must include which plan tasks were implemented, any assumptions made, any deviations from the plan and why, and test file locations — following this structure (replace every `<placeholder>` with content derived from your input; IDs shown are generic — use the story's real IDs):

```markdown
# Implementation: STORY-001

## Tasks Implemented
- STORY-001-T1 — <what this task built>
- STORY-001-T2 — <what this task built> (satisfies STORY-001-AC1, STORY-001-AC2)

## Assumptions
- <Assumption made while implementing, or "none">

## Deviations
- <Deviation from the plan and why, or "none">

## Test Files
- tests/example.test.ts
```

### Example output

The following is a filled example showing the expected specificity — do not copy its content; derive everything from your input.

```markdown
# Implementation: PANTRY-001

## Tasks Implemented
- PANTRY-001-T1 — PantryItem Prisma model and migration
- PANTRY-001-T2 — Add-item endpoint with validation (satisfies PANTRY-001-AC1, PANTRY-001-AC2)

## Assumptions
- Expiry dates are stored as ISO date strings; month-only input is rejected.

## Deviations
- Used Fastify schema validation instead of manual checks — matches the declared stack and covers the negative AC with less code.

## Test Files
- tests/pantry.test.ts
```

→ Maps to EC5.

### File Contract
- **Reads:** `plan.yaml` (REQUIRED — fails if missing)
- **Writes:** Code files as specified in plan.yaml `files_affected`, plus test files and `IMPLEMENTATION.md`
- **Consumed by:** `review-implementation` (reads the code alongside stories.yaml and plan.yaml)

---
