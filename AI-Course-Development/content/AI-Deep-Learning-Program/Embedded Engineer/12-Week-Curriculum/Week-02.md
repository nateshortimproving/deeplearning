# Week 2 — Loop 1: Product/Process Role Focus
*No training session this week*

---

## Role Focus This Week
**Product/Process** — The Embedded Engineer's primary coaching energy remains on the Product/Process role's workflow. This week shifts from introduction to application: the `epics-and-stories` skill built in the workspace during Session 1 now needs to transfer to real stories from the team's actual backlog. The Embedded Engineer is still present with and available to the whole team.

---

## Embedded Engineer Coaching Priorities

- **Day 1:** Check in with Product/Process role members on their Session 1 takeaways. Pull up the `epics-and-stories` skill they committed in the workspace. Is it RTCC-structured with Context (WHY) and Constraints (HOW) filled in? Is it pointing at their real story format and domain? If not, fix that together first. The skill was built against sample stories in the workspace — now check whether its Context and Constraints reflect the team's real story format.
- **Day 2:** Transfer the skill to real work. Run `epics-and-stories` alongside the team on stories from their actual backlog — not the sample stories from the workspace, but the real stories going into the next sprint. The skill lives in the workspace; the real stories come from the team's actual backlog. Embedded Engineer circulates, coaches the transfer, doesn't take over.
- **Day 3:** Broaden participation. Each Product/Process role member should run their skill independently on at least one real story from their backlog. Embedded Engineer watches and notes where the output breaks down relative to their Evaluation Criteria (EC) — and where the workspace-built skill needs adjustment for the real codebase's story format.
- **Day 4:** Informal quality review. For each generated epics-and-stories output: evaluate it against the EC the participant wrote in Session 1. What's the score? What's the most common failure criterion? Capture notes. If the skill works on workspace sample stories but fails on real stories, that's the gap to close — adjust Context or Constraints accordingly.
- **Day 5:** Retrospective with the Product/Process members. What worked? What produced weak output? What would make the skill better? These observations become seed material for Python evaluation scripts in Session 4.

**Key Embedded Engineer priority this week:** Get the skill into real, used workflow through transfer. A committed epics-and-stories output from a real backlog story that went into the sprint and was accepted by the team beats five generated sets that were discarded or rewritten. The workspace is where the skill was built; the real backlog is where it needs to work.

---

## Participant Activities

### Product/Process Role
- Transfer the `epics-and-stories` skill from the workspace to real backlog stories: run it on at least 3 real sprint stories
- Evaluate each output against the EC written in Session 1 (specific, measurable criteria — not "does it look good")
- Identify the skill's most significant weakness on their specific story types — where does the workspace-built skill need adjustment for real stories?
- Capture notes for Embedded Engineer review

### Development Role
- Continue using and refining their Week 1 skill on real coding tasks
- Evaluate outputs against whatever EC they wrote in Session 1
- Note what's working and what isn't — bring observations to Session 2

### Testing Role
- Continue using and refining their Week 1 skill on real testing tasks
- Evaluate outputs against whatever EC they wrote in Session 1
- Note what's working and what isn't — bring observations to Session 2

---

## Artifacts Due by End of Week 2
- [ ] Epics & stories generated from real backlog stories (transferred from workspace) and used for at least 3 real sprint stories — Product/Process role members
- [ ] Evaluation notes for each generated set (which EC passed, which failed — not just "it seemed good")
- [ ] Notes on where the workspace-built skill needed adjustment for real stories
- [ ] Embedded Engineer notes on skill gaps and team friction points (internal)

---

## Embedded Engineer Coaching Notes

**On "used":** "Used" means the epics-and-stories output was accepted by the team and went into the sprint — not just generated and set aside. If the team generates output and then rewrites it manually, that's critical signal. Find out why: Is the skill wrong? Is the story format unusual? Is there a domain gap in the Context section? Don't let "AI wrote it but we ignored it" become a pattern. Remember: the skill was built against sample stories in the workspace — if it produces good output on sample stories but fails on real backlog stories, the gap is in the Context or Constraints (they need to reflect the real domain, not the sample domain).

**On the transfer model:** This week is the first full week of transfer coaching. The workspace taught the skill on sample stories; your job is to help participants make it work on their real stories. Don't do the transfer for them — coach it. When a real story breaks the skill, ask: "What's different about this story compared to the sample stories? What would need to change in Context or Constraints to handle this?"

**On EDD in practice:** Participants should be evaluating against their Session 1 EC this week, not just observing output. If someone says "it looked pretty good," ask: "Which of your EC did it pass? Which did it fail?" Push the discipline from informal to explicit.

**On the "it's faster to write it myself" objection:** This is often true in Week 2, and it's not wrong. Speed is not the point yet. The point is building the habit and then iterating toward quality. Name this explicitly: "You're right that it's faster right now. That's expected. The question is whether we can make this worth the time."

**On converting skeptics:** Don't argue with skeptics. Find one curious person and work with them first. Visible results convert faster than arguments.

**On over-enthusiasm:** Watch for participants who run their skill constantly but don't evaluate quality. Running lots of outputs isn't the goal. The goal is running outputs and knowing whether they meet the EC. If quantity is high and evaluation hasn't happened, redirect.

**On Dev and Testing roles this week:** They're not the primary focus but they shouldn't go dark. Check in briefly — are they using their skills? Are they evaluating against EC? Their observations at Session 2 will be more valuable if they've been actively trying things and noting failure modes.