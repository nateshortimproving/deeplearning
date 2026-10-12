# Embedded Engineer Implementation Guide
*Embedded Engineer Operational Playbook — Deep Learning Program (DLP) Engagement*

> **You are the daily presence.** The Trainer delivers 6 sessions across 12 weeks. You are there every week, embedded with client teams, coaching the work as it happens. This guide tells you how to run the engagement.

---

## Before Week 1: Pre-Engagement Prep

Complete the following in the 5–7 business days before your first week on-site.

### Stakeholder Identification Checklist

- [ ] Confirm who the Account Manager or Executive Coach is for this engagement — this is your escalation contact for anything above team-level
- [ ] Get the list of participating teams (e.g., Website team, CRM team) from the Account Manager or Executive Coach — not role groups, actual named client teams
- [ ] Identify the team lead or manager for each participating team
- [ ] Know who the executive sponsor is (even if you won't interact with them directly — the Account Manager or Executive Coach owns that relationship)
- [ ] Identify any team members who may be skeptical or have been flagged as resistant

### Client Context Checklist

- [ ] Read any discovery notes or pre-engagement materials the Account Manager or Executive Coach has shared
- [ ] Understand the client's current tech stack and AI tooling (if any)
- [ ] Know what "Basic Prompting" (off-the-shelf AI use) looks like in this client's context
- [ ] Confirm which AI tools are approved/available for participants to use during the engagement
- [ ] Confirm that API keys are available for Python evaluation scripts and LLM judges (the Account Manager / Executive Coach handles provisioning — content assumes keys are available)

### Artifact Environment Setup Checklist

- [ ] Set up or confirm access to the artifact repository (where participants will commit their work)
- [ ] **Confirm the shared student workspace is ready** — the workspace repo contains all 7 SDLC skeleton skills (`skills/`), demo outputs (`demo-outputs/`), sample stories (`sample-stories/`), and empty directories for participant artifacts (`evaluations/`, `adversarial-agents/`, `harness-specs/`). This is the only thing participants need to clone for Session 1.
- [ ] Confirm how the workspace will be shared with participants — clone the repo, copy the subdirectory, or create a class-specific repo from the workspace
- [ ] Verify all participants have commit access to the workspace repo before Week 1
- [ ] Verify all participants can clone the workspace and open it in their IDE before Session 1 (setup friction should be near-zero)
- [ ] Prepare baseline skill templates (epics-and-stories skill template, plan-story skill template) so participants have a starting point at Session 1 — these are already in the workspace's `skills/` directory
- [ ] Confirm the SDLC skeleton skills are available in the workspace (all 7 with `disable-model-invocation: true`)
- [ ] Document where artifacts live and share the location with your Trainer before Session 1

### First Contact with Your Trainer

- [ ] Schedule your standing weekly 30-minute touchpoint — you own this recurring calendar invite
  - Cadence: every week for all 12 weeks
  - Timing: schedule it *before* Week 1 so it doesn't slip
- [ ] Share the client context with your Trainer: participating teams, tech stack, any known sensitivities
- [ ] Confirm Session 1 logistics: room, materials, participant list, time
- [ ] Align on what "ready to work with the Embedded Engineer immediately after Session 1" looks like for this cohort

### Your Own Readiness Check

- [ ] You have completed the AI Bootcamp and hold DLP Completion certification
- [ ] You have personally built and evaluated at least one skill with `disable-model-invocation: true`, one Python evaluation script with an LLM judge, and one adversarial agent prompt
- [ ] You can demonstrate Python evaluation (not just explain it) — the AI writes the code, you direct and evaluate
- [ ] You know the DLP Completion criteria cold: Craft, Evaluate, Iterate, Adopt
- [ ] You understand the Prompt/Harness/Model framework and can explain it to participants
- [ ] You are familiar with the 21-question, 7-dimension self-assessment instrument and can explain what each dimension measures to participants
- [ ] You understand the RTCC structure as WHO (Role) → WHAT (Task) → WHY (Context) → HOW (Constraints)
- [ ] You understand the EC/AC distinction: Evaluation Criteria (EC) = quality bar for skill output; Acceptance Criteria (AC) = product artifact, what a story must satisfy

---

## Weekly Rhythm: What a Typical Week Looks Like

Your week has four ongoing activities. Not all happen every day, but all happen every week.

### Daily: Embedded Coaching

You are physically (or virtually) present with client teams as they do actual work. This is not a class. You are coaching the transfer of skills from the shared student workspace to the real codebase.

**The transfer model is the coaching frame.** Sessions teach skills in the workspace — every participant works with the same sample stories, the same skeleton skills, and the same demo outputs. Your job between sessions is to help participants take the skills they built in the workspace and apply them to the client's actual codebase. The workspace is the training ground; the real codebase is the application.

**Each day on-site:**
- Identify 1–3 participants to pair with or observe (in breakout rooms or via screen share)
- Ask: "Have you tried using the skill from the workspace on a real story from your backlog?" — the transfer is the coaching work
- Watch for moments where their workflow could incorporate an AI step — the workspace skill, adapted for their real context
- When you pair, make the participant the driver; you are the navigator
- Note which participants are engaging with the transfer and which are hanging back
- If a skill works on workspace sample stories but fails on real stories, that's the coaching material — the gap is in Context or Constraints

**Do not:**
- Do the work for participants
- Run unsolicited demos (save those for the right moment, not as default)
- Let a week pass without touching base with every participant at least once
- Let participants stay in the workspace indefinitely — the transfer to the real codebase is the goal

### Weekly: Artifact Review and Commits

Participants should be committing artifacts throughout the week. Your job is to review and respond.

- Review new commits within 48 hours
- Leave specific feedback — not "looks good" but "this skill's Context section is missing the WHY — what intent is this skill serving?"
- Flag any participant with zero commits for a direct conversation (not an email — a conversation)
- Commit your own field notes: what you observed this week, what's working, what's not

**Artifact commit expectations (yours):**
- Weekly field notes: committed by end of week (Friday or equivalent)
- Participant progress notes: committed same day as your weekly Trainer touchpoint

### Weekly: Trainer Touchpoint (30 min, you own the schedule)

See the full protocol in the next section. This happens every week, no exceptions.

### Weekly: Participant Progress Self-Assessment

Before your Trainer touchpoint each week, do a mental (or written) roll-call:

For each participant, ask yourself:
- Have they committed at least one artifact this week?
- Are they asking better questions than last week?
- Have they adopted any new behavior — even one small thing — as default?
- Is there anything blocking them that I haven't addressed?

If someone is two weeks without meaningful progress, that is a signal — address it directly before it becomes a problem.

---

## Trainer Touchpoint Protocol

**Owner:** You (Embedded Engineer) own scheduling. You send the invite. You keep it on the calendar.

**Frequency:** Every week for all 12 weeks, including session weeks.

**Duration:** 30 minutes.

### What to Bring to Every Touchpoint

Come prepared. This is not a check-in — it is a working conversation.

1. **Participant pulse** — 2–3 specific observations: who is making progress, who is stuck, who surprised you
2. **A coaching challenge you're facing** — one thing you're unsure how to handle with a specific participant
3. **Questions from participants** — anything that came up in the week that you weren't confident answering
4. **Artifact examples** — bring one real artifact from the week (good or problematic) to review together
5. **Upcoming session prep** — if a session is in the next 1–2 weeks, flag what you're seeing in the field that the Trainer should incorporate

### What to Listen for from Your Trainer

- How to handle the coaching challenge you raised
- Adjustments to the next session based on what you've reported
- Feedback on your coaching approach (are you leading too much? not enough?)
- Whether anything you've described warrants escalation

### How to Document

After every touchpoint, commit a brief note (5–10 lines is fine) to your field notes:
- Date
- What you shared
- What the Trainer's guidance was
- Any action items for you before next week
- Any program design feedback captured (see below)

### Program Design Feedback Loop

If something in the program structure isn't working — a session concept didn't land, participants are confused about something specific, an artifact template is wrong for this client's context — capture it explicitly in your touchpoint notes with the label `[PROGRAM FEEDBACK]`. This feeds into program improvement cycles.

---

## Escalation Guide

**Rule of thumb:** If it requires changing how the client manages the engagement, it goes to the Account Manager or Executive Coach. If it requires changing how you coach, you handle it.

### Escalate to Account Manager or Executive Coach

| Situation | Why |
|-----------|-----|
| A manager is actively discouraging participation | You are not in a position to change organizational dynamics |
| A manager is pulling participants out of training sessions | This threatens program outcomes and requires an executive-level conversation |
| Participation rates are dropping and you've already addressed it with participants directly | Pattern of absence suggests org-level pressure |
| Executive sponsor alignment appears to have shifted | Account Manager or Executive Coach owns that relationship |
| You are being asked to scope-creep (do work that isn't DLP coaching) | Account Manager or Executive Coach needs to reset expectations |

**How to escalate:** Message or call your Account Manager or Executive Coach directly. Give them the specific situation, what you've already tried, and what outcome you need. Do not wait for your weekly touchpoint — some of these need same-day response.

### Handle Directly: Participant Resistance

Participant skepticism is normal and is your domain to address. Do not escalate individual participant attitude — coach it.

| Participant behavior | How to handle |
|---------------------|--------------|
| "I tried AI and it didn't work" | Ask them to show you what they tried. Get specific. Find the actual failure point. |
| "This takes longer than just doing it myself" | Agree — it does at first. Ask them what it would be worth if it were faster than doing it themselves. |
| "My skill is fine, I don't need to evaluate it" | Ask: "How do you know it's improving rather than just different?" |
| Silent disengagement | Direct 1:1 conversation — not in a group. Ask what's in the way. Listen before advising. |
| Openly arguing that AI is useless | Don't debate. Ask what would change their mind. Seek the real concern. |

### Handle Directly: Technical Blockers

If a participant can't access a tool, a model, or a repository — that's yours to solve. Don't wait for Trainer alignment.

- Fix access issues within 24 hours
- If you can't fix it yourself, escalate to whoever owns IT/tooling access at the client — not to the Account Manager or Executive Coach
- Document the blocker and resolution in your field notes

---

## Artifacts the Embedded Engineer Owns

### What You Commit

| Artifact | Where | By When |
|----------|-------|---------|
| **Weekly field notes** | `/artifacts/ee-field-notes/week-NN.md` | End of each week |
| **Participant progress notes** | `/artifacts/ee-field-notes/participant-progress-week-NN.md` | Before weekly Trainer touchpoint |
| **Trainer touchpoint notes** | `/artifacts/ee-field-notes/trainer-touchpoint-week-NN.md` | Within 24 hours of touchpoint |
| **Participant artifact reviews** | Comment in participant's artifact file or separate `/artifacts/ee-reviews/` folder | Within 48 hours of participant commit |
| **Week 12 handoff document** | `/artifacts/ee-handoff.md` | By end of Week 12 |
| **Program completion rubric** | Co-authored with Trainer | Week 12, before final Account Manager / Executive Coach call |

### Field Notes Format

Your weekly field notes do not need to be polished. They need to be honest.

```markdown
## Week NN Field Notes

**Observations this week:**
- [Participant name]: [what you saw]
- [Team/context]: [what you noticed]

**Coaching moments:**
- [What happened, what you tried, what the outcome was]

**What's working:**
- [Specific behavior changes you observed]

**What's not working:**
- [Stalls, confusion, resistance patterns]

**[PROGRAM FEEDBACK]:** (if applicable)
- [What the program got wrong for this context]
```

---

## Loop 1 vs Loop 2 Embedded Engineer Posture

The engagement runs in two 6-week loops. Your posture changes between them.

### Loop 1 (Weeks 1–6): You Lead More — Building in the Workspace, Transferring to the Real Codebase

In Loop 1, participants are learning the language and the basic mechanics. They have not yet built real artifacts. Your job is to make the path visible and walk it with them. Sessions teach in the workspace; your job between sessions is to coach the transfer to the real codebase.

**Loop 1 is about building out the SDLC skeleton pipeline.** Session 1 introduces all 7 skeleton skills and participants build out `epics-and-stories` in the workspace. Session 2 builds out `plan-story` and `implement-story` in the workspace. Session 3 builds out `review-implementation` in the workspace. Each skill is a skill with `disable-model-invocation: true` — participants invoke via slash command. They add Context (WHY) and Constraints (HOW) using EDD discipline: write EC first, run baseline, iterate, load-bearing audit. **Between sessions, you coach the transfer**: participants take the workspace-built skills and apply them to real stories from the team's actual backlog. The workspace is the training ground; the real codebase is where the skills need to work.

**Posture:**
- You demonstrate more often — show what good looks like (in the workspace, then on a real story)
- You pair closely, especially in the first two weeks — on both the workspace build-out and the transfer to real stories
- You give direct feedback on artifact quality
- You answer "how do I do this?" questions directly
- You create psychological safety for experimentation
- You coach the transfer explicitly: "This skill works on the sample story in the workspace. Now let's try it on a real story from your backlog. What's different?"

**Watch for:** participants who are going through the motions without internalizing — they produce artifacts in the workspace but haven't changed their default behavior on the real codebase. This is the primary Loop 1 failure mode. Also watch for participants who are comfortable in the workspace but never transfer — the workspace is the training ground, not the destination.

**Your own development:** Loop 1 is also where you deepen your own coaching instincts. The AI Bootcamp got you functional. Weeks 1–6 of the engagement are where you build the judgment needed for Loop 2's harder coaching work. Pay attention to what's hard for you, not just what's hard for participants.

### Loop 2 (Weeks 7–12): You Coach Independence — Transfer of Evaluation, Adversarial, and Harness Skills

By Week 7, participants have 6 weeks of artifacts. They have attended 3 training sessions. They have no excuse for not knowing what the expected behavior looks like. Your job shifts to coaching self-sufficiency. The transfer model continues — sessions teach evaluation, adversarial, and harness skills in the workspace; your job is to coach the transfer of these skills to the real codebase.

**Loop 2 is about deepening discipline with new tooling.** Session 4 introduces Python evaluation scripts with LLM judges (AI writes the code, participants direct and evaluate) — built in the workspace, then transferred to evaluate real skill output. Session 5 introduces model invocation (enabling `disable-model-invocation: false` on well-validated skills) and adversarial agent prompts (AI challenges AI) — built in the workspace, then applied to real codebase outputs. Session 6 has participants build a bounded agent (full SDLC pipeline run in the IDE with manual evaluation and adversarial review at key steps) and the instructor demos a custom harness (Python program with clean context per step and evaluation at each step). The bounded agent lab is hands-on; the custom harness is demonstrated, not assigned.

**Posture:**
- Ask more, show less
- When someone asks "how do I do this?", ask "what have you tried?"
- Push participants to review each other's artifacts
- Start fading your daily presence (if appropriate for the client context)
- Hold participants accountable to their own commitments — don't rescue them

**Watch for:** participants who are still dependent on you for every skill decision. If someone can't iterate without you in Week 9, that's a signal — name it and address it directly.

**Shift that should be visible by Week 12:** Participants are correcting their own skills before asking you. They reference their Python evaluation output. They can explain why a skill is better, not just that it is. They run adversarial agents against their output and act on what the agents find. **And critically: their skills are running against the real codebase, not just the workspace.** The transfer from workspace to real codebase is complete — the workspace was the training ground, and the real codebase is where the skills now live and produce value.

---

## Week 12 Close

### Final Weeks Checklist (Weeks 11–12)

- [ ] Confirm all participants have at least one complete artifact cycle: original skill → evaluated with Python evaluation script → iterated → adopted
- [ ] Review your full set of field notes and identify gaps in documentation
- [ ] Complete your section of the Program Completion Rubric (do this before the joint review with Trainer)
- [ ] Schedule the joint rubric review with your Trainer
- [ ] Draft the handoff document (see format below)
- [ ] Confirm final touchpoint with Account Manager or Executive Coach is scheduled
- [ ] Administer or confirm the Week 12 AI Adoption Maturity Assessment (21-question, 7-dimension instrument) has been sent to participants

### Handoff Document

The handoff document is the deliverable that outlives the engagement. It should tell the next person what's here.

**Include:**
- List of participants and their completion status against DLP Completion rubric
- Summary of what each team (not each participant) is now capable of
- Artifacts that represent the best work produced during the engagement
- Known risks: participants who passed the rubric but whose adoption feels thin
- Recommendations for follow-up or continued support
- A one-page executive summary for the Account Manager or Executive Coach to use with the sponsor

### Program Completion Rubric

The rubric is completed jointly with your Trainer in Week 12. You each assess independently first, then align.

**Rubric dimensions** (based on DLP Completion criteria):

| Criterion | What you're looking for |
|-----------|------------------------|
| **Craft** | Participant has built at least one skill and adversarial agent in their actual work context |
| **Evaluate** | Participant uses Python evaluation scripts with LLM judges — not just intuitively, demonstrably |
| **Iterate** | There is documented evidence of hypothesis → result → improvement on at least one artifact |
| **Adopt** | New AI-assisted behavior is default behavior, not a special-occasion behavior |

For each participant: rate each criterion as **Met / Partial / Not Met** with one line of evidence.

**Self-assessment corroboration:** Cross-reference rubric ratings against participants' Week 12 self-assessment scores. Participants who have achieved DLP Completion should be scoring 3.0+ averages on Dimensions 1–4 of the 7-dimension instrument (Prompt Engineering & AI Interaction, Task Agents & Single-Box Automation, Workflow Orchestration & Coordination, and Output Evaluation & Quality Judgment), with a total score in the 43–58 range. Significant gaps between rubric ratings and self-assessment scores are worth discussing in the joint Trainer review.

### Final Account Manager / Executive Coach Touchpoint

Before the engagement closes, you and your Trainer should both be on a call with the Account Manager or Executive Coach.

**What you own in that call:**
- Participant outcomes summary
- Notable wins and risks
- Your honest assessment of program effectiveness for this cohort
- Any follow-on work recommendations (this is a sales input, but it should be honest)

---

## Additional Resources

- **[EE Playbook](EE-Playbook.md)** — Field-tested coaching plays from Wave 1 Embedded Engineers. Practical techniques for process mapping, team dynamics, exercises, and cross-pollination. Use what fits your engagement.

---

*This guide is a working document. If something in the program design is wrong for your engagement, document it in your field notes with `[PROGRAM FEEDBACK]` and surface it in your next Trainer touchpoint.*