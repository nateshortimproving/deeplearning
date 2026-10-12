# E2: Loan Amortization Dashboard — Requirements

**Difficulty:** Expert
**Primary challenge areas:** Math (high), Visualization (high), State (medium), UI (medium)

---

## Challenge

Build a mortgage and loan calculator that generates a complete amortization schedule from three inputs: principal amount, annual interest rate, and loan term in years. Display the full schedule as a table with each payment's number, date, total payment amount, principal portion, interest portion, and remaining balance. Visualize the payment breakdown over the full loan term as a stacked area chart showing principal and interest portions. Allow users to add extra payments (one-time or recurring) and show how they reduce total interest paid and the loan term.

---

## Key Technical Requirements

- Correct amortization formula: monthly payment = `P × [r(1+r)^n] / [(1+r)^n − 1]`, where P is principal, r is monthly interest rate, n is number of payments
- Rounding handling to cents on each payment, with the final payment explicitly adjusted to bring the remaining balance to exactly $0.00
- Extra payment recalculation: a one-time extra payment reduces the principal at the point of payment and requires recalculating the entire remaining amortization schedule from that point forward — it is not a simple subtraction
- Chart rendering that remains readable and interactive at 360 data points (a 30-year mortgage)

---

## Optional Stretch Goals

- Multi-scenario comparison: two loans side-by-side showing the difference in total interest and monthly payment
- Refinancing analysis showing the break-even point where accumulated savings from a lower rate exceed the upfront refinancing costs
- Bi-weekly payment option (26 payments per year instead of 12) with accelerated payoff timeline and total interest savings
- Mortgage interest deduction calculation showing after-tax loan cost based on a configurable marginal tax rate
