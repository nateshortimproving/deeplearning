# LOAD-BEARING-AUDIT-5 — create-ux instruction → EC mapping

Date: 2026-10-16
Evaluator: `.devin/skills/create-ux/eval_ux.py` (deterministic checks)
Criteria: `.devin/skills/create-ux/eval-criteria.md`
Artifact under test: `.devin/skills/create-ux/SKILL.md`
Command: `python3 eval_ux.py <variant>.md` against a modified copy per instruction
LLM judge: not run (SKIP — verdicts live per-log under `LOG-PASS-*/judge_verdicts.json`)
Baseline: `../LOG-PASS-4/log.md` (6/6 GREEN); current deterministic 5/5 GREEN

Method (per Exercise 4): for every instruction in SKILL.md, predict which EC
fails if the instruction is removed, then verify by evaluating a modified
copy. "Tested" = a real removal + eval run on a temp file.

## Removal-test matrix

| Variant | required_sections | personas_min_2 | flows_min_2 | error_table_min_2 | design_a11y_resp | judge |
|---------|-------------------|----------------|-------------|-------------------|------------------|-------|
| baseline | PASS | PASS | PASS | PASS | PASS | SKIP |
| no `## Role` | PASS | PASS | PASS | PASS | PASS | SKIP |
| no `## Task` | PASS | PASS | PASS | PASS | PASS | SKIP |
| no `## Context` (whole) | PASS | PASS | PASS | PASS | PASS | SKIP |
| no `## Constraints` bullets | PASS | PASS | PASS | PASS | PASS | SKIP |
| no Output Format preamble | PASS | PASS | PASS | PASS | PASS | SKIP |
| no template `### [Persona 2 Name]` | PASS | **FAIL** | PASS | PASS | PASS | SKIP |
| no template `### Flow 2` | PASS | PASS | **FAIL** | PASS | PASS | SKIP |
| no template `## Key Interactions` | PASS | PASS | PASS | PASS | PASS | SKIP |
| no error-table row 2 | PASS | PASS | PASS | **FAIL** | PASS | SKIP |
| no `Accessibility:` bullet | PASS | PASS | PASS | PASS | **FAIL** | SKIP |
| no `Responsiveness:` bullet | PASS | PASS | PASS | PASS | **FAIL** | SKIP |
| no `### Example output` | PASS | PASS | PASS | PASS | PASS | SKIP |
| no `### File Contract` | PASS | PASS | PASS | PASS | PASS | SKIP |

## Instruction → EC mapping

| Instruction | Predicted EC | Tested | Result |
|-------------|--------------|--------|--------|
| `## Role` — senior UX designer persona | None (judge, indirect) | Yes | No failure — not load-bearing on deterministic checks; frames the judge-graded qualities |
| `## Task` — produce UX guidance incl. flows, interactions, decision/error identification | EC 1, EC 3 (judge decision quality) | Yes | No failure — intent-mapped to EC 1 and judge rubric items (plausible flows, real decisions) |
| `## Context` — PRD/architecture inputs, derive personas/flows from them | EC 2 + judge (persona traceability, plausible flows) | Yes | No failure — intent-mapped; judge rubric items 3–4 require personas to trace to the PRD and errors to be feature-realistic |
| `## Constraints` bullet — "Persona coverage: ≥2 personas, Role/Goals/Pain Points" | EC 2 | Yes | No failure — clean 1:1 intent map to EC 2; not load-bearing on the artifact eval |
| `## Constraints` bullet — "Flow completeness: ≥2 flows, ≥3 steps + Decision Point + Error Risk" | EC 3 | Yes | No failure — clean 1:1 intent map to EC 3 |
| `## Constraints` bullet — "Error states: table ≥2 rows, Scenario/User Sees/Recovery" | EC 4 | Yes | No failure — clean 1:1 intent map to EC 4 |
| `## Constraints` bullet — "Design coverage: accessibility AND responsiveness" | EC 5 | Yes | No failure — clean 1:1 intent map to EC 5 |
| `## Constraints` bullet — "Failure paths: ≥1 non-happy path" | None deterministic | Yes | **No EC mapping in eval-criteria.md** — covered only by judge rubric item 5 ("both happy and failure paths"). Closest thing to dead weight in this skill; either add to EC or accept as judge-only |
| Output Format preamble — "replace every bracketed placeholder…" | EC 1 | Yes | No failure — intent-mapped (non-empty, non-placeholder output) |
| Template `## User Personas` + 2 persona stubs (Role/Goals/Pain Points) | EC 1, 2 | Yes | **Load-bearing, verified** — removing Persona 2 fails `personas_min_2` (EC 2) |
| Template `## User Flows` + 2 flow stubs (3 steps, Decision Point, Error Risk) | EC 1, 3 | Yes | **Load-bearing, verified** — removing Flow 2 fails `flows_min_2` (EC 3) |
| Template `## Key Interactions` + 2 items | EC 1 | Yes | Individually NOT uniquely load-bearing — removal passes because the example's `## Key Interactions` re-binds the requirement. Load-bearing on EC 1 as part of the template/example pair |
| Template `## Design Considerations` + Accessibility + Responsiveness bullets | EC 1, 5 | Yes | **Load-bearing, verified** — removing either bullet fails `design_covers_a11y_responsive` (EC 5) |
| Template `## Error States` table + 2 rows | EC 1, 4 | Yes | **Load-bearing, verified** — removing row 2 fails `error_table_min_2` (EC 4) |
| `### Example output` + "do not copy" note | Judge (specificity) | Yes | No deterministic failure — verified load-bearing on the judge in LOG-PASS-3/4 (example carries the quality bar) |
| `### File Contract` | None | Yes | No failure — pipeline plumbing, not an EC-bearing instruction; keep or document as non-EC |

## Findings

1. **Five verified load-bearing instructions** (deterministic): Persona 2 stub
   (EC 2), Flow 2 stub (EC 3), error-table row 2 (EC 4), and both Design
   Considerations bullets (EC 5). Every content-bearing element in the template
   that an EC sets a minimum on was verified.
2. **Cleanest constraint block in the chain:** four of the five `## Constraints`
   bullets map 1:1 onto EC 2–5. Unlike create-prd, none is load-bearing on the
   artifact eval (the skill's `## Constraints` heading matches no required-section
   group, so the eval never reads these bullets) — they are load-bearing purely by
   intent for the generated output.
3. **One no-EC instruction:** the "Failure paths" constraint bullet has no
   counterpart in eval-criteria.md; it is enforced only by the judge rubric's
   "happy and failure paths" item. Flagged — not removed.
4. **Heading redundancy:** `## Key Interactions` removal still passes — the
   example's duplicate heading re-binds EC 1, same template/example redundancy
   seen in create-prd.
5. **Prose instructions** (`## Role`, `## Task`, `## Context`, preamble,
   `### File Contract`) map to EC 1 or judge-only criteria and are not
   deterministically testable on the artifact — consistent with their role as
   shaping instructions rather than format spec.
