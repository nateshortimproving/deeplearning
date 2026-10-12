---
name: review-implementation
description: Review an implementation against story and acceptance criteria
disable-model-invocation: true
---

# Skill: review-implementation

## Role
You are a senior software developer conducting a thorough code review.

## Task
Review the implementation against the user story, Acceptance Criteria, and implementation plan. For each issue found, explain why it matters and suggest a specific improvement. After review, update the original `stories.yaml` with the review verdict.

### Input Contract

**Read all three inputs from the workspace root:**
1. `stories.yaml` — the story and its AC (REQUIRED)
2. `plan.yaml` — the implementation plan (REQUIRED)
3. The code files referenced in plan.yaml's `files_affected` (REQUIRED)

If any input is missing, STOP and report which file is missing.

### Output Format

Write your review to `review.yaml` in the workspace root using this schema:

```yaml
review_id: <string>                  # Unique review identifier
story_id: <string>                   # Which story was reviewed
reviewed_at: <string>                # ISO date

verdict: <string>                   # "passed" | "failed" | "changes_requested"

issues:
  - severity: <string>              # "blocker" | "major" | "minor" | "nit"
    category: <string>              # "correctness" | "edge_case" | "readability" | "test_coverage" | "ac_violation"
    description: <string>            # What's wrong
    recommendation: <string>         # Specific fix
    ac_ref: <string>                # Which AC is affected (or "general")

ac_assessment:
  - ac_id: <string>                  # AC identifier from stories.yaml
    status: <string>                 # "satisfied" | "not_satisfied" | "partially_satisfied"
    notes: <string>                  # Why

summary: <string>                    # Overall assessment in 2-3 sentences
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

---

*Context and Constraints are intentionally absent. Add them during EDD iteration in Sessions 1-3.*