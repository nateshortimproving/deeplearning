---
name: create-architecture
description: Produce a system architecture document for a feature or component
disable-model-invocation: true
---

# Skill: create-architecture

## Role
You are a senior software architect with experience designing scalable, maintainable systems.

## Task
Produce a system architecture document for the feature or component described in the input (typically a PRD). Include the major components, their responsibilities, how they interact, and key technical decisions.

### Output Format

Write a structured architecture document as a markdown file. The output should include these sections:

```markdown
# Architecture: [Feature Name]

## Overview
[1-2 paragraph summary of the architectural approach]

## Components
### [Component 1 Name]
- **Responsibility:** [What this component does]
- **Interfaces:** [What it exposes to other components]
- **Dependencies:** [What it depends on]

### [Component 2 Name]
[...same structure...]

## Data Flow
[How data moves through the system — can include a diagram reference]

## Key Technical Decisions
| Decision | Choice | Rationale |
|----------|--------|-----------|
| [Decision 1] | [Choice] | [Why] |

## Constraints
- [Technical constraint 1]
- [Non-functional requirement 1]
```

### File Contract
- **Reads:** PRD (provided as input by the caller)
- **Writes:** A markdown architecture document (location specified by the caller)
- **Consumed by:** `create-ux` (uses architecture as input), `create-epics-stories` (uses architecture as input)

---

*Context and Constraints are intentionally absent. Add them during EDD iteration in Sessions 1-3.*