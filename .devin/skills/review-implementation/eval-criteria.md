[Definitions]
• Review Header: review_id, story_id, reviewed_at — identifies what was reviewed and when.
• Verdict: Overall outcome — "passed", "failed", or "changes_requested".
• Issues: Findings with severity, category, description, recommendation, and an ac_ref pointing at the affected AC (or "general").
• AC Assessment: Per-AC verdict — ac_id, status (satisfied / not_satisfied / partially_satisfied), and notes.
• Feedback Loop: The review updates stories.yaml's review_status and review_notes on the reviewed story.

EC 1: The output has review_id, story_id, reviewed_at, verdict, issues, ac_assessment, and summary fields. Fail if any is missing.
EC 2: verdict is one of "passed", "failed", or "changes_requested".
EC 3: Every issue has severity, category, description, recommendation, and ac_ref; severity is one of blocker/major/minor/nit and category is one of correctness/edge_case/readability/test_coverage/ac_violation.
EC 4: ac_assessment has at least one entry with ac_id, status (satisfied/not_satisfied/partially_satisfied), and notes.
EC 5: Verdict consistency — if verdict is "passed", every ac_assessment status must be "satisfied"; a "failed" or "changes_requested" verdict requires at least one non-satisfied AC or at least one issue.
