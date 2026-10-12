# Session 4 — Hypothetical Student Evaluations
## Evaluation-Driven Development (EDD)
*Week 7 | Deep Learning Program*

---

## Overview

This document presents hypothetical evaluation scenarios and student submissions from Session 4. These examples reflect real command assessment cases from Sessions 1–3, now formalized through documented evaluation cycles.

Students submitting for Session 4 evaluation would present:
1. **Written evaluation criteria** for a command they've been using (Acceptance Criteria, Unit Tests, or Test Plans)
2. **Baseline evaluation results** documented and committed
3. **One complete iteration cycle** with hypothesis, change, measured results, and refactor step applied
4. **Documented evidence** of improvement with reflection on what the measurement revealed

These examples show what that looks like across the three primary command types.

---

## Deterministic Examples
### Concrete, Directly Verifiable Criteria

Deterministic evaluation criteria check for the presence, absence, or structure of specific elements in the command output. These are evaluated by direct inspection or simple pattern matching.

---

### Example 1: Acceptance Criteria Command Evaluation

**Student: Alex (Product/Process Role)**

**Command Purpose:** Generate Acceptance Criteria from a user story using RTCC structure

**Test Case:** User story about filtering transactions by date range

**Evaluation Criteria Written in Session 1 (Before Building):**
1. Every Acceptance Criterion is written in Given/When/Then format (or equivalent structured behavior statement)
2. The output does not contain implementation details (no references to HTML, database, API calls, or technical specifics)
3. At least one criterion covers a failure case or edge case
4. There are between 3–8 criteria per story (not too few to be useful, not too many to be noisy)

**Baseline Evaluation (Week 7, Session 4):**

Generated Output:
```
Given a logged-in customer viewing the transaction list
When the customer enters a start date and end date in the filter controls
Then the system displays only transactions within that date range
And the list is sorted by transaction date in descending order
And the system displays "No transactions found" if no matches exist
```

Evaluation Against Criteria:
```
Criterion 1 — Given/When/Then format: ✓ PASS
  All criteria follow Given/When/Then structure

Criterion 2 — No implementation details: ✓ PASS
  No references to HTML, database, API, or technical mechanisms

Criterion 3 — Covers edge/failure case: ✗ FAIL
  The "No transactions found" criterion is present, but no boundary condition
  (e.g., start date > end date, date in future, or single-day range) is covered

Criterion 4 — Criteria count (3-8): ✓ PASS
  Output contains 5 criteria

Overall Score: 3/4 criteria passing (75%)
Most critical gap: Missing edge case coverage (boundary conditions)
```

**Improvement Hypothesis:**
"The edge case criterion is failing because the command doesn't explicitly ask for edge case categories. If I add specific examples of edge cases that matter for date-filtering (invalid date ranges, date in future, same start/end date), the output will include them."

**Change Made:**
```
OLD: Constraints: Do not include implementation details. Start each criterion 
with Given/When/Then. Generate 3–8 criteria per story.

NEW: Constraints: Do not include implementation details. Start each criterion 
with Given/When/Then. Generate 3–8 criteria per story, including at least one 
that covers a boundary condition or failure case specific to date filtering:
  - Start date after end date (invalid range)
  - Date range spanning a single day
  - Date in the future (after today)
  - Date range spanning more than 1 year
  - Empty or null date entry
```

**Result (Re-evaluation with same story input):**

Generated Output (after change):
```
Given a logged-in customer viewing the transaction list
When the customer enters a start date and end date in the filter controls
Then the system displays only transactions within that date range
And the list is sorted by transaction date in descending order
And the system displays "No transactions found" if no matches exist
And the system displays an error if the start date is after the end date
And the system shows all matching transactions if the date range spans more than 1 year
```

Evaluation Against Criteria:
```
Criterion 1 — Given/When/Then format: ✓ PASS
  All criteria follow Given/When/Then structure

Criterion 2 — No implementation details: ✓ PASS
  No references to HTML, database, API, or technical mechanisms

Criterion 3 — Covers edge/failure case: ✓ PASS
  Two criteria now explicitly cover edge cases:
  - Invalid date range (start > end)
  - Large date ranges (1+ year)

Criterion 4 — Criteria count (3-8): ✓ PASS
  Output contains 7 criteria

Overall Score: 4/4 criteria passing (100%)
No regressions: All previously passing criteria still pass
Hypothesis confirmed: Explicit edge case categories produced the intended output
```

**Refactor Step Applied:**
Review each instruction in the command to ensure every one corresponds to at least one evaluation criterion.

Instructions Audited:
- "Use professional language" → No criterion tests this; **removed**
- "Be concise" → Not explicitly tied to a criterion; **removed**
- "Follow Given/When/Then format" → Criterion 1 tests this; **keep**
- "Avoid implementation details" → Criterion 2 tests this; **keep**
- "Include edge case categories: [list]" → Criterion 3 tests this; **keep**
- "Generate 3–8 criteria" → Criterion 4 tests this; **keep**

After removal of dead instructions and re-evaluation: Still 4/4 criteria passing. Command is leaner and every instruction serves a measurement purpose.

---

### Example 2: Unit Test Generation Command Evaluation

**Student: Jordan (Development Role)**

**Command Purpose:** Generate unit tests from story + Acceptance Criteria

**Test Case:** Password validation requirements

**Story + Acceptance Criteria Input:**
```
Story: As a user, I want my password to be validated during signup so that 
my account is secure.

Acceptance Criteria:
  Given a new account signup flow
  When the user enters a password
  Then the system accepts passwords of 8+ characters
  And rejects passwords without uppercase letters
  And rejects passwords without numbers
  And rejects passwords without special characters
  And provides clear error messages for each failure
```

**Evaluation Criteria Written in Session 2 (Before Building):**
1. Each generated test maps to exactly one Acceptance Criterion
2. Tests use valid syntax for the project's test framework (Java/JUnit in this case)
3. Tests do not reference database, API, or other external dependencies that the command shouldn't touch
4. Tests include both positive assertions (what should pass) and negative assertions (what should fail)
5. Test code includes clear assertions using framework-standard methods (assertEquals, assertTrue, etc.)

**Baseline Evaluation (Week 7, Session 4):**

Generated Output (excerpt):
```java
@Test
public void testPasswordMinimumLength() {
  assertTrue(validator.isValid("Password1!"));
  assertFalse(validator.isValid("Pass1!"));
}

@Test
public void testPasswordUppercaseRequired() {
  assertTrue(validator.isValid("Password1!"));
  assertFalse(validator.isValid("password1!"));
}

@Test
public void testApprovalFlow() {
  var request = new SignupRequest("user@example.com", "Password1!");
  var result = database.saveUser(request);  // ISSUE
  assertEquals("APPROVED", result.status);
}
```

Evaluation Against Criteria:
```
Criterion 1 — Maps to AC: ✓ PASS
  Each test corresponds to one Acceptance Criterion (length, uppercase, etc.)

Criterion 2 — Valid JUnit syntax: ✓ PASS
  Tests use proper @Test annotations and method signatures

Criterion 3 — No DB/API references: ✗ FAIL
  The testApprovalFlow test calls database.saveUser() which violates the 
  constraint of unit testing in isolation. Unit tests should mock external 
  dependencies, not call them directly.

Criterion 4 — Positive and negative assertions: ✓ PASS
  Tests include both assertTrue (positive) and assertFalse (negative) cases

Criterion 5 — Framework assertions: ✓ PASS
  Tests use assertEquals, assertTrue, assertFalse correctly

Overall Score: 4/5 criteria passing (80%)
Most critical gap: Database calls in unit test scope (should be mocked)
```

**Improvement Hypothesis:**
"The DB/API criterion is failing because the command doesn't explicitly restrict external calls. If I add a constraint stating 'Do not call actual databases, APIs, or external services; mock them instead,' the output will avoid this anti-pattern."

**Change Made:**
```
OLD: Constraints: Generate unit tests that verify behavior, not implementation. 
Use @Test annotations. Each test should verify one Acceptance Criterion.

NEW: Constraints: Generate unit tests that verify behavior, not implementation. 
Use @Test annotations. Each test should verify one Acceptance Criterion.
CRITICAL: Unit tests must not call actual databases, APIs, or external services.
If a test requires database interaction, use Mockito or equivalent mocking 
framework. Example: @Mock DatabaseService dbService; instead of 
databaseService.saveUser(...). Do not import or instantiate real database 
classes in unit tests.
```

**Result (Re-evaluation with same input):**

Generated Output (after change):
```java
@Test
public void testPasswordMinimumLength() {
  assertTrue(validator.isValid("Password1!"));
  assertFalse(validator.isValid("Pass1!"));
}

@Test
public void testPasswordUppercaseRequired() {
  assertTrue(validator.isValid("Password1!"));
  assertFalse(validator.isValid("password1!"));
}

@Test
public void testApprovalFlow() {
  var mockDatabase = mock(DatabaseService.class);
  var validator = new PasswordValidator(mockDatabase);
  
  when(mockDatabase.isAccountActive(anyString())).thenReturn(true);
  assertTrue(validator.isValid("Password1!"));
  
  verify(mockDatabase).isAccountActive(anyString());
}
```

Evaluation Against Criteria:
```
Criterion 1 — Maps to AC: ✓ PASS
  Each test still maps to one Acceptance Criterion

Criterion 2 — Valid JUnit syntax: ✓ PASS
  Tests still use proper @Test annotations

Criterion 3 — No DB/API references: ✓ PASS
  Database is now mocked using Mockito; no actual database calls

Criterion 4 — Positive and negative assertions: ✓ PASS
  Tests include both when() mock expectations and assertions

Criterion 5 — Framework assertions: ✓ PASS
  Tests use assertTrue, verify() correctly

Overall Score: 5/5 criteria passing (100%)
No regressions: All previously passing criteria still pass
Hypothesis confirmed: Explicit mocking constraint produced isolated unit tests
```

---

## Rubric Examples
### Subjective Assessment of Quality Dimensions

Subjective evaluation criteria require judgment about quality aspects that can't be verified by simple pattern matching. These might be assessed by a human reviewer or evaluated through a secondary evaluation process. The criteria must be specific and derived from the evaluation standards written before command construction.

---

### Example 3: Acceptance Criteria Quality Assessment

**Student: Casey (Product/Process Role)**

**Command:** Acceptance Criteria generation from user stories

**Test Case:** Bank account transfer story

**Evaluation Criteria Written in Session 1 (Before Building):**
1. Every Acceptance Criterion describes a testable system behavior (observable outcome, not implementation mechanism)
2. Each Acceptance Criterion is independent — you could test it without needing another criterion to pass first
3. The criteria collectively cover happy path, failure cases, and at least one edge case
4. The criteria are written clearly enough that a developer could generate automated tests from them without needing clarification
5. No criterion is ambiguous — it contains specific values, formats, or error messages (not vague language like "reasonable amount")

**Story Input:**
```
As a bank customer, I want to transfer money between my own accounts 
so that I can manage my funds across accounts without fees.
```

**Baseline Evaluation (Week 7, Session 4):**

Generated Output:
```
Acceptance Criteria:

Given a logged-in customer with two or more accounts
When the customer initiates a transfer between their accounts
Then the system accepts the transfer
And the system processes the transfer without charging fees
And the customer receives confirmation

Given the customer enters an amount exceeding the source account balance
Then the system displays an appropriate error
And the transfer does not process

Given the customer enters a reasonable daily transfer limit
Then the system enforces the daily limit
And displays a helpful message about limits
```

Evaluator Assessment Against Criteria:
```
Criterion 1 — Testable system behavior: PARTIAL PASS
  • "Accept the transfer" is observable ✓
  • "Processes without charging fees" is testable ✓
  • "Customer receives confirmation" is observable ✓
  • But: "Initiates a transfer" describes the user action (testable) while 
    "processes" is somewhat implementation-focused. Could be clearer.

Criterion 2 — Independence of criteria: PASS
  Each criterion could be tested in isolation. No dependencies.

Criterion 3 — Coverage (happy + failure + edge): PARTIAL PASS
  • Happy path: transfers between accounts, no fees ✓
  • Failure case: insufficient funds ✓
  • Edge case: MISSING - no criteria for boundary conditions
    (e.g., transferring $0, transferring entire balance, daily limit edge)

Criterion 4 — Developer usability: PARTIAL PASS
  • Most criteria are clear enough to write tests from
  • Issue: "Appropriate error" is vague — what text should the error contain?
  • Issue: "Reasonable daily transfer limit" doesn't specify the amount
  • A developer would need to ask: "What's the actual daily limit value?"

Criterion 5 — Specificity: FAIL
  • "Reasonable daily limit" should be specific (e.g., "$50,000 daily limit")
  • "Appropriate error" should specify exact text or pattern
  • "Helpful message" is vague — what constitutes helpful?
  • Only 1 of 3 criteria contain specific values

Overall Score: 3/5 criteria passing; 2 partial
Most critical gaps: Missing edge case coverage, vague language, missing specific amounts
```

**Improvement Hypothesis:**
"The Coverage and Specificity criteria are failing because the command doesn't explicitly ask for edge cases or specific values. If I add instructions requesting edge case types and explicit amounts, both dimensions should improve."

**Change Made:**
```
OLD: Generate between 4–8 Acceptance Criteria using Given/When/Then format.
Cover the main workflow and error cases.

NEW: Generate 4–8 Acceptance Criteria using Given/When/Then format with:
- 1–2 criteria for happy path (normal successful transfers)
- 2–3 criteria for failure cases (insufficient funds, locked account, limit exceeded)
- 1–2 criteria for edge cases (zero amount transfer, transfer entire balance, 
  transfer on same account, daily limit boundary)

For all amounts or limits, use specific values: "$50,000 daily limit" not 
"reasonable limit". For error conditions, specify the exact error message 
text, not "appropriate error". For user communication, specify the exact 
text or behavior expected.
```

**Result (Re-evaluation with same story input):**

Generated Output (after change):
```
Acceptance Criteria:

Given a logged-in customer with two or more accounts
When the customer initiates a transfer of $1,500 between their accounts
Then the system accepts the transfer
And the system processes the transfer without charging fees
And the customer receives confirmation message: "Transfer of $X from [Account] 
to [Account] completed successfully"

Given the customer's source account has a balance less than the requested transfer amount
When the customer attempts to transfer
Then the system displays error: "Insufficient funds. Available balance: $X"
And the transfer does not process

Given the customer has already transferred $45,000 in a calendar day
When the customer attempts to transfer $10,000
Then the system displays error: "Daily transfer limit is $50,000. You have 
$5,000 remaining today"
And the transfer does not process

Given the customer enters $0 as the transfer amount
When the customer attempts to transfer
Then the system displays error: "Transfer amount must be greater than $0"
And rejects the transfer

Given the customer attempts to transfer to their own account
When the customer confirms the transfer
Then the system displays warning: "Transferring to the same account. Proceed?" 
And allows the user to confirm or cancel
```

Evaluator Assessment Against Criteria:
```
Criterion 1 — Testable system behavior: PASS
  All criteria describe observable outcomes, not internal mechanisms

Criterion 2 — Independence: PASS
  Each criterion tests a distinct behavior; no dependencies

Criterion 3 — Coverage (happy + failure + edge): PASS
  • Happy path: successful transfer with fee structure ✓
  • Failure cases: insufficient funds, daily limit exceeded ✓
  • Edge cases: $0 transfer, same-account transfer ✓

Criterion 4 — Developer usability: PASS
  Developer can write tests directly from these criteria with no clarification needed.
  Specific messages are provided; amounts are specified.

Criterion 5 — Specificity: PASS
  • Daily limit is "$50,000" (specific)
  • Error messages include exact text
  • All amounts and thresholds are numeric and precise

Overall Score: 5/5 criteria passing
No regressions: All previously passing criteria still pass
Hypothesis confirmed: Explicit edge case categories and specific values improved 
the output quality across all dimensions
```

**Refactor Step Applied:**
Removed instructions that don't correspond to an evaluation criterion:
- "Write clear, professional language" → No criterion tests this; removed
- "Be concise" → Not tied to any criterion; removed

After refactor and re-evaluation: Still 5/5 criteria passing.

---

### Example 4: Test Generation Quality Assessment

**Student: Morgan (Development Role)**

**Command:** Unit test generation from story + Acceptance Criteria

**Evaluation Criteria from Session 2:**
1. Each test maps to exactly one Acceptance Criterion (every AC has a test, no test orphaned)
2. Tests cover failure cases and edge cases, not just happy path (diverse coverage)
3. Tests verify observable behavior, not implementation details (correct scope)
4. Tests would compile and run in the project's framework without modifications (valid syntax)
5. Tests are deterministic — same inputs always produce same results (no randomness, no timing dependencies)

**Acceptance Criteria Input:**
```
AC1: Given a logged-in user entering a search term in the search box
     When the search completes
     Then the system returns matching transactions within 2 seconds

AC2: Given a logged-in user searching for a term with no matches
     When the search completes
     Then the system displays "No transactions found"

AC3: Given a logged-in user entering special characters (like @, #, $) in the search
     When the search processes
     Then the system escapes the characters and searches by literal text
```

**Baseline Evaluation (Week 7, Session 4):**

Generated Output (excerpt):
```java
@Test
public void testSuccessfulSearch() {
  List<Transaction> results = searchService.search("coffee");
  assertTrue(results.size() > 0);
  // No assertion on timing
}

@Test
public void testNoResultsFound() {
  List<Transaction> results = searchService.search("xyznonexistent");
  assertEquals("No transactions found", getDisplayMessage());
}

@Test
public void testSpecialCharacterHandling() {
  List<Transaction> results = searchService.search("@#$");
  assertFalse(results.stream()
    .anyMatch(t -> t.getRawQueryUsed().contains("@")));
}

@Test
public void testSearchDatabaseCall() {
  verify(mockDatabase).queryByTerm(anyString());
  // Testing implementation detail: the database call itself
}
```

Evaluator Assessment Against Criteria:
```
Criterion 1 — AC-to-Test Mapping: PASS
  AC1 → testSuccessfulSearch ✓
  AC2 → testNoResultsFound ✓
  AC3 → testSpecialCharacterHandling ✓

Criterion 2 — Coverage diversity: PARTIAL PASS
  • Happy path (successful search): ✓
  • Failure case (no results): ✓
  • Edge case: MISSING
    Boundary cases not covered: empty search term, single-character search, 
    very long search term, numeric-only search

Criterion 3 — Behavior vs implementation: PARTIAL PASS
  • Most tests verify observable results
  • ISSUE: testSearchDatabaseCall verifies the database was called, which is 
    an implementation detail, not user-observable behavior

Criterion 4 — Framework validity: PASS
  All tests use valid JUnit 4 syntax (@Test, assertEquals, assertTrue)

Criterion 5 — Determinism: PASS
  No sleep() calls, no random values, no time-dependent assertions

Overall Score: 3.5/5 criteria passing
Most critical gaps: Missing edge case coverage, one implementation-detail test
```

**Improvement Hypothesis:**
"The coverage criterion is weak because the command doesn't specify what edge cases are important. If I add specific edge case categories (empty search, single character, very long string), output will improve. The implementation-detail test suggests the command allows testing internal mechanics when it shouldn't."

**Change Made:**
```
OLD: Generate unit tests that verify the search behavior. Test successful 
searches, empty results, and special character handling.

NEW: Generate unit tests that verify observable search behavior. Each test 
should verify what the user sees/gets, not internal implementation.

Test Coverage Requirements:
- 1 test for happy path (normal successful search)
- 1 test for each Acceptance Criterion
- At least 3 edge case tests:
  • Empty or whitespace-only search term
  • Single-character search term
  • Very long search term (100+ characters)
  • Numeric-only search term

Critical Constraint: Tests must NOT verify internal implementation (database 
calls, method invocations, cache hits). Tests MUST verify observable output 
(returned data, displayed messages, computed results). If a test requires 
database interaction, mock it; never verify that the mock was called.
```

**Result (Re-evaluation with same criteria input):**

Generated Output (after change):
```java
@Test
public void testSuccessfulSearch() {
  List<Transaction> results = searchService.search("coffee");
  assertFalse(results.isEmpty(), "Search should return results");
  assertTrue(results.stream()
    .allMatch(t -> t.getDescription().toLowerCase().contains("coffee")),
    "All results should match search term");
}

@Test
public void testNoResultsFound() {
  List<Transaction> results = searchService.search("xyznonexistent");
  assertEquals("No transactions found", getDisplayMessage());
}

@Test
public void testSpecialCharacterHandling() {
  List<Transaction> results = searchService.search("@#$");
  assertFalse(results.stream()
    .anyMatch(t -> t.getRawQueryUsed().contains("@")));
}

@Test
public void testEmptySearchTerm() {
  List<Transaction> results = searchService.search("");
  assertEquals("Search term cannot be empty", getDisplayMessage());
}

@Test
public void testSingleCharacterSearch() {
  List<Transaction> results = searchService.search("a");
  // Returns results or "too broad" message, both valid
  assertNotNull(results);
}

@Test
public void testVeryLongSearchTerm() {
  String longTerm = "a".repeat(101);
  List<Transaction> results = searchService.search(longTerm);
  // Should either search or return message about term length
  assertNotNull(results);
}

@Test
public void testNumericOnlySearch() {
  List<Transaction> results = searchService.search("12345");
  // Numeric searches are valid (transaction IDs, amounts)
  assertNotNull(results);
}
```

Evaluator Assessment Against Criteria:
```
Criterion 1 — AC-to-Test Mapping: PASS
  All ACs have corresponding tests; no orphaned tests

Criterion 2 — Coverage diversity: PASS
  • Happy path ✓
  • Failure case (no results) ✓
  • Edge cases: empty search, single char, long term, numeric ✓

Criterion 3 — Behavior vs implementation: PASS
  All tests verify observable output (returned data, messages)
  No tests verify internal database calls or implementation details

Criterion 4 — Framework validity: PASS
  Valid JUnit 4 syntax throughout

Criterion 5 — Determinism: PASS
  No timing dependencies, no randomness

Overall Score: 5/5 criteria passing
Hypothesis confirmed: Explicit edge case categories and "behavior not 
implementation" constraint fixed both weak dimensions
```

---

### Example 5: Test Plan Quality Assessment

**Student: Taylor (Testing Role)**

**Command:** Test plan generation from story + Acceptance Criteria + unit test output

**Evaluation Criteria from Session 3:**
1. Every Acceptance Criterion has at least one corresponding test scenario in the plan
2. At least one risk area is identified that unit tests don't cover (not duplicative of unit scope)
3. The plan does not duplicate what unit tests already cover (builds on, not redundant)
4. Coverage scope is clear — test types are identified (integration, end-to-end, regression, load, etc.)
5. Business-relevant risks are identified in addition to technical risks (not just technical scenarios)

**Story Input:**
```
As an admin, I want to bulk approve user accounts in pending status 
so I can onboard multiple users at once.

Acceptance Criteria:
  AC1: Given an admin with bulk-approval permission, viewing pending accounts
       When the admin selects multiple accounts and clicks "Approve Selected"
       Then the system processes all checked accounts as approved

  AC2: When accounts are approved
       Then the system sends confirmation emails to the approved users

  AC3: When accounts are approved
       Then the system logs the approval action with timestamp and admin ID

Unit Tests Already Exist For:
  - Bulk selection (checkbox selection logic)
  - Approve button triggers processing
  - Confirmation email is generated (email service mocked)
  - Approval is logged to database
```

**Baseline Evaluation (Week 7, Session 4):**

Generated Test Plan:
```
Test Plan: Bulk Account Approval

Coverage:
- Integration: Test that email service receives confirmation requests
- Integration: Test that audit log records approval with correct timestamp
- End-to-end: Test full approval workflow from UI through email delivery

Identified Risks:
- Concurrency: Two admins approving same accounts simultaneously
- Email delivery: External email service failures or delays
- Database consistency: Partial failures (some accounts approved, others fail)

Notes:
- Unit tests cover basic selection and button behavior
- Integration tests verify email and logging subsystems
- Load tests should verify behavior with 1,000+ bulk approvals
```

Evaluator Assessment Against Criteria:
```
Criterion 1 — AC coverage in plan: PASS
  AC1 (processing) → End-to-end workflow test ✓
  AC2 (email) → Integration email test ✓
  AC3 (logging) → Integration audit test ✓

Criterion 2 — Non-unit risks identified: PASS
  • Concurrency risk (unit tests can't cover)
  • Email delivery reliability (beyond unit scope)
  • Database consistency (beyond unit scope)

Criterion 3 — No duplication: PARTIAL PASS
  Integration tests for email and logging are mentioned, but the plan could 
  be clearer about what the unit tests already cover. No explicit statement 
  of "we're not re-testing checkbox selection."

Criterion 4 — Coverage scope clarity: PARTIAL PASS
  • Integration tests mentioned but not clearly delineated
  • End-to-end mentioned but scope unclear
  • Load tests mentioned but no detail on what's being tested for load
  Issue: "Load tests should verify behavior with 1,000+ bulk approvals" is 
  vague. What behavior? Performance threshold? Error handling?

Criterion 5 — Business-relevant risks: FAIL
  Plan identifies only technical risks (concurrency, delivery, consistency)
  Missing business-relevant risks:
  - Audit compliance: Were approvals made by authorized admins?
  - Data integrity: Can an admin approve their own accounts? (compliance issue)
  - User communication: Are approved users notified they need to complete onboarding?
  - Error recovery: What happens if 500 accounts approve but 100 fail? 
    (business process question, not just technical)

Overall Score: 2.5/5 criteria passing
Most critical gaps: Load test scope undefined, business risks missing, 
deduplication with unit tests not explicit
```

**Improvement Hypothesis:**
"The scope clarity and business risk criteria are weak. The command asks for risks but doesn't distinguish technical from business-relevant, and doesn't give enough structure to define integration/load/end-to-end scope. If I add explicit risk categories and test type definitions, the output will be clearer and more complete."

**Change Made:**
```
OLD: Generate a test plan covering risks unit tests don't address. Identify 
concurrency, infrastructure, and performance concerns.

NEW: Generate a comprehensive test plan structured as follows:

PART 1 — Coverage Summary
For each Acceptance Criterion, identify which test type (unit/integration/e2e/load) 
covers it. Unit tests already cover: [list from input]. Do NOT duplicate these.

PART 2 — Test Types with Scope Definition
- Integration tests: Test interactions between subsystems (approval service + 
  email service, approval service + audit logging)
- End-to-end tests: Test complete user workflows from UI through persistence
- Load tests: Define the specific performance requirement being tested 
  (e.g., "1,000+ approvals in a batch process, with 95th percentile latency 
  under 5 seconds")
- Regression tests: Test that approval behavior doesn't break other account 
  management features

PART 3 — Risk Identification (BOTH technical AND business)
Technical Risks:
  - Concurrency (two admins approving same account simultaneously)
  - Infrastructure (email delivery failures, network timeouts)
  - Partial failures (500 accounts approved, 100 fail)

Business & Compliance Risks:
  - Authorization: Can admins approve their own accounts? (compliance requirement)
  - Audit trail: Is every approval logged with correct timestamp and admin ID?
  - User communication: Are approved users notified of approval + next steps?
  - Rollback: If bulk approval partially fails, how are partial results handled?
```

**Result (Re-evaluation with same input):**

Generated Test Plan (after change):
```
Test Plan: Bulk Account Approval

PART 1 — Coverage Summary
AC1 (Processing): Unit tests cover checkbox and button logic. 
                  Integration tests verify approval service processes all selected accounts
                  E2E tests verify UI → approval service → persistence
AC2 (Email):      Unit tests mock email generation. 
                  Integration tests verify email service receives and sends confirmations
AC3 (Logging):    Unit tests verify logging calls. 
                  Integration tests verify audit log persistence
                  E2E tests verify logs accessible through audit UI

PART 2 — Test Types & Scope
Integration Tests:
  - Approval service + Email service: Bulk request triggers 1+ emails per account
  - Approval service + Audit service: Bulk request creates 1 audit entry per approval
  - Performance requirement: 100 approvals processed in <2 seconds

End-to-End Tests:
  - Admin selects 50 accounts, clicks "Approve", receives success confirmation
  - Each approved user receives email within 5 minutes
  - Admin can view approval in audit log with timestamp and their ID

Load Tests:
  - Performance: Bulk approval of 1,000+ accounts completes with 95th percentile 
    latency under 5 seconds
  - Stability: No errors or partial failures during concurrent load

PART 3 — Risk Identification

Technical Risks:
  - Concurrency: Two admins approve same account → only one approval recorded
  - Email delivery: Email service unavailable → approval proceeds, user notified 
    of delivery delay
  - Partial failure: 500 approved, 100 fail → user sees which failed, can retry

Business & Compliance Risks:
  - Authorization: Admin cannot approve their own account (compliance requirement)
  - Audit trail: Every approval logged with timestamp, admin ID, account ID
  - User communication: Approved users notified of approval and required onboarding steps
  - Error recovery: If bulk action fails, admins can see which accounts succeeded 
    and retry failures
  - Data retention: Approval history retained per compliance policy (7 years)
```

Evaluator Assessment Against Criteria:
```
Criterion 1 — AC coverage in plan: PASS
  All ACs explicitly mapped to test types and scenarios

Criterion 2 — Non-unit risks identified: PASS
  Technical and business risks clearly separated
  Risks identified: concurrency, email reliability, partial failure, 
  authorization, audit, communication, retention

Criterion 3 — No duplication: PASS
  PART 1 explicitly states what unit tests cover and what integration/E2E builds on

Criterion 4 — Coverage scope clarity: PASS
  Each test type has explicit scope definition
  Load tests specify performance requirement (95th percentile <5 seconds)
  E2E tests specify user-observable behavior
  Integration tests specify system-interaction scope

Criterion 5 — Business-relevant risks: PASS
  Business risks identified:
  • Authorization/compliance (self-approval prevention)
  • Audit compliance (retention, complete logging)
  • User communication (onboarding requirement)
  • Error recovery (partial failure handling)

Overall Score: 5/5 criteria passing
Hypothesis confirmed: Explicit test type definitions and business risk 
categories improved clarity and completeness
```

---

## Complete Improvement Cycle Example

### Student: Sam (Development Role)

**Starting Command:** Unit test generation from story + Acceptance Criteria

**Session 4 Submission: Complete Iteration Cycle**

```markdown
IMPROVEMENT CYCLE LOG — Session 4
Date: Week 7

Command: unit-test-generation
Evaluation Criteria: 
  1. Each test maps to one Acceptance Criterion
  2. Coverage includes happy path + failure cases + edge cases
  3. Tests verify behavior, not implementation
  4. Tests compile and run in framework
  5. No non-deterministic elements (sleep, random)

---

BASELINE EVALUATION (Week 7 Session 4 Kickoff)
Test Inputs: 3 real stories from current sprint

Criteria Assessment:
  ✓ Criterion 1 (AC-to-Test Mapping): PASS
  ✗ Criterion 2 (Coverage): PARTIAL
     Issue: Tests cover happy path and basic failures, but miss edge cases
     (boundary values, concurrent scenarios, extreme inputs)
  ✓ Criterion 3 (Behavior vs Implementation): PASS
  ✓ Criterion 4 (Framework Compilation): PASS
  ✓ Criterion 5 (No Non-Determinism): PASS

Overall Baseline Score: 4/5 criteria passing (80%)
Most Critical Weakness: Coverage criterion — edge case tests are weak 
or missing in 2 of 3 story outputs.

---

HYPOTHESIS
Problem: The command asks for "edge case tests" but doesn't specify which 
edge cases are important.

Hypothesis: If I add explicit edge case categories to the Context section
(boundary values, empty inputs, concurrent access, time-based, resource 
limits), the Coverage criterion will pass consistently.

Rationale: When I specify "boundary values: min, max, zero, negative" the 
model will know what edge cases to test. Vague language ("edge cases") 
produces vague output.

---

CHANGE MADE
Command Section: Context (specific edge cases to test)

Before:
  Context: For each Acceptance Criterion, generate tests that cover happy 
  path, failure cases, and edge cases appropriate to the scenario.

After:
  Context: For each Acceptance Criterion, generate tests that cover:
  - Happy path: normal, expected behavior
  - Failure cases: what happens when something goes wrong
  - Edge cases: at least one of the following where applicable:
    • Boundary values (minimum, maximum, zero, negative, overflow)
    • Empty/null inputs (missing data, null fields)
    • Concurrent access (same action attempted simultaneously)
    • Time-based conditions (expired, not yet valid, very old, very new)
    • Resource limits (maximum retries, timeout limits, queue limits)
  
  Identify which categories apply to this specific story and ensure 
  at least one edge case test per category that applies.

---

RE-EVALUATION (Same 3 story inputs as baseline)

Criteria Assessment:
  ✓ Criterion 1 (AC-to-Test Mapping): PASS (no change)
  ✓ Criterion 2 (Coverage): PASS ← IMPROVED
     Edge cases now explicitly covered in all 3 outputs
     Story 1: Boundary-value tests added
     Story 2: Concurrent-access scenario added
     Story 3: Time-based and resource-limit tests added
  ✓ Criterion 3 (Behavior vs Implementation): PASS (no change)
  ✓ Criterion 4 (Framework Compilation): PASS (no change)
  ✓ Criterion 5 (No Non-Determinism): PASS (no change)

Overall New Score: 5/5 criteria passing (100%)
No regressions: All previously passing criteria remain unchanged.

---

CONCLUSION
Hypothesis confirmed. Adding explicit edge case categories with examples 
improved output quality directly. The model now generates appropriate edge 
case tests because it understands which categories apply to typical stories.

Key insight: "Edge cases" is too vague. "Boundary values: min, max, zero, 
negative" produces specific tests.

---

REFACTOR STEP — Load-Bearing Audit

For each instruction in the command, I asked: "Which evaluation criterion 
depends on this instruction? If I removed it, which criterion would fail?"

Instructions Removed (Dead Weight):
  - "Use clear, descriptive test names" → No criterion measures naming 
    clarity; removed
  - "Follow the project's best practices" → Too vague; not tied to any 
    criterion; removed
  - "Include helpful comments" → No criterion measures comment quality; 
    removed

Instructions Kept (Load-Bearing):
  - RTCC structure (Role, Task, Context, Constraints) → Required for 
    Criterion 1 (AC mapping) and Criterion 3 (behavior focus)
  - Language and framework specification → Required for Criterion 4 
    (compilation)
  - Coverage specification → Required for Criterion 2 (edge cases)
  - Edge case categories → Required for Criterion 2
  - "Do not test implementation details" → Required for Criterion 3
  - "No sleep() or random values" → Required for Criterion 5

After Refactor Score: 5/5 criteria still passing
The command is now tighter: every instruction serves at least one criterion.

---

NEXT HYPOTHESIS (For Week 8)
One remaining gap: The Framework Compilation criterion passes, but most 
tests lack proper setup/teardown for database mocking. The tests are 
valid syntax, but incomplete.

If I add: "Include @Before/@After (or @BeforeEach/@AfterEach) setup for 
any test that uses mocked external dependencies like databases or services"

Prediction: This will make the generated tests more complete and 
production-ready without changing the evaluation score (still 5/5 passing).
This is polish, not a criterion weakness.

---

ARTIFACTS COMMITTED (in codebase)
- Updated unit-test-generation command (Context with explicit edge case 
  categories, refactored instructions)
- This improvement cycle log (documentation of hypothesis, change, result)
- Baseline evaluation summary
- Re-run evaluation summary (showing no regressions)
```

---

## Cross-Student Patterns

### Common Evaluation Findings Across Student Submissions

**1. Vague Criteria Produce Vague Output**

Multiple students discovered that when they wrote evaluation criteria in Sessions 1–3 that were too vague ("good Acceptance Criteria", "quality tests"), the generated output was equally vague. The model's output inherits the clarity (or lack thereof) of the instructions.

Examples:
- Vague criterion: "Include edge cases" → Output: Generic edge cases that don't match the domain
- Clear criterion: "Include boundary value edge cases (min, max, zero, negative)" → Output: Specific boundary tests

Resolution: Students who revisited their original criteria (from Session 1) and rewrote them with specificity (e.g., "Every Acceptance Criterion describes a testable behavior — observable outcome, not implementation") saw their command output improve immediately.

Learning: Evaluation criteria quality directly predicts output quality. If you can't write the criterion clearly, the command won't produce clear output.

**2. Load-Bearing Audit Reveals Instructions That Don't Matter**

Most students found 1–3 instructions in their command that corresponded to no evaluation criterion. Common dead-weight instructions:
- Tone or style directions ("Be professional", "Use clear language")
- Unquantified quality aspirations ("Be thorough", "Be complete")
- Implicit assumptions the model doesn't act on ("Think step-by-step", "Do your best")

Removing these had no effect on evaluation scores but made commands shorter and easier to maintain. Students realized: if an instruction doesn't correspond to a measurement, there's no way to know if it's working.

**3. Edge Case Specification Requires Domain Knowledge**

Across test generation and test plan commands, coverage (happy path + failure cases + edge cases) was the most frequently failing evaluation criterion. Students discovered that generic "edge cases" language produces generic output.

Domain-specific improvement examples:
- For date-filtering features: specify edge cases (invalid ranges, future dates, single-day spans)
- For password validation: specify edge cases (boundary lengths, missing character types)
- For bulk operations: specify edge cases (partial failures, concurrent same-record access)

Learning: The command author must supply domain context about which edge cases matter. The model cannot infer this from the story alone.

**4. Behavior vs. Implementation Assessment Was Reliable**

The criterion "tests verify behavior, not implementation" was nearly universally passing by baseline in the second re-evaluation. Students had internalized this distinction from Session 2 training. When failures did occur, they came from technical frameworks (testing internal behavior sometimes required by the framework) or misunderstanding the difference between "what the user sees" and "what the code does."

Students who passed this criterion consistently had internalized: "If I had to explain this test to a non-programmer, could I describe what the user or system should do? Or would I have to explain code internals?"

**5. Refactor Step Was Often Skipped**

Students who reached 5/5 criteria passing sometimes stopped without applying the Load-Bearing Audit (the Refactor step). When Embedded Engineers pushed them to audit, students typically found 1–2 dead-weight instructions. Removing them didn't lower scores but made commands clearer.

The pattern: "If all criteria pass, my job is done." Better pattern: "All criteria passing is Green. Now Refactor — remove instructions that don't correspond to any criterion."

---

## What Session 4 Evaluations Demonstrate

By submitting these evaluations, students provide concrete evidence of two DLP Completion criteria:

**Criterion B — Evaluate:** Students are using documented evaluation criteria and systematic assessment to know whether their commands are producing the intended output. They measure before and after changes. They distinguish improvement from drift.

**Criterion C — Iterate:** Students have documented, hypothesis-driven improvement cycles with measurable outcomes. One change per iteration. One measurement per change. Evidence that they know how to improve a command rather than just change it.

The evaluations become part of the student's permanent record for Week 12 assessment and provide concrete signals to the Embedded Engineer: what aspects of command quality the student is measuring, whether the student's evaluation criteria are well-defined, whether they can form improvement hypotheses, and whether the Refactor step (removing dead instructions) is becoming habitual.

---

## Notes for Cyber Security Group

These examples represent **evaluation discipline, not tool choice**. Your client's internal evaluation framework serves the same function as any other tool — it allows students to measure output quality repeatably.

What matters for the DLP is that students have demonstrated:

1. **Written evaluation criteria** — before building the command, they wrote down what good looks like (Examples 1–5 show this)
2. **Baseline measurement** — they measured their current command output against the criteria they wrote
3. **Hypothesis-driven change** — they formed specific hypotheses about why a criterion failed and made targeted changes
4. **Re-measurement with regression checking** — they measured again against the same criteria to confirm improvement and ensure no unintended side effects
5. **Refactor step** — they removed instructions that didn't correspond to any evaluation criterion

This discipline applies identically whether the underlying tool is Promptfoo, your internal framework, a spreadsheet checklist, or manual human review. The rigor is in the *process*, not in the tool.

The progression from Session 1 (informal criteria) → Session 2 (written criteria) → Session 3 (criteria applied across multiple artifacts) → Session 4 (tooled, repeatable measurement with [client framework]) is the core of what makes DLP Completion distinct from Basic Prompting.

---

## Evaluation Approach: Deterministic vs. Rubric Criteria

The examples in this document show two types of evaluation approaches that work with any evaluation framework:

**Deterministic Criteria** — Directly observable, yes/no or pass/fail
- Presence of required elements (Given/When/Then format present?)
- Absence of prohibited elements (No database references?)
- Specific counts (Between 3–8 criteria per story?)
- Pattern matching (Test naming follows convention?)

These are fast to evaluate and objective. Use them for structural and formatting requirements.

**Rubric Criteria** — Subjective judgment about quality dimensions
- Testability (Does the criterion describe system behavior or implementation?)
- Coverage (Does the suite cover happy path, failures, and edge cases?)
- Business relevance (Are risks identified considering customer/compliance impact?)
- Clarity (Could a developer implement from this without clarification?)

These require judgment and are slower to evaluate. Use them for quality dimensions that matter but can't be measured directly.

A complete evaluation set uses both. Deterministic criteria catch structural issues fast. Rubric criteria assess quality dimensions that drive real impact.

---

## Structure of a Complete Session 4 Evaluation Submission

Based on these examples, a complete submission includes:

1. **Command**: The prompt/instruction you've been using in real work
2. **Evaluation Criteria** (written before building or baseline, from Sessions 1–3)
3. **Baseline Assessment**: Your command evaluated against those criteria
4. **Improvement Hypothesis**: Specific problem identified + predicted fix
5. **Change Made**: Exact modification to the command
6. **Re-Assessment**: Same command evaluated again with same inputs
7. **Refactor Application**: Load-Bearing Audit removing dead instructions
8. **Documentation**: The improvement cycle written and committed

This structure ensures improvement is measurable and repeatable.
