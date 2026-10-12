# DLP v2 — Major Changes Plan

*Planning document for the next version of the Deep Learning Program*
*Branch: `dlp-v2` | Date: August 2026*

---

## Purpose

This document describes the major structural and pedagogical changes planned for DLP v2 before we begin rewriting session content. The goal is to align on direction and rationale so the content work is purposeful, not exploratory.

DLP v1 established a strong foundation: RTCC prompt structure, EDD discipline, commands-first progression, Promptfoo evaluation, and bounded agents. DLP v2 preserves the core philosophy — artifacts over advice, evaluation is non-negotiable, behavior change is the bar — while evolving the tooling, concepts, and session progression to reflect what we've learned and where the AI tooling landscape has moved.

---

## What Stays the Same

These foundational elements from v1 are not changing:

- **12-week embedded engagement structure** with Trainer + Embedded Engineer + Account Manager / Executive Coach roles
- **Two 6-week loops** (Foundation, Deepening) cycling through Product/Process, Development, and Testing role focuses
- **DLP Completion criteria**: Craft, Evaluate, Iterate, Adopt
- **RTCC prompt structure** (Role, Task, Context, Constraints)
- **EDD discipline**: define Evaluation Criteria (EC) before building, baseline, iterate, load-bearing audit
- **Load-Bearing Rule**: every instruction must provably change output
- **AI Adoption Maturity Assessment** (21-question, 7-dimension instrument) at Weeks 1, 7, and 12
- **Program Completion Rubric** (joint EE + Trainer assessment at Week 12)
- **Artifact-first design**: every session ends with committed artifacts, not notes
- **All-roles-present principle**: every participant attends every session regardless of role
- **Real work not exercises**: Embedded Engineer works in the client's actual codebase

---

## Change 1: Define Prompt, Harness, and Model in Session 1

### What Changes

Session 1 gains a foundational conceptual block that does not exist in v1: an explicit definition of three terms and the relationship between them.

**Prompt** — The instructions you give to a model. What you want it to do, how you want it done, what constraints it must follow. This is what participants spend the program learning to write well.

**Harness** — The software environment that mediates between you and the model. The harness determines what the model can actually do on your machine. It decides what files the model can read, what commands it can run, what tools it has access to, and how its output reaches you. Claude Code, Devin, GitHub Copilot, and the ChatGPT web interface are all different harnesses with different capabilities and different boundaries.

**Model** — The AI itself. The model generates text based on its training and the prompt it receives. But the model cannot do anything on your box that the harness does not offer or allow it to. A model without a harness is a chat interface. A model with a harness can read files, run commands, and produce artifacts. The harness is the capability boundary; the model is the intelligence; the prompt is the instruction.

### Why This Matters

This three-part mental model is the foundation for everything that follows in v2:

- **Why skills need `disable-model-invocation`** — the harness controls invocation, not the model. Participants need to understand that the harness decides when a skill fires, and we're choosing to start with explicit (slash-command) invocation.
- **Why Session 6 needs a custom harness** — the IDE's built-in harness supports single-step interactions. Multi-step workflow integration requires a custom harness with API access that can orchestrate multiple model calls, pass artifacts between steps, and evaluate each step programmatically.
- **Why adversarial agents (Session 5) work** — an adversarial agent is a prompt running through a harness that has access to the output of another prompt. The harness makes the connection; the model provides the judgment.

Without this conceptual foundation, participants understand what they're building but not why it's structured this way. With it, the entire program's progression — from slash-command skills to model-invoked skills to custom harnesses — follows a clear logic.

### Where It Lands in Session 1

Early in the session, before the RTCC block. It replaces some of the "Basic Prompting vs. DLP Completion" framing time from v1 (that framing is still present but compressed — the Prompt/Harness/Model definition does the heavier lifting because it explains the "why" behind the program structure).

### Ripple Effects

- Session 6 can reference back to this definition when introducing custom harnesses
- Session 5 can reference it when explaining adversarial agents (the adversarial prompt runs through a harness that has access to the primary output)
- The EE Implementation Guide and Trainer Guide should use this vocabulary consistently throughout

---

## Change 2: Teach Skills from the Outset with `disable-model-invocation: true`

### What Changes

In v1, the program teaches "commands" (explicit slash-command invocation) for the first 8 weeks, then introduces "skills" (model-invoked) in Session 5. The commands-to-skills transition is a major conceptual moment in v1.

In v2, we teach **skills** from Session 1. Every artifact participants build is a skill file using the skill format. But we set `disable-model-invocation: true` on every skill, which means the skill only runs when explicitly invoked via slash command — the model will not auto-invoke it based on context.

The v1 "commands vs. skills" distinction collapses. There are no separate command files. Everything is a skill. The difference is a configuration flag: `disable-model-invocation: true` (slash-command only) vs. `false` or unset (model can auto-invoke).

### Why This Matters

1. **Participants learn one artifact format, not two.** In v1, participants learn command files, then later learn that skills are a different thing with different structure. In v2, they learn the skill format once. The only thing that changes later is a configuration flag.

2. **The progression is cleaner.** Instead of "commands → skills" as a conceptual leap, the progression is "skills with invocation disabled → skills with invocation enabled." The change is a configuration decision backed by evaluation evidence, not a format migration.

3. **It matches how modern tooling actually works.** Current agentic IDEs (Claude Code, Devin, etc.) use skill files as the primary artifact. Teaching a separate "command" concept that doesn't map to the tool's actual file format creates a translation step that doesn't help participants.

4. **It sets up the Session 5 model-invocation discussion naturally.** When we discuss enabling model invocation in Session 5, participants already have skills they've been using for 8 weeks. The question becomes: "Which of your skills is ready for the model to invoke automatically?" — not "which of your commands should be converted to a different format?"

### How It Works in Practice

- Session 1: Participants build their first skill (Acceptance Criteria generation) with `disable-model-invocation: true`. They invoke it via slash command. The RTCC structure lives inside the skill file.
- Sessions 2-4: All artifacts are skills with invocation disabled. The discipline is the same: write criteria first, build the skill, evaluate, iterate, load-bearing audit.
- Session 5: We introduce the concept of enabling model invocation. Participants evaluate which skills are ready. The three graduation criteria (exact trigger inputs, output specification, 3+ verified trigger test cases) still apply — but now they're about flipping a config flag on an existing, well-evaluated skill, not about converting to a new format.

### What This Replaces from v1

- The v1 "commands vs. saved prompts" framing (Week 1 coaching notes) is replaced by "skills with invocation disabled vs. ad-hoc prompts"
- The v1 Session 5 "Commands to Skills" lab is replaced by "Enabling Model Invocation" — the skills already exist; the question is whether to allow auto-invocation
- The v1 "automation spectrum" (Commands → Skills → Hooks + Sentinel Files → Governed Workflows) is replaced by a new spectrum: Skills (invocation disabled) → Skills (invocation enabled) → Adversarial Agents → Custom Harnesses

### Ripple Effects

- All session content that references "commands" needs to be updated to "skills" (with `disable-model-invocation: true` where relevant)
- The SDLC skeleton commands become SDLC skeleton skills (with invocation disabled)
- The EE weekly curriculum references to "command" need updating throughout
- The Program Completion Rubric's Craft criterion changes from "commands, skills, workflows, and agents" to "skills and adversarial agents"

---

## Change 3: Session 2 Teaches Plan → Code 2-Step Approach

### What Changes

v1 Session 2 is "Unit Test Generation" — participants build a command that generates unit tests from story + Acceptance Criteria. The session teaches the AC → Test dependency and the failure modes of AI-generated tests (false coverage, tautological tests, happy-path-only).

v2 Session 2 is **"Plan → Code"** — a two-step approach where participants use AI to first plan an implementation, then generate code from that plan. The session teaches the discipline of separating planning from coding when working with AI, and how the quality of the plan determines the quality of the code.

### Why This Matters

1. **Plan → Code is a more universal workflow than unit test generation.** Not every participant writes unit tests from Acceptance Criteria. Every developer plans before coding. The two-step approach applies to all roles: a Product/Process person plans requirements changes before writing them; a tester plans test scenarios before generating them; a developer plans implementation before coding.

2. **It teaches upstream quality dependency in a more tangible way.** In v1, the AC → Test dependency is real but abstract for non-developers. In v2, the Plan → Code dependency is immediately tangible: everyone can see that a vague plan produces vague code, and a specific plan produces specific code. The lesson is the same — upstream quality determines downstream quality — but the vehicle is more universal.

3. **It positions AI as a thinking partner, not just a generator.** The Plan step is where human judgment and AI assistance interact most productively. The participant writes the plan (or has AI draft it), reviews and refines it, then uses it as the specification for code generation. This is the discipline that separates DLP Completion from Basic Prompting: you don't ask AI to "write the code" — you plan first, then generate.

4. **It creates a natural evaluation surface.** The plan is an artifact that can be evaluated: Is it specific? Does it cover edge cases? Does it reference the Acceptance Criteria? The code generated from the plan can be evaluated against the plan. This two-layer evaluation is richer than v1's single-layer test evaluation.

### How It Works in Practice

- Session 2 teaches the Plan → Code two-step as a skill workflow:
  1. **Plan skill**: Given a story + Acceptance Criteria, generate an implementation plan (approach, key decisions, edge cases, file changes)
  2. **Code skill**: Given the implementation plan + Acceptance Criteria, generate the code
- Both skills are built using RTCC and EDD discipline (criteria first, baseline, iterate)
- The session teaches: what makes a good plan, what AI gets wrong in planning (over-specification, under-specification, missing edge cases), and how plan quality determines code quality
- The AC → Plan dependency replaces the v1 AC → Test dependency as the upstream quality lesson

### What This Replaces from v1

- v1 Session 2's "Unit Test Generation" content is replaced by "Plan → Code"
- v1's false coverage / tautological test / happy-path-only failure modes are replaced by plan failure modes: vague plans, plans that miss edge cases, plans that over-constrain the implementation
- v1's "Acceptance Criteria quality dependency" block becomes the "Plan quality dependency" — the plan is the new upstream artifact
- The SDLC skeleton skills may be re-framed around the Plan → Code workflow rather than the full SDLC pipeline

### What Happens to Unit Tests?

Unit tests don't disappear from the program. Testing is still a role focus in Loop 1 (Session 3 covers test planning). But the specific "generate unit tests from AC" command from v1 Session 2 is replaced by the Plan → Code workflow. Test generation can still happen — it's a natural output of the Plan step for developers — but it's not the primary artifact of Session 2.

### Ripple Effects

- Session 3 (Test Planning) needs to connect to the Plan → Code workflow rather than the v1 test generation chain
- The "full chain" concept changes from v1's "AC → Tests → Test Plan" to something like "AC → Plan → Code → Test Plan" or "Story → Plan → Code → Tests"
- The v1 Loop 1 retrospective ("you now have commands across all three workflow areas") needs reframing around the new artifacts

---

## Change 4: Session 4 Teaches AI-Generated Python Evaluations with LLM Judges

### What Changes

v1 Session 4 teaches EDD formalization using **Promptfoo** — a YAML-based assertion framework where participants define `contains`, `icontains`, and `llm-rubric` assertions against their command outputs. The Embedded Engineer introduces Promptfoo in Week 6, and Session 4 builds the full EDD discipline around it.

v2 Session 4 teaches EDD formalization using **AI-generated Python evaluations with LLM judges**. Instead of configuring a YAML assertion framework, participants write (with AI assistance) Python scripts that evaluate their skill outputs. The primary evaluation mechanism is the **LLM judge** — a Python script that sends the skill output to a model along with evaluation criteria and receives a structured judgment (pass/fail, score, reasoning).

### Why This Matters

1. **Python evaluations are more flexible and expressive than YAML assertions.** Promptfoo's assertion types are limited: string matching, case-insensitive matching, and LLM rubric. Python evaluations can check anything: count criteria, parse structured output, call external APIs, run subprocesses, compare across multiple runs, and use LLM judges for criteria that require judgment.

2. **Participants learn to build their own evaluation tools, not configure someone else's.** In v1, participants learn Promptfoo's configuration format — a tool-specific skill that doesn't transfer. In v2, participants learn to write Python evaluation scripts — a universally applicable skill. The evaluation tool is itself an artifact they own and can adapt.

3. **LLM judges are the industry-standard pattern for AI output evaluation.** Using an LLM to evaluate another LLM's output is how production AI systems measure quality. Teaching this pattern directly — rather than hiding it behind Promptfoo's `llm-rubric` assertion — gives participants a deeper understanding of how evaluation works and how to build it.

4. **It removes a tooling dependency.** Promptfoo is a specific tool with specific setup requirements, versioning concerns, and configuration formats. Python + an API key is universal. Every participant's environment has Python. The only requirement is an API key for the LLM judge, which the program can provide or the client can supply.

5. **It aligns with the custom harness concept from Session 6.** If participants are already writing Python evaluation scripts with LLM judges in Session 4, the leap to custom harnesses in Session 6 is smaller. They're already writing code that calls the model programmatically. The harness is a natural extension of that.

### How It Works in Practice

- The Embedded Engineer introduces Python evaluation in Week 6 (replacing the v1 Promptfoo introduction)
- Session 4 teaches:
  - The LLM judge pattern: send skill output + evaluation criteria to a model, receive structured judgment
  - Writing evaluation scripts in Python that: load skill output, run deterministic checks (count, format, structure), run LLM judge checks (quality, coverage, specificity)
  - The EDD discipline remains the same: write criteria first, baseline, iterate, load-bearing audit. The tooling changes.
  - Structured output from LLM judges: JSON responses with pass/fail, score, reasoning per criterion
  - One change per iteration, documented hypotheses, committed evaluation scripts

### What This Replaces from v1

- Promptfoo is removed entirely from the program
- The v1 assertion types (`contains`, `icontains`, `llm-rubric`) are replaced by Python code and LLM judge calls
- The v1 Promptfoo configuration files are replaced by Python evaluation scripts
- The v1 "configure Promptfoo" labs become "write an evaluation script" labs
- The v1 improvement cycle documentation format changes from Promptfoo scores to Python script output

### What Stays the Same

- The EDD discipline (Red/Green/Refactor for prompts) is unchanged
- The Load-Bearing Rule is unchanged — it's still about removing instructions that don't affect evaluation results
- The criteria-first discipline is unchanged — write criteria before building the skill
- The iteration cycle concept (hypothesis → change → measure → conclude) is unchanged

### Ripple Effects

- All references to Promptfoo throughout the curriculum need to be replaced with Python evaluation
- The EE Week 6 Promptfoo introduction becomes a Python evaluation introduction
- The Program Completion Rubric's Evaluate criterion changes from "working evaluator with 3+ iterations" to "Python evaluation script with LLM judge, 3+ iterations documented"
- The evaluation artifacts participants commit are `.py` files instead of YAML configs
- The program needs to ensure participants have Python and an API key for the LLM judge (or the instructor provides one for the session)

---

## Change 5: Session 5 Teaches Adversarial Agent Prompts + Model Invocation

### What Changes

v1 Session 5 is "Evaluation to Runtime Verification" — it teaches Commands to Skills graduation, then Hooks & Sentinel Files (deterministic runtime checks that verify output structure at the moment it's produced).

v2 Session 5 has two focuses:

1. **Adversarial Agent Prompts** — Instead of deterministic hooks and sentinel files, participants learn to build adversarial prompts: AI prompts designed to challenge, critique, and find weaknesses in the output of their primary skills. An adversarial agent is a skill (or a prompt within a custom harness) that receives the output of another skill and attempts to find problems with it — missing requirements, logical errors, edge cases the primary skill missed, quality gaps the evaluation script didn't catch.

2. **Model Invocation of Skills** — This is where we revisit the `disable-model-invocation: true` setting from Session 1. Participants evaluate which of their skills are ready for the model to invoke automatically based on context. The three graduation criteria (exact trigger inputs, output specification, 3+ verified trigger test cases) still apply, but now they're about enabling a config flag on an existing skill.

### Why This Matters

1. **Adversarial agents are more powerful than deterministic hooks.** A hook can check whether a required field is present. An adversarial agent can check whether the field's content is actually correct, whether the reasoning is sound, and whether the output misses something the criteria didn't anticipate. The adversarial approach catches semantic failures that deterministic checks cannot.

2. **Adversarial agents are AI-native, not code-native.** Hooks require writing shell scripts or code — a barrier for non-developer participants. Adversarial agents are prompts — every participant in the program can write one. This makes the runtime verification concept accessible to all roles, not just developers.

3. **It creates a natural pairing with Python evaluation.** Session 4 teaches Python evaluation scripts with LLM judges (retrospective quality assessment). Session 5 teaches adversarial agents (proactive quality challenge). The two are complementary: the evaluation script measures, the adversarial agent attacks. Both are needed for a complete quality strategy.

4. **Model invocation is the right discussion at Week 9.** By Week 9, participants have been using skills with invocation disabled for 8 weeks. They have evaluation evidence. They understand the Prompt/Harness/Model distinction from Session 1. They're ready to ask: "Should the model invoke this skill automatically?" The answer requires the three graduation criteria — and now the criteria are about a configuration decision, not a format migration.

### How It Works in Practice

- Session 5 teaches two things in sequence:

  **Part A: Enabling Model Invocation (shorter, ~30 min presentation + 30 min lab)**
  - Revisit the `disable-model-invocation` flag from Session 1
  - The three graduation criteria:
    1. Exact inputs that should trigger the skill
    2. What the skill does when triggered — the output specification
    3. At least 3 verified trigger test cases where the skill SHOULD invoke, confirmed the model invokes it and output meets spec
  - Lab: evaluate one skill against the three criteria. Either enable model invocation (with test cases) or document the gap.

  **Part B: Adversarial Agent Prompts (longer, ~35 min presentation + 40 min lab)**
  - What an adversarial agent is: a prompt that receives the output of another skill and attempts to find problems
  - How it differs from evaluation (Session 4): evaluation measures against criteria; adversarial agents find problems the criteria didn't anticipate
  - How it differs from v1 hooks: hooks are deterministic and check structure; adversarial agents are AI-based and check meaning
  - Lab: write an adversarial prompt for one of your existing skills. Run it against real outputs. What does it find that your evaluation script missed?

### What This Replaces from v1

- Hooks and Sentinel Files are removed entirely
- The v1 "Evaluation → Skills → Runtime Verification" progression is replaced by "Python Evaluation (Session 4) → Adversarial Agents (Session 5)"
- The v1 "deterministic vs. AI judgment" distinction is replaced by "retrospective measurement (Python eval) vs. proactive challenge (adversarial agent)"
- The v1 sentinel schema concept is removed
- The v1 evaluator-to-sentinel mapping lab is removed

### What Stays the Same

- The three skill graduation criteria (exact inputs, output spec, verified trigger test cases)
- The invocation boundary concept
- The EDD-validated prerequisite (skills should have 3+ documented iteration cycles before model invocation is enabled)

### Ripple Effects

- All references to hooks and sentinel files throughout the curriculum are removed
- The v1 "automation spectrum" (Commands → Skills → Hooks → Governed Workflows) becomes: Skills (invocation disabled) → Skills (invocation enabled) → Adversarial Agents → Custom Harnesses
- The EE weekly curriculum for Weeks 9-10 changes from "commands-to-skills + hooks" to "model invocation + adversarial agents"
- The Program Completion Rubric's Craft criterion changes to reference adversarial agents instead of hooks/sentinel files

---

## Change 6: Session 6 Introduces Custom Harnesses

> **NOTE: This section describes the original v2 plan. Session 6 was subsequently restructured to "Bounded Agents, Custom Harness Demo & Stage 4 Preview" — participants now BUILD a bounded agent (hands-on lab) and the custom harness is DEMOED only. The specification exercise was removed. See RELEASE-NOTES.md "Session 6 Restructure" section for the current state.**

### What Changes

v1 Session 6 is "Agents & Workflows" — it introduces bounded agents (orchestration of commands and skills within a single context window) and closes the program with capstone, final assessment, and commitment statements.

v2 Session 6 is **"Custom Harnesses"** — it introduces the concept that truly integrating multiple steps of a workflow requires building a custom harness: a Python program that orchestrates multiple model calls, passes artifacts between steps, evaluates each step, and manages the overall workflow. The instructor demos this capability (it requires an API key), then lectures on how the progression from single skills to multi-step workflows leads naturally to custom harnesses.

### Why This Matters

1. **It completes the Prompt/Harness/Model conceptual arc from Session 1.** Session 1 defines the three terms and explains that the model can only do what the harness allows. Sessions 1-5 use the IDE's built-in harness (Claude Code, Devin, etc.). Session 6 reveals the next step: when your workflow exceeds what the IDE harness supports, you build your own.

2. **It's the natural endpoint of the v2 progression.** Skills (invocation disabled) → Skills (invocation enabled) → Adversarial Agents → Custom Harnesses. Each step extends what participants can trust AI to do. The custom harness is where multi-step, multi-model, evaluated workflows become production systems.

3. **It connects to participants' existing Python evaluation skills.** By Session 6, participants have been writing Python evaluation scripts with LLM judges since Session 4. A custom harness is a natural extension: it's a Python program that calls models, and participants already know how to call models from Python. The conceptual leap is small; the capability leap is large.

4. **It sets up the post-program trajectory.** v1's post-program guidance talks about "continued adoption of core DLP skills" but doesn't give participants a concrete next step. v2's custom harness concept gives participants a concrete target: "Your IDE skills are the building blocks. A custom harness is how you compose them into production workflows."

### How It Works in Practice

- Session 6 has a bounded agent lab and a custom harness demo (the specification exercise from the original plan was removed):
  - **Demo (instructor-led, requires API key):** The instructor demonstrates a custom harness that implements the full chain: Story → Acceptance Criteria → Plan → Code → Test Plan. The harness:
    1. Calls the AC skill with a story input
    2. Evaluates the AC output with a Python evaluation script + LLM judge
    3. Calls the Plan skill with the AC output
    4. Evaluates the plan
    5. Calls the Code skill with the plan
    6. Runs an adversarial agent against the code output
    7. Produces a final artifact with evaluation scores at each step
  - **Lecture:** Why this requires a custom harness (the IDE harness is single-step; multi-step orchestration with evaluation at each step requires programmatic control), what the harness does (API calls, artifact passing, evaluation orchestration, error handling), and what participants would need to build one (API key, Python, the evaluation patterns from Session 4, the adversarial patterns from Session 5)
  - **Specification exercise (participants, no API key required):** Participants write a specification for a custom harness that would integrate their own skills into a multi-step workflow. They define: the steps, the artifacts passed between steps, the evaluation at each step, the failure handling. This is a committed artifact.

- The capstone, final assessment, and commitment statements from v1 Session 6 are preserved.

### What This Replaces from v1

- v1's "bounded agent" concept (orchestration within a single context window) is replaced by "custom harness" (orchestration via a Python program with API calls)
- v1's "context window discipline" content is preserved but reframed: the custom harness solves the context window problem by giving each step its own clean context
- v1's Lab 1 ("build or specify a bounded agent") becomes "specify a custom harness"
- v1's Lab 2 ("evaluate the agent across the full chain") becomes the instructor demo

### What Stays the Same

- Capstone artifact showcase (peer pairs presenting their best work)
- Final AI Adoption Maturity Assessment
- Commitment statements
- Program close

### Ripple Effects

- The v1 "bounded agent" terminology throughout the curriculum is replaced by "custom harness"
- The EE weekly curriculum for Weeks 11-12 changes from "agents & workflows" to "custom harnesses"
- The Program Completion Rubric's Craft criterion references skills and adversarial agents
- The Sustainment guides need updating to reference custom harnesses as the continued-adoption target
- The program needs to clearly communicate that Session 6 is bounded agent lab + custom harness demo + IIOS preview, not custom harness building (API key requirement makes hands-on impractical for all participants)

---

## Change 7: "Evaluation Criteria" (EC) as Consistent Terminology for Skill Evaluation

### What Changes

Throughout DLP v1, the criteria participants write to evaluate their skills/prompts are referred to inconsistently — sometimes as "evaluation criteria," sometimes as "success criteria," sometimes as just "criteria." This creates a specific, documented confusion in Session 1: participants are building a skill that generates **Acceptance Criteria (AC)** from stories, and simultaneously writing criteria to evaluate that skill's output. When both are called "criteria" or both abbreviated "AC," participants cannot tell which is which.

In v2, we standardize on **Evaluation Criteria (EC)** as the exclusive term for the criteria used to evaluate a skill's output — whether that evaluation is human-in-the-loop review (Sessions 1-3) or automated EDD with Python evaluation scripts and LLM judges (Sessions 4-6).

**Acceptance Criteria (AC)** always refers to the product artifact — the criteria a story must satisfy for it to be considered done. These are what the AC generation skill produces.

**Evaluation Criteria (EC)** always refers to the quality bar for a skill's output — the criteria a participant writes before building or iterating on a skill, used to measure whether the skill is producing good results. These are what the participant writes as part of EDD discipline.

### Why This Matters

1. **The confusion is real and has been experienced in the field.** In v1 Session 1, participants write "evaluation criteria" for their Acceptance Criteria generation command. The instructor says "write your criteria" and participants don't know whether they're writing acceptance criteria for a story or evaluation criteria for the skill. This is not a theoretical risk — it has happened in delivery.

2. **The confusion compounds across the program.** By Session 4, participants are running Promptfoo (v1) or Python evaluations (v2) against their skills. The evaluation assertions are based on "criteria" — but which criteria? The skill's evaluation criteria or the story's acceptance criteria? Without distinct terminology, every conversation about evaluation has to disambiguate from context.

3. **It aligns with the v2 emphasis on Python evaluation and LLM judges.** When participants write a Python evaluation script, the script evaluates the skill's output against EC. The LLM judge receives the skill output and the EC and returns a judgment. Having a single, unambiguous term for what the judge is evaluating makes the code, the prompts, and the conversation clearer.

4. **It creates a clean vocabulary for the program:**
   - **AC** = Acceptance Criteria (product artifact, what the story must satisfy)
   - **EC** = Evaluation Criteria (quality bar, what the skill's output must satisfy)
   - **RTCC** = the structure of the skill itself (Role, Task, Context, Constraints)
   - **EDD** = the discipline of writing EC before building, baselining, and iterating

   Four terms, four distinct meanings, no overlap.

### How It Works in Practice

- Session 1: "Write your Evaluation Criteria (EC) for your AC generation skill. Your EC define what good AC output looks like — specifically, in writing — so you can evaluate whether your skill is producing it."
- Session 4: "Your Python evaluation script checks your skill's output against your EC. Your LLM judge receives the output and the EC and returns a pass/fail per criterion."
- All session materials, weekly curriculum, implementation guides, rubrics, and assessments use "Evaluation Criteria" or "EC" consistently when referring to skill evaluation criteria.
- The term "success criteria" is retired — it was used in v1 as a synonym for evaluation criteria and adds no clarity.
- The term "criteria" is never used alone — it's always "Evaluation Criteria" or "Acceptance Criteria" with the abbreviation established on first use.

### What This Replaces from v1

- All instances of "evaluation criteria," "success criteria," and bare "criteria" (when referring to skill evaluation) are replaced with "Evaluation Criteria (EC)"
- The v1 Session 1 EDD block title "Define Success Before You Build" becomes "Define Your Evaluation Criteria Before You Build"
- The v1 Session 4 Promptfoo assertion terminology ("assertions") is replaced with "Evaluation Criteria" or "EC" — the Python evaluation script checks against EC, not against "assertions"

### Ripple Effects

- Every session file, weekly curriculum file, implementation guide, rubric, assessment, and sustainment guide needs to be reviewed for terminology consistency
- The v1 Load-Bearing Rule phrasing ("which criterion would fail if I removed this instruction?") becomes "which Evaluation Criterion would fail if I removed this instruction?"
- The v1 improvement cycle documentation format changes from listing "criteria" to listing "Evaluation Criteria (EC)"
- The Program Completion Rubric's Evaluate criterion should reference "Evaluation Criteria" explicitly
- The AI Adoption Maturity Assessment dimension names may need updating if they reference "criteria" ambiguously

---

## Change 8: Replace PPTX Decks with Deck Description Prompts

### What Changes

v1 ships PPTX slide decks for each session (Session-1.pptx through Session-6.pptx, plus client-specific variants). These binary files are difficult to diff, review, and version. They also couple content with visual design, making content updates require manual slide editing.

v2 removes all PPTX files. In their place, each session gets a **deck description prompt** — a detailed markdown file that describes the structure and content of the deck we want. These prompts are designed to be consumed by a specialized design harness (an AI agent or tool) that will generate the actual slide decks from the description. One prompt file per session, in the same directory the PPTXs occupied.

### File Naming

Deck prompt files use the same naming pattern as the session markdown files, but with a `.deck.md` extension to distinguish them from the session content files:

| Session markdown | Deck prompt |
|-----------------|-------------|
| `Session-1.md`  | `Session-1.deck.md` |
| `Session-2.md`  | `Session-2.deck.md` |
| `Session-N.md`  | `Session-N.deck.md` |

### Deck Prompt Structure

Every deck prompt must specify the following slide types. The design harness will use these to generate the actual slides.

**Required slides in every deck:**

1. **Intro Slide** — Session title, week number, loop (1 or 2), role focus, and a one-line framing of what this session is about and why it matters now.

2. **Check-In Slide** — The check-in question(s) for this session. Must connect to the prior session's work and set up the current session's content. This is a discussion prompt, not a content slide.

3. **Session Goals Slide** — The session goals, with each goal annotated for how it is relevant to each role (Product/Process, Development, Testing). Every goal must have a line for each role. No goal is role-agnostic — if a goal doesn't apply to a role, say so explicitly and explain why it still matters to them.

4. **Closing Slide** — Reviews the session goals and how they affected each role. This is the bookend to the Session Goals Slide. For each goal: what did Product/Process take away, what did Development take away, what did Testing take away. This is not a summary — it's a role-specific reflection prompt.

**Content slides (used throughout the deck as needed):**

5. **Exercise Slide** — Every lab in the session gets an Exercise Slide with:
   - **Lab Name** — clear, descriptive
   - **Lab Timing** — how long the lab takes (e.g., "45 minutes")
   - **Lab Steps** — the steps participants follow, as a numbered list
   - **"You'll know when you're done because..." footer** — a specific, checkable Evaluation Criterion. Not "you'll have learned something" but "you'll have a committed skill file with a load-bearing audit completed and at least 3 real-story outputs evaluated against your EC."

6. **Demo Slide** — Every demonstration in the session gets a Demo Slide with:
   - **Description** of what is about to be demonstrated and how it relates to the learning goals. This explains the *why* and the *what*, not the *how*. No step-by-step instructions on the slide — the instructor does those live.
   - **"What to focus on" section** — tells participants what to watch for during the demo. This is the observational instruction: "As the demo runs, notice how the evaluator catches a failure the instructor didn't anticipate" or "Watch what happens to the output when the Context section is empty vs. populated."

7. **Compare/Contrast Slide** — A slide that shows moving from left-side bad behaviors to right-side good behaviors. **Hard limited to 5 items** on the list. Each row is a single behavior shift (e.g., "Writing prompts ad-hoc → Writing skills with RTCC structure"). Used to make discipline shifts visible and memorable. If there are more than 5 contrasts to draw, split into two slides or pick the 5 most important.

8. **Lecture Slide** — For lecture/presentation blocks. Include **only what we want the students to learn** — the key concepts, definitions, or principles. Do not include slide formatting, layout instructions, or visual design notes. Leave it to the design agent to craft the slides as appropriate from the learning content. A lecture block might be one slide or several; the prompt should describe the content, not the visual treatment.

### What This Replaces from v1

- All `.pptx` files in the Training-Sessions directory are deleted from the branch
- The `AGENTS.md` file in Training-Sessions is updated: the slide deck generation instructions no longer reference `Session-Template.pptx` as the base — instead they reference the deck prompt files and the design harness
- The `Session-Template.pptx` file is deleted
- Client-specific variant PPTX files are deleted

### Ripple Effects

- The Trainer Implementation Guide needs updating to reference deck prompts instead of PPTX files
- The session content workflow changes: write session .md (content source) → write deck .md (deck structure prompt) → design harness generates .pptx
- The AGENTS.md in Training-Sessions is rewritten to describe the new workflow
- No PPTX files are committed to the repository — they are generated artifacts, not source files

---

## Change 9: RTCC — Context is WHY, Constraints absorb the Data

### What Changes

v1 teaches RTCC as:
- **R — Role:** Who is the AI acting as?
- **T — Task:** What specific action should it perform?
- **C — Context:** What background information does it need? What does it know about the situation, the codebase, the prior steps, the audience?
- **C — Constraints:** What rules must the output follow? What should it never do? What format is required?

v2 teaches RTCC as:
- **R — Role:** WHO the model should act as — a specific, credentialed persona that changes tone, vocabulary, and default assumptions
- **T — Task:** WHAT they should do — verb-first, unambiguous, the specific action to perform
- **C — Context:** WHY we want this done — the intent behind the task. What outcome are we trying to achieve? What problem are we solving? Why does this matter? Context is the purpose that shapes how the model interprets its role and task.
- **C — Constraints:** The data, rules, and specifications the model needs. What background information is relevant? What codebase, standards, or domain knowledge applies? What rules must the output follow? What should it never do? What format is required? Constraints absorb the data, background, and specification elements that v1 placed in Context.

### Why This Matters

1. **Context-as-intent produces better output than Context-as-data.** When Context is "here's why we're doing this and what we're trying to achieve," the model understands the purpose and can make better decisions about how to fulfill its Role and Task. When Context is "here's a bunch of background information," the model has data but no understanding of what matters about it.

2. **It creates a cleaner mental model.** WHO (Role) → WHAT (Task) → WHY (Context) → HOW (Constraints). Each letter answers a different question. Participants can remember and apply this structure because each element has a distinct purpose, not an overlapping one.

3. **It moves data into Constraints where it belongs.** Data, background, codebase context, and domain knowledge are constraints on the output — they define what the output must account for. Calling them "Context" blurs the line between "why am I doing this" and "what information do I need." Separating them makes both sharper.

4. **It aligns with how skilled prompt engineers actually think.** When an experienced practitioner writes a prompt, they first think "what am I trying to accomplish?" (intent), then "what information does the model need to accomplish it?" (constraints). Teaching Context as intent makes this natural thinking explicit.

5. **It makes the Load-Bearing Rule cleaner.** When auditing instructions, participants ask: "Does this instruction serve the WHY (Context) or provide data/rules (Constraints)?" If an instruction is background data sitting in Context, it's in the wrong place — move it to Constraints. If an instruction is intent sitting in Constraints, it's in the wrong place — move it to Context. The WHY/HOW distinction gives participants a diagnostic for structural problems in their skills.

### How It Works in Practice

**v1 AC generation skill (example Context):**
> Context: The team writes stories in the standard format: "As a [role], I want [capability], so that [benefit]." Stories are written in Azure DevOps. The team works in .NET 8 with xUnit.

**v2 AC generation skill (example Context + Constraints):**
> Context: We need Acceptance Criteria that are specific enough for developers to write tests from and testers to build test plans from. The purpose is to eliminate the back-and-forth between Product, Dev, and Testing that happens when stories arrive with vague or untestable criteria. Every story that enters the sprint should have AC that any role can read and know what "done" means.
>
> Constraints: Stories are written in the standard format: "As a [role], I want [capability], so that [benefit]." Stories are stored in Azure DevOps. The team works in .NET 8 with xUnit. Output must use Given/When/Then format. There must be 3-8 AC per story. At least one AC must cover a failure or edge case.

The Context section answers: why are we generating AC, and what makes AC good for this team? The Constraints section answers: what data does the model need, and what rules must the output follow?

### What This Replaces from v1

- All RTCC definitions throughout the curriculum change to the WHO/WHAT/WHY/HOW framing
- The v1 Session 1 RTCC lecture block changes: Context is no longer "what background information does it need" — it's "why we want this done"
- The v1 "why this order matters" explanation changes: the order matters because WHO and WHAT define the contract, WHY gives it purpose, and HOW (Constraints) provides the data and rules. Adding data before establishing purpose produces outputs that have information but miss the intent.
- All session files, weekly curriculum, implementation guides, and rubrics that reference RTCC need updating
- The SDLC skeleton skills (when converted to skill format) need their Context/Constraints sections restructured

### Ripple Effects

- Every deck prompt file that has an RTCC lecture slide needs updating (Sessions 1, 2, 3)
- Every session file that teaches or references RTCC structure needs updating
- The EE coaching notes throughout the 12-week curriculum that reference Context and Constraints need review
- The Load-Bearing Rule coaching changes: "which EC would fail if I removed this instruction?" is still the question, but participants now have a structural diagnostic too: "is this instruction in the right RTCC section?"
- The improvement cycle documentation format may benefit from asking participants to note whether changes are to Context (intent) or Constraints (data/rules) — this makes iteration more structural

---

## Change 10: SDLC Skeleton Skills Introduced in Session 1, Sessions Built Around Them

### What Changes

v1 introduces the 7 SDLC skeleton commands in Week 3 (Session 2) as RT-only stubs for the Development team to iterate on. They are a side resource, not the spine of the program.

v2 introduces the 7 SDLC skeleton skills in **Session 1** as the structural backbone of the entire program. Each session in Loop 1 focuses on building out specific skeleton skills:

- **Session 1**: Introduces the full SDLC pipeline (all 7 skeletons). Pre-generates demo outputs for create-prd, create-architecture, and create-ux so participants see the full pipeline and understand what feeds into epics-and-stories. The primary iteration target is the **epics-and-stories** skeleton skill — this is where participants learn RTCC, EC, and EDD by building out the Context and Constraints that the RT-only stub lacks.
- **Session 2**: Focuses on the **plan-story** and **implement-story** skeleton skills. Framed as "The Development Loop" — Plan → Code is the inner loop of development, and these two skeletons are its articulation. The plan skill generates the implementation plan; the develop skill generates code from the plan.
- **Session 3**: Focuses on the **review-implementation** skeleton skill — the testing/review step. This is where test planning lives, but it's framed as reviewing the implementation against the story + AC + plan, not as an isolated test planning exercise.

### Why This Matters

1. **The program has a concrete spine.** Instead of participants building disconnected skills (AC generation in Session 1, unit tests in Session 2, test plans in Session 3), every session builds out a piece of the same pipeline. By the end of Loop 1, participants have iterated on a connected set of SDLC skills that form a coherent workflow.

2. **The demo outputs ground the pipeline.** Pre-generating demo PRD, Architecture, and UX outputs in Session 1 means participants see what good upstream artifacts look like before they're asked to build downstream ones. The epics-and-stories skill consumes these demo outputs, making the upstream dependency concrete from day one.

3. **It eliminates the "what do I build?" question.** v1 participants often struggle with what to build their command around. v2 gives them the skeleton skill — the Role and Task are pre-defined, and their job is to add Context (WHY) and Constraints (HOW) using EDD discipline. This is more concrete and more pedagogically sound.

4. **The "Development Loop" framing in Session 2 is stronger than "Plan → Code" in isolation.** Plan → Code is the inner loop, but framing it as "The Development Loop" connects it to the broader SDLC pipeline. The plan skill says "here's how we'll implement this story," the develop skill says "here's the code," and the loop is: plan, code, evaluate, iterate.

### How It Works in Practice

**Session 1:**
- Walk through all 7 SDLC skeleton skills in pipeline order
- Show pre-generated demo outputs for create-prd, create-architecture, and create-ux
- Participants build out the **epics-and-stories** skill: add Context (WHY we need good stories, what makes a story actionable) and Constraints (HOW stories should be formatted, what data the model needs)
- The demo PRD/Architecture/UX outputs are the input that the epics-and-stories skill consumes — making the chain visible from Session 1

**Session 2:**
- The Development Loop: plan-story → implement-story
- Participants build out the **plan-story** skill: add Context (WHY we plan before coding, what a good plan enables) and Constraints (HOW the plan should be structured, what data from the story it needs)
- Participants build out the **implement-story** skill: add Context (WHY we generate code from the plan not the story, what a good plan enables for code generation) and Constraints (HOW the code should be generated, language, framework, conventions)
- The epics-and-stories output from Session 1 is the input to plan-story — the chain continues

**Session 3:**
- The **review-implementation** skill: add Context (WHY we review implementation against the story + plan, what a review catches that coding misses) and Constraints (HOW the review should be structured, what to check, what to flag)
- The plan and code output from Session 2 is the input to review-implementation — the chain completes

### What This Replaces from v1

- The v1 Session 1 "Acceptance Criteria Generation" content is reframed as "Epics and Stories Generation" using the skeleton skill. The RTCC, EC, and EDD discipline is the same; the artifact is now a skeleton skill being built out rather than a from-scratch command.
- The v1 Session 2 "Plan → Code" content is reframed as "The Development Loop" using the plan-story and implement-story skeleton skills.
- The v1 Session 3 "Test Planning" content is reframed as "Review Implementation" using the review-implementation skeleton skill.
- The v1 Week 3 introduction of SDLC skeleton commands is removed (they're introduced in Session 1 now).
- The v1 SDLC skeleton commands @Overview.md is updated to reflect the new introduction point and the session-by-session buildout.

### Ripple Effects

- Demo PRD, Architecture, and UX outputs need to be created as committed artifacts in the repository (in the Resources/SDLC-Commands/ directory alongside the skeleton skills)
- The skeleton skills themselves need to be converted from .md command files to skill format with `disable-model-invocation: true`
- Session 1, 2, and 3 deck prompts need updating to reflect the skeleton-skill-centric structure
- The EE weekly curriculum for Weeks 1-6 changes: the EE is now coaching participants on building out skeleton skills, not building from-scratch commands
- The SDLC-Workflow.png may need updating to reflect the v2 session-to-skeleton mapping

---

## Change 11: Shared Student Workspace Repo for All Sessions

### What Changes

v1 and current v2 sessions have participants work against their own real codebase during labs. This creates setup friction (every participant's environment is different), makes labs inconsistent (different people have different inputs), and complicates demos (the instructor can't predict what participants will see).

v2 with this change: all sessions assume a single shared **student workspace** — a subdirectory in the AI-Course-Development repo that contains everything participants need for the class. Cloning the repo (or copying the subdirectory) is the only setup required. All labs, demos, and exercises work against this shared workspace, not the student's real codebase. The EE's job between sessions is to help students apply the skills they learned in the workspace to their actual work.

### The Student Workspace

Location: `AI-Deep-Learning-Program/student-workspace/` in the AI-Course-Development repo.

A class-specific repo can be created per engagement by copying this directory into a new repo (or sharing the subdirectory). The source files live here; the trainer pushes additional files to the students' cloned repo as the program progresses.

**Contents at clone time (Session 1 start):**
- `README.md` — explains the workspace structure and how to use it
- `.gitignore` — standard ignores
- `skills/` — the 7 SDLC skeleton skills (RT-only stubs, `.skill.md` format with `disable-model-invocation: true`)
- `demo-outputs/` — pre-generated PRD, Architecture, and UX demo outputs for Session 1 pipeline walkthrough
- `sample-stories/` — 3-5 sample stories/epics for use in labs (so everyone has common inputs)
- `evaluations/` — empty directory where participants will commit their Python evaluation scripts (Session 4+)
- `adversarial-agents/` — empty directory where participants will commit their adversarial prompts (Session 5+)
- `harness-specs/` — directory for future Stage 4 harness specifications (not used in this program)

**Files pushed progressively by the trainer:**
- After Session 1: nothing additional (workspace is already complete for Session 1)
- After Session 2: nothing additional (plan-story and implement-story skeletons already in skills/)
- After Session 3: nothing additional (review-implementation skeleton already in skills/)
- Before Session 4: `evaluations/example-eval-script.py` — a sample Python evaluation script with LLM judge pattern (for participants to study before writing their own)
- Before Session 5: `adversarial-agents/example-adversarial-prompt.skill.md` — a sample adversarial agent skill (for participants to study)
- Before Session 6: No harness spec file is pushed (the specification exercise was removed; Session 6 now has a bounded agent lab)

The trainer guide should note what to push and when.

### Why This Matters

1. **Setup is trivial.** Clone one repo. Everything works. No per-participant environment debugging during Session 1.
2. **Labs are consistent.** Every participant works with the same sample stories, the same skeleton skills, and the same demo outputs. The instructor can predict what participants will see and design labs around known inputs.
3. **Demos are reliable.** The instructor demos against the same inputs participants will use in labs. No surprises from a participant's specific codebase.
4. **EE coaching is clearer.** The sessions teach skills in the workspace; the EE's job is transfer: "take what you learned in the workspace and apply it to your real work." This is a cleaner split than v1's blurred line between training and real work.
5. **Progressive complexity is manageable.** The workspace starts simple and grows as the program progresses. Participants aren't overwhelmed with the full structure on day one.

### How It Works in Practice

**During sessions:** All labs use the shared workspace. Participants clone it, work in it, and commit to it. The instructor demos against the same sample content.

**Between sessions (EE coaching):** The EE helps participants take the skills built in the workspace and apply them to the client's actual codebase. The workspace is the training ground; the real codebase is the application. The EE's coaching notes should emphasize this transfer.

**Session-specific workspace usage:**
- Session 1: Clone the workspace. Use demo-outputs/ for the pipeline walkthrough. Build out epics-and-stories skill in skills/. Use sample-stories/ as lab inputs.
- Session 2: Use the epics-and-stories output from Session 1 as input to plan-story. Build out plan-story and implement-story skills. Use sample-stories/ for lab inputs.
- Session 3: Use the plan-story and implement-story output as input to review-implementation. Build out review-implementation skill. Run the full pipeline on sample-stories/.
- Session 4: Write Python evaluation scripts against skills in the workspace. Use sample-stories/ as evaluation test inputs. Commit scripts to evaluations/.
- Session 5: Write adversarial agent prompts in adversarial-agents/. Run them against skills in the workspace.
- Session 6: Build a bounded agent (full pipeline run in the IDE). The instructor demos a custom harness using the full workspace pipeline.

### What This Replaces

- All session labs that currently reference "your real backlog" or "your actual codebase" change to reference the shared workspace sample content
- The Session 1 "IDE Setup + Rules File" lab changes from configuring against the participant's real project to configuring against the workspace
- The EE coaching notes change from "work alongside participants on their real codebase" to "help participants transfer skills from the workspace to their real codebase"
- The trainer guide gains a "what to push to the student repo" note per session

### Ripple Effects

- All 6 session content files need lab references updated to use the workspace
- All 6 deck prompt files need exercise slide lab steps updated
- EE 12-week curriculum needs coaching notes updated for the transfer model
- EE Implementation Guide needs the workspace transfer model explained
- Trainer Implementation Guide needs per-session workspace push notes
- The student workspace directory needs to be created with all initial content
- The DLPv2-Plan.md summary table needs updating

---

## Summary: The v2 Progression

| Session | Week | v1 Content | v2 Content |
|---------|------|------------|------------|
| 1 | 1 | Acceptance Criteria Generation (commands, Promptfoo preview) | **Prompt/Harness/Model** + **SDLC skeleton skills introduced** + build out **epics-and-stories** skill (skills with `disable-model-invocation: true`) |
| 2 | 3 | Unit Test Generation from story + AC | **The Development Loop**: build out **plan-story** and **implement-story** skeleton skills |
| 3 | 5 | Test Planning | Build out **review-implementation** skeleton skill (testing/review step) |
| 4 | 7 | EDD with Promptfoo | **EDD with Python evaluations + LLM judges** |
| 5 | 9 | Commands to Skills + Hooks & Sentinel Files | **Model invocation** + **Adversarial Agent prompts** |
| 6 | 11 | Bounded Agents & Workflows | **Bounded Agents, Custom Harness Demo & Stage 4 Preview** (bounded agent lab + instructor demo + IIOS stage framework + program close) |

**Terminology change (all sessions):** "Evaluation Criteria (EC)" replaces all v1 variants ("evaluation criteria," "success criteria," bare "criteria") for skill evaluation. "Acceptance Criteria (AC)" is exclusively the product artifact. This disambiguates the two in Session 1 where participants build an AC generation skill and write EC for it simultaneously.

**Deck format change (all sessions):** PPTX files are removed from the repo. Each session gets a `.deck.md` prompt file describing the deck structure (Intro, Check-In, Goals, Exercise, Demo, Compare/Contrast, Lecture, Closing slides) for a design harness to generate the actual slides.

**RTCC redefinition (Sessions 1-3+):** Context is redefined from "background information" to "WHY we want this done — the intent behind the task." Constraints absorb the data, rules, and specifications that v1 placed in Context. The mental model becomes WHO (Role) → WHAT (Task) → WHY (Context) → HOW (Constraints).

### The v2 Automation Spectrum

```
Skills (invocation disabled)
  → Skills (invocation enabled)
    → Adversarial Agents (AI challenges AI)
      → Bounded Agents (multi-step orchestration in the IDE)
        → Custom Harnesses (programmatic multi-step orchestration — demoed in Session 6, built in future Stage 4 DLP)
```

Each step extends what you can trust AI to do. Each step requires earning the right to the next one through evaluation evidence.

---

## Resolved Questions

1. **Session 3 adaptation — RESOLVED**: Session 3 focuses on the "test" prompt of the SDLC skeleton skills. The full chain becomes the SDLC skeleton pipeline: Session 1 covers epics-and-stories, Session 2 covers plan-and-develop, Session 3 covers the test prompt. The chain is the skeleton pipeline itself, not a separate AC → Plan → Code → Test Plan construct.

2. **SDLC skeleton skills — RESOLVED**: The 7 SDLC skeleton commands are introduced in Session 1 (not Week 3 as in v1). They are converted to skill format with `disable-model-invocation: true` and RT-only stubs. The program builds out specific skeleton skills across sessions:
   - Session 1: Focus on the **epics-and-stories** skeleton skill (with demo PRD, UX, and Architecture outputs pre-generated as examples)
   - Session 2: Focus on the **plan** and **develop** (implement-story) skeleton skills, framed as "The Development Loop"
   - Session 3: Focus on the **review-implementation** (test) skeleton skill
   - The remaining skeletons (create-prd, create-architecture, create-ux) are introduced in Session 1 with pre-generated demo outputs so participants see the full pipeline, but are not the primary iteration targets until later

3. **Loop structure — RESOLVED**: The two-loop structure (Foundation, Deepening) is unchanged. Loop 1 builds the foundation skills and the pipeline. Loop 2 deepens discipline with evaluation, adversarial agents, and custom harnesses.

4. **EE Week 6 introduction — RESOLVED**: The EE does NOT pre-teach anything in Week 6. There is no separate introduction to Python evaluation before Session 4. Session 4 is where participants first encounter Python evaluation, and the approach is fully AI-coded — participants have the AI write the evaluation scripts for them. The expectation is that every role (including non-technical roles) succeeds at having evaluations written. The models carry the coding load.

5. **API key logistics — RESOLVED**: The content assumes participants have access to an API key. The logistics of obtaining and distributing keys are left to the Account Manager / Executive Coach to work out as the program kicks off, and communicated to Trainers and Embedded Engineers. The session content does not need to address key provisioning.

6. **Python prerequisite — RESOLVED**: No Python competency is required beyond reading some Python. The models carry the load — participants ask the AI to write evaluation scripts, then read and review the output. The skill being taught is "directing AI to produce evaluation code," not "writing Python from scratch." This is consistent with the v2 philosophy: AI writes the code, participants direct and evaluate.

---

## Remaining Work Items (No Decisions Needed)

7. **Assessment updates**: The Program Completion Rubric and AI Adoption Maturity Assessment need updates to reflect the new vocabulary (skills instead of commands, adversarial agents instead of hooks, custom harnesses instead of bounded agents, Python evaluation instead of Promptfoo).

8. **Sustainment guides**: The post-program sustainment guides reference commands, skills, hooks, and bounded agents. All of these need updating to the v2 vocabulary and concepts.

9. **Terminology sweep**: Every file in the DLP directory needs to be reviewed for AC/EC disambiguation. The term "success criteria" should be eliminated. Bare "criteria" should be expanded to "Evaluation Criteria (EC)" or "Acceptance Criteria (AC)" based on context. This is a mechanical but important pass across all content.

10. **AGENTS.md rewrite**: DONE — the AGENTS.md in Training-Sessions has been rewritten to describe the deck prompt workflow.

11. **Session-Template.pptx**: DONE — the template file is deleted. No replacement template; deck prompt files and the design harness replace it.

---

## Document Status

All open questions are resolved. The plan has 11 changes:

1. Prompt/Harness/Model definition in Session 1
2. Skills from day one with `disable-model-invocation: true`
3. Session 2 teaches The Development Loop (Plan → Code)
4. Session 4 teaches Python evaluations + LLM judges (AI-coded, no Python prerequisite)
5. Session 5 teaches Adversarial Agents + model invocation
6. Session 6 teaches Bounded Agents, Custom Harness Demo & Stage 4 Preview
7. "Evaluation Criteria (EC)" terminology disambiguated from "Acceptance Criteria (AC)"
8. PPTX decks replaced with deck description prompts
9. RTCC redefined: Context = WHY (intent), Constraints = HOW (data/rules)
10. SDLC skeleton skills introduced in Session 1; Sessions 1-3 built around specific skeleton skills
11. Shared student workspace repo for all sessions — clone is the only setup

Three remaining work items require no decisions (assessment updates, sustainment guides, terminology sweep). The next step is to begin content work on the session files, starting with Session 1.