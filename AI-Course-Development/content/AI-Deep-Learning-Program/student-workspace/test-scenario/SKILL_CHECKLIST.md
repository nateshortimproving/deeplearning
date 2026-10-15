# review-implementation Skill: What to Check

This checklist shows what your skill should verify when reviewing an implementation against a plan.

## Before You Start

- [ ] `stories.yaml` exists and contains the story being reviewed
- [ ] `plan.yaml` exists and references a valid story_id
- [ ] All files in `plan.yaml`'s `files_affected` exist
- [ ] Story has 2-4 AC (check stories.yaml)
- [ ] Plan has 2-4 tasks (check plan.yaml)

---

## For Each Task in plan.yaml

### 1. Code Exists and Compiles
- [ ] Every file in `files_affected` exists
- [ ] Code is not a stub (has real logic, not just `return null`)
- [ ] Code compiles without errors (TypeScript, imports, syntax)
- [ ] No missing imports or undefined references

### 2. Code Implements the Task
- [ ] Task description is addressed by the code
- [ ] Code is not generic placeholder code
- [ ] Code actually uses the declared tech stack (Fastify, React, Prisma, etc.)

---

## For Each AC in the Story

### 1. Code Implements the AC
- [ ] There is code that implements the behavior described in AC
- [ ] You can trace AC → function/component → code logic

### 2. Tests Exist and Pass
- [ ] At least one test file exists for this AC
- [ ] Test is not a stub (has real assertions, not just `expect(true).toBe(true)`)
- [ ] Test exercises the AC behavior
- [ ] Test passes (or would pass if code was correct)

### 3. Positive, Negative, and Edge Cases Covered
- [ ] AC of type `positive` has a passing test
- [ ] AC of type `negative` has a test that verifies error/rejection
- [ ] AC of type `edge_case` has a test for the edge case

---

## Issues to Flag

### BLOCKER Severity
- [ ] Code doesn't compile
- [ ] Code is a stub (no real logic)
- [ ] AC is completely unimplemented
- [ ] Database persistence missing (for data-related AC)
- [ ] Core functionality missing (e.g., form validation for validation AC)

### MAJOR Severity
- [ ] AC partially implemented (missing one part)
- [ ] Test is a stub (no real assertions)
- [ ] Test coverage insufficient (< 2 tests per task)
- [ ] Edge case not handled
- [ ] Error handling missing

### MINOR Severity
- [ ] Code could be cleaner
- [ ] Test could be more thorough
- [ ] Comment missing
- [ ] Type safety issue (loose typing)

### NIT Severity
- [ ] Style issue
- [ ] Naming could be clearer
- [ ] Test could be more readable

---

## For This Test Scenario

### Expected Findings

**BLOCKER Issues:**
1. AC1: No database persistence in POST endpoint
2. AC1: No success confirmation shown to user

**MAJOR Issues:**
1. AC2: Items not grouped by category in InventoryList
2. AC3: No validation logic in AddItemForm
3. AC3: No error message display
4. AC4: No duplicate detection in POST endpoint
5. Test Coverage: Only 4 tests, need 8 (2 per task)

**Total Issues:** 7
- 2 BLOCKER
- 5 MAJOR

---

## How to Document Each Issue

```yaml
- severity: blocker|major|minor|nit
  category: correctness|edge_case|readability|test_coverage|ac_violation
  description: "What's wrong (specific, not vague)"
  recommendation: "How to fix it (actionable, specific)"
  ac_ref: "PANTRY-001-AC1 or 'general'"
```

### Good vs Bad Examples

❌ **Bad:**
```yaml
- severity: major
  description: "Code is incomplete"
  recommendation: "Fix the code"
```

✅ **Good:**
```yaml
- severity: major
  category: ac_violation
  description: "AC2 requires items grouped by category, but InventoryList renders flat list without grouping"
  recommendation: "Use reduce() or groupBy() to group items by category before rendering, add test that verifies grouped structure"
  ac_ref: PANTRY-001-AC2
```

---

## AC Assessment Format

For each AC in the story:

```yaml
ac_assessment:
  - ac_id: PANTRY-001-AC1
    status: satisfied|not_satisfied|partially_satisfied
    notes: "Why (reference code/test if possible)"
```

### Status Meanings

- **satisfied:** Code implements AC, test passes, all parts work
- **not_satisfied:** AC is missing or broken
- **partially_satisfied:** Some parts work, some don't (rare - usually just not_satisfied)

---

## Verdict Rules

- **passed:** All AC are satisfied, no issues
- **failed:** One or more AC not satisfied, or blocker issues exist
- **changes_requested:** All AC satisfied but major/minor issues exist

---

## Test This Skill

1. Run against `test-scenario/` files
2. Verify you find all 7 issues
3. Verify severity levels are correct
4. Verify all 4 AC are in ac_assessment
5. Verify verdict is "failed"
6. Verify summary explains the failures
