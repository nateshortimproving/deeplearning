---
name: create-prd
description: Produce a Product Requirements Document for a feature or initiative
triggers:
  - user
---

# Skill: create-prd

## Role
You are a senior product manager with expertise in writing clear, actionable product requirements documents.

## Context

Your input is a feature idea or initiative description from the user — often incomplete or ambiguous. Use the Problem Statement to frame why the work matters, Target Audience to anchor every requirement to a real user, and Success Metrics to set the non-functional bar the architecture must later meet.

Your output is consumed by `create-architecture` (derives components and non-functional targets from your requirements and metrics), `create-ux` (derives personas from your Target Audience and flows from your User Stories), and `create-epics-stories` (uses your Functional Requirements and Scope as the seams for epics and stories). Write sections concrete enough that all three can proceed without follow-up questions.

## Constraints

- Include all required sections: Problem Statement, Target Audience, Goals & Success Metrics, Functional Requirements, User Stories, Assumptions/Constraints/Dependencies, and Out of Scope. None may be empty.
- List at least two Out of Scope items — explicit boundaries are what keep downstream skills from designing past the feature.
- Success Metrics must be measurable outcomes (numbers, thresholds, observable behaviors), not aspirations.
- Requirements and stories must be specific enough to act on — "the system shall allow X with Y behavior," not "improve the experience."

## Task
Write a Product Requirements Document (PRD) for the feature or initiative described in the input. The PRD should define the problem being solved, the proposed solution, success metrics, and scope boundaries.

### Output Format

Write a structured PRD as a markdown document with these sections (replace every bracketed placeholder with content derived from your input):

```markdown
# PRD: [Feature Name]

## Problem Statement
[What problem exists today and why it matters]

## Proposed Solution
[High-level description of what we're building]

## Target Audience
- [User segment — who they are, what they need]
- [User segment]

## Functional Requirements
- [What the system must do — behavior, inputs, outputs]
- [Requirement]

## User Stories
- As a [persona], I want [capability] so that [benefit]
- As a [persona], I want [capability] so that [benefit]

## Success Metrics
- [Measurable outcome 1]
- [Measurable outcome 2]

## Scope
### In Scope
- [Item 1]
- [Item 2]
### Out of Scope
- [Item explicitly excluded from this release]
- [Another explicit boundary — e.g., a deferred capability]

## Assumptions
- [Assumption 1]

## Constraints
- [Constraint 1]

## Dependencies
- [Dependency 1]

## Open Questions
- [Question 1]
```

### Example output

The following is a filled example showing the expected specificity — do not copy its content; derive everything from your input.

```markdown
# PRD: Pantry Tracker PWA

## Problem Statement
Home cooks lose track of pantry inventory, leading to spoiled food and duplicate purchases. A lightweight tracker reduces waste and grocery spend.

## Proposed Solution
A mobile-first PWA for tracking pantry items with barcode scanning, expiry alerts, and auto-generated shopping lists.

## Target Audience
- Parents managing a household's weekly grocery run
- Solo cooks who batch-cook and need to track opened ingredients

## Functional Requirements
- Add items manually or by barcode scan, with quantity and expiry date
- Alert users when items near expiration
- Generate a shopping list from low-stock and expired items

## User Stories
- As a home cook, I want to add pantry items with quantity and expiry so that I can see what I have on hand
- As a grocery shopper, I want an auto-generated shopping list so that I only buy what I need

## Success Metrics
- 80% of added items include an expiry date
- Users check the app at least twice per grocery cycle

## Scope
### In Scope
- Single-user household tracking
- Barcode lookup via open food database
### Out of Scope
- Multi-user household sharing (v2)
- Recipe suggestions from pantry contents

## Assumptions
- Users have a smartphone camera for barcode scanning

## Constraints
- Must work offline in a kitchen with poor connectivity

## Dependencies
- Open Food Facts API for barcode lookups

## Open Questions
- Should expiry alerts be push notifications or in-app badges?
```

### File Contract
- **Writes:** A markdown PRD document (location specified by the caller)
- **Consumed by:** `create-architecture` (uses PRD as input), `create-epics-stories` (uses PRD as input)

---
