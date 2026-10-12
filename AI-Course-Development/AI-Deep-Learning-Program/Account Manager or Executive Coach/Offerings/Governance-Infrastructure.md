# Governance Infrastructure — AM Offering Sheet

*Account Manager reference for scoping, pricing, and including in an SOW*

---

## What This Is

Governance infrastructure is the layer that turns DLP training into measurable operational proof. Without it, the program outcome is "we trained people." With it, the program outcome is "here's the dashboard showing velocity improvement, acceptance rates, spend-to-output ratios, and compliance agents running in the SDLC."

This is the mechanism that makes scaling safe and makes the ROI story credible to a finance organization or steering committee. It is built during the pre-wave planning period and must be operational before Wave 1 cohorts go live.

---

## When to Sell This

| Client Signal | Include Governance? |
|---------------|---------------------|
| 5+ cohorts, enterprise-scale, needs executive ROI proof | Yes — required |
| 3–4 cohorts, moderate scale, some executive visibility needed | Recommended — talk to the client about it |
| 1–2 cohorts, small engagement | No — the standard DLP Completion Rubric and AI Adoption Maturity Assessment are sufficient |
| Client asks "how do we measure whether this is working?" at the org level | Yes — this is the answer to that question |

**Key question to ask during scoping:** *"How will you measure whether the program worked at the organizational level? Who needs to see that data, and what will they need to see?"* If the answer involves a steering committee, finance team, or C-level reporting, governance infrastructure is needed.

---

## What's Included — Six Components

### 1. Multi-Tool Spend Dashboard

**What it is:** A dashboard monitoring daily spend per user across all AI tools in use (GitHub Copilot, Claude, Microsoft Copilot, etc.), weekend usage anomalies, and spend-to-output ratios.

**Why the client needs it:** Organizations commonly spend 3–4x the necessary token cost in the first 90 days without monitoring. Developers run expensive models on tasks that smaller models handle adequately. The dashboard surfaces this before it compounds.

**What it delivers:** Real-time visibility into per-developer and per-team AI spend, with alerts for anomalies (weekend usage, spend spikes, high spend with low output). Integrates with the client's existing BI platform (Fabric, Power BI, or equivalent).

### 2. Adoption-to-Operate Signal Tracking

**What it is:** Tracking that distinguishes teams in the adoption stage (driving usage — getting people to use the tools) from teams in the operate stage (driving output quality — getting better results from the tools). The dashboard evolves as teams mature.

**Why the client needs it:** The coaching intervention for an adoption-stage team ("use the tool more, try these workflows") is different from the intervention for an operate-stage team ("your acceptance rate is too high, you're rubber-stamping"). Without this tracking, the Enterprise Coach can't target coaching effectively across multiple cohorts.

**What it delivers:** Signal tracking per team with stage classification, trend data showing teams progressing from adoption to operate, and alerting when teams stagnate or regress.

### 3. Acceptance Rate and Reliance Rate Monitoring

**What it is:** Monitoring that flags over-reliance (>90% acceptance rate = cognitive surrender, where developers rubber-stamp AI output) and under-reliance (<60% acceptance rate = not trusting the tool). Both extremes require coaching, not technology fixes.

**Why the client needs it:** The current observed accuracy rate for AI code generation is ~87%. A 100% acceptance rate means developers are introducing ~13% slop into the codebase without reviewing it. A <60% acceptance rate means the team isn't getting the productivity benefit. The monitoring catches both problems early.

**What it delivers:** Per-developer and per-team acceptance rate tracking with threshold alerts. Feeds into the Enterprise Coach's coaching dashboard so the EC knows who to talk to and what to talk about.

### 4. Agent Promotion Board

**What it is:** A bi-weekly review process where the Enterprise Coach and EEs evaluate team-built agents (task agents and workflow agents) for promotion to the shared repository. Promoted agents are available to all teams after the wave.

**Why the client needs it:** This is the mechanism that compounds value across waves. A good agent built by one team in Wave 1 becomes available to all teams in Wave 2. Without the promotion board, each team rebuilds what other teams already solved.

**What it delivers:** A defined review cadence, promotion criteria, version control for promoted agents, and a shared repository structure that organizes agents by scope (globally true, domain-specific, business-specific).

### 5. Skills Repository Structure

**What it is:** A three-tier structure for organizing promoted agents:
- **Globally true agents** — compliance, security, SOX/PCI audit — applicable to all teams
- **Domain-specific agents** — by tech stack (C#/.NET, Java, React/Node.js)
- **Business-specific agents** — the client's own systems and domain logic

**Why the client needs it:** This is the asset that the client owns after the engagement. It lives in their codebase and compounds over time. A team that builds a great agent for their commerce platform makes it available to every other team working on that platform.

**What it delivers:** Repository structure, contribution guidelines, version control, and documentation standards for promoted agents. Integrates with the agent promotion board process.

### 6. Governance Dashboard Templates

**What it is:** Dashboard templates built on the client's existing BI platform (Fabric, Power BI, or equivalent) and adapted from infrastructure used on prior engagements.

**Why the client needs it:** Avoids building from scratch. We bring templates and customize them to the client's tools and data sources. This reduces build time from months to weeks.

**What it delivers:** Operational dashboards showing spend, adoption stage, acceptance rates, reliance rates, agent inventory, and trend data across all active cohorts.

---

## Delivery Timeline

Built during the 4-week pre-wave planning period, overlapping with the MVP. Must be operational before Wave 1 cohorts go live — not built after the fact. The governance infrastructure should run alongside the program, not behind it.

---

## Staffing

Primarily the Enterprise Coach during pre-wave planning, with dashboard build support as needed. The build cost depends on the client's existing BI platform and how much customization is needed.

- **Simple:** Client has Fabric/Power BI and existing data pipelines — templates adapt quickly (~$50K build cost)
- **Moderate:** Client has a BI platform but needs data pipeline work to feed the dashboards (~$100K build cost)
- **Complex:** Client needs data pipeline work plus custom dashboard development (~$150K build cost)

---

## Pricing

| Component | Calculation | Example Cost |
|-----------|-------------|--------------|
| Enterprise Coach time (included in EC pre-wave) | Part of EC engagement | Included in EC line item |
| Dashboard build (if separate) | Per engagement | $50,000–$150,000 depending on complexity |

---

## SOW Language

The following can be adapted directly into an SOW:

> *Governance Infrastructure: Improving will establish a governance framework operational before Wave 1 cohort go-live, including: (1) a multi-tool spend dashboard monitoring daily per-user spend across AI tools with anomaly alerting; (2) adoption-to-operate signal tracking per team with stage classification and trend data; (3) acceptance rate and reliance rate monitoring with threshold alerts (>90% and <60%); (4) an agent promotion board process with bi-weekly review cadence and promotion criteria; (5) a skills repository structure with three-tier organization (globally true, domain-specific, business-specific agents); and (6) governance dashboard templates built on [client BI platform] and adapted from prior engagement infrastructure. The governance framework will be operational before Wave 1 cohorts begin and will run alongside the program for the duration.*

---

*Full delivery plans for governance infrastructure live with the Enterprise Coach guidance. This document gives the AM enough to scope, price, and sell the offering without the delivery detail.*