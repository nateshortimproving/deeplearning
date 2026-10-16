[Definitions]
• Epic: A named, described body of work that references its source PRD.
• Stories: Independently deliverable user stories — id, title, user_story, acceptance criteria, and review state.
• Acceptance Criteria: Given/When/Then statements describing observable behavior, typed positive, negative, or edge_case.
• Review State: Every story starts with review_status "pending" and empty review_notes.

EC 1: The output has an epic block (name, description, source_prd) and at least two stories. Fail if missing or empty.
EC 2: Every story has id, title, user_story, acceptance_criteria, review_status, and review_notes fields.
EC 3: Every story has at least two acceptance criteria, each with id, given, when, then, and type fields.
EC 4: At least one acceptance criterion across the output has type "negative" or "edge_case".
EC 5: Every story's review_status is "pending".
