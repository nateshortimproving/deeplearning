# Account Manager / Executive Coach Guidance Sheet — Executive Relationship Management
*Deep Learning Program (DLP) — Account Manager / Executive Coach Reference*
*Version: August 2026*

---

## Who This Document Is For

This document covers two distinct roles that share the same executive-facing responsibilities on a DLP engagement. Which role applies depends on how the engagement was booked and the engagement's scale.

### The Two Roles

**Account Manager (AM)** — Generally a sales professional who has been involved from the beginning of the pursuit. The AM owns the client relationship, the contract, and the commercial terms. The AM is typically non-technical — they understand the DLP's value proposition and positioning, but they are not the person who coaches delivery or handles technical escalations. The AM's primary job on a DLP engagement is relationship management, scope/contract adherence, and being the client's commercial point of contact.

**Executive Coach (EC)** — Generally someone with a degree of technical capability plus management and coaching experience, from the Delivery side of the organization. The EC owns the executive sponsor relationship during delivery, handles delivery-level escalations, monitors engagement health, and coaches the Embedded Engineer and Trainer through organizational friction. The EC is the person who can have a credible technical conversation with the executive sponsor about what's working and what isn't.

### When an Executive Coach Is Required

Not every engagement needs a dedicated Executive Coach. The requirement scales with the number of cohorts running concurrently on the engagement:

| Cohorts | Executive Coach Requirement |
|---------|-----------------------------|
| **1–2 cohorts** | The **Trainer serves as the EC**. Plan for additional time outside the classroom (approximately 1–2 hours/week) for the Trainer to handle executive sponsor touchpoints, escalation reception, and engagement health monitoring. The Trainer is already close enough to the delivery to do this effectively. |
| **3–4 cohorts** | Can be handled by the **Trainer or EE wearing both hats**, but this is the upper limit of what a dual-role person can manage. If the Trainer is already delivering sessions for multiple cohorts, adding EC duties across all of them may be too much — monitor workload. |
| **5+ cohorts** | **Dedicated Executive Coach required.** At this scale, no one wearing another hat can give the EC role the attention it needs. The EC is a separate person who owns engagement health across all cohorts, coordinates between Trainers and EEs, and is the single executive sponsor point of contact. |

**Strong recommendation:** For anything above 2 cohorts, strongly recommend a dedicated Executive Coach. The dual-role approach works for small engagements but creates a single point of failure — if the Trainer/EE is sick or overloaded, both the delivery and the executive relationship suffer simultaneously.

### The Account Manager's Role Regardless of EC

The Account Manager is involved in every engagement regardless of size — they own the commercial relationship. But the AM's involvement during delivery is lighter than the EC's. The AM:
- Owns the contract, scope changes, and commercial terms
- Is the escalation point for anything that affects the SOW or billing
- Participates in the Week 12 completion meeting
- Owns the "what comes after" conversation (continued engagement, expansion, etc.)

The AM does **not** own:
- Day-to-day engagement health monitoring (that's the EC, or the Trainer/EE in a dual-role engagement)
- Executive sponsor touchpoints during delivery (that's the EC)
- Delivery-level escalations about manager friction or participant struggles (that's the EC)

When an AM is involved but no dedicated EC is assigned (1–2 cohort engagements), the Trainer handling EC duties should still loop the AM in for anything that touches scope, contract, or commercial terms. The AM-Touchpoint-5 (Week 12 Completion) is always a joint AM + EC (or Trainer-as-EC) meeting.

### What This Document Covers

The touchpoint cadence, escalation handling, and engagement health guidance in this document apply to whoever is serving as the EC — whether that's a dedicated EC, a Trainer wearing both hats, or an EE wearing both hats. The AM-specific guidance (pricing, SOW structure, what to include) is in a separate document: see `Account Manager or Executive Coach/AM-DLP-Pricing-and-SOW-Guide.md`.

---

## API Key Logistics

The DLP v2 curriculum uses Python evaluation scripts with LLM judges (Session 4), adversarial agents (Session 5), and custom harness demos (Session 6). All of these require API keys for model access. The session content assumes API keys are available — it does not address key provisioning.

**You are responsible for ensuring API keys are provisioned and distributed** to Trainers and Embedded Engineers before Session 4 (Week 7). Confirm with the client or internal provisioning that keys are available. Communicate key availability to the Trainer and Embedded Engineer.

---

## Virtual Training: Cameras-On Expectation

The DLP is designed to work in-person or virtually. We strongly prefer in-person delivery when logistics allow, but we recognize that virtual delivery will often be the client's preference, particularly for internationally distributed teams where travel is impractical or cost-prohibitive.

**When virtual delivery is chosen, we have a strong expectation: cameras on for all training sessions.**

This is not a preference or a nice-to-have. Classroom engagement goes up measurably when participants are visible to the trainer and to each other. The DLP sessions are interactive — labs, breakout rooms, peer discussions, capstone showcases. Cameras-off transforms these into one-way lectures where the trainer is talking to a grid of black squares, unable to read the room, unable to see who is confused, who has checked out, and who is multitasking. The energy drops, participation drops, and the program's outcomes suffer.

### Setting This Expectation

**This is your conversation to have, not the Trainer's.** The Trainer can reinforce it on the day, but the expectation should be set before the program begins — during the Pre-Engagement Kickoff (Touchpoint 1) or earlier in the scoping conversation.

**Suggested language for the executive sponsor:**

> *"Our training sessions are highly interactive — labs, breakout rooms, peer discussions, artifact showcases. For these to work, we need cameras on. This isn't about surveillance; it's about engagement. When the trainer can see the room, they can read confusion, adjust pace, and call on people at the right moment. When participants can see each other, breakout discussions have real energy instead of feeling like a conference call. We've seen the difference repeatedly, and the outcomes are materially better with cameras on."*

**Ask the executive sponsor to communicate this expectation to participants before Session 1.** A message from the executive sponsor carries more weight than one from the Trainer or Account Manager. If the sponsor models the behavior (cameras on in their own meetings), adoption is faster.

### Coaching Tips for Common Objections

**Objection: "Some participants are in open offices or shared spaces where they can't have cameras on."**

> *"We understand that not every environment is camera-friendly. For participants in shared spaces, we recommend booking a small meeting room or quiet space for the 4-hour session — the same way they would if they were in a client call. If that's truly impossible for some individuals, we can accommodate exceptions, but the default should be cameras on. Can we identify who the exceptions are in advance so the trainer knows?"*

**Objection: "Our team is distributed across time zones and some will be joining very early or very late — cameras feel invasive in those conditions."**

> *"That's a fair concern for people joining outside their normal working hours. For those participants, we suggest a middle ground: camera on during introductions, breakout rooms, and capstone presentations; camera optional during lecture blocks. This preserves the engagement moments without requiring 4 hours of on-camera time at 6 AM. The key moments — where the trainer needs to read the room and where peer interaction happens — still get the benefit."*

**Objection: "Our culture doesn't typically use cameras in internal meetings."**

> *"That's exactly why we're raising it now, before the program starts. The DLP sessions aren't typical internal meetings — they're interactive workshops. We're asking the team to try a different norm for these sessions specifically. In our experience, once a team does it for one session, the resistance drops dramatically because the engagement improvement is obvious. Would you be willing to set this as an expectation for the DLP sessions as a pilot, and the team can decide whether to extend it to other meetings afterward?"*

### When Cameras-Off Persists Despite the Expectation

If the expectation has been set and participants still show up cameras-off:
- The Trainer should not shame individuals or make it a confrontation. Instead, the Trainer should note at the start of the session: *"We're going to be doing breakout rooms and peer discussions today — please plan to have cameras on for those blocks at minimum."*
- If the pattern persists across multiple sessions and is materially affecting engagement, escalate to the Account Manager / Executive Coach. This is a conversation for the executive sponsor, not the Trainer: *"We're seeing cameras-off across most of the cohort, and it's affecting the quality of breakout discussions. Can you reinforce the expectation?"*
- Document the impact: note specific sessions where cameras-off led to poor breakout participation, confused participants who didn't ask questions, or capstone presentations with no audience engagement. Concrete examples help the executive sponsor understand this isn't a stylistic preference — it's an outcomes issue.

---

## What You Own vs. What Others Own

| You Own | Embedded Engineer Owns | Trainer Owns |
|---------|---------|--------------|
| Executive sponsor relationship | Day-to-day participant coaching | Training session delivery |
| Engagement-level risk monitoring | Manager-level dynamics (first pass) | Embedded Engineer weekly touchpoints (30 min/week) |
| Escalation reception from Embedded Engineer | Participant DLP Completion progress | Curriculum and session content |
| Client contract and scope | Participant AI Adoption Maturity Assessment completion | Assessment co-completion at Week 12 |
| API key provisioning | Weekly touchpoints with Trainer | Program design feedback to Improving |
| "What comes after" conversation | | |

**Critical boundary:** The Embedded Engineer does not manage executive stakeholders. If a participant's manager is creating friction or resistance, the Embedded Engineer will try to address it peer-to-peer first, but escalation comes to you. You decide whether to handle it at your level or involve the executive sponsor.

---

## Enterprise-Scale Engagements

The guidance above covers a standard DLP engagement: one or a few cohorts running simultaneously. For large enterprise clients — where the DLP is being delivered to hundreds of developers across many cohorts — the engagement structure changes significantly. The following concepts apply primarily to engagements of **5+ cohorts** (typically 100+ participants) and are not required for small engagements.

If you are running 1–4 cohorts, the standard guidance in this document is sufficient. The enterprise-scale sections below are for engagements where the program is a multi-wave transformation, not a single training event.

### Key Terminology

| Term | Definition |
|------|------------|
| **Track** | A group of cohorts whose participants attend the same training session. When the EE-to-participant ratio is low (e.g., 1:8 — one EE per team of 8), a single cohort of 24 people needs 3 EEs. But all 24 can attend the same training session. The Track is that grouping — multiple teams sharing one Trainer delivery. A Track typically serves 20–30 people. As the EE ratio drops, Tracks become necessary because a single cohort is too small to justify a Trainer alone. |
| **Wave** | One full program execution: multiple cohorts running the 12-week DLP simultaneously, preceded by a 4-week planning period. A wave typically contains 10–12 cohorts. Waves run in series (not parallel) to control quality and let patterns compound before scaling. |
| **MVP (Phase 0)** | A single-cohort pilot before committing to a full wave. Uses the same EE, same EC setup, same workshop cadence, and produces the same governance outputs — it is not a watered-down version. It validates the approach in the client's specific context and produces the executive ROI narrative that unlocks the broader engagement. |
| **Enterprise Coach** | At enterprise scale (5+ cohorts), the EC role becomes a full-time position — this is the Enterprise Coach. The Enterprise Coach starts 4 weeks before each wave to design cohort composition, sequence waves against delivery commitments, drive OCM (organizational change management), establish governance infrastructure, and track governance maturity across all active cohorts. This is a significantly expanded role compared to the standard EC on a 1–2 cohort engagement. |
| **Agent Repository** | Shared library of promoted agents (task agents and workflow agents) accessible to all teams after Wave 1. Populated by EEs and governed by the Enterprise Coach through an agent promotion board. |

### When Enterprise-Scale Concepts Apply

| Engagement Size | Structure | EC Role |
|-----------------|-----------|---------|
| **1–2 cohorts** (8–48 people) | Single engagement, no waves | Trainer serves as EC (1–2 hrs/week) |
| **3–4 cohorts** (24–96 people) | Single engagement, no waves | Trainer or EE in dual role (2–3 hrs/week) |
| **5+ cohorts** (100+ people) | **Multi-wave program** (MVP → Wave 1 → Wave 2...) | **Dedicated Enterprise Coach** — full-time, starts 4 weeks before each wave |

The structural concepts below (waves, tracks, governance, compliance, DevOps) are **not required** for small engagements. They exist because at enterprise scale, the DLP transforms from a training engagement into an operational transformation. Do not over-complicate a 2-cohort engagement by importing wave structure or governance infrastructure that the client doesn't need.

### Pre-Wave Planning (Enterprise Coach, 4 weeks before each wave)

For enterprise-scale engagements, the Enterprise Coach's engagement starts **4 weeks before** the first cohort's Day 1. This pre-wave period is not optional — it is when the wave is designed. The standard EC touchpoint cadence (Touchpoints 1–5) still applies, but the pre-wave planning adds a significant block of work before the 12-week execution begins.

**Pre-wave planning responsibilities:**
- Design cohort composition: map teams to cohorts by tech stack and business priority. Teams within a cohort share languages and tools (e.g., C#/.NET, Java, React/Node.js) so EEs are not context-switching mid-wave.
- Sequence waves against delivery commitments: ensure the wave doesn't endanger critical client programs. The Enterprise Coach works with the executive sponsor to identify which teams can participate without jeopardizing sprint commitments.
- Establish governance infrastructure: skills repository structure, agent promotion process, cost-to-capacity dashboards. This should be operational before Wave 1 cohorts go live — not built after the fact.
- Drive OCM (Organizational Change Management): address identity-based resistance. Senior developers are the highest long-term multipliers but the slowest early adopters. They have spent years developing craft, and AI feels like it cheapens it. Getting them to change behavior requires a different conversation than the one that works for junior developers.
- Plan the passive-to-active compliance transition: if the client operates under regulatory regimes (PCI, SOX, GDPR), the Enterprise Coach coordinates the compliance infrastructure build (see below).

### Governance Infrastructure

At enterprise scale, governance is the mechanism that makes scaling safe and that turns training into measurable operational proof. Without it, the program is "we trained people" — with it, the program is "here's the dashboard showing velocity improvement, acceptance rates, spend-to-output ratios, and compliance agents running in the SDLC."

**Governance components (for enterprise-scale engagements):**
- **Multi-tool spend dashboard** — monitors daily spend per user across AI tools (Copilot, Claude, etc.), weekend usage anomalies, spend-to-output ratios. Prevents cost escalation: organizations commonly spend 3–4x the necessary token cost in the first 90 days without monitoring.
- **Adoption-to-operate signal tracking** — distinguishes teams in the adoption stage (driving usage) from teams in the operate stage (driving output quality). The dashboard evolves as teams mature.
- **Acceptance rate and reliance rate monitoring** — flags over-reliance (>90% acceptance = cognitive surrender) and under-reliance (<60% acceptance = not trusting the tool). Both extremes require coaching, not technology fixes. The current observed accuracy rate for AI code generation is ~87%, meaning 100% acceptance introduces ~13% slop into the codebase.
- **Agent promotion board** — bi-weekly review with the Enterprise Coach and EEs to evaluate team-built agents for promotion to the shared repository. Promoted agents are available to all teams after the wave.
- **Skills repository structure** — globally true agents (compliance, security, audit), domain-specific agents (by tech stack), and business-specific agents (client's systems). This is the asset that compounds across waves.

**When to include governance:** Governance infrastructure should be operational before Wave 1 cohorts go live. It is built during the pre-wave planning period, overlapping with the MVP. Governance templates can be adapted from infrastructure used on prior engagements (e.g., Fabric/Power BI dashboards).

**When NOT to include governance:** For 1–2 cohort engagements, governance infrastructure is overkill. The standard DLP Completion Rubric and AI Adoption Maturity Assessment are sufficient measurement. Don't sell governance dashboards to a client who needs one cohort of 12 people.

### Optional Workstreams for Enterprise Clients

Large enterprise clients — particularly those under regulatory regimes or with sub-mature DevOps — may need workstreams that run alongside the DLP but are not part of the DLP curriculum itself. These are separate SOW components, separately staffed, and separately priced (see the AM Pricing Guide for details).

**DevOps Acceleration Track (optional, recommended for teams with sub-mature CI/CD):**
Teams without robust CI/CD, automated testing, and infrastructure-as-code carry "verification debt" — AI generates output faster than humans can verify it. This caps the productivity gain achievable through the DLP alone. The DevOps track provides practitioners (not trainers) who build pipeline infrastructure so AI productivity gains can actually ship.

- CI/CD pipeline deployment per team
- Automated testing framework (unit, integration, regression)
- AI acceptance rate instrumentation
- Agent CI/CD integration (tested agents promoted through the repository are automatically evaluated on deploy)
- Token cost guardrails and spending controls

**Data & Compliance Enablement (for clients under PCI, SOX, GDPR):**
Passive compliance (end-of-cycle audits) does not catch AI-generated code that introduces scope creep, credential mishandling, or audit trail gaps. This workstream makes compliance active and continuous.

- PCI-active agents in the SDLC (run on every commit touching PCI-scope code, flag issues inline)
- SOX audit trail generation (AI-assisted code changes carry traceable attribution)
- Data classification layer (ensures PII and sensitive data is never passed to models without controls)
- Governance dashboards (real-time visibility into adoption, spend, acceptance rates, code quality)
- Audit-ready artifact generation (automatically produces evidence records for AI-assisted PRs)
- Agent policy infrastructure (enforces rules on which tools can access which data environments)

**When to include these workstreams:** Only for enterprise clients who need them. A 2-cohort engagement for a company with mature CI/CD and no regulatory concerns does not need either workstream. The AM should assess the client's DevOps maturity and compliance requirements during scoping and include these only when they address a real bottleneck.

### Measuring ROI: Capacity Recovery Framing

For enterprise-scale engagements, the ROI conversation is critical to justify the program cost. The framing is **FTE capacity recovery** — not headcount reduction, but teams completing more work in the same time. The freed capacity is directed elsewhere without adding headcount.

**The ROI calculation:**
1. Developer population in scope (e.g., 450 FTE)
2. Estimated fully loaded cost per developer (e.g., $165K/year)
3. Total annual developer investment (e.g., $74.3M)
4. Breakeven productivity improvement = program investment / annual developer investment (e.g., $7.28M / $74.3M = ~9.8%)
5. Expected productivity lift based on EE-to-participant ratio

**The EE ratio directly drives outcomes — but it's a dial, not a wall:**
- 1:8 ratio (one EE per team) → 11–18% in-program velocity improvement (our preference — best observed outcomes)
- 1:16 ratio (one EE across 2 teams) → ~7–12% in-program (estimated — middle ground)
- 1:24 ratio (one EE across 3 teams) → 3–7% in-program (budget-constrained — still viable, lower outcomes)
- Post-program compounding (6–12 months) → 20–30% productivity gain (observed at 1:8; less data at other ratios)

The ratio is a legitimate cost dial. The client may choose a different ratio for budget reasons — that's a valid choice. The EC's job is to make sure the client understands the outcome tradeoff and goes in eyes-open. Never refuse a lower ratio; present the data and document the decision.

**The measurement principle:** Measuring AI productivity in lines of code is a trap. The relevant measure is features shipped to production at quality — sprint output that actually ships, without regressions.

**When to use this framing:** Only for enterprise-scale engagements where the client needs to justify a significant investment to a finance organization or steering committee. For small engagements, the ROI is self-evident from the per-person cost and the DLP Completion outcomes — you don't need a capacity recovery model for 12 people.

### MVP Before Full Wave

For enterprise-scale engagements, strongly recommend a **single-cohort MVP** before committing to a full wave. The MVP:
- Uses the same EE, same EC setup, same workshop cadence, same governance outputs — it is not a watered-down version
- Validates the approach in the client's specific context
- Produces the executive ROI narrative with the client's own data (not benchmarks from other engagements)
- Gives the executive sponsor concrete evidence to justify the full wave internally

**MVP success metrics to align on before kickoff:**
- Velocity change (sprint story points or cycle time, measured Week 1 vs. Week 12)
- AI acceptance rate (target: ~85–90%, flagging over-reliance and under-reliance)
- Agent quality scores (bug rate, test failure rate compared to pre-program baseline)
- Team-reported confidence index (subjective, tracked at Weeks 4, 8, and 12)

The MVP is the proving ground. It turns a proposal's promised outcomes into observed outcomes on the client's own teams, with their own tools, in their own codebase. That is the narrative that unlocks the broader engagement.

---

## Executive Sponsor Touchpoint Cadence

Five touchpoints over 12 weeks. Each has a specific purpose. This is not a "check in and see how it's going" schedule — each touchpoint has a defined agenda.

---

### Touchpoint 1 — Pre-Engagement Kickoff
**Timing:** Before Week 1 (ideally 1–2 weeks before the program starts)
**Format:** 30–45 min. Video or in-person if possible. You + executive sponsor. Embedded Engineer may be introduced but does not need to attend.
**Goal:** Confirm shared understanding of what the program is and what success looks like.

**Agenda:**
1. Confirm the executive sponsor understands the DLP model — this is not a training event, it's a 12-week behavior change engagement. The Embedded Engineer is embedded. Participants will be doing real work differently, not just attending sessions.
2. Confirm scope: Which teams? Which participants? (Remember: Embedded Engineer is embedded with actual cross-functional teams, not role groups.)
3. Confirm what the executive sponsor has communicated to participants and managers. Ask directly: *"Have their managers been told that real work time will be redirected toward this program? Do they support it?"*
4. Establish DLP Completion as the outcome target. Walk through the four tangible outcomes briefly (iterative refinement of skills and adversarial agents, deliberate use of Python evaluation frameworks, at least one workflow step at 95%+ accuracy, and changed human behavior). Ask: *"At Week 12, when I tell you X% of participants meet all four criteria, will that feel like success to you?"*
5. Set expectations for your cadence of contact. Tell them when the next touchpoint will be and what will prompt you to reach out earlier.
6. Confirm escalation protocol: *"If something comes up mid-engagement that needs your attention, I will call you directly. That won't be a signal that the program is failing — it's how we protect it."*
7. If delivery is virtual, set the cameras-on expectation (see the "Virtual Training: Cameras-On Expectation" section above). Ask the executive sponsor to communicate this to participants before Session 1.

**What to listen for:**
- Ambiguity about which teams or participants are included
- Any hint that managers haven't been prepared
- "Success" definitions that don't match DLP Completion (e.g., "they'll be using Copilot more" is not DLP Completion)

---

### Touchpoint 2 — Week 3–4 Check-In
**Timing:** Week 3 or 4 (after Session 1 has run, Embedded Engineer has been embedded for 2–3 weeks)
**Format:** 20–30 min. Phone or video.
**Goal:** Confirm the program has launched cleanly and surface any early friction.

**Agenda:**
1. Report that Session 1 is complete and what participants worked on (Prompt/Harness/Model framework + SDLC skeleton skills introduced + building out the `epics-and-stories` skill). Keep it concrete — describe the artifact participants produced, not just that training happened.
2. Confirm the Embedded Engineer is embedded and report early participant engagement. Are people showing up to Embedded Engineer sessions? Bringing real work?
3. Surface any early signals to discuss. This is when early manager friction tends to appear.
4. Ask: *"Have you heard anything from the teams or their managers since we kicked off?"* Often the executive sponsor hears things through the org that the Embedded Engineer doesn't.
5. Preview what's coming: Session 2 in Week 3 (The Development Loop — building out `plan-story` and `implement-story`), Loop 1 completing at Week 6.

**What to listen for:**
- Manager resistance coming through back channels
- Any changes to team scope or staffing since kickoff
- Executive sponsor distancing (fewer responses, less interest) — catch this early

---

### Touchpoint 3 — Week 6 Midpoint Review
**Timing:** Week 6 (Loop 1 complete, midpoint AI Adoption Maturity Assessments just completed)
**Format:** 45 min. This one warrants a real meeting.
**Goal:** Present a substantive progress report. This is the first real data point.

**Agenda:**
1. Present midpoint AI Adoption Maturity Assessment results. The assessment has 7 dimensions; DLP Completion is indicated by dimensions 1–4 scoring consistently at 3.0+ averages. Don't just say "participants are progressing" — share where they rate themselves and where the Embedded Engineer sees gaps.
2. Note specific artifacts participants have produced. Real examples matter to executive sponsors. *"Three participants on the CRM team have committed skills they're iterating against real stories."*
3. Discuss any participants who are struggling and what's being done. You don't have to name individuals, but you shouldn't hide that variance exists.
4. Discuss Loop 2 — the program shifts from building the SDLC skeleton pipeline to deepening discipline with new tooling. Session 4 in Week 7 covers Python evaluation scripts with LLM judges. Explain why this matters: without evaluation, you don't know if you're improving skills or just changing them.
5. If any Embedded Engineer escalations have been received and addressed, brief the executive sponsor (appropriately, without throwing managers under the bus).
6. Ask: *"Based on what you're seeing from your side, are there team dynamics or organizational pressures we should know about for the second half?"*

**What to bring:**
- Midpoint AI Adoption Maturity Assessment summary (aggregated, not individual)
- Embedded Engineer's narrative of Loop 1 — qualitative, not just scores
- 1–2 specific participant examples (with names if appropriate)

---

### Touchpoint 4 — Week 9 Progress Review
**Timing:** Week 9 (Loop 2 underway, Session 5 about to run or just completed)
**Format:** 20–30 min. Can be lighter than the Week 6 meeting if progress is on track.
**Goal:** Confirm trajectory toward Week 12 completion and prepare for the completion conversation.

**Agenda:**
1. Report on Session 4 (Python Evaluations + LLM Judges) and Session 5 (Model Invocation + Adversarial Agents) — what participants are producing in Loop 2.
2. Identify who is on track for DLP Completion (all four behavioral criteria met) and who is at risk. Be honest.
3. Ask: *"Are there participants you want me to make sure we're paying attention to?"* Executive sponsors sometimes have organizational reasons to care about specific people.
4. Preview the Week 12 completion conversation. What will you present? What decisions do you want them ready to make?
5. Float the "what comes after" question early: *"At Week 12 we'll talk about next steps. I want to start warming that up — are there conversations happening internally about where AI goes after this?"*

---

### Touchpoint 5 — Week 12 Completion and Next Steps
**Timing:** Week 12 (after final AI Adoption Maturity Assessments and Program Completion Rubric are complete)
**Format:** 60 min. Formal meeting. Executive sponsor + you. Embedded Engineer may present briefly then exit.
**Goal:** Present program outcomes, close the engagement, and open the next conversation.

**Agenda:**
1. **Outcome presentation** (15 min): DLP Completion rates by behavioral criterion. How many participants met all four criteria (Craft, Evaluate, Iterate, Adopt)? Breakdown of where the gaps were. Embedded Engineer's qualitative assessment of the cohort. Specific artifacts produced and committed to the codebase. AI Adoption Maturity Assessment progression from Week 1 baseline to Week 12.
2. **What participants can do now** (10 min): Describe the capability the organization has that it didn't have 12 weeks ago. Tie it back to what the executive sponsor said success looked like in Week 1.
3. **Continued adoption of the core DLP skills** (10 min): Session 6 (Week 11) introduced custom harnesses as the path to continued growth. Participants know where to deepen their practice. This is a natural entry point for the next conversation.
4. **Recommendations** (10 min): What would you recommend as a next step? Options might include: sustaining with continued Embedded Engineer engagement, expanding to additional teams, a second loop to deepen adoption of the core DLP skills, or a different program track for specific participants.
5. **Close** (5 min): Thank the executive sponsor. Confirm any commitments or next steps. Ask for a referral or case study conversation if appropriate.

**What to bring:**
- Final DLP Completion summary (completed rubric + AI Adoption Maturity Assessment comparison from Week 1 to Week 12)
- 2–3 concrete artifacts the teams produced (ideally linked in the client's codebase)
- A written recommendation for what comes next (one page max)

---

## Receiving Embedded Engineer Escalations

The Embedded Engineer will occasionally escalate to you. This is expected and healthy — do not treat it as a problem signal by itself. The Embedded Engineer escalates when something is beyond their level to resolve, not when they've failed.

### When to Expect Escalations
- **Weeks 2–4:** Early friction. A manager is pulling participants off Embedded Engineer sessions, challenging the program's value, or competing with the Embedded Engineer's time with the team. Most common trigger.
- **Weeks 5–7:** Scope creep or team changes. A participant has been reassigned, a team has a major deliverable that's crowding out DLP work.
- **Weeks 8–10:** Completion risk. A participant or set of participants is not progressing and the Embedded Engineer believes it's structural, not motivational.

### What to Do When the Embedded Engineer Escalates

**Step 1: Listen and diagnose.**
Ask the Embedded Engineer to be specific: What has the manager said or done? What is the impact on participants? Has the Embedded Engineer already attempted to address it? What was the response?

**Step 2: Decide your intervention level.**
- **You handle it directly:** You contact the manager (or the manager's manager) and address the friction. Appropriate when the manager is simply uninformed about the program's design or scope.
- **You involve the executive sponsor:** The manager is actively resistant, and you believe an executive sponsor message will change the dynamic. This is a judgment call — use it when the friction is material to program outcomes, not for every grumble. When you involve the executive sponsor, brief them on the specific situation and ask for a targeted message or conversation with the manager, not a broad program defense.

**Step 3: Close the loop with the Embedded Engineer.**
Tell the Embedded Engineer what you did and what the outcome was. If you involved the executive sponsor, tell the Embedded Engineer when that conversation happened and what was said. The Embedded Engineer should not be left wondering whether anything was done.

### Typical Manager Resistance Patterns

| Pattern | What It Looks Like | Likely Response |
|---------|-------------------|-----------------|
| Scheduling conflict | "I need them on a sprint, they can't do Embedded Engineer sessions this week" | Account Manager / Executive Coach sets a direct expectation with the manager that DLP is protected time per executive sponsor agreement |
| Value skepticism | "I don't see how prompt-writing helps my team ship faster" | Brief the manager on DLP Completion outcomes, emphasize artifacts committed to codebase. Escalate to exec sponsor if unresolved |
| Scope change | "We reorganized; this person is on a different team now" | Assess whether the participant can still participate from new team. Involve exec sponsor only if the change threatens the program's scope |
| Passive withdrawal | Manager stops facilitating, stops asking about the program | Direct outreach. Follow up with exec sponsor if no change after one contact |

---

## Signs the Engagement Is at Risk

Review Embedded Engineer weekly touchpoint summaries and watch for these signals. If you see two or more, initiate a direct conversation with the Embedded Engineer and consider an unscheduled executive sponsor contact.

- **Participation declining:** Embedded Engineer reports that fewer participants are bringing real work to sessions. Embedded Engineer sessions are becoming demonstrations rather than working sessions.
- **Assessment stagnation:** Midpoint AI Adoption Maturity Assessment results show no movement from baseline — dimensions 1–4 remain flat or below 2.0 averages at the midpoint check.
- **No artifacts produced:** By Week 6, participants should have at least a committed skill with written EC. If the Embedded Engineer cannot point to anything committed to the codebase, something is wrong.
- **Embedded Engineer is teaching, not coaching:** Embedded Engineer reports spending most of their time re-teaching training content rather than coaching participants through their own work. May signal that Session 1 or 2 didn't land, or that participants aren't doing the work between sessions.
- **Manager friction unresolved after one cycle:** An escalation came in, you addressed it, but the friction recurred. Escalate to executive sponsor.
- **Embedded Engineer is struggling:** Embedded Engineer expresses doubt about their own ability to coach participants. This requires a Trainer conversation, possibly a program manager check-in.

---

## Quick Checklists

### Before Week 1
- [ ] Kickoff meeting complete with executive sponsor
- [ ] Executive sponsor has confirmed manager preparation
- [ ] DLP Completion defined as shared success metric
- [ ] Escalation protocol established
- [ ] API key provisioning confirmed for Session 4 (Week 7)
- [ ] If virtual delivery: cameras-on expectation communicated to executive sponsor and sponsor has agreed to reinforce with participants before Session 1
- [ ] Week 4 touchpoint on calendar

### At Week 6
- [ ] Midpoint AI Adoption Maturity Assessments collected
- [ ] Midpoint summary prepared for exec sponsor meeting
- [ ] Any escalations addressed and closed
- [ ] API keys confirmed available for Loop 2 (Sessions 4–6)
- [ ] Week 9 touchpoint on calendar

### At Week 12
- [ ] Final AI Adoption Maturity Assessments and completion rubric complete
- [ ] Completion summary prepared
- [ ] 2–3 artifact examples identified
- [ ] Written recommendation for next steps prepared
- [ ] Completion meeting confirmed with executive sponsor