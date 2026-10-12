# Session 2 Deck Prompt — The Development Loop (v2)
*Week 3 | Loop 1 | Role Focus: Development*

---

## Intro Slide

**Title:** The Development Loop: Plan → Code
**Week:** 3 | **Loop:** 1 | **Role Focus:** Development
**Framing:** You've been generating epics and stories for two weeks. Now we take the next step in the SDLC pipeline: planning the implementation and generating code. This is the inner loop of development — Plan → Code — and the quality of the plan determines the quality of the code.

**Callout:** Your Session 1 output (`stories.yaml`) is the INPUT to Session 2. This transition is vital — plan quality depends on story quality. Garbage in, garbage out.

---

## Check-In Slide

**Question:** In the two weeks since Session 1, how has your epics-and-stories skill been working? What did your EC scores show? Where did the skill fail, and what did you do about it?

*This connects Session 1's epics-and-stories work to Session 2's Plan → Code. The stories from Session 1 are the input to the plan skill.*

---

## Session Goals Slide

**Goal 1: Build out the plan-story skill from the SDLC skeleton**
- **Product/Process:** You need to understand what a good implementation plan looks like — your story quality directly determines plan quality. If the plan is vague, the stories were vague.
- **Development:** This is your primary artifact. You own the plan-story skill. The plan is the specification for code generation.
- **Testing:** You need to understand what a plan covers so your review skill (Session 3) can validate that the implementation followed it.

**Goal 2: Build out the implement-story skill from the SDLC skeleton**
- **Product/Process:** You'll see how stories → Plan → Code works as a chain. The quality dependency flows through your stories.
- **Development:** This is the second half of the Development Loop. The implement-story skill takes the plan as its primary input, not the raw story.
- **Testing:** The code generated from the plan is what you'll be reviewing. Understanding how the plan shapes the code tells you what to review.

**Goal 3: Understand the Plan quality dependency — upstream quality determines downstream quality**
- **Product/Process:** This is the key lesson: your story quality determines the plan quality. If you see vague plans, trace it back to the stories.
- **Development:** The plan quality determines the code quality. A specific plan produces specific code. A vague plan produces vague code.
- **Testing:** The plan quality determines what the review should cover. A plan with edge cases produces code with edge cases to review.

**Goal 4: Write EC for both skills before building them**
- **Product/Process:** Your EC for the plan-story skill defines what a good plan looks like. This is the standard the plan must meet.
- **Development:** You write EC for both the plan-story and implement-story skills. Same discipline as Session 1: EC first, build second.
- **Testing:** Seeing how EC is written for Plan and Code skills teaches you the pattern for your review skill in Session 3.

---

## Lecture Slide — The Development Loop

**Content to teach:**

The Development Loop is the inner loop of software development: Plan → Code → Evaluate → Iterate.

1. **Plan** — Use the plan-story skill to generate an implementation plan from the story + AC. The plan-story skill reads `stories.yaml` (it fails if the file is missing) and writes its output to `plan.yaml`. The plan includes: approach, key decisions, edge cases, file changes, and risks. The human reviews and refines the plan.
2. **Code** — Use the implement-story skill to generate code from the plan. The implement-story skill reads `plan.yaml` as its input. The plan is the specification, not the story. The code skill takes the plan as input and produces implementation.
3. **Evaluate** — Check the code against the plan and the AC. Does it do what the plan said? Does it satisfy the AC?
4. **Iterate** — If the code doesn't meet the standard, fix the plan (not the code directly), then regenerate.

Why this matters:
- The plan is an artifact that can be evaluated and refined before code is written
- A specific plan produces specific code; a vague plan produces vague code
- This is the discipline that separates DLP Completion from Basic Prompting: you don't ask AI to "write the code" — you plan first, then generate

---

## Lecture Slide — Plan Failure Modes

**Content to teach:**

What AI gets wrong when planning:
- **Vague plans** — "implement the feature" without specifying the approach, files, or decisions
- **Missing edge cases** — the plan covers the happy path but doesn't identify failure modes from the AC
- **Over-specification** — the plan prescribes implementation details that constrain the code skill unnecessarily
- **Story disconnect** — the plan doesn't reference the story's AC, so the code won't satisfy the requirements
- **Scope creep** — the plan includes work beyond the story's boundaries

---

## Compare/Contrast Slide — Direct Code vs. The Development Loop

| Direct Code (Basic Prompting) | Development Loop (DLP Discipline) |
|---|---|
| "Write the code for this story" | Plan the implementation, then generate code from the plan |
| No artifact to review before code exists | Plan is a reviewable, evaluable artifact |
| Can't tell if the approach was right | The approach is explicit and can be challenged |
| Edge cases discovered during coding | Edge cases identified during planning |
| No separation of thinking from generating | Thinking (plan) is separate from generating (code) |

---

## Demo Slide — The Development Loop on a Real Story

**Description:** The instructor takes a sample story from sample-stories/ + AC (ideally generated by the epics-and-stories skill from Session 1) and demonstrates the Development Loop: first invoking the plan-story skill to generate an implementation plan, then invoking the implement-story skill with the plan as input to generate code. This demonstrates the quality dependency: the plan's specificity directly shapes the code's quality.

**What to focus on:** As the demo runs, notice how the plan references specific AC items and edge cases. Watch what happens when the plan is specific vs. vague — the instructor will show both. See how the implement-story skill uses the plan as its specification, not the raw story.

---

## Exercise Slide — Lab 1: Write EC for Plan and Code Skills

**Lab Name:** Write Evaluation Criteria for Plan-Story and Implement-Story Skills
**Lab Timing:** 15 minutes
**Lab Steps:**
1. For your plan-story skill: write 4-6 EC (e.g., "Every AC item is addressed in the plan" / "At least one edge case per AC item is identified" / "File changes are specified" / "The approach is stated, not implied")
2. For your implement-story skill: write 4-6 EC (e.g., "Code maps to specific plan steps" / "Edge cases from the plan are handled" / "Code would compile in the project's framework" / "No implementation detail is added beyond what the plan specifies")
3. Commit your EC for both skills

**You'll know when you're done because...** you have 4-6 written EC for your plan-story skill and 4-6 for your implement-story skill, each specific and measurable, committed before building either skill.

---

## Exercise Slide — Lab 2: Build Out the Plan-Story Skill

**Lab Name:** Build the Plan-Story Skill
**Lab Timing:** 45 minutes
**Lab Steps:**
1. Open the plan-story.skill.md skeleton — Role and Task defined, Context and Constraints empty
2. Fill in Context (WHY: why we plan before coding, what a good plan enables for code generation) and Constraints (HOW: plan format, what data from the story it needs, team standards)
3. The skill has `disable-model-invocation: true` — invoke via slash command
4. Apply the Load-Bearing Rule: each instruction must map to at least one EC
5. The skill writes its output to `plan.yaml` in the workspace root — this is the YAML pipeline artifact that the implement-story skill will read
6. Test it on 2-3 sample stories from sample-stories/ with AC from the epics-and-stories skill
7. Evaluate the plan output against your EC
8. Commit the skill

**You'll know when you're done because...** you have a committed plan-story skill with RTCC structure that generates implementation plans from sample stories from sample-stories/ + AC, and you've evaluated the output against your EC with pass/fail scores noted.

**Stretch goal:** add Context and Constraints specific to the Pantry Tracker PWA tech stack (TypeScript, Express, React, ShadCN). Include framework-specific plan structure requirements.

---

## Exercise Slide — Lab 3: Build Out the Implement-Story Skill

**Lab Name:** Build the Implement-Story Skill
**Lab Timing:** 30 minutes
**Lab Steps:**
1. Open the implement-story.skill.md skeleton — Role and Task defined, Context and Constraints empty
2. Fill in Context (WHY: why we generate code from the plan not the story, what a good plan enables) and Constraints (HOW: language, framework, codebase conventions, output format)
3. The skill has `disable-model-invocation: true` — invoke via slash command
4. The implement-story skill takes the PLAN as input, not the raw story — this is the Development Loop discipline
5. Apply the Load-Bearing Rule
6. Test it on the plans generated in Lab 2
7. Evaluate the code output against your EC
8. Commit the skill

**You'll know when you're done because...** you have a committed implement-story skill with RTCC structure that takes plans as input and generates code, with output evaluated against your EC.

**Stretch goal:** generate code for both the Express API endpoint AND the React component with ShadCN components and TypeScript types.

---

## Exercise Slide — Lab 4: The Plan Quality Dependency

**Lab Name:** Plan Quality Dependency — Group Analysis
**Lab Timing:** 20 minutes
**Lab Steps:**
1. Take one vague story (or vague AC) and run it through Plan → Code. Note the quality of both outputs.
2. Take the improved version of the same story and run it through Plan → Code. Note the difference.
3. Group discussion: what would you change about your epics-and-stories skill right now based on what you just saw?
4. Capture the key insight: quality problems trace upstream. Fixing the plan rarely fixes a problem that originates in the stories.

**You'll know when you're done because...** you've demonstrated the quality dependency concretely — seen the difference between vague-story and specific-story plans and code — and written down one change you'd make to your epics-and-stories skill based on the evidence.

---

## Closing Slide

**Goal 1: Build the plan-story skill**
- **Product/Process:** You've seen how your story quality directly determines plan quality. If plans are vague, trace it back to the stories.
- **Development:** You own the plan-story skill. This is the first half of the Development Loop. You'll iterate on it with the Embedded Engineer this week.
- **Testing:** You now understand what a plan covers and can use it to validate implementations in Session 3.

**Goal 2: Build the implement-story skill**
- **Product/Process:** You've seen the full stories → Plan → Code chain. Your stories are the upstream input to everything downstream.
- **Development:** You own the implement-story skill. It takes plans as input, not stories. This separation is the discipline.
- **Testing:** The code generated from plans is what you'll review. The plan tells you what was intended, so you can review intent vs. implementation.

**Goal 3: Understand the Plan quality dependency**
- **Product/Process:** Vague plans trace to vague stories. You own the upstream quality.
- **Development:** Vague code traces to vague plans. The plan is the specification; fix it there, not in the code.
- **Testing:** Missing review coverage often traces to missing edge cases in the plan. Check the plan first.

**Goal 4: Write EC before building**
- **Product/Process:** Your EC for the plan-story skill defines the quality bar for plans. Use it to hold the plan accountable.
- **Development:** You've practiced EC-first for two skills now. This is the discipline you'll carry through the entire program.
- **Testing:** You've seen the EC pattern applied to Plan and Code. You'll apply it to your review skill in Session 3.