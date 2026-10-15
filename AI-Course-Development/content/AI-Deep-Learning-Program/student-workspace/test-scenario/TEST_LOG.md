# Test Scenario: review-implementation Skill Validation

## Overview
This test scenario contains intentional failures in code, tests, and implementation to validate that the `review-implementation` skill correctly identifies gaps and issues against the evaluation criteria (EC1-4).

## Test Setup
- **Story:** PANTRY-001 (Add Pantry Item Manually)
- **Plan:** `plan.yaml` (4 tasks covering model, form, API, and list)
- **Code Files:** Intentionally incomplete/buggy implementations
- **Expected Outcome:** review.yaml with identified issues and severity levels

---

## Intentional Failures by AC

### PANTRY-001-AC1: Item is saved and appears in inventory
**Failure Type:** Missing implementation + missing test

**Code Issues:**
1. `PantryItem.ts` - No validation of required fields (accepts empty strings)
2. `AddItemForm.tsx` - No success confirmation shown to user
3. `pantryRoutes.ts` - No actual database persistence (just returns object)

**Test Issues:**
1. `AddItemForm.test.tsx` - No test for successful save with confirmation
2. `pantryRoutes.test.ts` - No test for POST endpoint actually saving item

**Expected Review Finding:**
- **Severity:** BLOCKER
- **Category:** ac_violation, correctness
- **Issue:** AC1 requires "item is saved and appears in inventory" but code has no database persistence and no success confirmation
- **Recommendation:** Implement database save in POST endpoint, add success toast/modal in form, add test that verifies item appears in list after save

---

### PANTRY-001-AC2: Item grouped by category, count increases
**Failure Type:** Missing implementation

**Code Issues:**
1. `InventoryList.tsx` - Items rendered as flat list, not grouped by category
2. `pantryRoutes.ts` - GET endpoint returns empty array (not implemented)

**Test Issues:**
1. `InventoryList.test.tsx` - No test for category grouping
2. `pantryRoutes.test.ts` - No test for GET endpoint returning grouped items

**Expected Review Finding:**
- **Severity:** MAJOR
- **Category:** ac_violation
- **Issue:** AC2 requires items to be "grouped by category" but InventoryList renders flat list
- **Recommendation:** Implement category grouping in InventoryList (use reduce or groupBy), add test that verifies items are grouped and count is correct

---

### PANTRY-001-AC3: Validation message when required field empty
**Failure Type:** Missing implementation + missing test

**Code Issues:**
1. `AddItemForm.tsx` - No validation logic before submit
2. `AddItemForm.tsx` - No error message display

**Test Issues:**
1. `AddItemForm.test.tsx` - No test for validation error when name is empty
2. `AddItemForm.test.tsx` - No test for validation error when category is empty

**Expected Review Finding:**
- **Severity:** MAJOR
- **Category:** ac_violation, test_coverage
- **Issue:** AC3 requires validation message when required field is empty, but form submits without validation
- **Recommendation:** Add validation logic in handleSubmit, display error message, add tests for empty name and empty category scenarios

---

### PANTRY-001-AC4: Duplicate detection (same name updates quantity)
**Failure Type:** Missing implementation + missing test

**Code Issues:**
1. `pantryRoutes.ts` - No duplicate detection logic in POST endpoint
2. `PantryItemModel.ts` - No method to check for existing items

**Test Issues:**
1. `pantryRoutes.test.ts` - No test for duplicate detection
2. No test verifying that adding duplicate item updates quantity instead of creating new item

**Expected Review Finding:**
- **Severity:** MAJOR
- **Category:** ac_violation, edge_case
- **Issue:** AC4 requires duplicate detection (case-insensitive name match) but POST endpoint has no logic to check for existing items
- **Recommendation:** Query database for existing item with same name (case-insensitive), update quantity if found, create new item if not found, add test for both paths

---

## Test Coverage Issues (EC3)

**Current Test Count:** 4 tests across all files
**Required:** ≥ 2 tests per task = 8 tests minimum

**Missing Tests:**
- AC1: No test for successful save with confirmation
- AC2: No test for category grouping
- AC3: No test for validation errors (empty name, empty category)
- AC4: No test for duplicate detection (update vs create)

**Expected Review Finding:**
- **Severity:** MAJOR
- **Category:** test_coverage
- **Issue:** Only 4 tests exist but 4 tasks require ≥8 tests (2 per task). Missing tests for all 4 AC.
- **Recommendation:** Add minimum 4 more tests covering positive and negative cases for each AC

---

## Expected review.yaml Output

```yaml
review_id: REV-PANTRY-001-TEST-001
story_id: PANTRY-001
reviewed_at: "2026-10-15T00:00:00Z"

verdict: failed

issues:
  - severity: blocker
    category: ac_violation
    description: AC1 requires item to be saved and appear in inventory, but code has no database persistence
    recommendation: Implement database save in POST endpoint, add success confirmation in form, add test
    ac_ref: PANTRY-001-AC1

  - severity: major
    category: ac_violation
    description: AC2 requires items grouped by category, but InventoryList renders flat list
    recommendation: Implement category grouping in InventoryList component
    ac_ref: PANTRY-001-AC2

  - severity: major
    category: ac_violation
    description: AC3 requires validation message when required field empty, but form submits without validation
    recommendation: Add validation logic and error message display
    ac_ref: PANTRY-001-AC3

  - severity: major
    category: ac_violation
    description: AC4 requires duplicate detection but POST endpoint has no logic to check for existing items
    recommendation: Query database for existing item, update quantity if found
    ac_ref: PANTRY-001-AC4

  - severity: major
    category: test_coverage
    description: Only 4 tests exist but 4 tasks require minimum 8 tests (2 per task)
    recommendation: Add tests for all missing AC scenarios
    ac_ref: general

ac_assessment:
  - ac_id: PANTRY-001-AC1
    status: not_satisfied
    notes: Code has no database persistence and no success confirmation shown to user

  - ac_id: PANTRY-001-AC2
    status: not_satisfied
    notes: Items are rendered as flat list, not grouped by category

  - ac_id: PANTRY-001-AC3
    status: not_satisfied
    notes: No validation logic or error messages in form

  - ac_id: PANTRY-001-AC4
    status: not_satisfied
    notes: No duplicate detection logic in POST endpoint

summary: Implementation is incomplete. All 4 AC are not satisfied. Code lacks database persistence, validation, category grouping, and duplicate detection. Test coverage is insufficient (4 tests vs 8 required). Multiple blocker and major issues must be fixed before this story can pass.
```

---

## How to Use This Test Scenario

1. **Copy test files to workspace root** (or run review-implementation against this directory)
2. **Run review-implementation skill** against plan.yaml and code files
3. **Verify review.yaml output** matches expected findings above
4. **Check that:**
   - All 4 AC are listed in ac_assessment
   - All 4 are marked as "not_satisfied"
   - Severity levels are assigned (blocker, major)
   - Each issue has specific recommendation
   - Verdict is "failed"

---

## Validation Checklist for EC1-4

### EC1: Implementation must match plan with no gaps or failures
- ✅ Test validates that missing implementations are detected
- ✅ Test validates that incomplete code is flagged

### EC2: Every AC is confirmed to be completed
- ✅ Test validates that all 4 AC are assessed
- ✅ Test validates that unmet AC are marked "not_satisfied"

### EC3: Issues are documented with explanation and improvement
- ✅ Test validates that each issue has description and recommendation
- ✅ Test validates that issues explain why they matter

### EC4: Severity level assigned to each issue
- ✅ Test validates that severity (blocker, major, minor, nit) is assigned
- ✅ Test validates that blocker issues are caught (missing persistence)
- ✅ Test validates that major issues are caught (missing validation, grouping, duplicate detection)
