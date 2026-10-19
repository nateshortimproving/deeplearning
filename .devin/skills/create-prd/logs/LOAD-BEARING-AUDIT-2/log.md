# LOAD-BEARING-AUDIT-2 — create-prd instruction → EC mapping

Date: 2026-10-16
Evaluator: `.devin/skills/create-prd/eval_prd.py` (deterministic checks)
Criteria: `.devin/skills/create-prd/eval-criteria.md`
Artifact under test: `.devin/skills/create-prd/SKILL.md`
Command: `python3 eval_prd.py <variant>.md` against a modified copy per instruction
LLM judge: not run (SKIP — verdicts live per-log under `LOG-PASS-*/judge_verdicts.json`)
Baseline: `../LOG-PASS-1/log.md` (4/4 GREEN); current deterministic 3/3 GREEN

Method (per Exercise 4): for every instruction in SKILL.md, predict which EC
fails if the instruction is removed, then verify by evaluating a modified
copy. "Tested" = a real removal + eval run on a temp file.

## Removal-test matrix

| Variant | required_sections | sections_non_empty | out_of_scope_min | judge |
|---------|-------------------|--------------------|--------------------|-------|
| baseline | PASS | PASS | PASS | SKIP |
| no `## Role` | PASS | PASS | PASS | SKIP |
| no `## Context` para 1 | PASS | PASS | PASS | SKIP |
| no `## Context` para 2 | PASS | PASS | PASS | SKIP |
| no `## Context` (whole) | PASS | PASS | PASS | SKIP |
| no `## Constraints` bullets | PASS | **FAIL** | PASS | SKIP |
| no `## Constraints` (whole) | PASS | **FAIL** | PASS | SKIP |
| no `## Task` | PASS | PASS | PASS | SKIP |
| no Output Format preamble | PASS | PASS | PASS | SKIP |
| no template `## Problem Statement` | PASS | PASS | PASS | SKIP |
| no template `## Target Audience` | PASS | PASS | PASS | SKIP |
| no 2nd `### Out of Scope` item | PASS | PASS | **FAIL** | SKIP |
| no `### Example output` | PASS | PASS | PASS | SKIP |
| no `### File Contract` | PASS | PASS | PASS | SKIP |

## Instruction → EC mapping

| Instruction | Predicted EC | Tested | Result |
|-------------|--------------|--------|--------|
| `## Role` — senior PM persona | None (judge EC 3, indirect) | Yes | No failure — not load-bearing on deterministic checks; intent-mapped to judge EC 3 |
| `## Context` ¶1 — use Problem Statement / Target Audience / Success Metrics to frame sections | EC 1, 3 | Yes | No failure — instructs the model to produce the required sections (EC 1/5) and align content to definitions (EC 3); the artifact passes without it because template placeholders count as sentences |
| `## Context` ¶2 — downstream consumers, "concrete enough… without follow-up questions" | EC 3 (judge specificity) | Yes | No failure — intent-mapped to judge EC 3 (specificity) and EC 2 (meaningful content) |
| `## Constraints` bullet — "Include all required sections… None may be empty" | EC 1, 2, 5 | Yes (as a block) | **Load-bearing, verified** — the 4 bullets are the only ≥3-word sentences in the bound Assumptions/Constraints/Dependencies sections; removing them fails `sections_non_empty` (EC 2/5) |
| `## Constraints` bullet — "at least two Out of Scope items" | EC 4 | Yes (as a block) | Load-bearing by intent (EC 4); also part of the verified EC 2/5 block above |
| `## Constraints` bullet — "Success Metrics must be measurable" | EC 3 | Yes (as a block) | Load-bearing by intent (judge definition-alignment); part of verified EC 2/5 block |
| `## Constraints` bullet — "requirements/stories specific enough to act on" | EC 3 | Yes (as a block) | Load-bearing by intent (judge specificity); part of verified EC 2/5 block |
| `## Task` — define problem, solution, metrics, scope | EC 1 | Yes | No failure — intent-mapped to EC 1/5 (directs the doc's required coverage) |
| Output Format preamble — "replace every bracketed placeholder…" | EC 2 | Yes | No failure — intent-mapped to EC 2/3 (guards against empty/vague output in generated docs) |
| Template `## Problem Statement`, `## Target Audience`, `## Functional Requirements`, `## User Stories`, `## Success Metrics`, `## Assumptions`, `## Constraints`, `## Dependencies` headings | EC 1, 5 | Yes (2 of 8) | Individually NOT uniquely load-bearing — removing one heading passes because the skill's `## Context` (alias match) or the example's duplicate heading re-binds the requirement. Collectively load-bearing on EC 1/5 as the primary spec |
| Template `### Out of Scope` + 2 placeholder items | EC 4 | Yes | **Load-bearing, verified** — removing the 2nd item fails `out_of_scope_min_items` (EC 4) |
| Template `## Proposed Solution` | None | No | **No EC mapping** — not a required section in eval-criteria.md. Candidate for removal or for an EC addition |
| Template `### In Scope` + items | None | No | **No EC mapping** — EC only covers Out of Scope. Candidate for removal or EC addition |
| Template `## Open Questions` | None | No | **No EC mapping** — same flag |
| `### Example output` + "do not copy" note | EC 3 (judge) | Yes | No deterministic failure — verified load-bearing on the judge in LOG-PASS-1 (example is what the judge grades for specificity) |
| `### File Contract` | None | Yes | No failure — pipeline plumbing, not an EC-bearing instruction; keep (needed by the harness) or document as non-EC |

## Findings

1. **Two verified load-bearing instructions** (deterministic): the `## Constraints`
   bullet block (EC 2/5 via `sections_non_empty`) and the second `### Out of Scope`
   placeholder item (EC 4).
2. **Fragile coupling:** the EC 2/5 pass depends on the *skill's own* `## Constraints`
   prose — the eval binds the "constraint" required-section group to that heading and
   counts its bullets as the AC&D sentences. The template's own `## Assumptions` /
   `## Constraints` / `## Dependencies` bodies are 2-word placeholders
   (`[Assumption 1]` = 2 words < the 3-word floor). If the skill-level Constraints
   section is ever removed or renamed, `sections_non_empty` fails even though the
   template is unchanged. Recommendation: make the template placeholders ≥3 words
   (e.g., `[Assumption — what we're taking for granted]`) so the EC pass lives in
   the template, not in the prose around it.
3. **Heading redundancy:** every required section heading exists twice (template +
   example), and `## Context` aliasing covers `problem statement`, so no single
   heading removal can fail `required_sections_present`. The template and example
   are load-bearing on EC 1 as a pair, not individually.
4. **EC coverage gaps:** `## Proposed Solution`, `### In Scope`, and
   `## Open Questions` appear in the template but map to no EC. Either they earn
   their place in eval-criteria.md or they are removal candidates. (Kept — this
   audit maps, it does not delete.)
5. **Judge-only instructions:** `## Context` ¶2, the specificity/measurability
   constraint bullets, and the worked example map to EC 3, which is only exercised
   by the LLM judge — untestable here without a `judge_verdicts.json` at skill root.
