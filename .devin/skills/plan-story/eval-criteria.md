[Definitions]
• Plan Header: story_id, plan_version, and source_story (title + user_story copied from stories.yaml).
• Tasks: Sequenced implementation units — id, description, dependencies, files_affected, risks, acceptance_criteria_refs.
• Traceability: Every task references at least one AC from the source story; dependencies point only to earlier tasks.
• Assumptions & Open Questions: Explicit statements of what was assumed and what remains unresolved.

EC 1: The output has story_id, plan_version, source_story (with title and user_story), a tasks list, assumptions, and open_questions. Fail if any is missing.
EC 2: There are at least two tasks, each with id, description, dependencies, files_affected, risks, and acceptance_criteria_refs fields.
EC 3: Every task's acceptance_criteria_refs and files_affected lists are non-empty.
EC 4: Task dependencies reference only task ids that appear earlier in the list (no forward references).
EC 5: Every task lists at least one risk (or an explicit "none" entry).
