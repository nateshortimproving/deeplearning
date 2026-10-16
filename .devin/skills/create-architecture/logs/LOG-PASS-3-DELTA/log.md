# LOG-PASS-3 — create-architecture iteration 3 (delta study)

Date: 2026-10-16
Evaluator: `.devin/skills/create-architecture/eval_architecture.py`
Criteria: `.devin/skills/create-architecture/eval-criteria.md`
Artifacts under test:
- Baseline: `AI-Course-Development/.../SDLC-Commands/demo-architecture-output.md` (RT-only stub output)
- Improved: `../outputs/pantry-pwa/architecture.md` (skill with Context + Constraints, same Pantry Tracker PRD input)
Command: `python3 eval_architecture.py <demo-path> outputs/pantry-pwa/architecture.md`
LLM judge: Devin (verdicts in `judge_verdicts.json` beside this log)
Previous: `../LOG-PASS-2/log.md` (6/6 vs SKILL.md)

## Result: demo 1/6 RED vs improved 6/6 GREEN

### demo-architecture-output (RT-only stub)

| Check | EC | Verdict | Detail |
|-------|----|---------|--------|
| required_sections_present | EC 1 | FAIL (RED) | missing: Overview; Data Flow; Constraints |
| components_min_3 | EC 2 | PASS (GREEN) | 4 components, each with a Responsibility entry |
| decisions_table_min_2 | EC 3 | FAIL (RED) | no markdown table found in Key Technical Decisions |
| constraints_min_2 | EC 4 | FAIL (RED) | Constraints section missing |
| no_orphan_components | EC 5 | FAIL (RED) | Data Flow section missing |
| llm_judge_specificity | judge | FAIL (RED) | Content is specific and tradeoffs are real, but no Constraints section, decisions are unstructured bullets, and Service Worker / Express API Gateway / IndexedDB appear in the interaction diagram without being named components |

### architecture (improved skill output)

| Check | EC | Verdict | Detail |
|-------|----|---------|--------|
| required_sections_present | EC 1 | PASS (GREEN) | all 5 required sections present and non-empty |
| components_min_3 | EC 2 | PASS (GREEN) | 6 components, each with a Responsibility entry |
| decisions_table_min_2 | EC 3 | PASS (GREEN) | 4 decision rows with >= 3 filled cells |
| constraints_min_2 | EC 4 | PASS (GREEN) | 4 constraint items |
| no_orphan_components | EC 5 | PASS (GREEN) | all components referenced in Data Flow |
| llm_judge_specificity | judge | PASS (GREEN) | Concrete tech choices, tradeoff rationale tied to PRD, every named component exercised in Data Flow, scope respects PRD boundaries |

## Delta — what did Context and Constraints change?

### Hypothesis
*Adding Context (PRD pipeline inputs and how to use them) and Constraints
(component count, decision-table completeness, no-orphan rule) should produce
a structurally different architecture document, not just a marginally nicer
one — the deltas should map to specific ECs.*

**Change evaluated:** demo (RT-only) vs improved (RTCC) on the same PRD input.
**Result:** hypothesis held — 5 of 6 checks moved from RED to GREEN.

### Observable deltas

| Dimension | Demo (RT-only) | Improved (RTCC) |
|-----------|---------------|-----------------|
| Structure | Ad-hoc sections (Major Components, Component Interactions, Key Technical Decisions as bullets) | Canonical sections (Overview, Components, Data Flow, decision table, Constraints) |
| Decision format | Free-form bullet list | Decision/Choice/Rationale table — readable at a glance, comparable across rows |
| Constraints | Absent entirely — no stated limits | 4 explicit constraints incl. PRD out-of-scope boundaries |
| Component accounting | Interaction diagram invents nodes not in Components (Service Worker, API Gateway, IndexedDB) — orphans | Every named component appears in Data Flow; nothing flows that isn't defined |
| Traceability | Reasonable coverage but assumptions unstated | Decisions cite PRD requirements (offline-first kitchen use, single-user scope) |
| Specificity | Specific (React, Express, IndexedDB) — a strength even without Context | Equally specific, plus each choice tied to a stated rationale |

### Conclusion

The Context/Constraints sections are load-bearing: they changed the *shape*
of the output (required sections, decision table, component/Data Flow
consistency) not just its polish. The demo output's main strengths —
concrete technologies and honest tradeoffs — came through in the improved
output as well, indicating the added structure did not sacrifice content
quality.
