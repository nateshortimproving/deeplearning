# LOAD-BEARING-AUDIT-5 — create-architecture instruction → EC mapping

Date: 2026-10-16
Evaluator: `.devin/skills/create-architecture/eval_architecture.py` (deterministic checks)
Criteria: `.devin/skills/create-architecture/eval-criteria.md`
Artifact under test: `.devin/skills/create-architecture/SKILL.md`
Command: `python3 eval_architecture.py <variant>.md` against a modified copy per instruction
LLM judge: not run (SKIP — verdicts live per-log under `LOG-PASS-*/judge_verdicts.json`)
Baseline: `../LOG-PASS-4/log.md` (6/6 GREEN); current deterministic 5/5 GREEN

Method (per Exercise 4): for every instruction in SKILL.md, predict which EC
fails if the instruction is removed, then verify by evaluating a modified
copy. "Tested" = a real removal + eval run on a temp file.

## Removal-test matrix

| Variant | required_sections | components_min_3 | decisions_table | constraints_min_2 | no_orphan | judge |
|---------|-------------------|------------------|-----------------|-------------------|-----------|-------|
| baseline | PASS | PASS | PASS | PASS | PASS | SKIP |
| no `## Role` | PASS | PASS | PASS | PASS | PASS | SKIP |
| no `## Task` | PASS | PASS | PASS | PASS | PASS | SKIP |
| no `## Context` (whole) | PASS | PASS | PASS | PASS | PASS | SKIP |
| no `## Constraints` bullets | PASS | PASS | PASS | PASS | PASS | SKIP |
| no `## Constraints` (whole) | PASS | PASS | PASS | PASS | PASS | SKIP |
| no Output Format preamble | PASS | PASS | PASS | PASS | PASS | SKIP |
| no template `### [Component 3 Name]` | PASS | **FAIL** | PASS | PASS | PASS | SKIP |
| no decisions-table row 2 | PASS | PASS | **FAIL** | PASS | PASS | SKIP |
| no template constraint item 2 | PASS | PASS | PASS | PASS | PASS | SKIP |
| no Data Flow narrative | **FAIL** | PASS | PASS | PASS | **FAIL** | SKIP |
| no `## Constraints` + no template constraint items | **FAIL** | PASS | PASS | PASS | PASS | SKIP |
| no `### Example output` | PASS | PASS | PASS | PASS | PASS | SKIP |
| no `### File Contract` | PASS | PASS | PASS | PASS | PASS | SKIP |

## Instruction → EC mapping

| Instruction | Predicted EC | Tested | Result |
|-------------|--------------|--------|--------|
| `## Role` — senior software architect persona | None (judge, indirect) | Yes | No failure — not load-bearing on deterministic checks |
| `## Task` — produce architecture doc: components, responsibilities, interactions, decisions | EC 1 | Yes | No failure — intent-mapped to EC 1 (enumerates the required coverage) |
| `## Context` — derive components from Functional Requirements, non-functional bar from Success Metrics, boundaries from Out of Scope | EC 1 + judge (traceability) | Yes | No failure — intent-mapped; judge rubric item 5 grades whether the design traces to source requirements |
| `## Constraints` bullet — "No orphan components" | EC 5 | Yes | No failure — clean 1:1 intent map to EC 5; not load-bearing on the artifact eval |
| `## Constraints` bullet — "Decision table completeness: ≥2 rows, Decision/Choice/Rationale" | EC 3 | Yes | No failure — clean 1:1 intent map to EC 3 |
| `## Constraints` bullet — "Component count: ≥3 with Responsibility/Interfaces/Dependencies" | EC 2 | Yes | No failure — clean 1:1 intent map to EC 2 |
| Output Format preamble — "replace every bracketed placeholder…" | EC 1 | Yes | No failure — intent-mapped |
| Template `## Overview` | EC 1 | No | Load-bearing by intent (required + non-empty); not individually removal-tested |
| Template 3 × `### [Component N Name]` stubs with Responsibility/Interfaces/Dependencies | EC 1, 2 | Yes | **Load-bearing, verified** — removing Component 3 fails `components_min_3` (EC 2) |
| Template `## Data Flow` narrative naming all components | EC 1, 5 | Yes | **Load-bearing, verified** — removing the narrative fails both `required_sections_present` (empty) and `no_orphan_components` (EC 5) |
| Template `## Key Technical Decisions` table + 2 rows | EC 1, 3 | Yes | **Load-bearing, verified** — removing row 2 fails `decisions_table_min_2` (EC 3) |
| Template `## Constraints` + 2 items | EC 1, 4 | Yes | **Shadowed — not load-bearing as written** — removing an item passes because the skill's own `## Constraints` heading binds the "constraints" group first and its 3 bullets satisfy `constraints_min_2`. Fails only when the skill section AND template items are both removed |
| `### Example output` + "do not copy" note | Judge (specificity) | Yes | No deterministic failure — verified load-bearing on the judge in LOG-PASS-4 |
| `### File Contract` | None | Yes | No failure — pipeline plumbing, not an EC-bearing instruction; keep or document as non-EC |

## Findings

1. **Three verified load-bearing instructions** (deterministic): Component 3 stub
   (EC 2), decisions-table row 2 (EC 3), and the Data Flow narrative (EC 5 + the
   non-empty half of EC 1).
2. **Cleanest constraint block in the chain:** the three `## Constraints` bullets
   map 1:1 onto EC 5, EC 3, EC 2 — all intent-mapped, none needed by the artifact
   eval.
3. **EC 4 is enforced by accident:** `constraints_min_2` binds the *skill's own*
   `## Constraints` heading (first heading matching "constraint"), so its three
   bullets supply the pass — the template's `## Constraints` items are shadowed
   and can be removed freely without a failure. This is the same accidental
   binding seen in create-prd (there it fed `sections_non_empty`). Recommendation:
   either rename the skill-level section so evals bind the template heading, or
   accept the coupling and note that EC 4's real spec lives in the template.
4. **EC 5 detection weakness (verified):** dropping only `[Component 3 Name]`
   from the Data Flow narrative still passes `no_orphan_components` — the check
   strips stopwords, leaving "name" as the only distinguishing token in
   `[Component N Name]`, which components 1 and 2 still supply. In a generated
   document with real component names the check works; on the SKILL.md artifact
   a single dropped reference is undetectable.
5. **Non-list-item fallback quirk:** with the skill `## Constraints` heading
   emptied of bullets, `constraints_min_2` still passed — the check falls back to
   counting non-empty *lines* (`### Output Format`, the preamble sentence, the
   fence marker all count). EC 4 cannot fail on this artifact unless the whole
   region is gutted.
6. **No template content lacks an EC** — every required section in the template
   maps to at least one EC (unlike create-prd's Proposed Solution / In Scope /
   Open Questions). The only no-EC items are `## Role` and `### File Contract`
   (framing/plumbing, not content instructions).
