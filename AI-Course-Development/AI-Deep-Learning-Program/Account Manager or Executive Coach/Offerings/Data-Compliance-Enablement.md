# Data & Compliance Enablement — AM Offering Sheet

*Account Manager reference for scoping, pricing, and including in an SOW*

---

## What This Is

A parallel workstream that makes compliance active and continuous for clients operating under regulatory regimes (PCI DSS, SOX, GDPR). Passive compliance — end-of-cycle audits — does not catch AI-generated code that introduces scope creep, credential mishandling, or audit trail gaps. This workstream builds the infrastructure that catches these issues at commit time, not at audit time.

---

## When to Sell This

| Client Signal | Include Compliance Track? |
|---------------|--------------------------|
| Client operates under PCI DSS | Yes — PCI-active agents prevent AI-introduced scope creep |
| Client operates under SOX | Yes — SOX audit trail generation makes AI-assisted changes traceable |
| Client operates under GDPR or similar data protection regime | Yes — data classification prevents PII exposure to AI models |
| Client has regulatory compliance but no AI-specific controls | Yes — this is the gap this track fills |
| Client has no regulatory compliance requirements | No — not needed |

**Key questions to ask during scoping:**
- *"What compliance frameworks does your engineering organization operate under?"*
- *"How do you currently handle compliance for code changes — end-of-cycle audit, or continuous?"*
- *"If an AI tool generates code that touches PCI-scope data, how would you know?"*
- *"Can you trace which code changes were AI-assisted for SOX change management?"*

If the client has compliance requirements and can't answer the last two questions, the compliance track is needed.

---

## What's Included

### Staffing

2 BI/Data Engineers, 16 weeks. These are practitioners building the compliance infrastructure — not auditors, not consultants who deliver a gap analysis and leave. They build the tooling that makes compliance automated.

**BI/Data Engineer 1 (Governance):**
- PCI-active and SOX-aware agent framework
- Compliance signal dashboards on Fabric/Power BI
- Agent acceptance and reliance tracking
- Spend-to-output monitoring
- Agent promotion governance process

**BI/Data Engineer 2 (Data Compliance):**
- PCI + SOX scope boundary mapping
- Data classification agent integration
- Zero-retention policy enforcement tooling
- SOX-traceable audit artifact generation for AI-assisted PRs
- GDPR data residency controls

---

## Delivery Phases

| Phase | Weeks | Activities | Deliverables |
|-------|-------|-------------|--------------|
| **Discovery** | 1–4 | PCI scope boundary mapping, data classification audit, AI tool call chain analysis, governance dashboard requirements | Scope boundary map; data classification audit; dashboard requirements doc |
| **Build** | 5–8 | PCI-active agent build and testing, data classification layer deployment, initial governance dashboards live | PCI-active agent tested; data classification deployed; first dashboards operational |
| **Integrate** | 9–12 | Agent integration with Wave 1 CI/CD pipelines, audit artifact templates deployed, acceptance/reliance tracking live | Compliance agents running in CI pipeline; audit artifacts generating automatically; tracking live |
| **Operationalize** | 13–16 | Handoff to client data/governance team, runbooks, alert configurations, policy documentation, compliance infrastructure fully transferred | Runbooks, alerts, policy docs; client team owns operation |

**Critical timing:** Must be operational before Wave 1 cohorts go live. The 16-week engagement overlaps with the MVP and Wave 1 planning period by design. Compliance infrastructure built after the fact is too late — once AI tools are in use without controls, the exposure has already occurred.

---

## Deliverables by Compliance Framework

### PCI DSS

**What we build:** PCI-active agent in the SDLC — runs on every commit touching PCI-scope code, flags issues inline rather than at audit time. Prevents AI-generated code from silently introducing out-of-scope data handling.

**Why it matters:** Passive compliance (end-of-cycle audits) doesn't catch AI-introduced scope creep. A developer asks AI to "add a logging feature" and the AI includes cardholder data in the log output — passive compliance catches this at audit time, months later. Active compliance catches it at commit time, before it ships.

### SOX

**What we build:** SOX audit trail generation — every AI-assisted code change carries a traceable attribution record. AI-generated contributions are tagged at the commit level to satisfy SOX change management controls and support auditor review.

**Why it matters:** SOX IT General Controls require change management evidence. If AI-assisted changes aren't traceable, the audit trail has gaps. An auditor asking "who made this change and was it reviewed?" needs an answer that includes "this was AI-assisted, reviewed by [developer], and approved through [process]."

### GDPR

**What we build:** Data classification layer — classifies data across AI tool call chains to ensure PII, cardholder data, and SOX-sensitive systems data is never passed to models without proper controls. Zero-retention configurations for PCI-scope workflows. Permission scoping per team.

**Why it matters:** AI tools that receive PII without controls create a data exposure risk. If a developer pastes customer data into a Copilot prompt, that data may be retained by the model provider. Classification + zero-retention prevents this before it happens.

### All Frameworks

**What we build:** Audit-ready artifact generation — automatically produces evidence records for AI-assisted PRs. Designed to satisfy PCI DSS Req. 6.x and SOX IT General Controls for software development practices. Agent policy infrastructure — enforces rules on which tools can access which data environments, permission scoping per team.

**Why it matters:** Auditors need evidence. If evidence generation is manual, it's inconsistent and time-consuming. Automated generation makes audit preparation a non-event — the evidence is already there when the auditor asks.

---

## Relationship to the DLP and Governance Infrastructure

This workstream is separate from the DLP curriculum but integrates with the Governance Infrastructure offering. The compliance agents built in this track feed signals into the governance dashboards. The data classification layer integrates with the DevOps Acceleration Track's CI/CD pipelines — compliance checks run as pipeline gates, not as separate processes.

**Ordering:** If the client needs both DevOps and Compliance tracks, the DevOps track should start first (or concurrently). The compliance agents need a CI/CD pipeline to run in — building compliance agents without pipelines is infrastructure without a home.

---

## Pricing

| Staffing | Duration | Example Cost (at $200/hr) |
|----------|----------|---------------------------|
| 2 BI/Data Engineers × 40 hrs/week | 16 weeks | $256,000 |

The 16-week duration is standard — the phased delivery (Discovery → Build → Integrate → Operationalize) requires the full 16 weeks to complete before Wave 1 go-live. Shorter durations are not recommended as they compress the Build and Integrate phases, which are where the actual infrastructure is constructed.

---

## SOW Language

The following can be adapted directly into an SOW:

> *Data & Compliance Enablement: Improving will provide 2 BI/Data Engineers for 16 weeks to build compliance infrastructure alongside the DLP, making compliance active and continuous across [PCI DSS / SOX / GDPR] frameworks. The engagement is phased: (1) Discovery (Weeks 1–4) — PCI scope boundary mapping, data classification audit, AI tool call chain analysis; (2) Build (Weeks 5–8) — PCI-active agent build and testing, data classification layer deployment, initial governance dashboards live; (3) Integrate (Weeks 9–12) — agent integration with Wave 1 CI/CD pipelines, audit artifact templates deployed, acceptance/reliance tracking live; (4) Operationalize (Weeks 13–16) — handoff to [client] data/governance team, runbooks, alert configurations, policy documentation. Deliverables include: PCI-active agents in the SDLC, SOX audit trail generation for AI-assisted changes, data classification layer, governance dashboards on [client BI platform], audit-ready artifact generation, and agent policy infrastructure. Compliance infrastructure will be operational before Wave 1 cohorts go live.*

---

*Full delivery plans for the compliance track live with the delivery team. This document gives the AM enough to scope, price, and sell the offering without the delivery detail.*