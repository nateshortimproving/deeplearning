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
