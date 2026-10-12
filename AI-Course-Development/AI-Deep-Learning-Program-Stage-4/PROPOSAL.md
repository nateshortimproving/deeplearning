# Stage 4 Deep Learning Program — Proposal

*Proposed structure for a team engagement that takes Stage 3-certified practitioners through Stage 4 (Workflow) of the Improving Intelligence Operating System*

*Date: August 2026 | Status: Draft Proposal*

---

## 1. Purpose and Scope

### What This Program Is

The Stage 4 Deep Learning Program (Stage 4 DLP) is a **team engagement** that takes a cohort of Stage 3-certified practitioners from individual skill mastery to production-grade multi-step AI workflow integration. Participants build a real custom harness — a Python program that orchestrates multiple validated Stage 3 skills into an end-to-end workflow with automated guardrails, human punch-out points, measured success rates, and a full audit trail — for a real business process in their actual codebase.

The program is built around the five Stage 4 certification artifacts defined in the Improving Intelligence Operating System (IIOS):

1. **The Workflow Definition** — multiple Stage 3 agents wired into an end-to-end workflow with an automated harness/runner script
2. **The Guardrails** — adversarial review agents + deterministic hooks running automatically between steps
3. **The Punch-Out Evidence** — explicitly defined and bypass-tested human evacuation points
4. **The End-to-End Success Rate Report** — the composite success rate across the full workflow, not just per-step accuracy
5. **The Audit Trail** — every failure traceable to its origin step, with per-step model and token/cost data

### What This Program Is Not

- **Not an individual course.** Stage 4 is a team event. Personal agents from Stage 3 must be reconciled into shared workflows. IT is pulled in because gates and pipelines live in shared infrastructure. A single person cannot certify at Stage 4 in isolation.
- **Not a continuation of the Stage 3 DLP.** The Stage 3 DLP (12 weeks, 6 sessions, Trainer + EE) builds individual capability. The Stage 4 DLP builds team capability. The structure, roles, cadence, and deliverables are different.
- **Not tool training.** Participants arrive with Stage 3 skills: they can build, evaluate, and iterate AI skills using RTCC, EDD, Python evaluation scripts with LLM judges, and adversarial agents. This program does not re-teach those disciplines. It applies them at the workflow level.

### Relationship to Stage 3

The Stage 3 DLP ends with a custom harness demo and an IIOS stage framework preview that points participants toward this program. The Stage 4 DLP picks up where Stage 3 left off: participants already have evaluated, iterated skills in their codebase. The Stage 4 DLP shows them how to compose those skills into a production workflow.

**Prerequisite:** All participants must have achieved DLP Completion (Stage 3 certification) before the engagement begins. The AI Bootcamp 4-week program targets this for Improving's own Embedded Engineers; client teams must have completed a Stage 3 DLP engagement or equivalent.

### Stage 3 Workflow Prerequisite

In addition to individual Stage 3 certification, the team must arrive with a **documented Stage 3 workflow** for the business process they intend to use as the baseline for their custom harness. This means:

- The team has identified a real, bounded business process that they want to automate end-to-end
- Each step in that process already has a committed, evaluated Stage 3 skill (or a clear plan to build one as pre-work)
- The skills have Python evaluation scripts with documented iteration history (3+ cycles)
- The skills have been used on real work, not just synthetic inputs

This is not a soft suggestion. The Stage 4 DLP builds a custom harness that orchestrates Stage 3 skills into a multi-step workflow. If the Stage 3 skills don't exist yet, the team will spend the first half of the program building them — which is Stage 3 work, not Stage 4 work. The program is designed for teams who have already done Stage 3 and are ready to compose.

If a team arrives without a documented Stage 3 workflow, the engagement should be delayed. The Account Manager verifies this prerequisite during pre-engagement scoping.

---

## 2.5. Pre-Engagement Requirements

Before Session 1, the following must be in place:

| Requirement | Owner | Deadline |
|-------------|-------|----------|
| **Stage 3 workflow documented** — the team has identified their target business process and each step has a committed, evaluated Stage 3 skill | Team lead + EE | Before engagement begins |
| **IT Liaison identified** — the client has named the person who will own infrastructure coordination (API keys, CI/CD, deployment, security) | Client / Account Manager | Before engagement begins |
| **API access secured** — the IT Liaison has provisioned API keys for the models the harness will use | IT Liaison | Before Session 2 (Week 4) |
| **Shared Python environment** — a team-accessible Python environment for the harness project | IT Liaison | Before Session 2 (Week 4) |
| **Team composition confirmed** — 4–6 person team with at least 2 Stage 3-certified practitioners | Account Manager | Before engagement begins |

---

## 2. Design Principles (Carried Forward from Stage 3)

These principles from the Stage 3 DLP are preserved and extended:

1. **Artifacts over advice** — every session and week produces something committed and usable
2. **Measure don't guess** — every workflow step has a Python evaluation script; the full chain has an end-to-end success rate
3. **Deterministic first, LLM judge second** — guardrails start with deterministic checks (schema, format, counts) before escalating to adversarial agents
4. **Real work not exercises** — the team builds a harness for a real business process in their actual codebase, not a synthetic scenario
5. **Behavior change is the bar** — the program target is a production workflow the team actually uses, not a prototype that sits in a repo

### New Principles for Stage 4

6. **Team-scale, not individual-scale** — the workflow belongs to the team, not to one person. Reconciliation of personal Stage 3 skills into shared team workflows is explicit program work.
7. **Earn the right to automate** — every step must individually pass its Stage 3 quality bar (95%+ on real work) before being wired into the workflow. A workflow built on unreliable agents is a slop cannon.
8. **The harness is infrastructure, not UX** — the guardrail layer, audit trail, and failure handling are shared infrastructure. They live where the team operates, not in one person's IDE.
9. **Punch out, don't rubber-stamp** — human evacuation points are real gates, not ceremony. They must be tested for bypass. A workflow that proceeds past a punch-out point without human sign-off is not Stage 4.
10. **Cost-adjusted capacity** — you cannot manage what you do not measure. Per-step model, token, and cost data are required, not optional. The audit trail is the measurement system.

---

## 3. Program Structure

### Engagement Duration

**16 weeks** with **5 training sessions** (4 hours each, approximately one every 3 weeks). The longer cadence (3 weeks between sessions vs. the Stage 3 DLP's 2 weeks) reflects the ~10x effort multiplier of Stage 4 — participants need more build time between sessions because the work is harder, the artifacts are more complex, and the team coordination overhead is real.

```
Week  1–3   | Session 1: Workflow Mapping + Harness Architecture
Week  4–6   | Session 2: Building the Harness — Step Orchestration + Artifact Passing
Week  7–9   | Session 3: Guardrails — Deterministic Hooks + Adversarial Review Agents
Week 10–12  | Session 4: Punch-Out Points + Audit Trail + End-to-End Success Rate
Week 13–15  | Session 5: Integration, Certification Preparation, and Team Handoff
Week 16     | Certification submission and program close
```

### Why 16 Weeks, Not 12

The Stage 3 DLP runs 12 weeks because individual skill-building has a predictable cadence: learn a concept in a session, build the artifact over two weeks, evaluate and iterate. Stage 4 is different:

- **Team coordination overhead** — reconciling personal skills into shared workflows requires meetings, negotiation, and consensus. This doesn't happen in a sprint; it happens over weeks.
- **Infrastructure setup** — API access, shared Python environments, CI/CD integration, and deployment infrastructure require IT coordination. This is not instant.
- **The compounding-error reality** — at 95% per-step accuracy, a 5-step workflow completes correctly only ~77% of the time. Iterating each step to production quality takes real evaluation cycles, not a weekend.
- **The harness itself is a software project** — it needs tests, version control, error handling, logging, and deployment. It's not a script; it's a system.

### Roles

| Role | Stage 3 DLP | Stage 4 DLP |
|------|-------------|-------------|
| **Trainer** | Delivers 6 structured training sessions | **Trainer** — delivers 5 training sessions AND holds weekly office hours with the team (see below) |
| **Embedded Engineer** | Player-coach, works alongside developers | **Embedded Engineer** — deeper technical role: co-builds the harness, writes guardrails, sets up audit infrastructure, pairs on every artifact |
| **Account Manager / Executive Coach** | Owns executive relationship | **Account Manager** — owns executive relationship AND ensures IT coordination (API keys, infrastructure, deployment) |
| **IT Liaison** | Not present in Stage 3 | **New role** — client-side representative who owns infrastructure: API access, CI/CD pipelines, deployment environments, security review. Must be identified by the client before the program begins (see below) |

### Weekly Office Hours

A distinguishing structural feature of the Stage 4 DLP is **weekly office hours** — a standing 1-hour meeting each week where the Trainer, Embedded Engineer, and the full team meet together to discuss what they are working on. This is not a lecture or a training session; it is a working session where the team brings questions, blockers, and progress, and the Trainer and EE provide direction, unblock issues, and review artifacts.

**Structure:**
- **1 hour per week** is the baseline. The team can agree to add additional time as needed — some weeks will need more (e.g., when the harness first runs end-to-end, or when guardrails are being integrated), and some weeks will need less.
- The Trainer's role in office hours is architectural guidance and direction: helping the team make design decisions, reviewing the harness architecture, and keeping the team aligned with the five certification artifacts.
- The EE's role in office hours is technical depth: helping with specific implementation blockers, reviewing code, and pairing on guardrail and audit trail work.
- The team's role is to arrive prepared: what did we build this week, what's blocked, what decisions need to be made.

**Why office hours, not just sessions:**

The Stage 3 DLP's introduce → reinforce cadence (session introduces concept, EE reinforces over two weeks) works because individual skill-building is predictable. Stage 4 is not predictable — the harness will break in unexpected ways, the guardrails will surface failure modes nobody anticipated, and the team will need architectural guidance mid-week, not just at the next session. The weekly office hours give the team a reliable forum for that guidance without waiting 3 weeks for the next session.

This also means the Trainer role is closer to the Stage 3 Trainer than the original "Consultant Architect" concept — the Trainer delivers sessions AND holds office hours, but is not a full-time embedded architect. The architectural depth comes from the EE, who is embedded continuously. The Trainer provides the directional guidance and curriculum structure.

### IT Liaison

The IT Liaison is a **client-side role**, not an Improving consultant. The client must identify their IT Liaison **before the program begins** — this is a pre-engagement requirement (see Section 4 below).

The IT Liaison may be:
- A **DevOps engineer on the team** who already owns infrastructure and CI/CD
- Someone **external to the team** (e.g., a platform engineer, IT operations lead, or infrastructure manager) who can coordinate API access, deployment environments, and security review

Either is acceptable. The key requirement is that this person has the authority and access to provision what the harness needs: API keys, Python environments, CI/CD pipelines, deployment targets, and audit logging infrastructure. Without an identified IT Liaison, the program cannot begin — the infrastructure coordination bottleneck is a real risk, and it must be solved before Session 1, not during it.

The IT Liaison does not need Stage 3 certification. They need infrastructure authority.

### Team Composition

The Stage 4 DLP works with a **focused 4–6 person team** (the IIOS documentation notes that a well-operating 4–6 person team at Stage 4 can outpace an 8–10 person team). The team should include:

- **2–3 practitioners** who completed Stage 3 and have committed, evaluated skills in their codebase
- **1 IT Liaison** who owns infrastructure coordination
- **1 product/process representative** who owns the business process being automated
- **1 team lead** who owns the workflow definition and punch-out decisions

All practitioners must have Stage 3 skills: RTCC, EDD, Python evaluation scripts, adversarial agents. The program does not re-teach these.

---

## 4. Session Progression

### Session 1: Workflow Mapping + Harness Architecture (Week 1, 4 Hours)

**Goal:** Map a real business process to a multi-step AI workflow and design the harness architecture.

**Block 1: From Stage 3 to Stage 4 (45 min)**
- Recap the IIOS stage framework: where the team is (Stage 3), where they're going (Stage 4)
- The Stage 3 ceiling: personal skills, one-at-a-time review, no composition
- The Stage 4 breakthrough: shared workflows, automated guardrails, end-to-end measurement
- The power-law progression: ~10x effort, but the capability leap is larger than the effort leap
- The five certification artifacts: what they are, why each matters, what "done" looks like for each

**Block 2: Workflow Mapping Workshop (90 min)**
- The team arrives with a documented Stage 3 workflow for the business process they intend to automate — this is a prerequisite (see Section 1)
- Session 1 validates and refines that workflow, it doesn't create it from scratch
- Selection criteria: bounded process, clear handoffs, cost of mistakes is known, at least 3 steps where Stage 3 skills already exist
- Map the process as boxes (steps) and arrows (handoffs)
- For each step, identify: what skill runs, what input it needs, what output it produces, what evaluation checks the output
- The slop cannon warning: every step must individually pass Stage 3 (95%+ on real work) before being wired in. If any step isn't there yet, that's pre-work — not a reason to skip the step

**Block 3: Harness Architecture Design (75 min)**
- The harness is a Python program. What does it look like?
- Architecture components: step runner, artifact passing (YAML/JSON between steps), evaluation orchestration, guardrail execution, audit logging, failure handling
- Design decisions: sync vs async, retry policy, human notification, deployment target
- The context window discipline principle from Stage 3 Session 6: each step gets its own clean context
- Output: a **Harness Architecture Document** — the blueprint for what the team will build

**Session Artifacts:**
- [ ] **Workflow Map** — the selected business process mapped as steps and handoffs, with skills, inputs, outputs, and evaluations identified for each step
- [ ] **Harness Architecture Document** — the blueprint for the custom harness: components, data flow, evaluation points, guardrail placement, failure handling, deployment target

**Between Sessions 1–2 (Weeks 2–3):**
- Team reconciles personal Stage 3 skills into shared team skills — this is explicit reconciliation work
- Each step's skill is evaluated against its Stage 3 quality bar; gaps are documented and prioritized
- IT Liaison secures API access and sets up the shared Python environment
- Embedded Engineer begins scaffolding the harness project structure (repo, CI, testing framework)
- **Weekly office hours** (1 hr): Trainer + EE + team discuss architecture decisions, unblock on harness scaffold, review reconciliation progress

---

### Session 2: Building the Harness — Step Orchestration + Artifact Passing (Week 4, 4 Hours)

**Goal:** Build the harness skeleton that orchestrates the workflow's steps and passes artifacts between them.

**Block 1: Harness Foundation (60 min)**
- The harness as a Python project: structure, dependencies, configuration, testing
- API integration: calling the model API directly (not through the IDE) — the leap from Session 4's evaluation scripts to a full harness
- The step runner pattern: how the harness calls a skill, captures output, and passes it to the next step
- Structured artifact passing: YAML/JSON files between steps (extending the Stage 3 pipeline pattern)
- Demo: the instructor runs a minimal 2-step harness against the team's real skills, showing clean context per step and artifact passing

**Block 2: Build Lab — Harness Skeleton (90 min)**
- The team builds the harness skeleton: step runner, API integration, artifact passing for their mapped workflow
- Each step reads upstream YAML and writes its own — the same pipeline discipline from Stage 3
- The harness runs end-to-end but without guardrails, evaluation, or audit (that comes later)
- First end-to-end run: the workflow executes from start to finish, producing a final artifact
- Commit the harness to the team's repo

**Block 3: Evaluation Integration (60 min)**
- Integrating the Stage 3 Python evaluation scripts into the harness
- The harness runs the evaluation script after each step, before passing the artifact downstream
- If evaluation fails: halt, retry, or notify — the failure handling decision
- Demo: the instructor shows what happens when a step fails its evaluation and the harness halts

**Block 4: First End-to-End Run + Discussion (30 min)**
- The team runs their harness end-to-end with evaluation at each step
- What worked? What broke? Where did the harness catch a failure that the IDE would have missed?
- The compounding error reality: what's the per-step accuracy? What's the implied end-to-end success rate?

**Session Artifacts:**
- [ ] **Harness skeleton** — committed to the team repo, running end-to-end with step orchestration and artifact passing
- [ ] **Evaluation integration** — Python evaluation scripts running at each step in the harness
- [ ] **First end-to-end run log** — the harness output with evaluation scores at each step, committed

**Between Sessions 2–3 (Weeks 5–6):**
- Iterate the harness: fix failures from the first run, improve step skills where evaluation scores are low
- The EE pairs on each step with the practitioner who owns that skill — the transfer from personal to shared
- Track per-step accuracy across multiple runs — this becomes the baseline for the success rate report
- **Weekly office hours** (1 hr): Trainer + EE + team discuss harness issues, review evaluation integration, plan guardrail placement

---

### Session 3: Guardrails — Deterministic Hooks + Adversarial Review Agents (Week 7, 4 Hours)

**Goal:** Build the guardrail layer that runs automatically between workflow steps, catching failures before they propagate downstream.

**Block 1: The Guardrail Concept (45 min)**
- Guardrails sit BETWEEN steps, not inside them — they validate outputs before the next step begins
- Two complementary forms (from the Stage 4 certification requirements):
  - **Deterministic hooks**: code that checks structure, format, field presence, schema validation, file integrity. Fast, free, definitive. These are the same kind of checks from Stage 3's "deterministic first" evaluation principle — now automated as gates.
  - **Adversarial review agents**: Stage 3 skills whose sole purpose is to challenge the prior step's output with a distinct lens (security, compliance, completeness, domain-specific risk). These extend the adversarial agent concept from Stage 3 Session 5.
- The counterfeit warning: hooks that only check file existence or non-empty output are window dressing. They create the illusion of safety. Window-dressing guardrails are worse than no guardrails.
- The adversarial quality warning: an adversarial review agent must genuinely challenge with a DIFFERENT perspective than the producing agent. It must not simply re-check the same criteria. A redundant second opinion is not adversarial.

**Block 2: Building Deterministic Hooks (75 min)**
- Hook placement: between which steps do hooks run? (Answer: between every step, at minimum)
- Hook design: what does each hook check? Schema validation, field counts, format patterns, YAML structure, required fields, output size bounds
- Hook implementation: Python functions that receive the step's output, run deterministic checks, and return pass/fail with structured results
- The harness calls the hook after the evaluation script and before passing the artifact downstream
- Build lab: the team writes hooks for each step in their workflow

**Block 3: Building Adversarial Review Agents (75 min)**
- Each adversarial agent has: (1) a distinct purpose/lens, (2) its own prompt designed to find problems, (3) an explicitly adversarial posture
- Extending Stage 3 adversarial agents: the same prompt patterns, now integrated into the harness as automated gates
- Placement: not every step needs an adversarial agent, but high-risk steps (code generation, review, security-sensitive output) always do
- Build lab: the team writes adversarial review agents for key steps in their workflow

**Block 4: Integrated Guardrail Run (30 min)**
- The harness now runs: step → evaluation script → deterministic hook → adversarial agent → pass to next step
- What does the guardrail layer catch that the evaluation script alone misses?
- Discussion: where are the gaps? What's not yet guarded?

**Session Artifacts:**
- [ ] **Deterministic hooks** — committed to the team repo, running between every step
- [ ] **Adversarial review agents** — committed, running at key steps with distinct adversarial lenses
- [ ] **Guardrail configuration** — document showing where each guardrail sits, what it checks, and what happens on failure

**Between Sessions 3–4 (Weeks 8–9):**
- Iterate hooks and adversarial agents: tune false positive rates, add checks for failure modes discovered in runs
- Run the harness multiple times against real inputs; track what the guardrails catch
- The EE helps tune adversarial agent prompts — calibrated severity, actionable findings (same principles from Stage 3 Session 5)
- **Weekly office hours** (1 hr): Trainer + EE + team review guardrail effectiveness, discuss false positive tuning, plan punch-out point placement

---

### Session 4: Punch-Out Points + Audit Trail + End-to-End Success Rate (Week 10, 4 Hours)

**Goal:** Define and test human evacuation points, build the audit trail, and measure the end-to-end success rate.

**Block 1: Punch-Out Points (75 min)**
- A punch-out point is a place in the workflow where a human is required regardless of what the agent can technically do
- Two failure modes that must be separated:
  - "Fail the workflow" — handled by automation (retry, re-prompt, escalate within the system)
  - "Punch out to a human" — a genuine human decision point that must never be bypassed
- Designing punch-out points: where in the workflow does a human MUST sign off?
- **Bypass testing** — punch-out points must have been actively tested. Someone attempts to bypass them, and the system blocks it. A punch-out point that exists on paper but has never been tested for bypass is a red signal.
- Build lab: the team defines punch-out points in their workflow, implements enforcement in the harness, and writes bypass tests

**Block 2: Audit Trail (75 min)**
- The audit trail must allow tracing any failure to its exact origin step
- Required per-step data: which model was used, input tokens, output tokens, cost (in dollars or ACUs)
- Data sources: CLI session logs (Claude Code writes JSONL, Devin stores cog data), harness `--output-format json` responses, API proxy logs
- Implementation: the harness logs structured entries for each step execution with step ID, model, token counts, cost, pass/fail status, and failure trace
- Build lab: the team implements audit logging in their harness and produces a sample audit trail

**Block 3: End-to-End Success Rate (60 min)**
- The composite number: across N runs of the full workflow, what percentage complete correctly end-to-end?
- The compounding error math: at 95% per-step, a 5-step pipeline completes ~77%. At 90% per-step, ~59%. At 85%, ~44%.
- This is why per-step accuracy alone is not enough — you must know the end-to-end number
- Measurement methodology: run the harness N times against real inputs, count successful end-to-end completions, track over time
- Build lab: the team runs their harness 10+ times against real inputs and produces the first success rate report

**Block 4: The Five Artifacts Assembled (30 min)**
- Review the five Stage 4 certification artifacts and where the team stands on each:
  1. Workflow Definition — exists (Session 1)
  2. Guardrails — exists (Session 3)
  3. Punch-Out Evidence — in progress (Session 4)
  4. End-to-End Success Rate Report — first version today (Session 4)
  5. Audit Trail — in progress (Session 4)
- What's missing? What needs iteration before certification submission?

**Session Artifacts:**
- [ ] **Punch-out points defined and enforced** — with bypass test logs
- [ ] **Audit trail implementation** — structured logging with per-step model, token, and cost data
- [ ] **First End-to-End Success Rate Report** — the composite number with methodology and trend data

**Between Sessions 4–5 (Weeks 11–12):**
- Iterate the harness based on the success rate: which steps are the bottlenecks? Where does the chain break?
- Complete bypass testing for all punch-out points
- Fill gaps in the audit trail
- The EE helps the team prepare the certification submission artifacts
- **Weekly office hours** (1 hr): Trainer + EE + team review success rate trends, plan certification gaps, prepare submission artifacts

---

### Session 5: Integration, Certification Preparation, and Team Handoff (Week 13, 4 Hours)

**Goal:** Finalize all five certification artifacts, prepare for Stage 4 certification submission, and hand off the workflow to the team.

**Block 1: Integration Review (60 min)**
- Full harness run: the complete workflow with all guardrails, punch-out points, audit trail, and success rate measurement
- What's production-ready? What's still fragile?
- The team identifies remaining gaps and assigns owners
- The harness is a software project: does it have tests? Documentation? Deployment plan? Error handling for production scenarios?

**Block 2: Certification Artifact Review (90 min)**
- Walk through each of the five artifacts against the Stage 4 certification criteria:
  1. **Workflow Definition** — multiple Stage 3 agents wired in, each agent individually passes Stage 3, automated harness/runner script present, no "slop cannon" agents
  2. **Guardrails** — adversarial agents with distinct lenses + deterministic hooks with real validation, no window dressing, automated (not human review)
  3. **Punch-Out Evidence** — bypass-tested, clear separation of "fail the workflow" vs "punch out to human"
  4. **End-to-End Success Rate** — the composite number, methodology, trend data
  5. **Audit Trail** — per-step traceability with model/token/cost data, coverage of all steps
- Identify any automatic FAIL conditions:
  - No automated harness (human is the workflow)
  - Guardrails rely on human review
  - Window-dressing hooks
  - Non-adversarial "adversarial" agents
  - Untested punch-out points
  - No end-to-end success rate
  - No per-step cost data
  - Any agent still requires regular manual correction

**Block 3: Team Handoff and Operating Model (60 min)**
- The workflow is a team asset, not an individual one. Who owns it going forward?
- The maintenance model: 12 updates/month (vs Stage 3's 2/month). What does that look like in practice?
- The IT Liaison's ongoing role: infrastructure, API key rotation, deployment, monitoring
- Monitoring the success rate: what's the trend? When does the team investigate a drop?
- The iteration cadence: when do skills get re-evaluated? When do guardrails get updated?

**Block 4: Program Close and Next Steps (30 min)**
- What the team has built: a specific, named, production-grade custom harness for a real business process
- Stage 4 certification submission process
- Beyond Stage 4: the IIOS notes that most organizations stop here for a while — Stage 5 costs ~7x more
- The team's commitment: who maintains this? Who iterates it? Who monitors it?

**Session Artifacts:**
- [ ] **Complete Stage 4 certification submission** — all five artifacts documented and ready for examination
- [ ] **Team handoff document** — ownership, maintenance model, monitoring plan
- [ ] **Program retrospective** — what worked, what to improve for the next engagement

**Between Sessions 5–6 (Weeks 14–15):**
- Final iteration on any gaps identified in Session 5
- The EE helps with last-minute fixes and documentation
- Certification submission prepared
- **Weekly office hours** (1 hr): Trainer + EE + team final review of certification artifacts, last-minute fixes

**Week 16: Certification Submission and Program Close**
- Submit the five artifacts for Stage 4 certification examination
- Program close: EE departs, team owns the workflow
- 30-day check-in scheduled (EE follows up on production usage)

---

## 5. The Workspace Model

### Real Codebase, Not Shared Workspace

The Stage 3 DLP uses a shared student workspace (`student-workspace/`) with sample stories, skeleton skills, and demo outputs. All participants work against the same inputs. The EE's job is to transfer skills from the workspace to the real codebase.

The Stage 4 DLP **does not use a shared workspace**. The team works entirely in their real codebase from day one. There is no training ground; there is only the application. This is appropriate because:

- Stage 4 is about team-scale workflows, not individual skill-building
- The workflow being automated is a real business process — synthetic scenarios don't test the real handoffs, real guardrail needs, or real failure modes
- The team already has Stage 3 skills in their codebase — those are the building blocks
- The harness must run against real infrastructure (API keys, CI/CD, deployment) — not a sandbox

### What the Trainer Provides

Instead of a shared workspace, the Trainer provides:

- **Reference harness implementations** — example custom harnesses (including the one demoed in Stage 3 Session 6) as reference code
- **Guardrail templates** — starting points for deterministic hooks and adversarial review agent prompts
- **Audit trail schemas** — structured logging formats for per-step model/token/cost data
- **Certification artifact templates** — document templates for each of the five artifacts

These are reference materials, not training exercises. The team adapts them to their real workflow.

---

## 6. Assessment and Certification

### Stage 4 Certification

The program's target is Stage 4 certification. Certification is assessed by submitting the five artifacts for examination against the criteria defined in `CERTIFICATION.md`. The examination is performed by the Stage 4 Certification Examiner (an automated or human review process, as defined by Improving's certification framework).

The five artifacts and their automatic FAIL conditions (from `CERTIFICATION.md`):

| Artifact | What's Required | Automatic FAIL |
|----------|----------------|----------------|
| **Workflow Definition** | Multiple Stage 3 agents wired into end-to-end workflow, automated harness/runner script, each agent individually passes Stage 3 | No automated harness; any agent requires regular manual correction; Stage 3 evaluation artifacts not present |
| **Guardrails** | Adversarial review agents with distinct lenses + deterministic hooks with real validation, automated between steps | Guardrails rely on human review; window-dressing hooks; non-adversarial "adversarial" agents |
| **Punch-Out Evidence** | Explicitly defined, bypass-tested human evacuation points | Punch-out points exist on paper but never tested for bypass |
| **End-to-End Success Rate** | Composite success rate across full workflow, with methodology and trend data | No end-to-end success rate reported (only per-step accuracy) |
| **Audit Trail** | Every failure traceable to origin step, with per-step model/token/cost data, coverage of all steps | No per-step model/token/cost data |

### Program Completion

The program is complete when:
1. All five artifacts are submitted for Stage 4 certification
2. The team handoff document is signed (ownership transferred)
3. The 30-day check-in is scheduled

Completion does not require certification approval — that's a separate process. But the program's job is to get the team to a submission-ready state.

---

## 7. Differences from Stage 3 DLP

| Dimension | Stage 3 DLP | Stage 4 DLP |
|-----------|-------------|-------------|
| **Target** | Individual capability (Stage 3: Task) | Team capability (Stage 4: Workflow) |
| **Duration** | 12 weeks | 16 weeks |
| **Sessions** | 6 × 4 hours | 5 × 4 hours |
| **Cadence** | ~1 session per 2 weeks | ~1 session per 3 weeks |
| **Roles** | Trainer + Embedded Engineer | Trainer + Embedded Engineer + IT Liaison (client-side) |
| **Workspace** | Shared student workspace (synthetic) | Real codebase (no sandbox) |
| **Primary artifact** | Skills, evaluation scripts, adversarial agents | Custom harness with 5 certification artifacts |
| **Prerequisite** | Basic prompting (Stage 2) | DLP Completion (Stage 3) + documented Stage 3 workflow |
| **Team size** | Any size (all participants attend) | 4–6 person focused team |
| **IT involvement** | Minimal (API keys for sessions) | Significant (infrastructure, CI/CD, deployment) — client-side IT Liaison required |
| **Office hours** | None | 1 hour/week (Trainer + EE + team) |
| **Maintenance** | 2 updates/month | 12 updates/month |
| **Effort** | ~18h median per person | ~172h median per team |
| **Assessment** | Program Completion Rubric (Trainer + EE) | Stage 4 Certification Examination |

---

## 8. Session Summary Table

| Session | Week | Focus | Primary Artifact |
|---------|------|-------|-----------------|
| 1 | 1 | Workflow Mapping + Harness Architecture | Workflow Map + Harness Architecture Document |
| 2 | 4 | Building the Harness — Step Orchestration + Artifact Passing | Harness skeleton running end-to-end with evaluation at each step |
| 3 | 7 | Guardrails — Deterministic Hooks + Adversarial Review Agents | Guardrail layer: hooks + adversarial agents between every step |
| 4 | 10 | Punch-Out Points + Audit Trail + End-to-End Success Rate | Punch-out enforcement + audit trail + first success rate report |
| 5 | 13 | Integration, Certification Preparation, and Team Handoff | Complete Stage 4 certification submission + handoff document |

---

## 9. Key Risks and Mitigations

### Risk: Stage 3 Foundations Not Solid
**Problem:** The team arrives with skills that haven't been iterated to 95%+ accuracy. The harness gets built on unreliable agents. Errors compound. The workflow is a slop cannon.
**Mitigation:** Session 1 includes explicit Stage 3 readiness assessment. Any step not at 95%+ is documented as pre-work. The harness cannot wire in a step that hasn't passed its Stage 3 bar. The Trainer has authority to delay the engagement if foundations are weak. The Stage 3 workflow prerequisite (Section 1) ensures the team arrives with documented, evaluated skills.

### Risk: IT Coordination Bottleneck
**Problem:** The harness requires API access, shared Python environments, CI/CD integration, and deployment infrastructure. If IT can't deliver, the program stalls.
**Mitigation:** The IT Liaison is a client-side role, identified before the program begins (pre-engagement requirement). The Account Manager verifies IT coordination begins before Session 1. API keys, environments, and deployment targets must be ready by Week 2. If they're not, the engagement timeline adjusts — the program does not proceed without infrastructure.

### Risk: The Workflow Is Too Ambitious
**Problem:** The team selects a 15-step workflow with branching logic and external integrations. The harness is too complex to build and iterate in 16 weeks.
**Mitigation:** Session 1's workflow mapping workshop enforces the selection criteria: bounded process, clear handoffs, at least 3 steps with existing Stage 3 skills. The Trainer has authority to scope down. The discipline is: start with the simplest workflow that delivers real value, not the most impressive one.

### Risk: Guardrails Become Window Dressing
**Problem:** The team builds hooks that only check file existence and adversarial agents that just re-check the same criteria as the producing agent. The guardrail layer creates an illusion of safety.
**Mitigation:** Session 3 explicitly teaches the counterfeit patterns. The certification artifact review in Session 5 checks for automatic FAIL conditions. The Trainer and EE review every hook and adversarial agent during the build labs and weekly office hours.

### Risk: The Team Reverts to Stage 2 Behavior
**Problem:** After the program ends, the team stops maintaining the harness. Skills degrade. Guardrails go stale. The workflow silently reverts to human-in-the-loop (Stage 2).
**Mitigation:** Session 5's handoff block establishes the maintenance model (12 updates/month), ownership, and monitoring plan. The 30-day check-in verifies production usage. The handoff document names who owns what — no ambiguity.

---

## 10. Costing Model

### Assumptions

- **Embedded Engineer:** $200/hr bill rate, 40 hrs/week, dedicated to one team (8–16 people) for the full 16 weeks
- **Trainer:** $3,000 per training session (5 sessions total) + $500/hr for weekly office hours
- **Office hours:** baseline 1 hr/week, expandable to 2 hrs/week as needed
- **IT Liaison:** client-side role, no Improving cost
- **Account Manager:** not included in this model (executive relationship overhead, varies by engagement)

### Baseline Cost (1 hr/week office hours)

| Component | Calculation | Cost |
|-----------|-------------|------|
| Embedded Engineer | 40 hrs/week × 16 weeks × $200/hr | $128,000 |
| Trainer — Sessions | 5 sessions × $3,000 | $15,000 |
| Trainer — Office Hours | 1 hr/week × 16 weeks × $500/hr | $8,000 |
| **Total Program Cost** | | **$151,000** |

### Expanded Cost (2 hrs/week office hours)

| Component | Calculation | Cost |
|-----------|-------------|------|
| Embedded Engineer | 40 hrs/week × 16 weeks × $200/hr | $128,000 |
| Trainer — Sessions | 5 sessions × $3,000 | $15,000 |
| Trainer — Office Hours | 2 hrs/week × 16 weeks × $500/hr | $16,000 |
| **Total Program Cost** | | **$159,000** |

### Per-Person Cost

| Team Size | Baseline (1 hr) | Expanded (2 hr) |
|-----------|-----------------|-----------------|
| 8 people | $18,875/person | $19,875/person |
| 12 people | $12,583/person | $13,250/person |
| 16 people | $9,438/person | $9,938/person |

### Comparison to Stage 3 DLP

| Dimension | Stage 3 DLP | Stage 4 DLP (Baseline) |
|-----------|-------------|------------------------|
| EE duration | 12 weeks | 16 weeks |
| EE cost (at $200/hr) | $96,000 | $128,000 |
| Trainer sessions | 6 × $3,000 = $18,000 | 5 × $3,000 = $15,000 |
| Trainer office hours | None | $8,000 |
| **Total** | **$114,000** | **$151,000** |

Stage 4 is ~$37K more (~32% increase) than Stage 3 for 4 additional weeks of EE, 1 fewer session, and the addition of weekly office hours. This is a modest increase for a program targeting a ~10x capability jump.

### What's Not Included

- Account Manager time (executive relationship, pre-engagement scoping, IT coordination verification)
- IT Liaison (client-side, no Improving cost)
- Stage 4 certification examination cost (if any — TBD, see Open Questions)
- Reference materials and templates development (one-time build cost, amortized across engagements)
- Expenses (travel, lodging if in-person sessions are required)

### Cost Drivers

The Embedded Engineer is the dominant cost at ~85% of the total. The Trainer is relatively inexpensive because they are only engaged for sessions plus a weekly hour. The per-person cost ranges from ~$9.4K to ~$18.9K depending on team size, making Stage 4 cost-effective for teams of 8+ where the per-person investment is comparable to or less than typical per-seat enterprise training programs — while delivering a production-grade custom harness the team owns and maintains.

---

## 11. Post-Program Trajectory

### Stage 4 Certification
The program targets Stage 4 certification. If achieved, the team has a production-grade, fully evaluated custom harness for a real business process.

### Stage 5 and Beyond
The IIOS documentation notes that Stage 5 costs ~7x more to build than Stage 4. Most organizations stop at Stage 4 for a while. The program does not push teams toward Stage 5 — it makes them aware it exists and ensures they know the trajectory.

### Continued Engagement Options
If the team wants to build a second workflow harness after the first is certified, a follow-on engagement (8–12 weeks, lighter touch — the team does most of the building, the EE consults) is the natural next step. Each additional workflow gets easier because the harness patterns, guardrail templates, and audit infrastructure are reusable.

---

## 12. Open Questions

1. **Certification examiner:** Who performs the Stage 4 certification examination? Is it automated (like the Stage 3 Certification Validator), human, or hybrid? The Stage 3 Certification Validator at `~/source/stage3-certification-validator/` handles Stage 3 submissions. A Stage 4 equivalent would need to evaluate five artifacts with different criteria. This is a separate build effort.

2. **Trainer qualifications for Stage 4:** The Trainer needs to provide architectural guidance during office hours, not just deliver curriculum. They need to understand harness architecture, guardrail design, and the five certification artifacts at a depth beyond Stage 3 delivery. What's the qualification path? Likely a Stage 4-certified Embedded Engineer or a Trainer who has co-delivered a Stage 4 engagement.

3. **IT Liaison sourcing:** The IT Liaison must be a client-side role, identified before the program begins. The client may choose a DevOps engineer on the team or someone external to the team. Either is acceptable. The Account Manager verifies this during pre-engagement scoping. This is not an Improving-provided role.

4. **Multiple workflow harnesses:** Should the program target one workflow or allow teams to build multiple? The proposal recommends one (depth over breadth), but some clients may want to parallelize. This is a scoping decision per engagement.

5. **Relationship to the Stage 3 Certification Validator:** The Stage 4 certification artifacts are more complex than Stage 3 (five artifacts vs. three). Should we build a Stage 4 Certification Validator analogous to the Stage 3 one? If so, it should be scoped as a separate project after this proposal is approved.

6. **Online vs. in-person delivery:** Eric Sowell's feedback on the Stage 3 DLP highlighted that all-participants-every-session doesn't work well online. The Stage 4 DLP is inherently more hands-on and team-based, which may work better online (smaller group, more build time, less lecture). But the workflow mapping workshop (Session 1) and the certification artifact review (Session 5) may benefit from in-person collaboration. This should be a per-engagement decision.

---

## 13. Proposed File Structure

```
AI-Deep-Learning-Program-Stage-4/
├── PROPOSAL.md                                      ← This file
├── @Overview.md                                     ← Program overview (to be written after proposal approval)
├── Trainer/
│   ├── Implementation-Guide.md                      ← How to deliver the program (to be written)
│   └── Reference-Harness/                          ← Example harness implementations
│       ├── README.md
│       └── (reference harness code)
├── Embedded-Engineer/
│   ├── EE-Implementation-Guide.md                    ← EE coaching guide for Stage 4 (to be written)
│   └── EE-Playbook.md                                ← Field-tested coaching plays (to be written)
├── Templates/
│   ├── workflow-map-template.md                     ← Template for Session 1 artifact
│   ├── harness-architecture-template.md             ← Template for Session 1 artifact
│   ├── guardrail-config-template.md                 ← Template for Session 3 artifact
│   ├── punch-out-evidence-template.md               ← Template for Session 4 artifact
│   ├── success-rate-report-template.md              ← Template for Session 4 artifact
│   └── audit-trail-schema-template.md               ← Template for Session 4 artifact
├── Sessions/
│   ├── Session-1.md through Session-5.md            ← Session content (to be written)
│   └── Session-1.deck.md through Session-5.deck.md ← Deck prompts (to be written)
├── Certification/
│   ├── Stage-4-Certification-Requirements.md        ← Mirrors CERTIFICATION.md Stage 4 section
│   └── Submission-Checklist.md                      ← Pre-submission self-check
└── Assessments/
    └── Team-Readiness-Assessment.md                 ← Pre-engagement Stage 3 readiness check
```

---

*This proposal is a draft for review. It should be discussed with Devlin Liles (Chief AI Officer, framework authority), Tim Rayburn (Global Head of AI Training), and the trainer cohort before any content development begins.*