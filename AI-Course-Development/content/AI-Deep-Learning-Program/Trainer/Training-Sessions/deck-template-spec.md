# DLP Slide Deck Template Specification

*General structure for all DLP v2 session slide decks. This file describes the slide types, their required elements, and the constraints the design harness must follow when generating decks from `.deck.md` prompt files. No session-specific content is included here — each session's `.deck.md` file provides the content; this file defines the structure.*

---

## Purpose

DLP v2 decks are generated from `.deck.md` prompt files by a design harness. This specification defines the slide types, their required elements, and the rules the harness must follow. The design harness reads a `.deck.md` file and this specification, then produces a `.pptx` deck that conforms to the structure defined here.

---

## Slide Types

Every deck is composed of the following slide types. Each `.deck.md` file specifies which slides to include and what content goes on them. The design harness is responsible for the visual layout, formatting, and design — the prompt file provides the content and structure, not the visual treatment.

### Required Slides (every deck must have these)

#### 1. Intro Slide

The opening slide of every deck.

**Required elements:**
- Session title
- Week number
- Loop number (1 or 2)
- Role focus (Product/Process, Development, or Testing)
- One-line framing: what this session is about and why it matters now

**Purpose:** Orient participants immediately. They should know within 10 seconds what session they're in, where it sits in the program, and why it matters today.

---

#### 2. Check-In Slide

A discussion prompt that connects prior work to this session.

**Required elements:**
- One or more check-in questions
- A brief note (in speaker notes or small text) on what the question is setting up

**Purpose:** Bridge from the prior session or prior weeks of work into today's content. This is a discussion prompt, not a content slide. The instructor asks the question; participants answer.

**Rules:**
- The question must connect to prior work (previous session's artifacts, EC scores, observations from the field)
- The question must set up the current session's content
- It is not a rhetorical question — participants are expected to answer

---

#### 3. Session Goals Slide

The goals of the session, annotated per role.

**Required elements:**
- Each session goal listed clearly
- For every goal, a line for each role (Product/Process, Development, Testing) explaining how that goal is relevant to that role
- If a goal does not apply to a role, say so explicitly and explain why it still matters to them

**Rules:**
- No goal is role-agnostic. Every goal must have a line for each of the three roles.
- If a goal genuinely doesn't apply to a role, write "Not directly applicable, but relevant because [reason]" — never leave a role's line blank.
- The per-role annotations should be specific, not generic. "Helps you understand the pipeline" is too vague; "Your stories are the input to this skill, so understanding how it works makes you a better story author" is specific.

**Purpose:** Every participant sees themselves in every session. The all-roles-present principle is enforced structurally, not just by invitation.

---

#### 4. Closing Slide

The bookend to the Session Goals Slide.

**Required elements:**
- Each session goal revisited
- For each goal, a per-role takeaway: what did Product/Process get, what did Development get, what did Testing get
- The takeaways should be reflection prompts, not summaries — they should make participants think about what they're leaving with, not just confirm what was covered

**Rules:**
- Must match the goals from the Session Goals Slide — same goals, same per-role structure
- Takeaways should be in the voice of the participant ("You now understand..." / "You've built..."), not the instructor ("We covered...")
- This is not a summary slide. It is a reflection prompt that closes the loop on the goals.

---

### Content Slides (used throughout the deck as needed)

#### 5. Exercise Slide

Every lab or hands-on exercise in the session gets an Exercise Slide.

**Required elements:**
- **Lab Name** — clear, descriptive title
- **Lab Timing** — how long the lab takes (e.g., "45 minutes")
- **Lab Steps** — the steps participants follow, as a numbered list
- **"You'll know when you're done because..." footer** — a specific, checkable success criterion

**Rules for the "You'll know when you're done because..." footer:**
- Must be specific and checkable — not "you'll have learned something" but "you'll have a committed skill file with a load-bearing audit completed and at least 3 sample-story outputs evaluated against your EC"
- Must reference a concrete artifact or observable outcome, not a feeling or understanding
- If the lab produces a committed artifact, the footer should name what gets committed and what must be true about it

**Purpose:** Participants should be able to look at the Exercise Slide and know exactly what to do, how long they have, and how to tell when they're finished — without asking the instructor.

**Optional element — Stretch Goals:**

If the session `.md` file includes a "Stretch Goals (for advanced users)" subsection for a lab, the Exercise Slide should include a **Stretch Goals** section. This section is optional — not every lab has stretch goals, and labs without them should not include an empty stretch goals section.

**Required elements when present:**
- **Label:** "Stretch Goals (for advanced users)" — clearly labeled so participants know this is optional, not required
- **1–2 advanced challenges** — specific, actionable extensions beyond the base lab, not vague encouragement
- Each stretch goal should build on the base lab's output (e.g., "using the skill you just built, also add...") not be a separate unrelated task

**Rules for Stretch Goals:**
- Stretch goals must be visually distinct from the base lab steps — e.g., a separate boxed section, different background color, or clearly delineated area. Advanced participants should be able to spot them immediately; other participants should be able to ignore them without confusion.
- Stretch goals are not required for completion. The "You'll know when you're done because..." footer applies to the base lab only. If a stretch goal has its own completion criterion, it should be stated separately and clearly marked as optional.
- Stretch goals should be challenging enough to engage participants who would otherwise finish early and disengage, but achievable within the lab's time allotment by someone who is already comfortable with the base material.
- If the design harness renders stretch goals, they should appear after the "You'll know when you're done because..." footer, not before it — the base lab is the default; stretch goals are the extension.

---

#### 6. Demo Slide

Every demonstration in the session gets a Demo Slide.

**Required elements:**
- **Description** — what is about to be demonstrated and how it relates to the learning goals. This explains the *why* and the *what*, not the *how*. No step-by-step instructions on the slide — the instructor does those live.
- **"What to focus on" section** — tells participants what to watch for during the demo

**Rules:**
- Do NOT include step-by-step instructions on the slide. The instructor performs the demo live; the slide tells participants what to watch for, not how to do it.
- The "What to focus on" section should direct participants' attention to the learning moment, not the mechanics. "Watch how the evaluator catches a failure the instructor didn't anticipate" is good. "Watch the instructor type the command" is not.
- The description must connect to at least one session goal — the demo is not entertainment, it's a learning vehicle

**Purpose:** Focus participants' attention during the demo. Without guidance, participants watch the instructor's actions; with guidance, they watch the learning moment.

---

#### 7. Compare/Contrast Slide

A slide showing the shift from left-side bad behaviors to right-side good behaviors.

**Required elements:**
- Two columns: left side = the behavior being left behind, right side = the behavior being adopted
- Each row is a single behavior shift (e.g., "Writing prompts ad-hoc → Writing skills with RTCC structure")

**Hard constraint: maximum 5 items.** If there are more than 5 contrasts to draw, split into two slides or pick the 5 most important. This is a hard limit, not a guideline.

**Rules:**
- The left side should describe a real behavior participants actually have, not a strawman. "Writing prompts ad-hoc" is real. "Using AI without thinking" is a strawman.
- The right side should describe the DLP discipline replacement, not an aspiration. "Writing skills with RTCC structure" is a discipline. "Being thoughtful about AI use" is an aspiration.
- Each row should be parallel in structure — both sides should be the same type of statement (a behavior, a practice, a tool choice)

**Purpose:** Make discipline shifts visible and memorable. The left-right visual makes the change concrete in a way that prose does not.

---

#### 8. Lecture Slide

For presentation and teaching blocks.

**Required elements:**
- Only what we want the students to learn — the key concepts, definitions, or principles

**Rules:**
- Do NOT include slide formatting, layout instructions, or visual design notes. Leave it to the design harness to craft the slides as appropriate from the learning content.
- A lecture block might be one slide or several; the `.deck.md` prompt should describe the content, not the visual treatment
- Include only the learning content — the facts, concepts, definitions, principles, or frameworks participants need to understand
- Do not include teaching instructions, pacing notes, or "say this to the class" text — that goes in the session `.md` file's trainer notes, not on the slide

**Purpose:** Teach a concept clearly. The design harness decides how to present it visually; the prompt file provides the content.

---

## Deck Structure Rules

### Ordering

1. Intro Slide (always first)
2. Check-In Slide (always second)
3. Session Goals Slide (always third)
4. Content slides in session order (Lecture, Demo, Exercise, Compare/Contrast as the session content dictates)
5. Closing Slide (always last)

### What Does NOT Go on Slides

- Trainer notes or teaching instructions
- Step-by-step demo instructions (the Demo Slide describes what and why, not how)
- Timing for non-lab blocks (lab timing goes on Exercise Slides only)
- Speaker notes (these go in the PPTX speaker notes section, not on the slide face)
- Session logistics (room location, break times, etc.)

### Content Source

The companion `.md` file for each session is the authoritative content source. When there is any discrepancy between the `.deck.md` prompt and the session `.md` file, the `.md` file wins. The deck prompt is the structure specification; the session markdown is the content specification.

---

## Design Harness Notes

- The design harness should produce a `.pptx` file from the `.deck.md` prompt file using the slide types defined here
- The design harness has full control over visual design: layout, colors, fonts, imagery, animations, transitions
- The design harness should NOT add content that is not in the `.deck.md` prompt file
- The design harness should respect the Improving brand guidelines (see `.agents/skills/improving-brand/` in the repository)
- The hard limit of 5 items on Compare/Contrast slides is non-negotiable
- The "You'll know when you're done because..." footer on Exercise Slides must be visually distinct (e.g., boxed, colored, or set apart from the steps) so participants can find it quickly