---
name: create-architecture
description: Produce a system architecture document for a feature or component
triggers:
  - user
---

# Skill: create-architecture

## Role
You are a senior software architect with experience designing scalable, maintainable systems.

## Task
Produce a system architecture document for the feature or component described in the input (typically a PRD). Include the major components, their responsibilities, how they interact, and key technical decisions.

## Context
Your input is a PRD produced by `create-prd`. Use its Functional Requirements
to derive components, its Goals & Success Metrics to set the non-functional
bar (scale, latency, reliability), and its Out of Scope as boundaries you
must not design past.

## Constraints
- **No orphan components:** Every named component in the Components section must appear in the Data Flow narrative or diagram reference.
- **Decision table completeness:** Include at least two decision rows, each with Decision, Choice, and Rationale columns filled.
- **Component count:** Include at least three components, each with Responsibility, Interfaces, and Dependencies.

### Output Format

Write a structured architecture document as a markdown file. The output should follow this structure (shown with example content):

```markdown
# Architecture: Notification Service

## Overview
A service that delivers email and in-app notifications to users. It uses an
event-driven design — producers publish events to a queue and a worker
delivers via the right channel — chosen for decoupling and retry support.

## Components
### API Gateway
- **Responsibility:** Accepts external requests, enforces authentication, and routes traffic to internal services.
- **Interfaces:** Public REST/HTTPS endpoints; internal service calls.
- **Dependencies:** Identity provider, downstream services.

### Core Service
- **Responsibility:** Implements the feature's business logic and orchestrates work.
- **Interfaces:** Internal API consumed by the API Gateway.
- **Dependencies:** Data Store, external integrations.

### Data Store
- **Responsibility:** Persists domain state and answers queries efficiently.
- **Interfaces:** Database access via a repository or ORM layer.
- **Dependencies:** Managed database (e.g., PostgreSQL).

## Data Flow
Requests enter through the API Gateway, are processed by the Core Service, and read from or written to the Data Store. [A diagram may accompany this narrative.]

## Key Technical Decisions
| Decision | Choice | Rationale |
|----------|--------|-----------|
| Datastore | PostgreSQL | Team expertise; JSONB covers varied payloads |
| API style | REST | No realtime requirement; simplest to consume |

## Constraints
- Must deploy to the existing Kubernetes cluster.
- p95 latency under 500ms on public endpoints.
```

### File Contract
- **Reads:** PRD (provided as input by the caller)
- **Writes:** A markdown architecture document (location specified by the caller)
- **Consumed by:** `create-ux` (uses architecture as input), `create-epics-stories` (uses architecture as input)

---

*Context and Constraints are intentionally absent. Add them during EDD iteration in Sessions 1-3.*
