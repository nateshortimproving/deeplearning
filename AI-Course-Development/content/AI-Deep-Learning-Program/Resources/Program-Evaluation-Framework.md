# Deep Learning Program (DLP) — Program-Level Evaluation Framework
*Improving Internal*
*Version: August 2026*

---

## Why This Exists

The DLP teaches participants to use Python evaluation scripts with LLM judges because it makes them rigorous about improvement rather than just change. We apply the same discipline to the program itself.

This document defines how Improving evaluates whether the DLP is working — not at the participant level (that's the completion rubric), but at the program level. It answers: *Are our Embedded Engineers effective? Are our training sessions landing? Are the design decisions we've made producing the outcomes we expect?*

This is a working document. It defines the data we collect, when we collect it, and how we use it.

---

## What We're Measuring

Three levels, each with a distinct question:

### Level 1 — Participant Outcomes
*Did participants move from Basic Prompting to DLP Completion?*

The primary outcome of the program. Measured via DLP Completion rates against all four behavioral Evaluation Criteria (Craft, Evaluate, Iterate, Adopt). An engagement succeeds when a substantial majority of participants meet all four Evaluation Criteria by Week 12.

This is the output we sell. It's also the outcome the executive sponsor defined as success at kickoff.

### Level 2 — Engagement Quality
*Did our Embedded Engineer and Trainer deliver the program effectively?*

Even when outcomes are good, we want to know whether the Embedded Engineer and Trainer contributed to those outcomes or whether participants succeeded despite the delivery. This level focuses on Embedded Engineer coaching effectiveness, Trainer session quality, and the Embedded Engineer–Trainer coordination that holds the program together.

### Level 3 — Program Design
*Are the materials and structure working as intended?*

If the same problem appears in multiple engagements — a session consistently doesn't land, a particular DLP Completion criterion proves harder to achieve than others, the 6-week loops create friction — that's a design signal, not a delivery signal. This level asks whether the program itself needs refinement.

---

## Data Sources

| Source | What It Tells Us | When Collected |
|--------|-----------------|---------------|
| Participant AI Adoption Maturity Assessments | Participant's own perception of progress across 7 dimensions (21 questions) | Week 1 (baseline), Week 7 (midpoint), Week 12 (completion) |
| Program Completion Rubric | Embedded Engineer + Trainer's joint external assessment of each participant | Week 12 |
| Participant feedback on Embedded Engineer | How participants experienced their Embedded Engineer's coaching | Week 7, Week 12 |
| Embedded Engineer weekly touchpoint notes | Embedded Engineer's running account of participant progress, challenges, design observations | Weekly (captured in touchpoint with Trainer) |
| Account Manager / Executive Coach executive sponsor feedback | Executive sponsor's perception of engagement value and organizational impact | Week 12 completion meeting |
| Embedded Engineer self-assessment of delivery | Embedded Engineer's own honest assessment of where they struggled to coach effectively | Week 12 |

### Notes on Data Quality

**AI Adoption Maturity Assessments reflect perception, not ground truth.** A participant who rates themselves high on the Adopt-related dimension may have changed a few skills without it becoming default behavior. The completion rubric — jointly assessed by Embedded Engineer and Trainer — is the more reliable signal. When the two diverge significantly, that's a data point worth investigating.

**Embedded Engineer weekly touchpoint notes are qualitative and informal.** They are valuable precisely because they are informal. Require the Embedded Engineer to maintain them, but don't over-engineer the format — brief running notes are more likely to be honest than a formal weekly report.

**Executive sponsor feedback is subject to relationship bias.** An executive sponsor who had a positive experience will say the program worked. Ask specific questions (see completion meeting agenda in the Account Manager / Executive Coach Guidance document) to get more useful signal.

---

## Per-Engagement Scorecard

Complete this template within 2 weeks of each engagement's completion. Owned by the Embedded Engineer and Account Manager / Executive Coach jointly. Submitted to the program manager (or designated program owner at Improving).

---

```
DLP ENGAGEMENT SCORECARD

Engagement ID: _______________
Client: _______________
Teams engaged: _______________
Embedded Engineer: _______________
Trainer: _______________
Account Manager / Executive Coach: _______________
Engagement dates: Week 1 ___________ → Week 12 ___________

---

PARTICIPANT OUTCOMES

Total participants (at kickoff): ___
Total participants (at completion): ___
Participants who completed all 4 DLP Completion Evaluation Criteria: ___  (___ %)

DLP Completion Criterion Rates:
  a. Craft (can create skills, adversarial agents):  ___ / ___ (___ %)
  b. Evaluate (uses Python evaluation scripts with LLM judges):        ___ / ___ (___ %)
  c. Iterate (evidence-driven, documented against EC):                ___ / ___ (___ %)
  d. Adopt (behavior change, skills are default):                      ___ / ___ (___ %)

AI Adoption Maturity Assessment — Average dimension scores at Week 12 (1–4):
  Dimension 1: ___   Dimension 2: ___   Dimension 3: ___   Dimension 4: ___
  Dimension 5: ___   Dimension 6: ___   Dimension 7: ___
  (DLP Completion indicator: Dimensions 1–4 averaging 3.0+)

Evaluation Criterion most commonly not achieved: _______________
Brief note on why: _______________

Participant attrition (left the program before Week 12): ___
Primary reason(s): _______________

---

CONCRETE ARTIFACTS PRODUCED

List artifacts participants committed to the client codebase by program end:
(Include type: skill, adversarial agent, custom harness, Python evaluation script)

1. _______________
2. _______________
3. _______________
(add rows as needed)

---

ENGAGEMENT QUALITY

Embedded Engineer Effectiveness (based on participant feedback, Week 7 + Week 12 combined):
  Overall Embedded Engineer rating (1–5): ___
  Notable strengths observed: _______________
  Notable gaps observed: _______________

Embedded Engineer Self-Assessment of Delivery (brief):
  Where did you coach effectively? _______________
  Where did you struggle? _______________
  What would you do differently? _______________

Trainer Session Quality (Embedded Engineer's assessment):
  Sessions that landed well: _______________
  Sessions that didn't land / needed supplementing: _______________

Embedded Engineer–Trainer Coordination:
  Did weekly touchpoints happen consistently? Yes / No / Mostly
  Notable issues with coordination: _______________

---

PROGRAM DESIGN OBSERVATIONS

Design gaps observed (materials missing, sequence issues, Evaluation Criteria definitions unclear):
_______________

Manager/org friction encountered:
_______________

Anything about the Loop 1 / Loop 2 structure that created problems:
_______________

Anything that worked better than expected:
_______________

---

ACCOUNT MANAGER / EXECUTIVE COACH NOTES

Executive sponsor feedback (qualitative):
_______________

Was the completion metric (DLP Completion %) understood and accepted by the executive sponsor? Yes / No
Notes: _______________

Recommended next step for this client: _______________

---

OVERALL ENGAGEMENT RATING

Embedded Engineer rating: Strong / Adequate / Needs improvement
Program design (this engagement): No significant gaps / Minor gaps / Design issues identified
Outcome: Full success (85%+ complete all 4) / Partial success (50–84%) / At risk (<50%)
```

---

## Cross-Engagement Learning

### Who Owns It
The **program manager** (or designated program owner at Improving) owns cross-engagement synthesis. This is not the Embedded Engineer's job after completing an engagement — they submit the scorecard and move on. The program manager aggregates, identifies patterns, and decides what changes.

### Cadence
- **After each engagement:** Scorecard submitted within 2 weeks of completion. Program manager reviews within 1 week of receipt.
- **Quarterly (or after every 3 engagements, whichever is sooner):** Program manager synthesizes scorecards into a design review. Identifies patterns. Brings proposed changes to the Trainer and a senior Embedded Engineer for review.
- **Annually:** Full program review. Design decisions revisited. Embedded Engineer profile requirements updated if needed. Training materials refreshed.

### What Gets Changed and How

Not every design observation from a single scorecard warrants a change. The threshold:

| Pattern | Action |
|---------|--------|
| One Embedded Engineer mentions a session didn't land | Note it; watch for recurrence |
| Two engagements report the same session gap | Flag for Trainer review; consider supplemental material |
| Three or more engagements show the same DLP Completion criterion gap | Investigate criterion definition, training alignment, and Embedded Engineer coaching approach; likely warrants a design change |
| Consistent attrition pattern (same weeks, same reasons) | Structural issue; prioritize for next quarterly review |

**Changes to training materials are owned by the Trainer.** The program manager identifies the need and the pattern; the Trainer decides the solution and owns the updated content.

**Changes to the Embedded Engineer playbook are owned by the program manager** in collaboration with a senior Embedded Engineer.

---

## Leading Indicators

These signals appear *during* the engagement — not at Week 12. The Embedded Engineer and Trainer should watch for them actively. Flag anything in this list to the Account Manager / Executive Coach immediately.

### Positive Signals (on-track indicators)
- **Participants bring real work to Embedded Engineer sessions without prompting** — they're integrating the program into their actual workflow, not treating it as separate
- **Embedded Engineer sessions are pull, not push** — Embedded Engineer is coaching participants who are already working; not re-teaching or demonstrating
- **Participants reference training content without the Embedded Engineer prompting it** — training is landing and being applied
- **First committed artifact appears by Week 4** — any participant has a committed skill with `disable-model-invocation: true` in the codebase; strong signal that Craft is activating
- **Participants start mentioning the program to people outside the cohort** — word is spreading; engagement quality is high

### At-Risk Signals
- **Embedded Engineer sessions are optional-feeling** — participants cancel, reschedule, or come unprepared
- **No artifacts by Week 7** — the midpoint review arrives with nothing in the codebase; either Embedded Engineer coaching or participant motivation is not producing real outputs
- **AI Adoption Maturity Assessment baseline is lower than expected** — if Week 1 assessments show participants who thought they were at Basic Prompting discover they're below even that level, the program may not be the right fit for this cohort
- **Participants treat sessions as training, not coaching** — they want to be taught, not to work. This surfaces as lots of questions about "the right way" rather than testing approaches and iterating.
- **Embedded Engineer is covering for participants** — Embedded Engineer produces artifacts as examples, and participants aren't replacing them with their own work
- **DLP Completion criterion "Adopt" lags all others significantly at midpoint** — the hardest criterion to move late; if it hasn't budged by Week 8, it almost certainly won't move by Week 12 without active intervention
- **Embedded Engineer and Trainer touchpoints are being skipped** — weekly coordination breaking down is an early signal that the Embedded Engineer is overwhelmed or isolated

### When to Escalate a Leading Indicator
If two or more at-risk signals are present simultaneously by Week 7, this should trigger an unscheduled Account Manager / Executive Coach conversation and a considered decision about whether to alert the executive sponsor.

---

## Program Maturity Threshold

The DLP is **proven and ready to scale** when we have evidence of the following:

### Minimum Evidence Required

| Criterion | Threshold |
|-----------|-----------|
| Engagements completed | At least 5 full 12-week engagements with different clients |
| Participant outcome consistency | 75% or higher DLP Completion rate (all 4 Evaluation Criteria) across at least 3 of 5 engagements |
| Multi-Embedded-Engineer replication | At least 3 different Embedded Engineers have delivered the program successfully (not all outcomes from one Embedded Engineer) |
| Design stability | No major structural changes required after Engagement 3; material refinements only |
| Artifact production | Documented artifacts in client codebases across at least 3 engagements (demonstrates transfer, not just assessment improvement) |
| Executive sponsor satisfaction | Positive completion-meeting feedback from at least 4 of 5 executive sponsors; at least 2 have made a referral or expanded the engagement |

### What "Ready to Scale" Enables
- We can confidently represent DLP Completion rates to prospective clients
- We can certify Embedded Engineers with an established track record behind the certification
- We can publish a repeatable delivery model and train new Embedded Engineers against it without relying on tribal knowledge
- We can begin conversations about program licensing or white-labeling if appropriate

### What It Doesn't Mean
Ready to scale does not mean the program is finished. The evidence threshold authorizes scaling — it does not eliminate the obligation to continue measuring and refining.

---

## Version Notes

*This framework should be reviewed and updated by the program manager after each quarterly synthesis. If more than 6 months pass without a review, flag it — the program is either inactive or the evaluation discipline has lapsed.*