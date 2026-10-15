# Skill-to-EC Mapping: review-implementation

This document maps each instruction in the review-implementation skill to the corresponding Evaluation Criteria (EC1-4).

---

## Evaluation Criteria (from evaluation-criteria.md)

```
EC1: The implementation must match the plan (plan.yaml) with no gaps or failures.
EC2: Every AC is confirmed to be completed.
EC3: If issue found, it must be documented to explain why it matters and the suggested improvement.
EC4: Severity level must be assigned to each issue.
```

---

## Skill Instructions → EC Mapping

### Input Contract (Lines 25-32)

**Instruction:** "Read all three inputs from the workspace root: stories.yaml, plan.yaml, code files"

**Maps to:** EC1, EC2
- **Why EC1:** To verify implementation matches the plan, you must read the plan.yaml
- **Why EC2:** To confirm every AC is completed, you must read stories.yaml and code files
- **Validation:** All three inputs are required before review can proceed

---

### Output Format - verdict (Lines 43)

**Instruction:** "verdict: 'passed' | 'failed' | 'changes_requested'"

**Maps to:** EC1, EC2
- **Why EC1:** Verdict reflects whether implementation matches plan with no gaps
- **Why EC2:** Verdict reflects whether all AC are satisfied
- **Rules:**
  - "passed" = implementation matches plan AND all AC satisfied
  - "failed" = implementation has gaps OR AC not satisfied
  - "changes_requested" = implementation mostly matches but needs refinement

---

### Output Format - issues (Lines 45-50)

**Instruction:** "For each issue found: severity, category, description, recommendation, ac_ref"

**Maps to:** EC3, EC4

#### Severity Assignment (Line 46)
**Maps to:** EC4
- **Instruction:** "severity: 'blocker' | 'major' | 'minor' | 'nit'"
- **EC4 Requirement:** "Severity level must be assigned to each issue"
- **Validation:** Every issue must have one of these four severity levels

#### Description & Recommendation (Lines 48-49)
**Maps to:** EC3
- **Instruction:** "description: What's wrong, recommendation: Specific fix"
- **EC3 Requirement:** "If issue found, it must be documented to explain why it matters and the suggested improvement"
- **Validation:** 
  - Description explains WHY the issue matters
  - Recommendation is specific and actionable (not vague)

#### AC Reference (Line 50)
**Maps to:** EC1, EC2
- **Instruction:** "ac_ref: Which AC is affected (or 'general')"
- **Why EC1:** Links issue to specific AC in the plan
- **Why EC2:** Tracks which AC are affected by issues
- **Validation:** ac_ref must match an AC ID from stories.yaml or be "general"

---

### Output Format - ac_assessment (Lines 52-55)

**Instruction:** "For each AC: ac_id, status, notes"

**Maps to:** EC2

#### AC Status (Line 54)
**Maps to:** EC2
- **Instruction:** "status: 'satisfied' | 'not_satisfied' | 'partially_satisfied'"
- **EC2 Requirement:** "Every AC is confirmed to be completed"
- **Validation:** 
  - Every AC from stories.yaml must appear in ac_assessment
  - Status reflects whether AC is implemented and working

#### AC Notes (Line 55)
**Maps to:** EC3
- **Instruction:** "notes: Why"
- **EC3 Requirement:** "explain why it matters"
- **Validation:** Notes explain the status (why AC is satisfied/not satisfied)

---

### Schema Rules (Lines 60-63)

**Instruction:** "story_id must match, every AC must appear, if passed then all AC satisfied"

**Maps to:** EC1, EC2
- **Rule 1:** "story_id must match a story in stories.yaml"
  - **EC1:** Ensures you're reviewing the correct implementation
- **Rule 2:** "Every AC in the source story must appear in ac_assessment"
  - **EC2:** Ensures all AC are evaluated
- **Rule 3:** "If verdict is 'passed', all ac_assessment entries must be 'satisfied'"
  - **EC1, EC2:** Ensures verdict is consistent with AC assessment

---

### Update stories.yaml (Lines 65-71)

**Instruction:** "After review, update stories.yaml with review_status and review_notes"

**Maps to:** EC1, EC2
- **Why EC1:** Feedback loop ensures plan is updated with review results
- **Why EC2:** Updates story with verdict on AC completion
- **Fields:**
  - `review_status` = verdict ("passed", "failed", "changes_requested")
  - `review_notes` = summary from review.yaml

---

### Context (Lines 17-19)

**Instruction:** "We review the implementation to ensure it meets the user story, AC, and implementation plan to prevent scope creep and gaps."

**Maps to:** EC1, EC2
- **EC1:** Prevents gaps between plan and implementation
- **EC2:** Ensures all AC are met

---

### Constraints (Lines 21-23)

**Instruction:** "For each issue, explain why it matters and suggest a specific improvement including severity levels while mentioning the specific AC."

**Maps to:** EC3, EC4
- **EC3:** "explain why it matters and suggest improvement"
- **EC4:** "including severity levels"
- **Additional:** "mentioning the specific AC" = ac_ref field

---

## Summary: Instruction → EC Coverage

| Instruction | EC1 | EC2 | EC3 | EC4 |
|---|---|---|---|---|
| Read inputs | ✓ | ✓ | - | - |
| verdict field | ✓ | ✓ | - | - |
| issues.severity | - | - | - | ✓ |
| issues.description | - | - | ✓ | - |
| issues.recommendation | - | - | ✓ | - |
| issues.ac_ref | ✓ | ✓ | - | - |
| ac_assessment.status | - | ✓ | - | - |
| ac_assessment.notes | - | - | ✓ | - |
| Schema rules | ✓ | ✓ | - | - |
| Update stories.yaml | ✓ | ✓ | - | - |
| Context | ✓ | ✓ | - | - |
| Constraints | - | - | ✓ | ✓ |

---

## Validation Checklist

When implementing the review-implementation skill, verify:

### For EC1 (Implementation matches plan with no gaps)
- [ ] Skill reads plan.yaml and code files
- [ ] Skill identifies missing implementations
- [ ] Skill identifies incomplete implementations
- [ ] verdict reflects whether implementation matches plan
- [ ] ac_ref links issues to specific AC

### For EC2 (Every AC is confirmed completed)
- [ ] Skill reads stories.yaml and extracts all AC
- [ ] Skill assesses each AC (satisfied/not_satisfied/partially_satisfied)
- [ ] ac_assessment includes ALL AC from the story
- [ ] verdict reflects whether all AC are satisfied
- [ ] If verdict="passed", all AC must be "satisfied"

### For EC3 (Issues documented with explanation and improvement)
- [ ] Each issue has a description explaining WHY it matters
- [ ] Each issue has a specific, actionable recommendation
- [ ] ac_assessment.notes explain why AC is satisfied/not satisfied
- [ ] Recommendations are not vague (e.g., "fix the code" is bad)

### For EC4 (Severity assigned to each issue)
- [ ] Every issue has a severity level (blocker/major/minor/nit)
- [ ] Severity levels are appropriate to the issue
- [ ] BLOCKER issues are for critical failures (AC not met, code doesn't compile)
- [ ] MAJOR issues are for significant gaps (missing test coverage, edge cases)
- [ ] MINOR issues are for improvements (code could be cleaner)
- [ ] NIT issues are for style/readability

---

## Example: How Instructions Implement EC

**Scenario:** Code is missing a required feature for AC1

**Instruction Flow:**
1. Read plan.yaml → identifies task for AC1
2. Read code files → finds no implementation
3. Create issue with:
   - `severity: blocker` (EC4: critical failure)
   - `description: "AC1 requires feature X but code has no implementation"` (EC3: explains why)
   - `recommendation: "Implement feature X in file Y"` (EC3: specific improvement)
   - `ac_ref: AC1` (EC1, EC2: links to AC)
4. Set `ac_assessment[AC1].status: not_satisfied` (EC2: confirms AC not met)
5. Set `verdict: failed` (EC1, EC2: reflects gaps)
6. Update stories.yaml with `review_status: failed` (EC1, EC2: feedback loop)

**Result:** All 4 EC are satisfied by this single issue documentation.

---

## Notes

- **EC1 and EC2 are interconnected:** Implementation matches plan AND all AC are satisfied
- **EC3 and EC4 are about issue quality:** Every issue must be documented well AND have severity
- **All EC are validated through the review.yaml output:** The skill's output is the evidence of EC compliance
