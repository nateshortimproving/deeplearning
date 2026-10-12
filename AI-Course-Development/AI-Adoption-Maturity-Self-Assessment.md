# AI Adoption Maturity Self-Assessment

## Assessment Statements

Rate each statement from 1 to 5. Each group of three progresses from foundational (Stage 2–3 evidence) to intermediate (Stage 3–4) to advanced (Stage 5+).

### Prompt Engineering & AI Interaction

| # | Statement | Rating (1–5) |
|---|-----------|--------------|
| 1 | When AI produces output that feels generic or verbose, I can point to the specific missing context or codebase patterns that caused it. I adjust my prompt to correct the root cause rather than editing the output by hand. | 3 |
| 2 | I have a rules file, project instructions, or system prompt that tells AI which patterns in my codebase represent my standards and which represent technical debt it should not replicate. These persist across sessions. | 2 |
| 3 | When AI output is more than 5% off from what I would produce, I update the agent's opinions, constraints, or standards rather than fixing the output manually. I treat every manual edit as a signal that my agent definition needs work. | 2 |

### Task Agents & Single-Box Automation

| # | Statement | Rating (1–5) |
|---|-----------|--------------|
| 4 | I can draw my workflow as boxes and arrows right now, labeling each discrete step from receiving work to delivering output. I know which boxes a human must own and which ones an agent could handle. | 1 |
| 5 | For at least one box in my workflow, I hand it to an agent with opinions (what approach to take), constraints (what to never do), and standards (definition of done), then review the result rather than guiding each step. | 3 |
| 6 | Most boxes in my workflow have a dedicated agent with documented opinions, constraints, and standards. I have refined each through multiple iterations and can name the specific failure modes I've corrected for. | 2 |

### Workflow Orchestration & Coordination

| # | Statement | Rating (1–5) |
|---|-----------|--------------|
| 7 | The output of one task agent feeds directly into the next without manual handoff. AI manages the arrows between boxes, not just the boxes themselves. | 2 |
| 8 | A workflow agent sequences my task agents, manages state between steps, and captures artifacts at each stage. I review checkpoints and final output rather than managing each transition. | 3 |
| 9 | My workflow agents operate across systems (IDE, project management, CI/CD, documentation). If someone watched me work for a week, they would see me approving checkpoints and reading status updates, not typing instructions into a chat window. | 3 |

### Governance, Trust & Safety Nets

| # | Statement | Rating (1–5) |
|---|-----------|--------------|
| 10 | I can list the specific anti-patterns, legacy workarounds, and inconsistent naming in my codebase that AI treats as signal for what "good" looks like. I have explicit rules that override those patterns. | 2 |
| 11 | My workflow includes quality gates where one agent's output gets checked before proceeding: tests pass, builds succeed, coverage thresholds are met, and prohibited actions are blocked. These gates fire automatically, not because I remembered to check. | 2 |
| 12 | I have agents whose job is to challenge other agents' output. A code generation agent writes, a review agent checks against architectural standards, and a security agent scans for vulnerabilities — all before the output reaches me. Slop gets caught inside the pipeline. | 1 |

### Trust Progression & Identity Shift

| # | Statement | Rating (1–5) |
|---|-----------|--------------|
| 13 | When an agent delivers output that meets my defined standards, I ship it without rewriting. I no longer feel the need to read every line to make sure it "sounds like me" — the agent's opinions already encode what that means. | 3 |
| 14 | Agents run outside my IDE — command line, background processes, cloud environments — and I receive status updates and deliverables without watching the work happen. I trust the quality gates built into Stages 3–4 to catch problems. | 1 |
| 15 | If someone asked what I do, I would describe the outcomes I produce, not the tasks I perform. I manage multiple agents working in parallel on separate work items and spend my time on integration and decisions that require my expertise. | 2 |

### Team & Organizational Practices

| # | Statement | Rating (1–5) |
|---|-----------|--------------|
| 16 | My agents encode my personal opinions about how work should be done — naming conventions, architecture patterns, error handling style. A colleague could read my agent definitions and understand my working standards without asking me. | 2 |
| 17 | My team shares workflow agents with a collective definition of done. PR bots catch coding anti-patterns, missing test coverage, and security vulnerabilities before code merges — these standards are encoded in agents, not just documented in a wiki. | 3 |
| 18 | Our organization provides governance agents (security scanning, compliance checking, architecture validation) that plug into every team's workflow. There are explicit policies for what agents are allowed to do at each stage, and those policies are enforced by other agents, not just by people remembering to check. | 1 |

### Scaling, Coordination & Supervision

| # | Statement | Rating (1–5) |
|---|-----------|--------------|
| 19 | Last week, I gave an agent a user story (or equivalent unit of work) and received a usable deliverable that needed only review and minor correction. The agent handled the full sequence from start to finish without me re-entering the loop mid-process. | 5 |
| 20 | I run multiple agents simultaneously on separate work items, each in its own isolated environment (branches, worktrees, containers). I track their status and merge their outputs, managing a team of agents the way a tech lead manages a team of developers. | 4 |
| 21 | An orchestrator assigns work to agents, manages the full pipeline from requirements through deployment, and escalates to me only for decisions and approvals. My primary interaction with the system is setting goals and reviewing escalations. | 1 |

---

## Scoring Your Results

### Step 1: Dimension Scores

Add the three ratings in each dimension (range: 3–15). Calculate the average (sum ÷ 3). Dimensions below 3.0 are your strongest growth opportunities.

| Dimension | Sum (3–15) | Average |
|-----------|------------|---------|
| Prompt Engineering & AI Interaction | 7 | 2.3 |
| Task Agents & Single-Box Automation | 6 | 2.0 |
| Workflow Orchestration & Coordination | 8 | 2.7 |
| Governance, Trust & Safety Nets | 5 | 1.7 |
| Trust Progression & Identity Shift | 6 | 2.0 |
| Team & Organizational Practices | 6 | 2.0 |
| Scaling, Coordination & Supervision | 10 | 3.3 |
| **TOTAL SCORE** | **48** | **2.3** |

### Step 2: Map to the Adoption Model

Your total score (21–105) maps to the model. Most teams vary across dimensions. Use both your total and dimension averages to find your current stage and next target.

| Score | Stage | Name | Interpretation & Focus |
|-------|-------|------|------------------------|
| 21–35 | Stage 2 | **Off the Shelf (Wave 1)** | You use off-the-shelf AI tools without structured workflows. The human does all the work. Focus: Build prompt engineering fundamentals, document your workflow as boxes and arrows, and begin experimenting. |
| 36–49 | Approaching 3 | **Inflection Point** | You are building trust but haven't yet delegated full tasks. Focus: Pick one box in your workflow, define a task agent for it, refine until output is within 5% of what you would produce. |
| 50–63 | Stage 3 | **Task (Wave 2)** | AI executes single tasks independently. You review output. Focus: Build task agents for every remaining box. Learn where AI fails and encode boundaries. |
| 64–77 | Stage 4 | **Workflow (Wave 2)** | AI coordinates your full workflow with governance and quality gates. Focus: Refine governance, add combative agents, align team on shared workflow definitions. |
| 78–91 | Stage 5–6 | **Delegate & Coordinate (Wave 3)** | AI works outside your IDE. You manage multiple agents in parallel. Focus: Build isolation/merging practices, add organizational governance, shift identity to coordinator. |
| 92–105 | Stage 7–8 | **Supervise & Orchestrate (Wave 3)** | AI manages full pipelines with meta-orchestration. You define goals and approve. Focus: Optimize end-to-end pipelines, mentor others through earlier stages. |

---

## My Results

- **Total score:** 48 / 105 (average 2.3)
- **Stage:** Approaching Stage 3 — **Inflection Point**
- **Strongest dimension:** Scaling, Coordination & Supervision (3.3)
- **Weakest dimension / biggest growth opportunity:** Governance, Trust & Safety Nets (1.7)
- **Focus:** Pick one box in the workflow, define a task agent for it, and refine until output is within 5% of what I would produce. Add automated quality gates (tests, builds, coverage checks) that fire before agent output reaches me.
