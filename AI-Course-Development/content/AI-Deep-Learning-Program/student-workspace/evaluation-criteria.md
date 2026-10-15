# Evaluation Criteria: create-epics-stories

EC evaluate the quality of the skill's output (`stories.yaml`). They are not the Acceptance Criteria (AC) inside each story.

Inputs: PRD, architecture, and UX outputs.

| ID  | Criterion | How to measure (pass/fail) |
|-----|-----------|----------------------------|
| EC1 | Every story has clear Acceptance Criteria | Each story has 3-8 AC. Every AC has non-empty `given`, `when`, `then`, and a `type` of positive, negative, or edge_case. |
| EC2 | Stories are independently deliverable | Each story can be built, tested, and shipped without another story in the same epic being finished first. No story's AC depend on another story's output. |
| EC3 | Epic is well-scoped | The epic contains 3-8 stories. |
| EC4 | Failure and edge cases are covered | Every story has at least one AC of type `negative` or `edge_case`, and at least one story in the epic covers a failure path. |
| EC5 | No implementation detail | No story or AC names specific technologies, libraries, endpoints, tables, or code structure. AC describe observable behavior only. |
| EC6 | No duplicated or overlapping work | No two stories deliver the same capability, and no two stories share a substantially identical AC. |

# Evaluation Criteria: plan-story

EC evaluate the quality of the skill's output (`plan.yaml`). They are not the Acceptance Criteria (AC) inside each story.

Inputs: `stories.yaml` (must exist; one story is selected by `story_id` or the first story with `review_status: "pending"`).

| ID  | Criterion | How to measure (pass/fail) |
|-----|-----------|----------------------------|
| EC1 | Plan references a real story | `story_id` matches a story in `stories.yaml`. `source_story.title` and `source_story.user_story` match the selected story. |
| EC2 | Every AC is covered | Every acceptance criterion in the selected story is referenced by at least one task's `acceptance_criteria_refs`. |
| EC3 | Tasks are in dependency order | No task lists a dependency on a task that appears later in the `tasks` list. All `dependencies` values resolve to existing task IDs. |
| EC4 | Each task has AC coverage | Every task has at least one non-empty `acceptance_criteria_refs` entry, and every referenced AC ID exists in the selected story. |
| EC5 | Task granularity is appropriate | Each task is small enough to complete in a single session (typically 1-2 hours) and describes a concrete, verb-first action. |
| EC6 | Risks and unknowns are identified | Every task lists at least one risk or unknown in `risks`. |
| EC7 | Files affected are tracked | Every task lists at least one file in `files_affected`. |
| EC8 | Output follows the required schema | `plan.yaml` contains `story_id`, `plan_version`, `source_story`, `tasks`, `assumptions`, and `open_questions`. Every task has `id`, `description`, `dependencies`, `files_affected`, `risks`, and `acceptance_criteria_refs`. |

# Evaluation Criteria: implement-story

**EC are written BEFORE code generation to define what "done" means.**

EC evaluate the quality of the skill's output (code files and implementation summary). They are not the Acceptance Criteria (AC) inside each story.

Inputs: `plan.yaml` (must exist; the skill consumes the plan, not the raw story).

| ID  | Criterion | How to verify (executable check) |
|-----|-----------|----------------------------|
| EC1 | Every task has code that compiles and runs | For every task in `plan.yaml`: (1) All files in `files_affected` exist. (2) Code compiles without errors (`tsc --noEmit` for TS, `npm run build` for web). (3) Code is not a stub — it contains logic addressing the task. Verify: `npm run build` succeeds in api/ and web/. |
| EC2 | Every AC is satisfied by working code | For every `acceptance_criteria_refs` in the plan: (1) Code contains a function/method/component implementing the behavior. (2) At least one test case exercises this AC and passes. (3) Reviewer can trace AC → code → test. Verify: `npm test` passes; grep for AC ID in test files. |
| EC3 | All tests pass and cover implemented behavior | (1) `npm test` in api/ returns 0 exit code (all tests pass). (2) `npm test` in web/ returns 0 exit code (all tests pass). (3) Test count: ≥ 1 test per task. (4) Tests cover positive, negative, and edge cases for each AC. Verify: `npm test` output shows all passing; test file count ≥ task count. |
| EC4 | Code follows declared architecture and tech stack | (1) Backend code uses Fastify (if API tasks exist), Prisma (if database tasks exist), TypeScript. (2) Frontend code uses React functional components, hooks, TypeScript. (3) No paradigm mixing (no class components if plan specifies functional). (4) Code passes linting if available. Verify: `npm run build` succeeds; manual review of imports and patterns. |
| EC5 | Implementation documents assumptions and deviations | `IMPLEMENTATION.md` exists and contains: (1) List of tasks implemented. (2) Assumptions made (e.g., "assumed categories are predefined"). (3) Deviations from plan with justification, or "None". (4) Test file locations. (5) File is ≥ 100 words and complete. Verify: `grep -l "IMPLEMENTATION.md" src/ web/src/` returns at least one file. |
| EC6 | Implementation stays in scope | (1) No source files exist outside `files_affected` + test files + `IMPLEMENTATION.md`. (2) No behavior for AC not in the plan. (3) No extra features. Verify: `git status` shows only expected files; code review confirms scope. |
