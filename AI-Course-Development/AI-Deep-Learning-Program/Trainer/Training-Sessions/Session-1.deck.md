# Session 1 Deck Prompt — SDLC Skeletons + Epics & Stories (v2)
*Week 1 | Loop 1 | Role Focus: Product/Process*

---

## Intro Slide

**Title:** SDLC Pipeline + Epics & Stories
**Week:** 1 | **Loop:** 1 | **Role Focus:** Product/Process
**Framing:** Today you'll see the full SDLC pipeline you'll build over the next 3 sessions. You'll learn what makes AI work possible — Prompt, Harness, and Model. And you'll build your first skill: epics-and-stories, the foundation that everything downstream depends on.

---

## Check-In Slide

**Question:** Before we start: when you use AI today, what exactly are you using? Where does the AI end and your tool begin? Think about what the AI can and cannot do on your machine.

*This question sets up the Prompt/Harness/Model definition and surfaces assumptions participants bring into the program.*

---

## Session Goals Slide

**Goal 1: Understand Prompt, Harness, and Model as distinct concepts**
- **Product/Process:** The AI can only do what your tool allows. When you ask for epics and stories, the harness determines what context the AI can see and what it can produce.
- **Development:** The harness is the capability boundary — it determines what files the AI can read, what commands it can run, and how output reaches you. Everything you build in this program runs inside a harness.
- **Testing:** The harness mediates everything — evaluation, output, and integration. Your review skills will only work within the harness's boundaries.

**Goal 2: See the full SDLC pipeline and understand the 7 skeleton skills**
- **Product/Process:** You'll see demo PRD, Architecture, and UX outputs — these are the upstream artifacts that feed into your epics-and-stories skill. Understanding the pipeline means understanding where your work fits.
- **Development:** You'll see where Plan and Code (which you'll build in Session 2) fit in the pipeline. The epics-and-stories output is your input.
- **Testing:** You'll see where Review (which you'll build in Session 3) fits. The full pipeline ends with review — that's your domain.

**Goal 3: Build the epics-and-stories skill using RTCC and EDD**
- **Product/Process:** This is your primary artifact. You'll add Context (WHY good stories matter) and Constraints (HOW stories should be formatted for your team) to the RT-only skeleton. You'll iterate on it for 12 weeks.
- **Development:** Understanding how stories are generated makes you a better consumer of them when planning and coding.
- **Testing:** Understanding how stories are generated tells you what to look for when reviewing implementations against them.

**Goal 4: Write Evaluation Criteria (EC) before building the skill**
- **Product/Process:** Your EC define what good epics-and-stories output looks like. This is NOT the same as the Acceptance Criteria (AC) inside the stories — EC evaluates the skill's output quality; AC is what the story must satisfy.
- **Development:** Seeing how EC is written teaches you the discipline you'll apply to your Plan and Code skills in Session 2.
- **Testing:** EC for epics-and-stories is the pattern you'll follow when writing EC for your review skill in Session 3.

---

## Lecture Slide — Prompt, Harness, Model

**Content to teach:**

Three terms define everything in this program:

**Prompt** — The instructions you give to a model. What you want it to do, how you want it done, what constraints it must follow.

**Harness** — The software environment that mediates between you and the model. The harness determines what the model can actually do on your machine. It decides what files the model can read, what commands it can run, what tools it has access to, and how its output reaches you. Claude Code, Devin, GitHub Copilot, and the ChatGPT web interface are all different harnesses with different capabilities and different boundaries.

**Model** — The AI itself. The model generates text based on its training and the prompt it receives. But the model cannot do anything on your box that the harness does not offer or allow it to. A model without a harness is a chat interface. A model with a harness can read files, run commands, and produce artifacts. The harness is the capability boundary; the model is the intelligence; the prompt is the instruction.

---

## Lecture Slide — Skills with `disable-model-invocation: true`

**Content to teach:**

Everything we build in this program is a **skill** — a structured file using RTCC format that lives in the student workspace and can be invoked by anyone on the team.

We start every skill with `disable-model-invocation: true`. The skill only runs when you explicitly invoke it via slash command — the model will not auto-invoke it based on context.

Later in the program (Session 5), we'll discuss when and why to enable model invocation — letting the model decide when to trigger a skill automatically. But we start with explicit invocation because you need to understand what your skill does before you trust the model to decide when to use it.

---

## Lecture Slide — The SDLC Pipeline

**Content to teach:**

This program is built around 7 SDLC skeleton skills. Each is an RT-only stub — Role and Task are defined, but Context (WHY) and Constraints (HOW) are intentionally empty. Your job across Sessions 1-3 is to build them out using EDD discipline.

The pipeline:
1. create-prd → Product requirements
2. create-architecture → System architecture
3. create-ux → UX design guidance
4. create-epics-stories → Epics and stories breakdown ← **Session 1 builds this**
5. plan-story → Story planning ← **Session 2 builds this**
6. implement-story → Story implementation ← **Session 2 builds this**
7. review-implementation → Implementation review ← **Session 3 builds this**

Today you'll see demo outputs for steps 1-3 (PRD, Architecture, UX). These show what RT-only stubs produce without Context and Constraints — and the gaps are the lesson. Then you'll build out step 4: epics-and-stories.

**YAML pipeline note:** Each skill writes to a specific file that the next skill reads — this is the YAML pipeline that connects the 7 skills into a chain. The epics-and-stories skill writes its output to `stories.yaml`. Session 2's plan-story skill will read that file as its input. Understanding the handoff between skills is part of understanding the pipeline.

---

## Demo Slide — RT-Only Skeleton Outputs

**Description:** The instructor runs the RT-only create-prd, create-architecture, and create-ux skeleton skills against a realistic feature ("Pantry Tracker PWA") and shows the demo outputs. This demonstrates what the pipeline produces when Context and Constraints are empty — the output looks plausible but has gaps, wrong assumptions, and missing domain-specific detail. This connects to the learning goals by making the WHY of Context and Constraints concrete: without them, the model guesses, and the guesses are wrong.

**What to focus on:** As the demo outputs appear, notice what the model assumed that nobody told it to assume. Notice what's missing — domain detail, team standards, specific format requirements. These gaps are what you'll fix when you add Context (WHY) and Constraints (HOW) to your epics-and-stories skill.

---

## Lecture Slide — RTCC Prompt Structure

**Content to teach:**

Every skill in this program uses RTCC structure — four elements, each answering a different question:

- **R — Role (WHO):** Who is the model acting as? A specific, credentialed persona that changes tone, vocabulary, and default assumptions.
- **T — Task (WHAT):** What should they do? Verb-first, unambiguous, the specific action to perform.
- **C — Context (WHY):** Why do we want this done? What outcome are we trying to achieve? What problem are we solving? Context is the intent behind the task — the purpose that shapes how the model interprets its role and task.
- **C — Constraints (HOW):** What data, rules, and specifications does the model need? What background information is relevant? What rules must the output follow? What should it never do? What format is required? Constraints absorb the data and rules that define what the output must account for.

Why this order matters: WHO and WHAT define the contract — who is doing what. WHY gives it purpose — why are we doing this at all. HOW provides the data and rules — the constraints the output must satisfy. Adding data before establishing purpose produces outputs that have information but miss the intent.

---

## Lecture Slide — EDD: Define Your Evaluation Criteria Before You Build

**Content to teach:**

Before building out the epics-and-stories skill, participants write their **Evaluation Criteria (EC)** — the quality bar for the skill's output.

**Why this matters:** If you define EC after seeing the output, the model has already shaped your expectations. Writing EC first forces an honest definition of the target before you see whether it was hit.

**Acceptance Criteria (AC)** = the product artifact, what a story must satisfy. This is what the epics-and-stories skill produces inside each story.

**Evaluation Criteria (EC)** = the quality bar for the skill's output. This is what you write before building the skill.

These are different things. Your EC defines what good epics-and-stories output looks like. Your AC is the output itself — the criteria inside each story.

---

## Compare/Contrast Slide — Basic Prompting vs. DLP Completion

| Basic Prompting | DLP Completion |
|---|---|
| Ad-hoc prompts, never committed | Skills with RTCC structure, committed to repo |
| No way to know if changes improve or just change | EC written first; evaluation is non-negotiable |
| AI used occasionally, off-the-shelf | AI-assisted work is default behavior |
| No shared artifacts across the team | Skills are transferable, repeatable, shareable |
| "It seemed better" is the quality bar | Documented iteration cycles with evidence |

---

## Demo Slide — What Good Epics and Stories Look Like

**Description:** The instructor shows 3 examples of epics and stories from the `sample-stories/` directory in the student workspace: one good (`pantry-inventory.md` / `shopping-list.md` — clear AC, testable, edge cases covered), one vague (`vague-pantry-stories.md` — plausible-sounding but untestable, missing AC detail, no edge cases), and one AI-generated-without-care (`ai-generated-pantry-stories.md` — polished-sounding but AC describe implementation detail like PostgreSQL/JWT/Redux, epics too large, edge cases missing). This demonstrates what the epics-and-stories skill should produce and what it shouldn't. The demo connects to learning goals by making the quality bar concrete before participants build their own skill.

**What to focus on:** As the demo runs, notice the difference between "plausible-sounding but untestable" and "specific and testable." Watch for what AI gets wrong: stories without clear acceptance criteria, epics that are too large, missing edge cases.

---

## Exercise Slide — Lab 1: IDE Setup + Rules File

**Lab Name:** IDE Setup + Rules File
**Lab Timing:** 20 minutes
**Lab Steps:**
1. Configure your agentic IDE of choice (Claude Code, Devin, GitHub Copilot, or equivalent)
2. Create a project-level rules file that gives the AI context about your codebase, team conventions, and domain
3. Verify the tool is running and the rules file is committed
4. If you hit setup issues, pair with someone in your breakout room

**You'll know when you're done because...** you have a running agentic IDE with a committed rules file that gives the model context about the student workspace.

**Stretch goal:** configure a project-level rules file with specific TypeScript/React conventions for the Pantry Tracker PWA — naming patterns, ShadCN/Tailwind usage, Express route conventions, and strict-mode settings that go beyond the minimum workspace-structure rules.

---

## Exercise Slide — Lab 2: Write EC for the Epics-and-Stories Skill

**Lab Name:** Write Evaluation Criteria for Your Epics-and-Stories Skill
**Lab Timing:** 15 minutes
**Lab Steps:**
1. For your epics-and-stories skill: write 4-6 EC that define what good output looks like
2. Suggested starting EC: "Every story has clear Acceptance Criteria (Given/When/Then or testable behavior statement)" / "Stories are independently deliverable" / "There are 3-8 stories per epic" / "At least one story covers a failure or edge case" / "No story describes implementation detail"
3. Remember: EC evaluates the skill's output quality. AC is what each story must satisfy. Don't confuse them.
4. Commit your EC

**You'll know when you're done because...** you have 4-6 written EC for your epics-and-stories skill, each specific and measurable, committed before building the skill.

---

## Exercise Slide — Lab 3: Build Out the Epics-and-Stories Skill

**Lab Name:** Build the Epics-and-Stories Skill
**Lab Timing:** 45 minutes
**Lab Steps:**
1. Open the create-epics-stories.skill.md skeleton — it has Role and Task defined, Context and Constraints empty
2. Using RTCC, fill in Context (WHY: what makes good stories for your team, what the downstream developers and testers need) and Constraints (HOW: story format, team standards, domain details, output requirements)
3. The skill already has `disable-model-invocation: true` — invoke it via slash command
4. Apply the Load-Bearing Rule: for each instruction you add, identify which EC it corresponds to. If no EC would fail when this instruction is removed, don't add it
5. The skill writes its output to `stories.yaml` in the workspace root — this is the YAML pipeline artifact that Session 2 will read
6. Run the skill on the demo PRD/Architecture/UX outputs from the earlier demo
7. Evaluate the output against your EC
8. Commit the skill

**You'll know when you're done because...** you have a committed epics-and-stories skill with RTCC structure, Context (WHY) and Constraints (HOW) filled in, every instruction mapped to at least one EC, and output evaluated against your EC on the demo inputs.

**Stretch goal:** write 3+ positive trigger test cases where the skill SHOULD invoke, preparing for model invocation in Session 5.

---

## Exercise Slide — Lab 4: Evaluate, Audit, and Iterate

**Lab Name:** Evaluate Output and Apply the Load-Bearing Rule
**Lab Timing:** 20 minutes
**Lab Steps:**
1. Share outputs across the room (anonymized if preferred)
2. Group scores each output against the EC
3. Identify the most common failure pattern in the room's output
4. For each instruction in your skill: which EC would fail if you removed it? If no EC would fail, flag it for removal
5. Remove flagged instructions and re-run to verify scores don't drop
6. Commit the leaner skill

**You'll know when you're done because...** your epics-and-stories skill has been load-bearing audited — every instruction is provably load-bearing — and you've verified this by running the skill after removal.

---

## Lecture Slide — Baseline Self-Assessment

**Content to teach:**

Participants complete the AI Adoption Maturity Assessment — the Week 1 baseline. 21 questions across 7 dimensions. Each answered A through D (1-4 points). Total score range 21-84.

Not graded. The only instruction is honesty. The value of the baseline is comparison at Week 7 and Week 12, not accuracy at Week 1.

---

## Closing Slide

**Goal 1: Prompt, Harness, Model**
- **Product/Process:** Your epics-and-stories skill is a Prompt, running through your IDE Harness, powered by a Model. The harness limits what your skill can access.
- **Development:** The harness is the capability boundary for everything you'll build — Plan, Code, evaluation scripts.
- **Testing:** The harness mediates evaluation and output — your review skills will work within the same boundaries.

**Goal 2: See the full SDLC pipeline**
- **Product/Process:** You've seen the 7 skeleton skills and where your epics-and-stories work fits. You've seen what RT-only stubs produce — and why Context and Constraints matter.
- **Development:** You've seen where Plan and Code fit. Your input is the epics-and-stories output.
- **Testing:** You've seen where Review fits. The pipeline ends with your domain.

**Goal 3: Build the epics-and-stories skill**
- **Product/Process:** You own this skill. You'll iterate on it for 12 weeks. It's your primary artifact.
- **Development:** You've seen the skill format and the RTCC structure. You'll apply the same format to Plan and Code skills in Session 2.
- **Testing:** You've seen how stories are generated. You'll use this understanding when building review skills in Session 3.

**Goal 4: Write EC before building**
- **Product/Process:** Your EC defines what good epics-and-stories output looks like. You'll evaluate every iteration against it. Remember: EC evaluates the skill; AC is what each story must satisfy.
- **Development:** You've practiced the EC-first discipline. You'll apply it to your Plan and Code skills next session.
- **Testing:** You've seen the EC pattern. You'll use it when writing EC for your review skill in Session 3.