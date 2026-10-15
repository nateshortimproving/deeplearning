# Test Scenario for review-implementation Skill

## What You Have

This directory contains a **complete test scenario** to validate your `review-implementation` skill against your evaluation criteria (EC1-4).

### Files

```
test-scenario/
├── plan.yaml                          # Implementation plan for PANTRY-001
├── src/
│   ├── models/PantryItem.ts          # Model with missing validation
│   ├── components/
│   │   ├── AddItemForm.tsx           # Form with missing validation & confirmation
│   │   ├── AddItemForm.test.tsx      # Incomplete tests
│   │   ├── InventoryList.tsx         # Missing category grouping
│   │   └── InventoryList.test.tsx    # Incomplete tests
│   └── api/routes/
│       ├── pantryRoutes.ts           # API with missing persistence & duplicate detection
│       └── pantryRoutes.test.ts      # Stub tests
├── TEST_LOG.md                        # Detailed breakdown of all failures
└── README.md                          # This file
```

### What's Intentionally Broken

**By Acceptance Criteria:**

| AC | Issue | Severity |
|---|---|---|
| AC1 | No database persistence, no success confirmation | BLOCKER |
| AC2 | Items not grouped by category | MAJOR |
| AC3 | No validation, no error messages | MAJOR |
| AC4 | No duplicate detection logic | MAJOR |

**By Test Coverage:**
- Only 4 tests exist (4 are stubs/incomplete)
- Required: ≥8 tests (2 per task)
- Missing: Tests for all 4 AC scenarios

---

## How to Use This

### Option 1: Manual Review (Recommended for Testing)

1. **Read the code files** in `src/` directory
2. **Read the plan** in `plan.yaml`
3. **Run your review-implementation skill** (manually or as a script)
4. **Check the output** against `TEST_LOG.md`

### Option 2: Automated Test

If you build a test harness:

```bash
# Copy test scenario to workspace
cp -r test-scenario/* /path/to/workspace/

# Run review-implementation skill
# (your skill invocation here)

# Compare output
diff review.yaml test-scenario/EXPECTED_review.yaml
```

---

## Expected Output

Your `review-implementation` skill should produce a `review.yaml` with:

✅ **Verdict:** `failed`

✅ **Issues:** 5 total
- 1 BLOCKER (AC1 - no persistence)
- 4 MAJOR (AC2, AC3, AC4, test_coverage)

✅ **AC Assessment:** All 4 AC marked as `not_satisfied`

✅ **Summary:** Explains why implementation fails and what needs to be fixed

---

## Validating Your EC1-4

| EC | How This Test Validates It |
|---|---|
| **EC1** | Implementation has gaps (missing persistence, validation, grouping, duplicate detection) - skill should detect all of them |
| **EC2** | All 4 AC are assessed and marked not_satisfied |
| **EC3** | Each issue has description explaining why it matters + specific recommendation |
| **EC4** | Severity levels assigned (blocker for persistence, major for others) |

---

## Next Steps

1. **Run your review-implementation skill** against this test scenario
2. **Compare output** to TEST_LOG.md expected findings
3. **If output matches:** Your EC1-4 are correct and skill works
4. **If output differs:** Refine your EC or skill logic
5. **Iterate** until skill consistently finds all failures

---

## Files to Keep

- `plan.yaml` - Use as template for real plan files
- `TEST_LOG.md` - Reference for what a good review looks like
- Code files - Examples of incomplete implementations

## Files to Replace

When testing against real sprint outputs, replace:
- `src/` directory with actual implementation
- `plan.yaml` with actual plan from sprint
