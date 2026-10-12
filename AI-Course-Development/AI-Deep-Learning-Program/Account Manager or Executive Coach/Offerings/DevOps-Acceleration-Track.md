# DevOps Acceleration Track — AM Offering Sheet

*Account Manager reference for scoping, pricing, and including in an SOW*

---

## What This Is

A parallel workstream that builds the CI/CD and testing infrastructure AI-augmented teams need to actually ship productivity gains. The DLP teaches teams to build AI skills; the DevOps track ensures those skills can run in a pipeline with automated verification, cost guardrails, and quality gates.

This is for clients whose DevOps maturity is a limiting factor. Teams without robust CI/CD, automated testing, and infrastructure-as-code carry "verification debt" — AI generates output faster than humans can verify it. This is the most common bottleneck in organizations with sub-mature SDLC practices, and it caps the productivity gain achievable through the DLP alone.

---

## When to Sell This

| Client Signal | Include DevOps Track? |
|---------------|----------------------|
| Teams lack automated build/test/deploy pipelines | Yes — recommended |
| Teams have CI/CD but no meaningful test coverage | Yes — the testing framework is the gap |
| Infrastructure is provisioned manually, not via IaC | Yes — IaC is needed for agent CI/CD |
| Teams have robust CI/CD, automated testing, and IaC | No — teams can proceed directly to the DLP |
| Client asks "can AI-generated code go through our existing pipeline?" and the answer is "what pipeline?" | Yes |

**Key questions to ask during scoping:**
- *"Do your teams have automated build, test, and deploy pipelines?"*
- *"What's your current test coverage — unit, integration, regression?"*
- *"Is infrastructure provisioned via code or manually?"*
- *"When a developer makes a PR, what automated checks run before merge?"*

If the answer to most of these is "we don't have that" or "it varies by team," the DevOps track is needed.

---

## What's Included

### Staffing

2 DevOps Specialists, 12–24 weeks. These are practitioners embedded alongside the DLP — not trainers, not consultants who deliver a plan and leave. They build the pipeline infrastructure.

**DevOps Specialist 1 (Pipeline & CI/CD):**
- CI/CD pipeline deployment per team
- Automated testing framework (unit, integration, regression)
- PR gates and protected branch configuration
- Merge automation guardrails with mandatory human review thresholds

**DevOps Specialist 2 (Observability & IaC):**
- Infrastructure-as-code for deployment environments
- AI acceptance rate and code quality instrumentation
- Governance signal feeds into BI dashboards (spend, acceptance, reliance)
- Token guardrail alerts (configures alerts and spending controls for GitHub Copilot, Claude, and Microsoft Copilot)
- Agent CI/CD integration (tested prompts and agents promoted through the repository are automatically evaluated on deploy; performance regressions fail the pipeline before they reach teams)

---

## Delivery Phases

| Phase | Weeks | Activities | Deliverables |
|-------|-------|-------------|--------------|
| **Assessment** | 1–4 | Current-state CI/CD audit per team, testing coverage baseline, IaC gap analysis, prioritized build list for Wave 1 readiness | Assessment report per team; prioritized build list |
| **Build (Wave 1 Prep)** | 5–12 | CI/CD pipelines deployed for Wave 1 cohort teams, automated testing frameworks live, acceptance rate instrumentation active before first cohort day one | Pipelines operational per team; testing frameworks deployed; instrumentation feeding governance dashboards |
| **Extend (Wave 1 Run)** | 13–20 | Remaining teams onboarded, agent CI/CD integration, token guardrails and cost monitoring live, governance signal feeds into dashboards | All teams have CI/CD; agent promotion pipeline automated; cost monitoring live |
| **Handoff (Optional)** | 21–24 | IaC templates and runbooks transferred to client platform team, pipeline templates published to internal repository, Improving in advisory role only | Runbooks, templates, and documentation transferred; client team owns maintenance |

**Critical timing:** The Build phase (Weeks 5–12) must complete before Wave 1 cohorts go live. Cohort teams cannot sustain AI productivity gains without pipeline infrastructure. The DevOps track starts before the DLP wave, not during it.

---

## Relationship to the DLP

The DevOps track is not part of the DLP curriculum. It runs alongside the DLP as a separate workstream. The DLP teaches teams to build AI skills; the DevOps track builds the infrastructure that lets those skills produce shippable, verified output.

**What happens without it:** Teams build AI skills, generate code faster, but can't verify or deploy it faster. The productivity gain from AI is capped by the verification bottleneck. The team generates output that sits in PRs waiting for manual review because there's no automated testing to give confidence.

**What happens with it:** Teams build AI skills, generate code faster, and the pipeline automatically tests, verifies, and surfaces quality signals before merge. The productivity gain compounds because the verification step doesn't become the new bottleneck.

---

## Pricing

| Staffing | Duration | Example Cost (at $200/hr) |
|----------|----------|---------------------------|
| 2 DevOps Specialists × 40 hrs/week | 12 weeks | $192,000 |
| 2 DevOps Specialists × 40 hrs/week | 18 weeks | $288,000 |
| 2 DevOps Specialists × 40 hrs/week | 24 weeks | $384,000 |

The duration depends on the number of teams and the starting DevOps maturity. A client with 10 cohorts and no existing CI/CD needs the full 24 weeks. A client with 5 cohorts and partial CI/CD may need only 12–18 weeks.

---

## SOW Language

The following can be adapted directly into an SOW:

> *DevOps Acceleration Track: Improving will provide 2 DevOps Specialists for [12–24] weeks to build pipeline infrastructure alongside the DLP. The engagement is phased: (1) Assessment (Weeks 1–4) — current-state CI/CD audit per team, testing coverage baseline, IaC gap analysis; (2) Build (Weeks 5–12) — CI/CD pipelines deployed for Wave 1 cohort teams, automated testing frameworks live, AI acceptance rate instrumentation active before first cohort day one; (3) Extend (Weeks 13–20) — remaining teams onboarded, agent CI/CD integration, token guardrails and cost monitoring live; (4) Handoff (Weeks 21–24, optional) — IaC templates and runbooks transferred to [client] platform team. Deliverables include: CI/CD pipeline deployment per team, automated testing framework (unit, integration, regression), PR gates and protected branch configuration, AI acceptance rate instrumentation, agent CI/CD integration, and token cost guardrails.*

---

*Full delivery plans for the DevOps track live with the delivery team. This document gives the AM enough to scope, price, and sell the offering without the delivery detail.*