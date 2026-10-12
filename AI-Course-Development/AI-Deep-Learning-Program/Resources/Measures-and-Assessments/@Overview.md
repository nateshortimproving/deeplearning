# Measures & Assessments — Overview

---

## Purpose

Every stage of the Deep Learning Program (DLP) has structured evaluation. This section contains:

1. **AI Adoption Maturity Assessment** — a 21-question, 7-dimension instrument administered at Week 1 (baseline), Week 7 (midpoint), and Week 12 (completion)
2. **Embedded Engineer Participant Feedback** — for participants to evaluate their Embedded Engineer (quality of coaching, knowledge, presence)
3. **Program Completion Rubric** — the final evaluation of participant achievement at Week 12
4. **Trainer Session Feedback** — post-session evaluation of training quality

---

## Evaluation Philosophy

- **Assessment is not self-grading.** The AI Adoption Maturity Assessment is a reflection and measurement tool, not a score to optimize. Embedded Engineers use it to calibrate conversations, not to rubber-stamp completion.
- **Participant feedback on the Embedded Engineer matters.** The Embedded Engineer's job is to change behavior, not to be liked. Feedback should capture both how much learning happened *and* how the coaching experience felt — these can diverge, and both are useful signals.
- **Completion is behavioral, not knowledge-based.** A participant who can describe the DLP outcomes but hasn't changed their default behavior has not achieved DLP Completion. The rubric reflects this.

---

## Terminology

- **Evaluation Criteria (EC)** — the quality bar for a skill's output. Participants write EC before building or iterating on a skill, then measure whether the skill's output meets the EC. The term "Evaluation Criteria" or "EC" is used consistently throughout — never "success criteria" or bare "criteria."
- **Acceptance Criteria (AC)** — the product artifact: what a story must satisfy to be considered done. The AC generation skill produces these.
- **Skills** — every artifact participants build is a skill file using the skill format. Skills with `disable-model-invocation: true` are invoked via slash command; skills with invocation enabled can be auto-invoked by the model.
- **Python evaluation scripts with LLM judges** — the primary evaluation mechanism. Participants write (with AI assistance) Python scripts that evaluate skill outputs against EC, using LLM judges for criteria that require judgment.
- **Adversarial agents** — AI prompts designed to challenge, critique, and find weaknesses in the output of a primary skill. Adversarial agents catch semantic failures that deterministic checks cannot.
- **Custom harnesses** — Python programs that orchestrate multiple model calls, pass artifacts between steps, evaluate each step, and manage multi-step workflows. Demoed by the instructor in Session 6; building one is the work of a future Stage 4 Deep Learning Program. The progression from single skills to custom harnesses is the v2 automation spectrum.

---

## Files
- [AI-Adoption-Maturity-Assessment](AI-Adoption-Maturity-Assessment.md) — AI Adoption Maturity Assessment reference (21 questions, 7 dimensions; full instrument is a separate document)
- [EE-Participant-Feedback](EE-Participant-Feedback.md) — Participant evaluation of Embedded Engineer
- [Program-Completion-Rubric](Program-Completion-Rubric.md) — Week 12 formal completion assessment