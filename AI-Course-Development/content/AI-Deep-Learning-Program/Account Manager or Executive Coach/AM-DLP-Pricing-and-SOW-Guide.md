# Account Manager's Guide to Pricing and Bidding the DLP

*Deep Learning Program (DLP) — Account Manager Reference for SOW Construction and Pricing*

*Version: August 2026*

---

## Who This Document Is For

You are the **Account Manager** on a DLP pursuit. You may be non-technical, but you need to understand what the DLP includes, what it costs, and what should — and should not — be in the Statement of Work. This document gives you the framework for pricing a DLP engagement and constructing an SOW that covers what we need to deliver successfully.

This document does not cover delivery — that's the Executive Coach guidance (`AM-EC-Executive-Guidance.md`). This covers the commercial side: what to price, what to include, and what to watch for.

---

## DLP Engagement Components

A DLP engagement has the following cost components. Every SOW should account for each one, even if some are bundled or discounted.

### 1. Embedded Engineer (the dominant cost)

The EE is embedded with the client team for the full 12 weeks (Stage 3) or 16 weeks (Stage 4), 40 hours/week. This is the largest line item — typically 80–85% of the total engagement cost.

**What to include in the SOW:**
- EE time for the full engagement duration (12 or 16 weeks)
- EE time for pre-engagement preparation (typically 1 week before Week 1 — reading discovery notes, setting up the workspace, briefing with the Trainer)
- EE time for post-engagement wrap-up (typically Week 12 or 16 — handoff document, internal program summary, artifact review)

**The EE-to-Participant Ratio Is a Cost Dial**

The ratio of EEs to participants is the single biggest cost lever in the engagement — and the single biggest outcome lever. This is a negotiable point, not a hard line. The AM should present multiple ratio options with their outcome tradeoffs and let the client make an informed choice.

| Ratio | Configuration | Observed Velocity Improvement | Cost Implication |
|-------|---------------|-------------------------------|-------------------|
| 1:8 | One EE per team of 8 | 11–18% in-program; 20–30% at 6–12 mo | Highest cost, highest outcome |
| 1:16 | One EE across 2 teams | ~7–12% in-program (estimated) | ~50% EE cost reduction |
| 1:24 | One EE across 3 teams | 3–7% in-program | ~67% EE cost reduction |

**Our preference:** 1:8 produces the best outcomes. The data from prior engagements is clear — the more embedded the coaching, the higher the velocity improvement and the better the DLP Completion rates.

**Talking points when the client asks to reduce the ratio:**
- *"The ratio is the biggest dial on both cost and outcomes. We can absolutely flex it — but it's important you understand what you're trading. At 1:8 we see 11–18% velocity improvement during the program. At 1:24, that drops to 3–7%. Both can be the right choice depending on your goals and budget. What matters is that we go in eyes-open."*
- *"If budget is the primary driver, a 1:16 or 1:24 ratio with a longer engagement (e.g., 16 weeks instead of 12) can partially recover the coaching depth. More weeks gives the EE more time with each team even if they're covering multiple teams."*
- *"For teams that are already strong AI adopters, a higher ratio may be fine — they need less coaching intensity. For teams that are starting from scratch or have significant resistance, the 1:8 ratio matters more."*

**What to watch for:**
- EE hours/week must be 40 — full engagement is non-negotiable. The EE's value comes from being present in sprint work every day. If the client asks to reduce EE hours below 40/week, this is a hard line: the coaching model requires full-time presence. If budget is the concern, reduce the ratio (fewer EEs covering more teams) rather than making any single EE part-time.
- Clients may ask to share an EE across teams in different cohorts (different session schedules). This is workable but means the EE splits time across teams and can't be fully present with any one. Present this as a tradeoff, not a refusal.

### 2. Trainer

The Trainer delivers the structured training sessions and (for Stage 4) weekly office hours.

**Stage 3 DLP (12 weeks):**
- 6 training sessions × 4 hours each
- No weekly office hours (the EE handles between-session coaching)

**Stage 4 DLP (16 weeks):**
- 5 training sessions × 4 hours each
- Weekly office hours: 1 hour/week baseline, expandable to 2 hours/week

**What to include in the SOW:**
- Trainer session delivery fees
- Trainer preparation time (typically 1–2 hours per session)
- For Stage 4: office hours at the baseline 1 hour/week, with a note that additional hours may be billed if the team needs more
- Trainer travel expenses if in-person delivery is required

**What to watch for:**
- Clients may ask the Trainer to deliver sessions for more than one cohort in the same week. This is possible but increases Trainer fatigue and reduces preparation quality. Price accordingly.
- Clients may ask for additional sessions beyond the standard 6 (Stage 3) or 5 (Stage 4). This is possible — price per additional session.

### 3. Executive Coach (scale-dependent)

Whether a dedicated EC is required depends on the number of cohorts (see `AM-EC-Executive-Guidance.md` for the full guidance):

| Cohorts | EC Requirement | SOW Implication |
|---------|----------------|-----------------|
| 1–2 | Trainer serves as EC | Add 1–2 hours/week to Trainer's engagement for EC duties |
| 3–4 | Trainer or EE in dual role | Add 2–3 hours/week to the dual-role person's engagement; monitor for overload |
| 5+ | Dedicated EC required | Separate EC line item — typically 5–10 hours/week across all cohorts |

**What to include in the SOW:**
- If Trainer-as-EC (1–2 cohorts): Trainer EC time at the Trainer's hourly rate
- If dedicated EC (5+ cohorts): EC time as a separate line item
- EC travel expenses if in-person touchpoints are required

### 4. Account Manager

The AM's involvement is lighter but non-zero. The AM participates in:
- Pre-engagement scoping and SOW construction (already done by this point)
- Week 12 completion meeting (joint with EC)
- "What comes after" conversation
- Any scope changes or commercial escalations during the engagement

**What to include in the SOW:**
- AM time is typically bundled into the engagement overhead — it's not a separate line item in most pricing models. But internally, account for approximately 2–4 hours/week of AM time across the engagement for relationship management, scope guardrails, and the completion meeting.

### 5. API Keys and Infrastructure (Stage 4 only)

Stage 4 requires API access for the custom harness. The client is responsible for provisioning API keys (see the IT Liaison requirement in the Stage 4 proposal). However, the SOW should note:
- API key provisioning is a client responsibility
- The program does not include API usage costs — the client pays for model API calls directly
- If the client cannot provision keys, the engagement may be delayed

### 6. Enterprise-Scale Components (5+ cohorts only)

The following components apply **only to enterprise-scale engagements** (typically 5+ cohorts, 100+ participants). They are not part of a standard single-cohort or small engagement SOW. Include them when the client is running a multi-wave program and needs the infrastructure to make scaling safe and measurable. Do not include them for small engagements where they add cost without value.

**6a. Enterprise Coach (full-time, per wave)**

At enterprise scale, the EC role becomes a full-time position. The Enterprise Coach starts 4 weeks before each wave (pre-wave planning) and remains full-time through the 12-week execution. This is a significantly larger time commitment than the standard EC (5–10 hours/week across cohorts).

**What to include in the SOW:**
- Enterprise Coach time: 4 weeks pre-wave + 12 weeks execution = 16 weeks, full-time
- Pre-wave planning deliverables: cohort composition plan, wave sequencing, governance infrastructure design, OCM plan
- Enterprise Coach travel expenses if in-person touchpoints are required

**6b. Governance Infrastructure**

The infrastructure that turns training into measurable operational proof. Built during pre-wave planning, operational before Wave 1 cohorts go live.

**What to include in the SOW:**
- Multi-tool spend dashboard (Copilot, Claude, etc.) — monitors daily spend per user, spend-to-output ratios, usage anomalies
- Adoption-to-operate signal tracking — distinguishes adoption stage from operate stage across cohorts
- Acceptance rate and reliance rate monitoring — flags over-reliance (>90%) and under-reliance (<60%) as coaching triggers
- Agent promotion board — bi-weekly review process for promoting team-built agents to the shared repository
- Skills repository structure — globally true agents, domain-specific agents, business-specific agents
- Governance dashboard templates (e.g., Fabric/Power BI) adapted from prior engagement infrastructure

**Full offering detail (scoping questions, per-component descriptions, SOW language, pricing):** see `Offerings/Governance-Infrastructure.md`

**6c. DevOps Acceleration Track (optional, recommended for sub-mature CI/CD)**

Practitioners (not trainers) who build pipeline infrastructure so AI productivity gains can actually ship. Recommended for any team that lacks baseline pipeline automation before entering Wave 1. Optional for teams with mature CI/CD.

**What to include in the SOW:**
- 2 DevOps Specialists, 12–24 weeks
- Deliverables: CI/CD pipeline deployment per team, automated testing framework (unit, integration, regression), AI acceptance rate instrumentation, agent CI/CD integration, token cost guardrails and spending controls
- Phased: Assessment (Weeks 1–4), Build for Wave 1 prep (Weeks 5–12), Extend during Wave 1 run (Weeks 13–20), Optional handoff (Weeks 21–24)

**Full offering detail (scoping questions, per-role deliverables, phased delivery table, SOW language, pricing):** see `Offerings/DevOps-Acceleration-Track.md`

**6d. Data & Compliance Enablement (for clients under PCI, SOX, GDPR)**

Practitioners who make compliance active and continuous. For clients operating under regulatory regimes where passive end-of-cycle audits do not catch AI-introduced issues.

**What to include in the SOW:**
- 2 BI/Data Engineers, 16 weeks
- Deliverables: PCI-active agents in SDLC, SOX audit trail generation, data classification layer, governance dashboards, audit-ready artifact generation, agent policy infrastructure
- Phased: Discovery (Weeks 1–4), Build (Weeks 5–8), Integrate with CI/CD (Weeks 9–12), Operationalize and handoff (Weeks 13–16)
- Must be operational before Wave 1 cohorts go live — the 16-week engagement overlaps with MVP and Wave 1 planning by design

**Full offering detail (scoping questions, per-framework deliverables, phased delivery table, SOW language, pricing):** see `Offerings/Data-Compliance-Enablement.md`

**When to include 6a–6d:** Only for enterprise-scale engagements where the client needs them. A 2-cohort engagement for a company with mature CI/CD and no regulatory concerns needs none of these. The AM should assess DevOps maturity and compliance requirements during scoping. These are optional workstreams that address specific bottlenecks — not standard DLP components.

---

## Pricing Framework

### Stage 3 DLP (12 weeks, per cohort)

| Component | Calculation | Baseline Cost |
|-----------|-------------|---------------|
| Embedded Engineer | 40 hrs/week × 12 weeks × EE bill rate | (e.g., $200/hr → $96,000) |
| Trainer — Sessions | 6 sessions × Trainer session rate | (e.g., $3,000/session → $18,000) |
| Trainer — EC duties (if 1–2 cohorts) | 1–2 hrs/week × 12 weeks × Trainer hourly | (e.g., $500/hr × 18 hrs → $9,000) |
| Executive Coach (if 5+ cohorts) | EC hours × EC bill rate | (varies by EC and cohort count) |
| **Subtotal per cohort** | | **~$114,000–$123,000** (at example rates, no dedicated EC) |

### Stage 4 DLP (16 weeks, per team)

| Component | Calculation | Baseline Cost |
|-----------|-------------|---------------|
| Embedded Engineer | 40 hrs/week × 16 weeks × EE bill rate | (e.g., $200/hr → $128,000) |
| Trainer — Sessions | 5 sessions × Trainer session rate | (e.g., $3,000/session → $15,000) |
| Trainer — Office Hours | 1 hr/week × 16 weeks × Trainer hourly | (e.g., $500/hr → $8,000) |
| Executive Coach (if 5+ cohorts) | EC hours × EC bill rate | (varies) |
| **Subtotal per team** | | **~$151,000** (at example rates, no dedicated EC) |

### Multi-Cohort Pricing

When pricing multiple cohorts, watch for:
- **EE sharing:** If one EE serves multiple teams within a single cohort (all in the same sessions), the EE cost is shared. If multiple cohorts run concurrently, each needs its own EE.
- **Trainer sharing:** One Trainer can deliver sessions to multiple cohorts, but each cohort needs its own session delivery (you can't combine cohorts in a single session without compromising the interactive format). Price per cohort for sessions.
- **EC scaling:** The EC cost doesn't scale linearly — one EC can cover multiple cohorts. The marginal cost per additional cohort decreases for the EC line item.

### What to Discount (and What Not To)

**Can discount:**
- Additional cohorts after the first (marginal cost decreases — same Trainer prep, shared EC if applicable)
- Trainer session rate for bulk engagements (e.g., 3+ cohorts)
- EE rate for long-term engagements (e.g., Stage 3 + Stage 4 back-to-back)

**Do NOT discount:**
- EE hours/week below 40 — full-time engagement is non-negotiable. If budget is the concern, reduce the ratio instead.
- The number of sessions — each session introduces critical content; removing one creates gaps
- API key provisioning (Stage 4) — this is a client responsibility, not something we absorb
- Pre-engagement preparation time — the EE needs this to be effective in Week 1

**Negotiate with eyes open (present the tradeoff, don't refuse):**
- EE-to-participant ratio — this is the biggest cost dial. Lower ratios (1:16, 1:24) are viable but reduce expected velocity improvement. Present the ratio table and let the client choose informed. The EE hours stay at 40/week regardless of ratio — what changes is how many teams each EE covers.

### Enterprise-Scale Pricing (5+ cohorts, multi-wave)

For enterprise-scale engagements, the pricing structure changes from per-cohort to per-wave, with optional workstreams added as separate line items. This section applies only to large engagements — not to single-cohort or small engagements.

**Wave pricing structure:**

A wave consists of: 4-week pre-wave planning (Enterprise Coach) + 12-week execution (all cohorts simultaneously). A wave typically contains 10–12 cohorts.

| Component | Calculation | Example (10 cohorts, 1:8 EE ratio) |
|-----------|-------------|-------------------------------------|
| Enterprise Coach (pre-wave + execution) | 16 weeks × 40 hrs/week × EC bill rate | (e.g., $250/hr → $160,000) |
| EEs (1 per team, ~3 teams per cohort, 10 cohorts) | 30 EEs × 12 weeks × 40 hrs/week × EE bill rate | (e.g., $200/hr → $28,800,000) |
| Trainers (2 trainers cover 10 cohorts) | 2 × 6 sessions × Trainer session rate | (e.g., $3,000 → $36,000) |
| Governance infrastructure build | Per engagement (template adaptation + customization) | (varies — typically $50K–$150K) |
| **Subtotal per wave (DLP only)** | | **~$29M+ at example rates** |

Note: Enterprise-scale pricing is highly dependent on the client's EE ratio, number of teams per cohort, and which optional workstreams are included. The example above uses a 1:8 ratio (one EE per team of 8) which is the highest-cost, highest-outcome configuration. A 1:24 ratio (one EE across 3 teams) would reduce the EE line item by ~67% but also reduces the expected velocity improvement from 11–18% to 3–7%.

**Optional workstream pricing:**

| Workstream | Staffing | Duration | Example Cost |
|------------|----------|----------|--------------|
| DevOps Acceleration Track | 2 DevOps Specialists | 12–24 weeks | (e.g., $200/hr × 2 × 12 wks × 40 hrs → $192,000) |
| Data & Compliance Enablement | 2 BI/Data Engineers | 16 weeks | (e.g., $200/hr × 2 × 16 wks × 40 hrs → $256,000) |
| Governance Infrastructure | Enterprise Coach + dashboard build | Pre-wave period | (included in EC pre-wave time, or separate build cost $50K–$150K) |

**Phase-gated pricing option:**

For enterprise clients hesitant to commit to the full program, offer phase-gated pricing:
- MVP (1–2 cohorts, 16 weeks): priced independently as a proof-of-value entry point
- Wave 1: priced separately, contingent on MVP outcomes
- Wave 2: priced separately, contingent on Wave 1 outcomes
- Higher per-cohort cost but lower initial commitment

This structure reduces the client's risk and gives the executive sponsor concrete evidence to justify each subsequent wave. The MVP's observed outcomes — not promised outcomes — unlock the broader engagement.

### ROI Framing for Enterprise Proposals

For enterprise-scale engagements, the program cost is significant (often millions of dollars). The AM must frame the investment against value creation, not against cost. The framing is **FTE capacity recovery** — teams completing more work in the same time, without headcount changes.

**The ROI calculation framework:**

1. **Developer population in scope** (e.g., 450 FTE)
2. **Estimated fully loaded cost per developer** (e.g., $165K/year — salary + benefits)
3. **Total annual developer investment** (e.g., 450 × $165K = $74.3M)
4. **Program investment** (e.g., $7.28M)
5. **Breakeven productivity improvement** = program investment / annual developer investment (e.g., $7.28M / $74.3M = ~9.8% — call it 10%)

At 10% sustained productivity improvement, the program pays for itself in Year 1. Every scenario above 10% is upside.

**Productivity lift scenarios:**

| Scenario | Productivity Lift | FTEs Recovered | Annualized Value | Payback |
|----------|-------------------|----------------|------------------|---------|
| Breakeven | ~10% | ~45 FTEs | ~$7.4M | ~12 months |
| Conservative (sub-breakeven) | 5% | ~23 FTEs | ~$3.7M | ~24 months |
| In-program (1 EE/team) | 11–18% | ~50–81 FTEs | $8.2–13.4M | 7–11 months |
| Post-program (6–12 mo) | 20–30% | ~90–135 FTEs | $14.9–22.3M | 4–6 months |

**3-year cumulative value:**

| Scenario | Annual Gain | 3-Year Cumulative | 3-Year Multiple on Investment |
|----------|-------------|-------------------|-------------------------------|
| Breakeven (~10%) | ~$7.4M | ~$22.3M | 3.1x |
| In-program (11–18%) | $8.2–13.4M | $24.5–40.1M | 3.4–5.5x |
| Post-program (20–30%) | $14.9–22.3M | $44.6–66.8M | 6.1–9.2x |

**Key framing principles for the AM:**
- **Capacity recovery, not headcount reduction.** The client's goal is to build more, ship faster, and carry less maintenance burden with the same team. The productivity lift is measured as features shipped to production at quality.
- **The EE ratio drives outcomes — present it as a dial, not a wall.** 1:24 yields 3–7%; 1:8 yields 11–18%. The ratio is the single biggest lever on both cost and outcomes. The client may choose a different ratio for budget reasons — that's a legitimate choice. The AM's job is to make sure the client understands the outcome tradeoff and goes in eyes-open. Don't refuse a lower ratio; present the ratio table and document the decision.
- **Post-program compounding is upside, not the thesis.** The in-program lift (11–18% at 1:8) already exceeds breakeven (~10%). Post-program compounding (20–30%) is additional, not required for the investment to make sense.
- **The MVP produces the client's own data.** Don't promise benchmarks from other engagements. The MVP gives the executive sponsor observed outcomes on their own teams, which is far more persuasive than any projection.

**When to use this framing:** Only for enterprise-scale engagements where the client needs to justify a significant investment to a finance organization or steering committee. For small engagements, the per-person cost (~$9K–$19K) is self-evidently reasonable and the DLP Completion outcomes are sufficient. You don't need a capacity recovery model for 12 people.

---

## SOW Structure: What to Include

### Standard SOW Components for a DLP Engagement

1. **Engagement duration and schedule**
   - Stage 3: 12 weeks from Week 1 start date
   - Stage 4: 16 weeks from Week 1 start date
   - Session schedule: sessions occur approximately every 2 weeks (Stage 3) or 3 weeks (Stage 4)
   - Note: exact session dates will be confirmed at kickoff

2. **Roles and staffing**
   - Embedded Engineer: named individual (or "to be assigned from Improving's certified EE pool"), 40 hrs/week
   - Trainer: named individual, session delivery + (Stage 4) weekly office hours
   - Executive Coach: named individual if dedicated EC, or "Trainer will serve as EC" for 1–2 cohort engagements
   - Account Manager: named individual

3. **Deliverables**
   - Stage 3: Participants' committed artifacts (skills, evaluation scripts, adversarial agents) in the client's codebase; Program Completion Rubric; AI Adoption Maturity Assessment results (Week 1, 7, 12); handoff document
   - Stage 4: Custom harness committed to the client's repo; five Stage 4 certification artifacts; team handoff document; 30-day check-in

4. **Client responsibilities**
   - Identify participating teams and participants before Week 1
   - Ensure managers have been briefed that DLP is protected time
   - For Stage 4: identify IT Liaison before engagement begins; provision API keys and infrastructure before Session 2
   - For Stage 3: provision API keys before Session 4 (Week 7)
   - Provide access to the client's codebase, development environments, and tools
   - If virtual delivery: communicate cameras-on expectation to participants

5. **Exclusions (what the DLP is NOT)**
   - The DLP is not a training event — it is a behavior change engagement. The SOW should explicitly state that success is measured by DLP Completion (behavior change), not session attendance.
   - The DLP does not include building the client's production AI features. The EE coaches participants to build their own skills; the EE does not write the client's production code for them.
   - The DLP does not include API usage costs (Stage 4). The client pays for model API calls directly.
   - The DLP does not include infrastructure setup (Stage 4). The client's IT Liaison provisions and owns infrastructure.

6. **Assumptions**
   - Participants have prerequisite skills (Stage 3: basic prompting; Stage 4: DLP Completion + documented Stage 3 workflow)
   - The client provides a named executive sponsor who will participate in touchpoints
   - Session dates will be scheduled at kickoff and protected by the client
   - Participants attend all sessions (the all-roles-present principle)
   - For virtual delivery: cameras-on expectation has been communicated

7. **Change management**
   - Scope changes (additional cohorts, additional sessions, extended EE time) are billed as change orders
   - Timeline changes (delays, pauses) are handled as amendments — the EE's availability is not guaranteed beyond the original end date without an amendment

8. **Pricing and payment terms**
   - Per the pricing framework above
   - Payment schedule: typically monthly billing based on actual hours, or milestone-based (Week 1 kickoff, Week 6 midpoint, Week 12/16 completion)
   - Expenses billed separately (travel, lodging for in-person sessions)

9. **Enterprise-scale components (include only for 5+ cohort engagements)**
   - If multi-wave: wave structure (MVP → Wave 1 → Wave 2...), 4-week pre-wave planning period per wave, series delivery (not parallel)
   - If governance infrastructure: spend dashboards, adoption tracking, acceptance rate monitoring, agent promotion board, skills repository structure — operational before Wave 1 cohorts go live
   - If DevOps track: 2 DevOps Specialists, 12–24 weeks, phased delivery (assessment → build → extend → handoff), deliverables per the engagement scope
   - If compliance track: 2 BI/Data Engineers, 16 weeks, phased delivery (discovery → build → integrate → operationalize), deliverables per the engagement scope
   - If phase-gated pricing: MVP priced independently, subsequent waves contingent on prior wave outcomes, go/no-go decision points
   - Hard team size limits (if enterprise-scale): max 8 people per team, max 3 teams per cohort (24 people), max 10–12 cohorts per wave, waves in series (not parallel)
   - Agent repository: shared library of promoted agents, governed by Enterprise Coach and agent promotion board, accessible to all teams after Wave 1

---

## Common SOW Pitfalls

### Pitfall: "Just the sessions" pricing

**Problem:** The client asks to price only the training sessions, without the EE. "Can we just do the 6 sessions and see how it goes?"

**Why this fails:** The sessions introduce concepts and skills, but the EE is what makes them stick. Without the EE, participants attend sessions, are inspired, and then go back to their normal workflow with no coaching. DLP Completion rates without an EE are near zero. The sessions without the EE are a workshop, not a DLP.

**Response:** *"The DLP is a 12-week behavior change engagement, not a training event. The sessions introduce the discipline; the Embedded Engineer is what makes it stick. We've found that without the EE, session attendance doesn't translate to behavior change — which is the whole point. The sessions and the EE are a package. We can talk about reducing the EE's hours if budget is a concern, but we can't remove the EE entirely without fundamentally changing what we're delivering."*

### Pitfall: EE ratio reduced to cut cost without understanding the tradeoff

**Problem:** The client wants to reduce the EE-to-participant ratio to save cost. "Do we really need one EE per team? Can one EE cover 3 teams?"

**Why this matters:** The ratio is a legitimate cost dial — but it's also the biggest outcome dial. The client may be making a budget decision without understanding what they're trading away. The risk isn't that they choose a lower ratio; the risk is that they choose it uninformed.

**Response:** *"That's absolutely a choice we can make together. The ratio is the biggest dial on both cost and outcomes. At 1:8 — one EE per team of 8 — we see 11–18% velocity improvement during the program. At 1:24 — one EE across three teams — that drops to 3–7%. Both are legitimate configurations. What I want to make sure is that we go in eyes-open about what the lower ratio means for outcomes. Some clients choose a middle ratio — 1:16, one EE across two teams — and extend the engagement a few weeks to partially recover the coaching depth. What's driving the ratio question for you — is it total budget, EE availability, or something else?"*

### Pitfall: No executive sponsor identified

**Problem:** The client wants to start the DLP but hasn't named an executive sponsor. "We'll figure out the sponsorship thing as we go."

**Why this fails:** Without an executive sponsor, there's no one to protect the program when managers pull participants off DLP time. There's no one to receive the completion report. There's no one to make the "what comes after" decision. The program drifts.

**Response:** *"We need a named executive sponsor before we start. This person doesn't need to be technical — they need to be someone who can protect the program's time and make decisions about what comes after. Without that, we see the program get deprioritized within the first 4 weeks as managers pull people onto sprint work. Can we identify that person before we schedule kickoff?"*

### Pitfall: No API key plan (Stage 3 Session 4+ and Stage 4)

**Problem:** The SOW doesn't mention API keys, and the client's security team blocks API access mid-engagement. Sessions 4–6 (Stage 3) or the entire Stage 4 program can't run.

**Response:** *"The DLP curriculum uses Python evaluation scripts with LLM judges starting in Session 4. These require API access to a model provider. This is a client responsibility — your security team needs to approve API access before Week 7. We've found that corporate security teams typically approve custom Python with API access without friction, but the approval process can take 2–4 weeks. Let's start that conversation now so it doesn't block us mid-program."*

### Pitfall: Over-engineering a small engagement

**Problem:** The AM sells governance dashboards, DevOps tracks, and compliance workstreams to a 2-cohort engagement. The client is paying for enterprise-scale infrastructure they don't need.

**Why this fails:** Enterprise-scale components add cost and complexity without value when the engagement is small. A 12-person engagement doesn't need a multi-tool spend dashboard or an agent promotion board. The standard DLP Completion Rubric and AI Adoption Maturity Assessment are sufficient measurement for small engagements.

**Response:** None needed — don't do this. The enterprise-scale components in this guide are clearly marked as applying to 5+ cohort engagements. If you're pricing a 2-cohort engagement, use the standard pricing framework, the standard SOW structure, and the standard measurement tools. Reserve governance infrastructure, DevOps tracks, and compliance workstreams for enterprise clients who need them. Selling unnecessary complexity damages trust.

### Pitfall: Under-scoping an enterprise engagement

**Problem:** The AM prices a 10-cohort wave the same way they price a single cohort — just multiplied by 10. No Enterprise Coach, no governance infrastructure, no pre-wave planning.

**Why this fails:** At 10 cohorts, the program is a transformation, not a training event. Without an Enterprise Coach, there's no one designing cohort composition, driving OCM, or establishing governance. Without governance infrastructure, there's no way to measure outcomes at scale or prevent cost escalation. The program runs but the outcomes are invisible and unmanaged.

**Response:** *"At this scale, the program is a multi-wave transformation, not a series of training events. We need an Enterprise Coach who designs the wave, drives organizational change management, and establishes the governance infrastructure that makes scaling measurable and safe. Without that, we're training 240 people with no way to measure whether it's working or prevent the common failure modes — cost escalation, cognitive surrender, compliance exposure. The Enterprise Coach and governance infrastructure are what turn training into measurable operational proof."*

---

## Quick Pricing Reference

### Stage 3 DLP — Single Cohort (at example rates)

| Component | Hours | Rate | Cost |
|-----------|-------|------|------|
| EE (12 weeks, 40 hrs/week) | 480 | $200/hr | $96,000 |
| EE pre-engagement prep (1 week) | 40 | $200/hr | $8,000 |
| Trainer (6 sessions) | 6 sessions | $3,000/session | $18,000 |
| Trainer EC duties (1–2 hrs/week × 12) | 18 | $500/hr | $9,000 |
| **Total (Trainer-as-EC, 1 cohort)** | | | **$131,000** |

Note: The $131K total includes EE prep week ($8K) which the $114K comparison in the Stage 4 proposal did not. Both calculations are consistent — the difference is whether prep time is broken out separately.

### Stage 3 DLP — Additional Cohort (marginal cost)

| Component | Hours | Rate | Cost |
|-----------|-------|------|------|
| EE (second cohort, 12 weeks) | 480 | $200/hr | $96,000 |
| Trainer (6 sessions, second cohort) | 6 sessions | $3,000/session | $18,000 |
| Trainer EC duties (shared across cohorts) | — | — | $0 (already covered) |
| **Marginal cost per additional cohort** | | | **$114,000** |

### Stage 4 DLP — Single Team (at example rates)

| Component | Hours | Rate | Cost |
|-----------|-------|------|------|
| EE (16 weeks, 40 hrs/week) | 640 | $200/hr | $128,000 |
| EE pre-engagement prep (1 week) | 40 | $200/hr | $8,000 |
| Trainer (5 sessions) | 5 sessions | $3,000/session | $15,000 |
| Trainer office hours (1 hr/week × 16) | 16 | $500/hr | $8,000 |
| **Total (Trainer-as-EC, 1 team)** | | | **$159,000** |

### Enterprise Wave — Per Wave (at example rates, 10 cohorts, 1:8 EE ratio)

| Component | Calculation | Cost |
|-----------|-------------|------|
| Enterprise Coach (16 weeks, 40 hrs/week) | 640 hrs × $250/hr | $160,000 |
| EEs (30 EEs × 12 weeks × 40 hrs/week) | 14,400 hrs × $200/hr | $2,880,000 |
| Trainers (2 trainers × 6 sessions) | 12 sessions × $3,000 | $36,000 |
| Governance infrastructure (template + build) | Per engagement | $50,000–$150,000 |
| **DLP subtotal per wave** | | **~$3.13M–$3.23M** |
| DevOps Acceleration Track (optional) | 2 specialists × 12–24 weeks | ~$192,000–$384,000 |
| Data & Compliance Enablement (optional) | 2 engineers × 16 weeks | ~$256,000 |
| **Total with all workstreams** | | **~$3.6M–$3.9M** |

Note: Enterprise wave pricing is highly variable. The example above uses a 1:8 EE ratio (one EE per team of 8). A 1:24 ratio would reduce the EE cost by ~67% but also reduce expected outcomes from 11–18% to 3–7% velocity improvement. The EE ratio is the single biggest cost and outcome lever — the AM should present multiple ratio options with their outcome tradeoffs.

---

*This document is a pricing and SOW reference for Account Managers. It should be used alongside the AM-EC-Executive-Guidance.md (delivery guidance) when constructing a DLP proposal and SOW. Pricing examples use illustrative bill rates — actual rates vary by engagement, region, and client relationship.*