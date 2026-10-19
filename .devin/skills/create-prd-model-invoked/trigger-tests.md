# Trigger Tests: create-prd-model-invoked

## 1. Exact Triggers

The model should invoke this skill when ALL of the following hold:

- The user describes a new feature, product idea, or initiative they want built
- No PRD exists yet for that feature (this skill is the pipeline entry point)
- The request is not limited to UX/design guidance, implementation, or discussion
  of an existing PRD

Example utterances that should match:

- "I want to build X"
- "Let's add Y to the product"
- "Write up requirements for Z"
- "Help me spec out this feature"

## 2. Output Spec

When triggered, the skill produces a PRD markdown file satisfying
`eval-criteria.md` (EC 1–5): all required sections present, non-empty,
aligned with definitions, and at least two Out of Scope items.

Verification: check output against `eval-criteria.md`, or run
`python3 eval_prd.py` with the output placed under `../create-prd-outputs/<case>/prd.md`.

## 3. Verified Trigger Test Cases

Each case runs in a FRESH session (prior conversation contaminates invocation
decisions). Pass = `create-prd-model-invoked` invokes with no slash command
AND the produced PRD passes EC 1–5.

| # | Test input | Expected | Invoked? | Output meets spec? | Result |
|---|------------|----------|----------|--------------------|--------|
| 1 | "I want to build a mobile app that reminds me to water my plants." | Skill fires; PRD produced | | | |
| 2 | "Let's add a dark mode toggle to the settings screen." | Skill fires; PRD produced | | | |
| 3 | "Help me spec out a feature that exports reports to CSV." | Skill fires; PRD produced | | | |

### Boundary cases (optional — defines the invocation boundary)

| # | Test input | Expected | Result |
|---|------------|----------|--------|
| B1 | "What do you think about adding social login?" (casual brainstorm, no request to build) | Should NOT fire | |
| B2 | "Design the UX for the pantry tracker feature." | Should NOT fire — UX request → create-ux | |
| B3 | "Update the PRD's success metrics." | Should NOT fire — existing PRD | |

## Log

After each test run, write `logs/TRIGGER-TEST-<n>/log.md` with:

- **Fired:** yes / no
- **When:** timestamp of the run
- **Input:** the exact user input that triggered (or failed to trigger) it
