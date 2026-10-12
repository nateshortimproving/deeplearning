# Pipeline YAML Schemas

This document defines the structured YAML formats that flow between SDLC skeleton skills. Each skill produces or consumes these YAML files. The structured format makes the pipeline tangible — each skill has a contract with the next.

## Why YAML?

- **Human-readable** — participants can open and read any pipeline artifact
- **Schema-validatable** — deterministic evaluation can check structure before quality
- **File-based** — each skill writes to a specific file, making the handoff explicit
- **No parser needed for reading** — unlike JSON, YAML reads naturally as documentation

## File Locations

All pipeline YAML files live in the student workspace root (or a per-story subdirectory):

```
student-workspace/
├── stories.yaml          ← Output of create-epics-stories
├── plan.yaml             ← Output of plan-story
├── review.yaml           ← Output of review-implementation
```

---

## stories.yaml

Output of: `create-epics-stories`
Input to: `plan-story`, `review-implementation`, evaluation scripts, adversarial agents

```yaml
epic:
  name: <string>                    # Epic name (e.g., "Pantry Inventory Management")
  description: <string>              # 1-3 sentence epic description
  source_prd: <string>               # Reference to PRD section or filename

stories:
  - id: <string>                     # Unique story identifier (e.g., "PANTRY-001")
    title: <string>                  # Story title (e.g., "User adds a pantry item")
    user_story: <string>             # "As a [role], I want [capability], so that [benefit]"
    acceptance_criteria:
      - id: <string>                  # AC identifier (e.g., "PANTRY-001-AC1")
        given: <string>              # Given context/precondition
        when: <string>               # When action/event
        then: <string>               # Then expected outcome
        type: <enum>                 # "positive" | "negative" | "edge_case"
    review_status: <enum>            # "pending" | "passed" | "failed" | "changes_requested"
    review_notes: <string>           # Empty until review-implementation updates it
```

### Validation Rules
- Every story must have 3-8 acceptance_criteria
- At least one AC per story must have type: "negative" or "edge_case"
- No AC may describe implementation detail (validated by LLM judge, not schema)
- story.id must be unique across the file
- review_status starts as "pending" and is updated by review-implementation

---

## plan.yaml

Output of: `plan-story`
Input to: `implement-story`, `review-implementation`, evaluation scripts

```yaml
story_id: <string>                   # References the story from stories.yaml (e.g., "PANTRY-001")
plan_version: <string>               # Semantic version or date (e.g., "2026-08-03-v1")
source_story:
  title: <string>                    # Copied from stories.yaml for context
  user_story: <string>               # Copied from stories.yaml for context

tasks:
  - id: <string>                     # Task identifier (e.g., "PANTRY-001-T1")
    description: <string>            # What to do (verb-first)
    dependencies: [<string>]         # Task IDs this depends on (empty list if none)
    files_affected: [<string>]       # Expected files to create or modify
    risks: [<string>]                # Known risks or unknowns
    acceptance_criteria_refs: [<string>]  # Which AC IDs this task addresses

assumptions: [<string>]              # Assumptions made during planning
open_questions: [<string>]          # Unresolved questions for the team
```

### Validation Rules
- story_id must match a story in stories.yaml
- Every AC in the source story must be referenced by at least one task's acceptance_criteria_refs
- tasks must be in dependency order (no forward references to later task IDs)
- Each task must have at least one acceptance_criteria_ref

---

## review.yaml

Output of: `review-implementation`
Updates: `stories.yaml` (sets review_status and review_notes on reviewed stories)

```yaml
review_id: <string>                  # Unique review identifier
story_id: <string>                   # Which story was reviewed
reviewed_at: <string>                 # ISO date

verdict: <enum>                      # "passed" | "failed" | "changes_requested"

issues:
  - severity: <enum>                 # "blocker" | "major" | "minor" | "nit"
    category: <enum>                 # "correctness" | "edge_case" | "readability" | "test_coverage" | "ac_violation"
    description: <string>            # What's wrong
    recommendation: <string>         # Specific fix
    ac_ref: <string>                 # Which AC is affected (or "general")

ac_assessment:
  - ac_id: <string>                  # AC identifier from stories.yaml
    status: <enum>                   # "satisfied" | "not_satisfied" | "partially_satisfied"
    notes: <string>                  # Why

summary: <string>                    # Overall assessment in 2-3 sentences
```

### Validation Rules
- story_id must match a story in stories.yaml
- Every AC in the source story must appear in ac_assessment
- If verdict is "passed", all ac_assessment entries must be "satisfied"
- review-implementation also writes back to stories.yaml: sets review_status to the verdict and review_notes to a summary

---

## Pipeline Data Flow

```
create-epics-stories → stories.yaml
                           ↓
plan-story reads stories.yaml (FAILS if not found)
plan-story → plan.yaml
                           ↓
implement-story reads plan.yaml (FAILS if not found)
implement-story → code
                           ↓
review-implementation reads stories.yaml + plan.yaml + code
review-implementation → review.yaml
review-implementation updates stories.yaml (review_status, review_notes)
```