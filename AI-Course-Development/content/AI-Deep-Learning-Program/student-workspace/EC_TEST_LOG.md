# Evaluation Criteria Test Log: plan-story

**Plan Tested:** plan.yaml (PANTRY-005)
**Story:** PANTRY-005 (Filter and Search Inventory)
**Test Date:** 2026-10-15

---

## EC1: Plan references a real story

**Criterion:** `story_id` matches a story in `stories.yaml`. `source_story.title` and `source_story.user_story` match the selected story.

**Check:**
- story_id in plan: `PANTRY-005` ✓
- story_id exists in stories.yaml: YES ✓
- source_story.title: "Filter and Search Inventory" ✓
- Matches stories.yaml title: "Filter and Search Inventory" ✓
- source_story.user_story: "As a home cook, I want to search and filter my pantry so that I can quickly find specific items without scrolling through the entire list." ✓
- Matches stories.yaml user_story: YES ✓

**Result:** ✅ **PASS**

---

## EC2: Every AC is covered

**Criterion:** Every acceptance criterion in the selected story is referenced by at least one task's `acceptance_criteria_refs`.

**Story AC:**
- PANTRY-005-AC1 (search by text)
- PANTRY-005-AC2 (filter by category)
- PANTRY-005-AC3 (empty state with clear filters)

**Coverage Check:**
- PANTRY-005-AC1: Referenced in PANTRY-005-T1 ✓, PANTRY-005-T3 ✓, PANTRY-005-T4 ✓
- PANTRY-005-AC2: Referenced in PANTRY-005-T2 ✓, PANTRY-005-T3 ✓, PANTRY-005-T4 ✓
- PANTRY-005-AC3: Referenced in PANTRY-005-T3 ✓, PANTRY-005-T4 ✓, PANTRY-005-T5 ✓

**Result:** ✅ **PASS** - All 3 AC are covered by at least one task

---

## EC3: Tasks are in dependency order

**Criterion:** No task lists a dependency on a task that appears later in the `tasks` list. All `dependencies` values resolve to existing task IDs.

**Dependency Chain:**
```
PANTRY-005-T0 (no deps)
  ↓
PANTRY-005-T1 (depends on T0) ✓
PANTRY-005-T2 (depends on T0) ✓
  ↓
PANTRY-005-T3 (depends on T1, T2) ✓
  ↓
PANTRY-005-T4 (depends on T3) ✓
  ↓
PANTRY-005-T5 (depends on T4) ✓
```

**Check:**
- T0: No dependencies ✓
- T1: Depends on T0 (appears before T1) ✓
- T2: Depends on T0 (appears before T2) ✓
- T3: Depends on T1, T2 (both appear before T3) ✓
- T4: Depends on T3 (appears before T4) ✓
- T5: Depends on T4 (appears before T5) ✓
- All dependency IDs exist: T0, T1, T2, T3, T4, T5 ✓

**Result:** ✅ **PASS** - All dependencies are valid and in correct order

---

## EC4: Each task has AC coverage

**Criterion:** Every task has at least one non-empty `acceptance_criteria_refs` entry, and every referenced AC ID exists in the selected story.

**Task AC Coverage:**

| Task | AC Refs | Valid? |
|---|---|---|
| T0 | [] (empty) | ❌ NO |
| T1 | [PANTRY-005-AC1] | ✓ YES |
| T2 | [PANTRY-005-AC2] | ✓ YES |
| T3 | [PANTRY-005-AC1, PANTRY-005-AC2, PANTRY-005-AC3] | ✓ YES |
| T4 | [PANTRY-005-AC1, PANTRY-005-AC2, PANTRY-005-AC3] | ✓ YES |
| T5 | [PANTRY-005-AC3] | ✓ YES |

**Issues:**
- **PANTRY-005-T0** has empty `acceptance_criteria_refs` ❌
  - Task: "Create the Prisma schema file..."
  - This is a setup task but should still reference at least one AC it enables

**Result:** ❌ **FAIL** - T0 has no AC coverage

---

## EC5: Task granularity is appropriate

**Criterion:** Each task is small enough to complete in a single session (typically 1-2 hours) and describes a concrete, verb-first action.

**Task Granularity Check:**

| Task | Description | Verb | Granularity | Session? |
|---|---|---|---|---|
| T0 | Create the Prisma schema file... | Create | Schema + migration | ✓ 1-2 hrs |
| T1 | Implement a search query method... | Implement | Service method | ✓ 1-2 hrs |
| T2 | Implement a category filter query... | Implement | Service method | ✓ 1-2 hrs |
| T3 | Add a REST API endpoint... | Add | API endpoint | ✓ 1-2 hrs |
| T4 | Update the web client... | Update | Component + hook | ✓ 1-2 hrs |
| T5 | Add an EmptyState component... | Add | Component | ✓ 1-2 hrs |

**Result:** ✅ **PASS** - All tasks are verb-first, concrete, and completable in 1-2 hours

---

## EC6: Risks and unknowns are identified

**Criterion:** Every task lists at least one risk or unknown in `risks`.

**Risk Check:**

| Task | Risks | Count |
|---|---|---|
| T0 | Prisma must be installed; DATABASE_URL must be set | 2 ✓ |
| T1 | Database query performance; may need indexing | 1 ✓ |
| T2 | Category values must be validated | 1 ✓ |
| T3 | Query parameter validation and sanitization required | 1 ✓ |
| T4 | Network latency may require debouncing | 1 ✓ |
| T5 | Empty state must be visually distinct | 1 ✓ |

**Result:** ✅ **PASS** - All 6 tasks have at least one risk identified

---

## EC7: Files affected are tracked

**Criterion:** Every task lists at least one file in `files_affected`.

**Files Check:**

| Task | Files Affected | Count |
|---|---|---|
| T0 | api/prisma/schema.prisma, api/prisma/migrations/001_init.sql | 2 ✓ |
| T1 | api/src/types/pantry.ts, api/src/services/PantryService.ts, api/src/services/PantryService.test.ts | 3 ✓ |
| T2 | api/src/services/PantryService.ts, api/src/services/PantryService.test.ts | 2 ✓ |
| T3 | api/src/routes/pantry.ts, api/src/routes/pantry.test.ts | 2 ✓ |
| T4 | web/src/components/PantryInventory.tsx, web/src/hooks/usePantryFilter.ts, web/src/types/pantry.ts | 3 ✓ |
| T5 | web/src/components/EmptyState.tsx | 1 ✓ |

**Result:** ✅ **PASS** - All 6 tasks list at least one file affected

---

## EC8: Output follows the required schema

**Criterion:** `plan.yaml` contains `story_id`, `plan_version`, `source_story`, `tasks`, `assumptions`, and `open_questions`. Every task has `id`, `description`, `dependencies`, `files_affected`, `risks`, and `acceptance_criteria_refs`.

**Top-level Schema Check:**
- story_id: ✓ Present
- plan_version: ✓ Present (2.1.0)
- source_story: ✓ Present (with title and user_story)
- tasks: ✓ Present (6 tasks)
- assumptions: ✓ Present (4 assumptions)
- open_questions: ✓ Present (3 questions)

**Task Schema Check (all 6 tasks):**

| Field | T0 | T1 | T2 | T3 | T4 | T5 |
|---|---|---|---|---|---|---|
| id | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| description | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| dependencies | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| files_affected | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| risks | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| acceptance_criteria_refs | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

**Result:** ✅ **PASS** - Schema is complete and valid

---

## Summary

| EC | Result | Notes |
|---|---|---|
| EC1 | ✅ PASS | Story reference is correct |
| EC2 | ✅ PASS | All 3 AC covered by tasks |
| EC3 | ✅ PASS | Dependencies in correct order |
| EC4 | ❌ FAIL | T0 has empty acceptance_criteria_refs |
| EC5 | ✅ PASS | All tasks appropriately scoped |
| EC6 | ✅ PASS | All tasks have risks identified |
| EC7 | ✅ PASS | All tasks track files affected |
| EC8 | ✅ PASS | Schema is complete |

**Overall Result: 7/8 PASS (87.5%)**

---

## Issues Found

### Issue 1: EC4 Failure - T0 Missing AC Coverage

**Severity:** MAJOR

**Description:** Task PANTRY-005-T0 ("Create the Prisma schema file...") has an empty `acceptance_criteria_refs` list. EC4 requires every task to have at least one AC reference.

**Why It Matters:** This task is foundational (no other tasks can run without it), but it doesn't explicitly reference which AC it enables. This makes it unclear how this task contributes to the story's acceptance criteria.

**Recommendation:** Add `acceptance_criteria_refs` to T0. Since this task enables the search and filter functionality, it should reference at least one AC (likely AC1 or AC2, or both). Example:
```yaml
acceptance_criteria_refs:
  - PANTRY-005-AC1
  - PANTRY-005-AC2
```

---

## Test Conclusion

Your plan.yaml is **mostly well-formed** with 7 out of 8 EC passing. The only issue is that the foundational schema task (T0) lacks explicit AC coverage. This should be fixed before the plan is considered complete.

**Action:** Add AC references to PANTRY-005-T0 and re-test.
