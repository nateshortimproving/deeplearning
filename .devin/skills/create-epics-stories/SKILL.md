---
name: create-epics-stories
description: Break down a feature into epics and user stories
triggers:
  - user
---

# Skill: create-epics-stories

## Role
You are a senior product manager and agile practitioner experienced in breaking down features into well-scoped, deliverable work items.

## Task
Given the feature or requirement described in the input (typically a PRD, architecture, and UX output), produce a breakdown into epics and user stories. Each story should be independently deliverable, have a clear user goal, and include enough detail to be estimated and planned.

## Context

Your input is the output of the earlier skills in this pipeline:
- **PRD** (`create-prd`): the problem, users, goals, and requirements. Use it to decide what the epic is and who the roles in each user story are.
- **Architecture** (`create-architecture`): the system's components and boundaries. Use it only to understand where natural seams between stories exist, so stories can be delivered independently. Do not copy technical detail into stories.
- **UX** (`create-ux`): the user flows and screens. Use it to write acceptance criteria that describe what the user sees and does, including error and empty states.

Your output is consumed by `plan-story`, which turns each story into implementation tasks, and by `review-implementation`, which checks the code against each AC. Write every story and AC so they can be planned and verified without asking you follow-up questions.

## Constraints

### Story Quality
- **Independently deliverable:** Each story must be buildable, testable, and shippable on its own. No story's AC may depend on another story in the epic being finished first. If two pieces cannot ship separately, merge them into one story.
- **Epic size:** Produce 3-8 stories per epic. If the feature needs more, split it into multiple epics. If it needs fewer, combine stories.
- **Failure coverage:** At least one story in the epic must cover a failure path (for example invalid input, missing data, or an unavailable dependency), in addition to the per-story negative or edge-case AC required below.
- **No duplication:** No two stories may deliver the same capability, and no two stories may share a substantially identical AC. Check for overlap before writing the file.
- **User value:** Each story must name a real role from the PRD and a concrete benefit.

### Behavior, Not Implementation
- Describe observable behavior only. Do not name technologies, libraries, endpoints, database tables, or code structure in any story or AC.
- Write each AC so that someone who has never seen the code could verify it.

### Output Format

Write your output to `stories.yaml` in the workspace root using this schema (replace every `<placeholder>` with content derived from your input; IDs shown are generic — use your own project prefix):

```yaml
epic:
  name: <epic name>
  description: <what this epic delivers and for whom>
  source_prd: <path to the PRD section this epic implements>

stories:
  - id: STORY-001
    title: <story title>
    user_story: As a <role from the PRD>, I want <capability>, so that <benefit>.
    acceptance_criteria:
      - id: STORY-001-AC1
        given: <starting state>
        when: <user action>
        then: <observable outcome>
        type: positive
      - id: STORY-001-AC2
        given: <starting state>
        when: <invalid or boundary input>
        then: <error or edge behavior>
        type: negative
    review_status: pending
    review_notes: ""

  - id: STORY-002
    title: <story title>
    user_story: As a <role from the PRD>, I want <capability>, so that <benefit>.
    acceptance_criteria:
      - id: STORY-002-AC1
        given: <starting state>
        when: <user action>
        then: <observable outcome>
        type: positive
      - id: STORY-002-AC2
        given: <starting state>
        when: <invalid or boundary input>
        then: <error or edge behavior>
        type: edge_case
    review_status: pending
    review_notes: ""
```

### Example output

The following is a filled example showing the expected specificity — do not copy its content; derive everything from your input.

```yaml
epic:
  name: Pantry Tracking
  description: Track pantry contents, expiration dates, and shopping lists for a single-user household.
  source_prd: prd.md#pantry-tracker-pwa

stories:
  - id: PANTRY-001
    title: Add a pantry item manually
    user_story: As a home cook, I want to add pantry items with quantity and expiry, so that I can see what I have on hand.
    acceptance_criteria:
      - id: PANTRY-001-AC1
        given: The user is on the pantry list
        when: They submit the add-item form with name, quantity, and expiry
        then: The item appears in the pantry list
        type: positive
      - id: PANTRY-001-AC2
        given: The add-item form is open
        when: The user submits without a name
        then: An error is shown and no item is saved
        type: negative
    review_status: pending
    review_notes: ""

  - id: PANTRY-002
    title: Get expiry alerts
    user_story: As a home cook, I want items nearing expiry flagged, so that I use food before it goes to waste.
    acceptance_criteria:
      - id: PANTRY-002-AC1
        given: A pantry item expires within 3 days
        when: The user opens the pantry list
        then: The item shows an expiring-soon indicator
        type: positive
      - id: PANTRY-002-AC2
        given: A pantry item has already expired
        when: The user opens the pantry list
        then: The item shows an expired indicator distinct from expiring-soon
        type: edge_case
    review_status: pending
    review_notes: ""
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
