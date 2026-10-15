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

EC evaluate the quality of the skill's output (code files and implementation summary). They are not the Acceptance Criteria (AC) inside each story.

Inputs: `plan.yaml` (must exist; the skill consumes the plan, not the raw story).

| ID  | Criterion | How to measure (pass/fail) |
|-----|-----------|----------------------------|
| EC1 | Every task in the plan has corresponding code | For every task in `plan.yaml`, at least one file listed in `files_affected` is created or modified with code that addresses the task's description. |
| EC2 | Every referenced AC is satisfied | For every `acceptance_criteria_refs` entry in the plan, the affected code implements behavior that would satisfy that AC. |
| EC3 | Code includes tests | At least one test file is created or modified, and the tests exercise the behavior for every AC covered by the plan. |
| EC4 | Code follows architecture and conventions | Generated code follows the architecture in `sample-docs/ARCHITECTURE.md` and uses the declared tech stack (Fastify + Prisma for backend, React for frontend). If the plan includes backend tasks, backend code must exist and use Prisma for database access. If the plan includes frontend tasks, frontend code must use React and TypeScript. |
| EC5 | Implementation records assumptions and deviations | A brief implementation summary (markdown file or code comment) notes any assumptions made and any deviations from the plan, or explicitly states "None" if there are none. |
| EC6 | Implementation uses the plan as its sole input | The generated code maps to the tasks, dependencies, and AC refs in `plan.yaml` and does not introduce behavior for AC that are not referenced in the plan. |
