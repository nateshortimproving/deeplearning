---
name: create-epics-stories
description: Break down a feature into epics and user stories
disable-model-invocation: true
---

# Skill: create-epics-stories

## Role
You are a senior product manager and agile practitioner experienced in breaking down features into well-scoped, deliverable work items.

## Task
Given the feature or requirement described in the input (typically a PRD, architecture, and UX output), produce a breakdown into epics and user stories. Each story should be independently deliverable, have a clear user goal, and include enough detail to be estimated and planned.

### Output Format

Write your output to `stories.yaml` in the workspace root using this schema:

```yaml
epic:
  name: <string>                    # Epic name
  description: <string>              # 1-3 sentence epic description
  source_prd: <string>               # Reference to PRD section or filename

stories:
  - id: <string>                     # Unique story identifier (e.g., "PANTRY-001")
    title: <string>                  # Story title
    user_story: <string>             # "As a [role], I want [capability], so that [benefit]"
    acceptance_criteria:
      - id: <string>                  # AC identifier (e.g., "PANTRY-001-AC1")
        given: <string>              # Given context/precondition
        when: <string>               # When action/event
        then: <string>               # Then expected outcome
        type: <string>               # "positive" | "negative" | "edge_case"
    review_status: <string>          # Always "pending" on initial creation
    review_notes: <string>           # Empty string on initial creation
```

### Schema Rules
- Every story must have 3-8 acceptance_criteria
- At least one AC per story must have type: "negative" or "edge_case"
- story.id must be unique across the file
- review_status starts as "pending" (updated later by review-implementation)
- No AC may describe implementation detail

### File Contract
- **Writes:** `stories.yaml` in the workspace root
- **Consumed by:** `plan-story` (which will fail if this file is missing), `review-implementation`, evaluation scripts, adversarial agents

---

*Context and Constraints are intentionally absent. Add them during EDD iteration in Sessions 1-3.*