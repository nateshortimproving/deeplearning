# Post-Program Sustainment Guide — Executive Sponsors

*For executive sponsors of the Deep Learning Program (DLP)*
*Improving AI Transformation | August 2026*

---

Your organization just completed the Deep Learning Program. This guide is written for you — the person who approved and funded this engagement — to help you understand what was delivered, how to assess whether it's holding, and what comes next if you want to continue building.

---

## 1. What Was Delivered

The program moved a team of developers, product/process people, and testers from **Basic Prompting to DLP Completion** on Improving's AI Maturity Model.

Here is what that means in practical terms:

**Before the program (Basic Prompting):** Your team was using AI tools off-the-shelf — GitHub Copilot, ChatGPT, or similar — in an ad-hoc way. Useful for one-off tasks, but not systematically integrated. No shared tooling. No discipline around whether it was getting better or worse. No institutional knowledge in the codebase about how to use AI for your team's specific work.

**After the program (DLP Completion):** Your team now owns committed AI artifacts — skill files, Python evaluation scripts with LLM judges, and adversarial agents — that live in your codebase and encode how to use AI effectively for your specific development tasks. These artifacts have been built, tested, evaluated against measurable Evaluation Criteria (EC), and iterated on. The team understands the discipline: you don't change a skill because it gave a bad result once. You run your evaluation script, form a hypothesis, test it, and commit the improvement with documentation.

**What is in your codebase now that wasn't before:**
- AI skills encoding expert knowledge about generating epics and stories, planning implementations, and reviewing code — tailored to your team's standards
- Python evaluation scripts with LLM judges that function like a test suite for your AI tooling — providing a measurable baseline so you can know if things are improving or degrading
- Adversarial agents that challenge the output of primary skills, catching problems the evaluation scripts didn't anticipate
- Custom harness awareness — participants saw a custom harness demoed in Session 6 and understand the trajectory to Stage 4 (Workflow)
- Documented iteration histories showing how those artifacts improved over the 12 weeks

**What changed in how the team works:**
For the tasks these artifacts were built around, AI assistance is now default behavior, not occasional use. The team has a method for extending this to new tasks. They know how to evaluate, iterate, and commit improvements — not just write better prompts.

---

## 2. Return on Investment Framing

The honest framing at this stage is trajectory, not payoff — because the full value of DLP Completion compounds over 6–18 months, not in the first 90 days after the program ends.

**What you can measure now:**
- Velocity on the tasks the artifacts were built for. If the team automated epics-and-stories generation with a high-quality, evaluated skill file, the time per story that requires detailed Acceptance Criteria should be measurably lower.
- Reduction in back-and-forth on handoffs between roles. DLP Completion artifacts were built around Product/Dev/Testing handoff points — the places where ambiguity costs the most time. Look there first.
- Artifact adoption rate — are the skill files, evaluation scripts, and adversarial agents actually being used in production work, or sitting in the repo?

**What you're building toward:**
The deeper return is institutional AI capability. You now have a team that understands how to build and maintain AI tooling for your specific context. That's a durable organizational asset — particularly as AI capabilities continue to evolve. Teams that have this discipline will extend it. Teams that don't will continue buying point solutions and hoping for the best.

**What the trajectory looks like:**
DLP Completion compounds if the behaviors are maintained. A team that keeps iterating on its artifacts for six months will have meaningfully better tooling than it has today — and will be capable of extending to multi-step, cross-role custom harnesses via a future Stage 4 Deep Learning Program. A team that stops iterating will have slowly degrading tooling and will plateau.

The program created the capability. Whether it returns full value depends on what happens in the next six months.

---

## 3. What Requires Continued Investment to Sustain

DLP Completion is not self-sustaining without organizational conditions that support it. Here is what those conditions are:

**Manager buy-in and time protection**

The behaviors that define DLP Completion — evaluating skills with Python evaluation scripts, iterating on artifacts, maintaining the codebase — require dedicated time. Not much, but consistent. If managers are measuring team output purely on feature velocity and treating AI tooling as optional personal preference, the discipline will erode. The managers of your DLP participants need to understand what DLP Completion looks like, protect the time it requires, and treat AI artifact maintenance as real work on the backlog.

If those managers have not already received guidance on this, they should. A separate guide for managers is available as part of this package.

**Artifact maintenance as an ongoing commitment**

AI models update. Team processes evolve. Skill files and Python evaluation scripts that work today will require maintenance over time — the same way any software dependency requires maintenance. This should be visible on the engineering backlog, not treated as optional cleanup work.

**A peer accountability structure on the team**

The Embedded Engineer was an external accountability mechanism. The team needs an internal one now. This can be as simple as two participants with a standing biweekly check-in on what they iterated. It doesn't require investment — but it requires that managers don't inadvertently destroy informal peer structures by over-scheduling or constant re-prioritization.

---

## 4. Continued Adoption: Extending the Core DLP Skills

Your team can now see the next horizon from where they're standing. Here is what continued adoption looks like and what it would take.

**What continued adoption means:**

Continued adoption means extending the core DLP skills to multi-step business processes spanning multiple people's work. Not one person's IDE workflow — an end-to-end process where AI is doing substantive, evaluated work at each step, the output of each step is explicitly designed to be the input of the next, and the quality is consistent enough to operate without human review at every handoff.

Examples of continued adoption targets:
- A fully automated Story → Epics → Plan → Code → Review pipeline implemented as a custom harness, where each step uses its own skill, evaluated against its Evaluation Criteria (EC) with a Python evaluation script and LLM judge, with structured handoffs between steps — this is Stage 4, demonstrated in Session 6
- Automated code review against your specific standards, using adversarial agents to challenge the review skill's output, with structured output that feeds into developer feedback workflows
- A requirements-to-test-coverage pipeline that spans Product, Dev, and QA without manual translation at each handoff

**What it would take:**

Extending to multi-step processes is a design project before it's an implementation project. It requires:
- Identifying one high-value, end-to-end process where handoff quality or coordination overhead is the bottleneck
- Mapping the steps, defining what "good output" looks like at each step (the EC), and explicitly designing the interfaces between steps
- Building and iterating each step's skill and adversarial agent to production quality
- Building a custom harness — a Python program that orchestrates multiple model calls, passes artifacts between steps, evaluates each step, and manages the overall workflow (Stage 4 Deep Learning Program)
- Coordinating across roles — Product, Dev, and Testing all have a stake in the chain

The team you have is capable of doing this work. They lack experience at that level of complexity and coordination. That's where structured support adds the most value.

**Assessing readiness:**

Your team is ready to extend when:
- The DLP Completion artifacts are stable, actively maintained, and actually used in daily work
- At least a few participants have completed multiple iteration cycles on their own initiative, without external prompting
- There is a clear candidate process — one that is pain-producing enough to justify the investment and bounded enough to succeed in a focused engagement

**Improving's role:**

Extending to custom harnesses is a different engagement than the DLP. It's the Stage 4 Deep Learning Program — targeted at a specific process, not capability-building across the board. We work with you to identify the right target, design the pipeline, embed with the team through the build-and-iterate phase, and transfer ownership of a production-grade, fully evaluated custom harness.

---

## 5. What to Watch For

These are the signals worth paying attention to over the next 90 days.

**Leading indicators that adoption is holding:**
- Artifact commit history in the repo shows regular updates — skills, evaluation scripts, and adversarial agents are being iterated, not just sitting at their Week 12 state
- Your engineering managers can tell you what the team's AI artifacts do and which ones are actively in use
- When you ask a participant to walk you through a recent story, they describe AI tooling as a natural part of how they worked it — not something they pulled out for a demo
- The team is asking questions about extending their skills to new processes — they're looking forward

**Leading indicators that adoption is fading:**
- No commits to skills, evaluation scripts, or adversarial agents since the program ended
- Managers describe the program as "something the team did" rather than "how the team works now"
- Sprint retrospectives don't mention AI tooling — it's not part of the vocabulary
- The people who were least engaged during the program are the reference point for the team's behavior rather than the people who were most engaged

**Organizational signals worth attention:**
- A manager who is consistently deprioritizing iteration time or treating AI artifacts as optional — this is the most common failure mode and it's worth addressing directly and early
- Turnover among program participants — if the people who built the artifacts leave, the institutional knowledge goes with them unless the documentation and peer practices are strong
- A major model or tooling change that the team is handling by switching tools rather than iterating on existing artifacts — a sign that the discipline didn't fully take

---

## 6. Next Steps with Improving

The program is complete, but the engagement doesn't have to be. Here are the options worth considering:

**Custom harness design and implementation**
A targeted engagement around a specific multi-step business process. We work with your existing DLP-completed team to design, build, and transfer ownership of a production-grade custom harness — a Python program that orchestrates skills, evaluation scripts, and adversarial agents into a multi-step workflow. Typical timeline: 8–12 weeks depending on process complexity. This is the highest-leverage next step if your DLP adoption is strong. This is the Stage 4 Deep Learning Program.

**Second team cohort**
If you have additional teams that would benefit from the DLP, running a second cohort makes use of your internal DLP Completion practitioners as peer resources — people who can speak credibly to what the discipline looks like inside your specific context. Second cohorts often move faster than first cohorts for exactly this reason.

**Program expansion**
If the DLP ran on one team and you want to scale to the organization, we can design a scaled program that uses your internal practitioners as part of the delivery model — reducing external dependency and accelerating adoption across multiple teams.

**Advisory and check-in**
If you want structured progress visibility without a full new engagement, we can set up quarterly advisory sessions — reviewing artifact health, assessing DLP Completion maintenance, and identifying candidates for continued adoption when the time is right.

The right next step depends on where your team is in 90 days. The best way to assess that is to have a direct conversation with your Account Manager or Executive Coach.

---

*Deep Learning Program | Improving*
*Contact your Account Manager or Executive Coach to discuss continued engagement.*