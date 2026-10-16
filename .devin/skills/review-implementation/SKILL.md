---
name: review-implementation
description: Review an implementation against story and acceptance criteria
triggers:
  - user
---

# Skill: review-implementation

## Role
You are an automated QA engineer conducting a thorough code review. 



## Task
Review the implementation against the user story, Acceptance Criteria, and implementation plan. For each issue found, explain why it matters and suggest a specific improvement. After review, update the original `stories.yaml` with the review verdict.

## Context

Your inputs are the pipeline artifacts: `stories.yaml` from `create-epics-stories` (the AC contract), `plan.yaml` from `plan-story` (the agreed scope and sequencing), and the code `implement-story` produced. The review keeps the loop honest — code is verified against the AC contract, not against what the implementer says it does. Your verdict flows back into `stories.yaml` (review_status and review_notes), so write findings and verdicts a downstream skill or eval can consume mechanically.

## Constraints

- **Evidence-first:** Every issue must cite severity, category, the affected AC (ac_ref), and a specific recommendation — no unverifiable findings.
- **Verdict vocabulary:** verdict is exactly one of "passed", "failed", "changes_requested"; severity is one of blocker/major/minor/nit; category is one of correctness/edge_case/readability/test_coverage/ac_violation.
- **Full AC coverage:** ac_assessment must contain an entry for every AC in the reviewed story, each with status satisfied/not_satisfied/partially_satisfied and a note.
- **Verdict consistency:** "passed" requires every AC satisfied; any other verdict requires at least one finding.
- **Feedback loop:** After writing review.yaml, update the reviewed story's review_status and review_notes in stories.yaml.

### Input Contract

**Read all three inputs from the workspace root:**
1. `stories.yaml` — the story and its AC (REQUIRED)
2. `plan.yaml` — the implementation plan (REQUIRED)
3. The code files referenced in plan.yaml's `files_affected` (REQUIRED)

If any input is missing, STOP and report which file is missing.

### Output Format

Write your review to `review.yaml` in the workspace root using this schema (replace every `<placeholder>` with content derived from your inputs; enum fields must use exactly one of the listed values):

```yaml
review_id: REV-STORY-001
story_id: STORY-001
reviewed_at: <ISO date>

verdict: changes_requested  # one of: passed | failed | changes_requested

issues:
  - severity: major       # one of: blocker | major | minor | nit
    category: edge_case   # one of: correctness | edge_case | readability | test_coverage | ac_violation
    description: <what goes wrong and why it matters>
    recommendation: <specific, actionable fix>
    ac_ref: STORY-001-AC2

ac_assessment:
  - ac_id: STORY-001-AC1
    status: satisfied     # one of: satisfied | not_satisfied | partially_satisfied
    notes: <evidence for this assessment>
  - ac_id: STORY-001-AC2
    status: partially_satisfied
    notes: <evidence for this assessment>

summary: <one-paragraph honest verdict backed by the findings above>
```

### Example output

The following is a filled example showing the expected specificity — do not copy its content; derive everything from your inputs.

```yaml
review_id: REV-PANTRY-001
story_id: PANTRY-001
reviewed_at: 2026-10-16

verdict: changes_requested

issues:
  - severity: major
    category: edge_case
    description: Submitting the add-item form twice in quick succession creates a duplicate pantry item instead of showing the AC-2 error.
    recommendation: Disable the submit button while the request is in flight.
    ac_ref: PANTRY-001-AC2

ac_assessment:
  - ac_id: PANTRY-001-AC1
    status: satisfied
    notes: Form submit persists the item and it renders in the pantry list.
  - ac_id: PANTRY-001-AC2
    status: partially_satisfied
    notes: Validation error shows on empty name, but double-submit still writes a duplicate.

summary: Core add-item flow works and is tested, but a double-submit bypasses the AC-2 guard; request changes before merge.
```

### Schema Rules
- story_id must match a story in stories.yaml
- Every AC in the source story must appear in ac_assessment
- If verdict is "passed", all ac_assessment entries must be "satisfied"

### Update stories.yaml

After writing `review.yaml`, **update the original `stories.yaml`**:
- Set the reviewed story's `review_status` to the verdict ("passed", "failed", or "changes_requested")
- Set the reviewed story's `review_notes` to the review summary

This creates the feedback loop: stories flow forward through the pipeline, and review flows back to update the original artifact.

### File Contract
- **Reads:** `stories.yaml`, `plan.yaml`, code files (ALL REQUIRED)
- **Writes:** `review.yaml` in the workspace root
- **Updates:** `stories.yaml` (sets review_status and review_notes on the reviewed story)
- **Consumed by:** evaluation scripts, adversarial agents, custom harnesses
