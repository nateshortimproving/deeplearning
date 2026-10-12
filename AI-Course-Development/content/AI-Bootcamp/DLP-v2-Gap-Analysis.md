# AI Bootcamp vs. DLP v2 — Gap Analysis and Recommended Updates

*Prepared 2026-09-29. Compares AI-Bootcamp (last touched 2026-05-05) against AI-Deep-Learning-Program (v2 rewrite Aug 2026, field-feedback revisions through 2026-09-17). Working document, not yet committed.*

---

## The Core Problem

The bootcamp certifies Embedded Engineer candidates as ready to deliver the DLP. The DLP they will actually deliver is v2. The bootcamp still teaches v1. Three of the bootcamp's four weeks are built on tooling and concepts the DLP has explicitly retired or replaced:

1. **Promptfoo is gone.** DLP v2 evaluates with AI-written Python scripts (deterministic checks + LLM judges). The bootcamp's Week 1-2 measurement apparatus, several certification gate artifacts, and Week 4's handoff checklist all assume Promptfoo.
2. **The commands-vs-skills distinction is gone.** DLP v2 uses skill files from day one with `disable-model-invocation: true`. Moving to auto-invocation is a config-flag flip governed by three graduation criteria, not a format migration. Bootcamp Weeks 1-2 build plain "command" markdown files, and Week 3 Day 1-2 teaches a commands-to-skills conversion that no longer exists in the DLP world.
3. **Hooks and sentinel files are retired.** DLP Session 5 states this explicitly: "deterministic hooks (v1, retired)," replaced by adversarial agents. Hooks/sentinels are now positioned as Stage 4 (post-program) material. Bootcamp Week 3 Days 3-4 are built entirely on hooks, sentinel files, and governed flows.

A candidate graduating the current bootcamp would arrive at a DLP engagement fluent in tools the client team will never see, and never having built the artifacts the DLP Completion rubric actually requires (Python evaluation script, adversarial agent).

---

## Breaking Changes (must fix)

### 1. Replace Promptfoo with Python evaluation scripts + LLM judges

**What DLP does now (Session 4 / Weeks 7-8):**
- Evaluation = a Python script the AI writes and the participant directs. No Python prerequisite. "The models carry the coding load."
- Discipline: **deterministic first, LLM judge second.** Schema validation, field counts, format patterns run as code. LLM judges (structured JSON verdicts with per-criterion reasoning) only for genuinely qualitative criteria. "If you're using an LLM judge for something that could be a regex, your EC needs refinement."
- Rationale for dropping Promptfoo: corporate security teams approve custom Python without friction; third-party tools face approval challenges. Python scripts also combine deterministic and judged checks in one artifact.
- Scripts are committed artifacts in `evaluations/`.

**Bootcamp impact:** Week 1 Tuesday 3:30-5:00 (Intro to Promptfoo), Wednesday and Thursday Promptfoo cycles, all of Week 2's measurement loop, Week 3's "sentinel vs. Promptfoo" division of labor, Week 4's handoff checklist item ("every Promptfoo configuration file committed alongside the command"), and the certification gate ("Promptfoo configuration and run results showing baseline + 3+ iterations"). All need rewriting around Python eval scripts. The EDD pedagogy (Red/Green/Refactor, one change per iteration, documented hypotheses, load-bearing audit) survives intact; only the measurement tool changes.

### 2. Adopt skills-from-day-one with `disable-model-invocation: true`

**What DLP does now (Session 1 / Sessions 5, Week 9-10):**
- Every artifact is a `.skill.md` with YAML frontmatter (`name`, `description`, `disable-model-invocation: true`). Invocation-disabled skills are run explicitly via slash command, which is functionally what the bootcamp calls a "command."
- Enabling model invocation is a **graduation**, gated on: (1) exact trigger inputs defined, (2) output specification defined, (3) at least 3 verified positive trigger test cases, plus a prerequisite of 3+ documented EDD iteration cycles. Negative invocation tests guard against over-invocation, which DLP Week 10 calls "the most common and most urgent failure."

**Bootcamp impact:** Week 1-2 artifacts become skill files (small format change, big conceptual simplification). Week 3 Monday-Tuesday ("Commands vs. Skills," "Building Skills") gets reframed around the graduation criteria. The bootcamp's excellent rationale content (team consensus, wrong-time invocation harm, over-invocation danger) survives but attaches to the flag flip instead of a format migration. Note the DLP frame is subtly different from the bootcamp's: the bootcamp says "stay commands until team consensus," the DLP says "earn the flip with evaluation evidence." Adopt the DLP frame.

### 3. Replace hooks/sentinel-files with adversarial agents (and bounded agents)

**What DLP does now (Session 5 / Weeks 9-10, Session 6 / Week 11):**
- **Adversarial agents**: a prompt that receives another skill's output and tries to find problems: missing requirements, logical errors, edge cases, quality gaps the evaluation script didn't catch. AI-native, so every role can build one. Taught with: the two-prompt problem (worker prompt vs. evaluator prompt, both can have bugs), calibrated severity (blocker/major/minor/nit), actionable findings, domain-expert critic personas, and the value test ("if it only finds what the eval script catches, it's not adding value"). Key complementarity line: "evaluation measures against EC; adversarial challenge finds problems the EC didn't anticipate." A skill that passes its evaluator but fails its adversarial agent has a gap in its EC, and that is itself a finding.
- **Bounded agents**: the full SDLC pipeline chained in one IDE session, with manual evaluation and adversarial review at key steps. Session 6 sequences it as build, then feel the problem (context window degradation at later steps), then see the solution (custom harness demo). Custom harnesses are demo-only; building one is Stage 4 work.
- Hooks and sentinel files: "teams may add deterministic hooks or sentinel files for automated gates; that's the next step after this program, not part of it."

**Bootcamp impact:** Week 3 Wednesday-Thursday (sentinel files, hooks, governed flows) should become adversarial agents + a bounded-agent exercise. This also fixes an internal bootcamp bug: the bootcamp @Overview certification gate already requires "one bounded agent with evaluator evidence of improvement," but no week file ever teaches or builds one. DLP Session 6's bounded agent lab is the content that fills that hole. The governance rationale (never automate what you can't govern) can be preserved as framing for why bounded agents keep humans at the checkpoints.

---

## Vocabulary and Concept Updates (high value, lower effort)

### 4. Add the Prompt/Harness/Model framework to Week 1
The DLP's foundational triad, introduced in Session 1 and referenced through Session 6: Prompt (the instruction), Harness (the capability boundary: Claude Code, Devin, Copilot, ChatGPT web are all different harnesses), Model (the intelligence). It explains why invocation is a harness-level flag, why adversarial agents work, and what a custom harness even is. The bootcamp never defines it. Cost: one 30-45 minute block on Week 1 Monday.

### 5. Adopt the v2 RTCC definition: Context = WHY, Constraints = HOW
The bootcamp teaches Context as "background information." DLP v2 redefined it: Context is the **intent** behind the task (WHY); Constraints are the data, rules, and specifications (HOW). This gives the load-bearing audit a structural diagnostic ("is this instruction in the right RTCC section?"). A bootcamp grad teaching the old definition would directly contradict Session 1 of the program they're delivering. Small edit, high coherence value.

### 6. Adopt EC/AC terminology
DLP v2 is strict: **EC (Evaluation Criteria)** is exclusively the quality bar for a skill's output; **AC (Acceptance Criteria)** is exclusively the product artifact; "success criteria" is retired. This was a documented field confusion in v1. The bootcamp says "test criteria" and "Expected Outputs" throughout. Sweep the vocabulary so candidates speak the program's language. The bootcamp's manual-test-file discipline maps cleanly: writing Input Prompts + Expected Outputs by hand before building *is* writing EC first.

### 7. Update the automation spectrum to the v2 version
Bootcamp Week 3: Commands → Skills → Hooks + Sentinel Files → Governed Workflows.
DLP v2: Skills (invocation disabled) → Skills (invocation enabled) → Adversarial Agents → Bounded Agents → Custom Harnesses (demoed, built in Stage 4).
Each step is earned through evaluation evidence. Also adopt the **IIOS stage framing** (Stage 3 = Task, what this program achieves; Stage 4 = Workflow, roughly 10x the effort, team coordination and IT infrastructure; "a Stage 4 workflow on weak Stage 3 foundations is a slop cannon"). Week 4's "articulate the full DLP arc" objective depends on candidates knowing this map.

### 8. Align the certification gate with the actual DLP Completion bar
The DLP Completion rubric (assessed jointly by EE + Trainer at Week 12) rates four criteria: **Craft** (a committed skill with invocation disabled, plus a skill with invocation enabled or an adversarial agent, at least one built independently), **Evaluate** (a working Python eval script with LLM judge, specific EC, 3+ documented iterations), **Iterate** (3+ documented improvement cycles), **Adopt** (one real workflow task done differently as default behavior, persisting without the EE). Completion correlates with 3.0+ averages on dimensions 1-4 of the 21-question / 7-dimension maturity assessment (total 43-58).

The EE-Implementation-Guide additionally requires EE candidates to have personally built: 1+ skill with `disable-model-invocation: true`, 1+ Python evaluation script with LLM judge, 1+ adversarial agent prompt, and to *demonstrate* (not explain) Python evaluation.

**The bootcamp gate should mirror these exactly.** Current mismatches: it requires Promptfoo results (retired tool), a governed-flow artifact (retired concept), and a bounded agent (fine to keep, but now teach it); it does not require an adversarial agent or a Python eval script (both required by the program candidates will deliver). Also: use the maturity assessment as a scored instrument in the gate, not just rehearsal calibration material (Week 4 Wednesday currently only "reviews" it). The 7 dimensions include Python Evaluation and Adversarial Thinking; the current bootcamp cannot move either needle.

---

## Week-by-Week Recommendations

### Week 1 (Foundations): keep the shape, change the tools
- Keep EDD-first and the load-bearing rule. They are the program's spine and match DLP v2 exactly.
- Keep the social-media pipeline theme if desired (deliberately non-technical, no right answer). It is bootcamp-specific and harmless. But the four pipeline artifacts become skill files with frontmatter, and measurement becomes a Python eval script instead of Promptfoo. Tuesday afternoon becomes "have the AI write your evaluation script," which is itself a great first lesson in the AI-writes-the-code pattern.
- Add: Prompt/Harness/Model block (Monday), RTCC WHY/HOW definitions, EC vocabulary.
- Add: deterministic-first / LLM-judge-second as an explicit teaching point when criteria are defined Monday.
- Update tool examples: DLP v2 uses Claude Code, Devin, Copilot as example harnesses (Windsurf was swapped for Devin in the Session 6 restructure).

### Week 2 (SDLC workflow): adopt the real DLP artifacts
- Biggest coherence win available: **replace the inline RT-only stubs with the actual DLP student-workspace** (`AI-Deep-Learning-Program/student-workspace/`). Same 7 skeleton skills, same names, but with YAML file contracts (`stories.yaml`, `plan.yaml`, `review.yaml`), schemas, fail-fast missing-input behavior, pre-generated demo outputs, and the Pantry Tracker PWA sample domain. Bootcamp grads then coach the exact artifacts they trained on, and the bootcamp stops maintaining a divergent copy.
- Teach the YAML pipeline contract: each skill writes a file the next reads; `plan-story` fails fast if `stories.yaml` is missing; `review-implementation` writes `review_status`/`review_notes` back into `stories.yaml` (the literal feedback loop).
- Add the three-way contrast demo (good stories vs. vague stories vs. plausible-but-bad AI-generated stories from `sample-stories/`) as an EC-sharpening exercise.
- Keep the upstream-quality-dependency content; the DLP's plan-quality dependency (vague plan → vague code; code is generated from the plan, never directly from the story) is the same lesson and should be named explicitly.
- Replace the `../Resources/SDLC-Workflow.png` reference with the DLP's maintained diagrams (`images/sdlc-pipeline.svg` and `sdlc-pipeline-simple.svg`, Mermaid-sourced).

### Week 3 (Automation spectrum): rebuilt around v2
- Monday-Tuesday: from "commands vs. skills" to "invocation disabled vs. enabled." Same concerns (team consensus, wrong-time invocation, over-invocation danger), new mechanism (the flag, the three graduation criteria, 3 positive + 2 quality invocation tests, 3+ EDD cycles prerequisite, negative invocation tests).
- Wednesday: adversarial agents (replacing sentinel files). Two-prompt problem, calibrated severity, evaluator-vs-adversarial comparison exercise (run both against the same outputs, map the delta).
- Thursday: bounded agents (replacing governed flows). Chain a two-step or full pipeline in one session with evaluation at the checkpoints; deliberately feel context-window degradation; name the custom harness as the beyond-IDE answer and Stage 4 as future work.
- Friday synthesis: map Week 1-2 artifacts onto the v2 spectrum; rewrite the "governance explanation paragraph" exercise around adversarial agents + bounded agents.

### Week 4 (Coaching and certification): mostly durable, targeted updates
- The four resistance scenarios, player-coach model, behavior-change observation, and artifact-transferability checklist are all still right. Keep them.
- Update the artifact checklist: Python eval scripts committed alongside the skill they evaluate (not Promptfoo configs); adversarial prompts documented; drop sentinel-schema items.
- Add the DLP operating model: the Trainer/EE introduce-then-reinforce cadence, the standing weekly 30-minute Trainer touchpoint the EE owns, the `[PROGRAM FEEDBACK]` loop, independence checks at Weeks 8 and 10, and the Week 12 joint rubric conversation. Current Week 4 never mentions the Trainer role. Candidates are certifying into a two-person delivery model and should know their half of it.
- Add required reading: the **EE-Playbook** (8 field-tested plays from Wave 1: Rough Process Mapping, Divide and Conquer, Goals→Measures→Actions, An Exercise After Each Workshop, Build Your Own SDLC Pipeline, Everyone Gets a Turn at Show-and-Tell, One Meeting One Artifact, Cross-Pollination). This is the best coaching material in the repo and did not exist when the bootcamp was written. Week 4 Monday already says "review feedback from existing DLP engagements"; point it at the playbook.
- Add to rehearsal prep: the sustainment guides (Executive Sponsors, Managers, Team Members), so EEs know what post-program support looks like and can coach toward it. The Managers guide's "real adoption vs. performance" checklist is directly relevant to the polite-compliance discussion already in Week 4.
- Cert gate: rebuild per section 8 above.

---

## Asset and Infrastructure Items

- **Katas are orphaned.** `AI-Bootcamp/Resources/Katas/` (14 katas, Requirements + Expected-Outcomes pairs) is referenced by no week file and no overview. Either wire them in (e.g., optional evening practice for Week 1-2, or stretch material) or remove them. They predate the DLP's stretch-goal-per-lab pattern; the cleaner move is probably to use them as stretch material for candidates who finish early, and say so in the week files.
- **PDFs are derived artifacts.** `AI-Bootcamp/PDFs/` is generated by `generate_pdfs.py`. After any content update, regenerate. Consider noting in the README/@Overview that PDFs are derived so nobody edits them directly.
- **Reference DLP assessment instruments by path** rather than copying them: `Resources/Measures-and-Assessments/AI-Adoption-Maturity-Assessment.md` and `Program-Completion-Rubric.md` are the live versions; the bootcamp should point at them so a future terminology sweep doesn't fork them again.

## What Does NOT Need to Change

- EDD as the foundational discipline, Red/Green/Refactor for prompts, the load-bearing rule, manual test files before building. DLP v2 kept all of it and doubled down.
- Week 2's core pedagogy: RT-only starters as the deliberate Red state, Context-before-Constraints sequencing, upstream quality tracing, generalization check on an unseen input.
- Week 4's coaching core: player-coach model, four resistance scenarios, rehearsal engagement, behavior-change observation. Timeless.
- The 4-week structure and travel-day timing. No DLP change pressures it.

## Out of Scope for the Bootcamp

The AM/EC enterprise-engagement material (Track/Wave/MVP packaging, Governance Infrastructure, DevOps Acceleration, Data & Compliance Enablement, pricing/SOW guidance) is sales-side. EE candidates do not need it to pass the gate. At most, one paragraph in Week 4 so they know these offerings exist when a client asks "what's next."

---

## Suggested Sequencing of the Update

1. **Vocabulary + framework sweep** (sections 4-6): Prompt/Harness/Model, RTCC WHY/HOW, EC/AC, tool examples. Low risk, high coherence.
2. **Week 1-2 measurement swap** (section 1): Promptfoo out, Python eval scripts in, including the certification gate artifacts.
3. **Week 2 adopts the student workspace** (Week 2 recs): delete the inline stubs, teach the real skeletons and YAML contracts.
4. **Week 3 rebuild** (sections 2-3): graduation criteria, adversarial agents, bounded agents.
5. **Week 4 + certification gate realignment** (section 8, Week 4 recs): mirror the EE-Implementation-Guide requirements and the Program Completion Rubric; add Trainer/EE operating model and EE-Playbook reading.
6. **Cleanup**: katas decision, diagram reference, PDF regeneration, maturity-assessment references by path.
