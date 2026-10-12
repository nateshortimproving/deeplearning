# AI Bootcamp — Week 4: Coaching Readiness & Certification Gate

---

## Timing

- **Monday–Friday:** 9:00 AM – 5:00 PM with 1-hour lunch (7 hours each day)

---

## Objectives

By end of Week 4, the candidate is cleared for Deep Learning Program (DLP) engagement — meaning they can:

- Deliver the player-coach model in a live pairing session with a Basic Prompting-level developer
- Recognize the difference between real adoption and polite compliance
- Handle the four most common resistance patterns (skeptic, over-truster, identity-protective senior, management blocker)
- Explain EDD, RTCC (WHO/WHAT/WHY/HOW), the load-bearing rule, and the Prompt/Harness/Model framework clearly to a developer who has never heard of any of them
- Produce artifacts that a client can use after the Embedded Engineer is gone
- Articulate the full DLP arc: two 6-week loops, 6 Trainer sessions landing at weeks 1/3/5/7/9/11, the introduce-then-reinforce cadence, the transfer model (workspace to real codebase), and the Stage 3 to Stage 4 trajectory
- Operate their half of the two-person delivery model: Trainer touchpoints, escalation rules, and the Week 12 joint rubric
- Pass the Certification Gate

---

## Monday (9:00 AM – 5:00 PM): The Player-Coach Model

### 9:00 – 11:00 AM — What the Player-Coach Is (and Isn't)

An Embedded Engineer is not a trainer, not a consultant, and not a developer-for-hire. They are a player-coach: they do real work *alongside* the client team, making the learning visible in the actual codebase.

**Key discipline:** A chapter ahead, not a textbook ahead. The Embedded Engineer operates at the edge of their own capability, not from a position of complete mastery. This is honest, and it is what makes the coaching credible.

Exercise: Read the EE Playbook (`../AI-Deep-Learning-Program/Embedded Engineer/EE-Playbook.md`), the field-tested coaching plays from Wave 1 Embedded Engineers: Rough Process Mapping, Divide and Conquer, Goals → Measures → Actions, An Exercise After Each Workshop, Build Your Own SDLC Pipeline, Everyone Gets a Turn at Show-and-Tell, One Meeting One Artifact, and Cross-Pollination. These are the moves that worked on real engagements.

Discussion: Which two plays would you reach for first, and why? Which play addresses a failure mode you have seen on your own teams? What does "good Embedded Engineer presence" look like vs. what fell short?

Discussion: What is the difference between a developer who has learned something and one who is being politely compliant? What does polite compliance look like in practice? How do you distinguish it from real adoption?

### 11:00 AM – 12:00 PM — Teaching EDD and RTCC to a First-Time Learner

Weeks 1–3 were about doing these disciplines. This week is about teaching them. An Embedded Engineer must be able to explain EDD, RTCC, and the load-bearing rule to a developer who has never encountered formal prompt structure.

**Exercise:** Prepare a 10-minute explanation of EDD — specifically the Red/Green/Refactor analogy and the load-bearing rule — for a developer who is comfortable with TDD but has never thought about prompts as something you can test. No slides. No jargon from this program. Just clear explanation with a concrete example.

Deliver it to a colleague or instructor. Debrief: what landed? What confused?

### 12:00 – 1:00 PM — Lunch

### 1:00 – 3:00 PM — Teaching the Earn-the-Next-Step Principle

A client team will ask: "why aren't we letting the model invoke these skills automatically and automating this yet?" The Embedded Engineer needs a clear, non-defensive answer that speaks to evaluation evidence, the graduation criteria, and the automation spectrum without making the developer feel like they are being held back.

**Exercise:** Prepare a 5-minute explanation (no slides, conversational) of:

- Why the DLP starts with skills that have `disable-model-invocation: true`, invoked explicitly
- What the three graduation criteria are for enabling model invocation, and why 3+ documented EDD iteration cycles must come first
- Why adversarial agents and bounded agents come after evaluation evidence exists, at a conceptual level, without getting into implementation

Deliver it. Debrief: did it feel like a clear answer or a rationale? There is a difference.

### 3:00 – 5:00 PM — Artifacts: Are They Transferable?

Concept: Every artifact the Embedded Engineer commits must survive their departure. A skill file that only works because the Embedded Engineer is there to explain it is not a passing artifact.

**Artifact review checklist:**

- Is it committed and in the right location?
- Does it have a comment header explaining what it is, what it does, and when to use it?
- Does the comment header reference the EC test file so someone can verify it?
- Has it been tested by someone other than the Embedded Engineer?
- Would a new developer on this team know it exists and know how to use it?

Begin applying this checklist to your Week 1–3 artifacts. Note failures. These will be fixed on Day 3.

---

## Tuesday (9:00 AM – 5:00 PM): Resistance Scenarios

Four scenarios, approximately 45–60 minutes each including debrief.

For each scenario: the Embedded Engineer candidate plays the Embedded Engineer role. A program manager or peer plays the developer or manager. Run the scenario, then debrief before moving to the next.

### Scenario 1: The Skeptic

Developer doesn't believe AI improves their workflow. Not hostile, just unpersuaded. They've tried it, got mediocre results, and moved on. They are willing to engage but are not going to change their behavior based on faith.

How do you get them to try something real without turning it into a debate? The EDD and RTCC disciplines are your tools here — a skeptic responds to evidence, not enthusiasm.

**Debrief focus:** Did the candidate try to persuade? Or did they build a test the skeptic could run themselves?

### Scenario 2: The Over-Truster

Developer ships AI output without review. They love it. They're moving fast. They're producing more than anyone else on the team. They're also accumulating invisible debt: tests that pass because they test what the AI generated, not what the requirement asked for; documentation that is fluent but wrong; code that compiles but has subtle logic errors the AI confidently introduced.

How do you slow them down without making them feel punished for enthusiasm? The EDD discipline — specifically the load-bearing test concept — is your lever here.

**Debrief focus:** Did the candidate address the enthusiasm positively while introducing the rigor? Or did they come across as skeptical of AI, which would be wrong and counterproductive?

### Scenario 3: The Identity-Protective Senior

Senior engineer who has built their identity on deep technical knowledge. AI tools feel like a challenge to their value — as if the thing they spent years mastering can now be approximated by a tool anyone can use. They are not hostile. They are careful, thorough, and skeptical of shortcuts.

How do you engage them without triggering defensiveness? The key: EDD and RTCC are engineering disciplines. The senior engineer's instinct for rigor is exactly what makes them valuable here — if you can frame it correctly.

**Debrief focus:** Did the candidate treat the senior's skepticism as a resource or a problem? Skepticism from a senior engineer that is channeled into good test case writing is an asset.

### Scenario 4: The Management Blocker

Manager is skeptical or actively interfering — "we don't have time for this right now" or "just teach them to use Copilot and move on." They are not hostile to AI in general; they are protecting their team's delivery commitments and they see the DLP as a distraction.

How do you navigate this without burning the relationship? The DLP's artifacts-over-advice and real-work-not-exercises design principles are directly relevant here — the Embedded Engineer is not running workshops, they are committing things to the codebase.

**Debrief focus:** Did the candidate make the business case? Or did they try to explain the program's philosophy, which the manager does not care about?

### 12:00 – 1:00 PM — Lunch (between scenarios as schedule allows)

---

## Wednesday (9:00 AM – 5:00 PM): The DLP Operating Model and Artifact Handoff Preparation

### 9:00 – 10:30 AM — The DLP Operating Model

An Embedded Engineer never delivers a DLP alone. The engagement is a two-person model: the Trainer delivers 6 four-hour sessions (weeks 1, 3, 5, 7, 9, 11) and the Embedded Engineer is the daily presence for all 12 weeks. The cadence is **introduce → reinforce**: each session lands at the start of a 2-week block, participants leave with a working artifact, and the Embedded Engineer spends the following two weeks coaching the transfer of that artifact from the shared student workspace to the client's real codebase.

Walk through the operating commitments from the EE Implementation Guide (`../AI-Deep-Learning-Program/Embedded Engineer/EE-Implementation-Guide.md`):

- **The weekly Trainer touchpoint (30 min, every week, all 12 weeks).** The Embedded Engineer owns the invite. Fixed agenda: participant pulse (2–3 specific observations), one coaching challenge, participant questions, one real artifact example from the week, session prep for anything coming in the next 1–2 weeks. Documented in field notes within 24 hours.
- **The `[PROGRAM FEEDBACK]` loop.** When something in the program design does not work for this client, capture it in touchpoint notes with the `[PROGRAM FEEDBACK]` label. This is how the program improves; silence is how it stagnates.
- **Escalation rules.** If it requires changing how the client manages the engagement (manager discouraging participation, participants pulled from sessions, scope creep), escalate to the Account Manager or Executive Coach, same day, not at the weekly touchpoint. If it is a coaching or technical blocker (tool access, repository permissions), the Embedded Engineer owns it with a 24-hour fix target. Participant resistance is never escalated; it is coached.
- **The posture shift.** Loop 1 (weeks 1–6): lead more, demonstrate, pair closely. Loop 2 (weeks 7–12): coach independence, ask more and show less, do not rescue. The **independence checks at Weeks 8 and 10** (the team runs the full workflow with the Embedded Engineer absent) are the objective test of whether the posture shift worked.
- **The Week 12 close.** The Program Completion Rubric is completed jointly with the Trainer: each assesses independently against Craft, Evaluate, Iterate, Adopt, then align. The **handoff document** records each skill's transfer status: "transferred and in use," "transferred but needs iteration," or "workspace-only, not yet transferred." Participants exit with **commitment statements**: specific, observable, next-sprint behavior changes.

Discussion: which of these commitments would be easiest to let slip under client pressure? What protects it?

### 10:30 AM – 12:00 PM — Apply the Handoff Checklist

Return to the artifact checklist from Monday. Apply it to every artifact from Weeks 1–3. Fix what fails. The bar: could you hand this artifact to a developer who just joined the client team — someone who was not in this pre-program training — and would they be able to use it correctly?

Specific checks:

- Every skill file has a comment header: what it does, when to use it, what the expected input format is, where the EC test file lives
- Every Python evaluation script is committed alongside the skill it evaluates (in `evaluations/`), not separately
- Every adversarial agent prompt documents what it is designed to find and the severity scale it uses, not just in your head
- The load-bearing audit results are recorded: for each removed instruction, note what EC justified the removal

### 12:00 – 1:00 PM — Lunch

### 1:00 – 3:00 PM — Behavior Change Checkpoint

This is the hardest part of the certification gate, and the most important.

The question is not "did you build things?" You built things. The question is: **did you change how you work?**

For each artifact you are submitting, answer:

- Is this artifact in your actual daily workflow now, or did you build it for this program?
- When did you last use it? What was the task?
- If you were not in this program, would you still use it?

The program manager will ask you to screen-share a normal work session during Day 4 or Day 5. They will watch you work. If you instinctively reach for old habits and only use the artifacts when prompted, that is detectable. It is not a pass.

### 3:00 – 5:00 PM — Rehearsal Preparation

Tomorrow you will run a simulated pairing session with a colleague playing a Basic Prompting-level developer. Prepare for it today:

- Review the AI Adoption Maturity Assessment (7 dimensions, 21 questions) to understand where a Basic Prompting participant typically scores. You will complete this same assessment as part of the Certification Gate, where the target is 3.0+ averages on dimensions 1–4 and a total in the 43–58 range
- Read the sustainment guides (`../AI-Deep-Learning-Program/Resources/Sustainment/`), especially the Managers guide's "real adoption vs. performance" checklist. This is the sharpest available lens for the polite-compliance problem from Monday: what a team looks like when adoption is real, and what it looks like when it is theater. You will coach managers toward the real column
- Decide which skill from your artifact set is the right one to introduce in a first pairing session, and why
- Prepare how you will introduce EDD to someone who has never heard of it — not as a lecture, but as a live activity

You will not have a script. Prepare by thinking, not by writing.

---

## Thursday (9:00 AM – 5:00 PM): Rehearsal Engagement

### 9:00 AM – 10:30 AM — Simulated Pairing Session

Run a simulated 90-minute "Week 1 Day 1" pairing session with a colleague playing a Basic Prompting-level developer.

The colleague should:

- Use Basic Prompting behaviors (off-the-shelf prompts, no structure, no evaluation, full trust in AI output)
- Ask realistic questions ("why do we need test cases if the AI output looks good?")
- Resist where a real developer would resist, but not be hostile
- Refer to the AI Adoption Maturity Assessment for calibration

The Embedded Engineer candidate facilitates without a script. Their goal in this session is not to teach the whole program — it is to get the developer to do one EDD cycle on one real task from their actual work.

### 10:30 – 11:30 AM — Debrief

Structured debrief with the colleague and instructor:

- What worked? Where did the developer engage?
- Where did the candidate default to telling rather than coaching?
- Where did the candidate lose the developer?
- Did the candidate get to EDD, or did they spend the whole session on RTCC setup?
- If the developer left this session and came back tomorrow, what would they do differently?

### 11:30 AM – 12:00 PM — Adjustments

Based on the debrief: what would you do differently in the first 15 minutes? Revise your approach and briefly demonstrate the adjusted opening.

### 12:00 – 1:00 PM — Lunch

### 1:00 – 3:00 PM — Behavior Change Observation

Program manager observes the candidate doing a normal work task — ideally something genuinely from their current real work, not a constructed exercise. The candidate works naturally, without narrating.

The observer notes: which artifacts are used? Which are not? Does the candidate run manual test cases before building, or after? Does the candidate perform the load-bearing audit, or is that only something they do when reminded?

Debrief afterward: what the observer saw, not what the candidate thought they did.

### 3:00 – 5:00 PM — Final Artifact Review and Submission Preparation

Review the full certification gate checklist. Identify any outstanding items. For any item that is incomplete, commit to a specific completion time before the end of Day 5.

---

## Friday (9:00 AM – 5:00 PM): Certification Gate

### 9:00 AM – 12:00 PM — Final Submission and Candidate Self-Assessment

Candidates finalize and submit all artifacts. The written self-assessment against DLP Completion criteria (Craft, Evaluate, Iterate, Adopt) must be submitted by 12:00 PM.

**Self-assessment guidance:** For each criterion, provide:

- One specific artifact that demonstrates this criterion
- One specific example of using it in real work (not a program exercise)
- An honest assessment of where you are still developing

### 12:00 – 1:00 PM — Lunch

### 1:00 – 3:00 PM — Reviewer Evaluation

Program manager reviews submitted artifacts and self-assessment. Candidate is available for questions.

### 3:00 – 5:00 PM — Certification Gate Decision and Feedback

---

## Certification Gate

To be cleared for DLP engagement, the Embedded Engineer candidate must submit:

### Artifacts (all committed, all passing handoff checklist)

These mirror what the EE Implementation Guide requires of a certified Embedded Engineer: at least one skill with `disable-model-invocation: true`, one Python evaluation script with an LLM judge, and one adversarial agent prompt, all built personally.

**From Weeks 1–2 (EDD and RTCC):**

- [ ] Manual EC test file (Input Prompts + Expected Outputs) written before the skill was built (at least one, Trend Identification or equivalent; commit order will be checked)
- [ ] Four RTCC skill files from the Week 1 pipeline (Trend ID, Ideation, Development, Graphics), with `disable-model-invocation: true`
- [ ] Python evaluation scripts with baseline + 3+ iteration results and documented hypotheses for at least 3 skills
- [ ] Load-bearing audit documentation: at least 2 skills with removed instructions documented
- [ ] Seven SDLC skill files from Week 2, built out from the DLP student-workspace skeletons, all with completed Context (WHY) and Constraints (HOW)
- [ ] Upstream quality dependency trace: at least one documented case

**From Week 3 (Invocation, Adversarial Agents, Bounded Agents):**

- [ ] One skill graduated to invocation-enabled, with the three graduation criteria documented and invocation test cases (3 positive trigger, 2 negative, 2 quality), OR a written gap specification explaining what the skill has not yet earned
- [ ] One adversarial agent prompt with documented findings, plus an evaluator-vs-adversarial comparison on the same outputs
- [ ] One bounded agent run: a chained pipeline executed in a single session with evaluation at the checkpoints

### Documentation
- [ ] Automation spectrum assessment: written evaluation of artifacts against the v2 spectrum criteria (invocation-disabled skills → invocation-enabled skills → adversarial agents → bounded agents → custom harnesses)
- [ ] Earn-the-next-step explanation paragraph (manager-audience, coaching-ready)
- [ ] Behavior change reflection: which artifacts are in active daily use, with evidence
- [ ] Artifact handoff review: checklist completed for all artifacts

### Demonstrated Skills
- [ ] Python evaluation demonstrated live, not explained: run a script, interpret the results, state what change the results justify
- [ ] Player-coach session observed or recorded (Thursday rehearsal)
- [ ] All four resistance scenario role plays completed (Tuesday)
- [ ] EDD explanation delivered to a non-expert and debriefed (Monday)
- [ ] Behavior change observation session completed (Thursday)
- [ ] Written self-assessment against DLP Completion criteria (Craft, Evaluate, Iterate, Adopt)
- [ ] AI Adoption Maturity Assessment scored as part of the gate: target 3.0+ averages on dimensions 1–4, total score in the 43–58 range

### Reviewer Decision
- **Pass** — Cleared for DLP engagement
- **Conditional pass** — Cleared with specific remediation items to complete before solo engagement
- **Not yet** — Specific gaps identified; recommended path to resubmission

---

## Coaching Notes for Program Managers

- The certification gate is a gate, not a formality. A candidate who is not ready should not be deployed. The client and the program's reputation depend on it.
- The most common reason for "not yet": behavior change has not actually happened. The candidate built things but did not change how they work. This is detectable — the Thursday behavior change observation session exists specifically to catch it. An artifact that has not been used since the week it was built is not a DLP Completion artifact.
- The second most common reason: EC test files that were written after the skill, not before. Check commit timestamps. The discipline of EDD is violated the moment you build before you define success, even if the test file looks right after the fact.
- A conditional pass must have a specific, time-bound remediation plan. "Keep improving" is not a plan. Name the artifact, the specific gap, the specific fix, and the date by which the fix must be submitted and reviewed.
- The player-coach simulation is not a performance — it is a diagnostic. A candidate who delivers a polished presentation is not necessarily ready to coach someone who is confused, resistant, or distracted. Look for adaptability, not fluency.
- A candidate who built strong artifacts but cannot explain the v2 automation spectrum, or where adversarial agents fit in it, will struggle the first time a client team asks "can we automate more of this?" Probe the spectrum verbally during the review. Fluency here is a gate criterion, not a nice-to-have.
