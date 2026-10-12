# E2: Loan Amortization Dashboard — Expected Outcomes

---

## What the Completed Application Delivers

A user enters a principal, annual interest rate, and loan term and immediately sees the calculated monthly payment, total interest paid over the life of the loan, and the full amortization table. The table shows every payment — for a 30-year mortgage, all 360 rows — with each payment's date, total amount, principal portion, interest portion, and remaining balance. The stacked area chart shows how the proportion shifts from interest-heavy early payments to principal-heavy later payments.

Adding a one-time extra payment at a specific month recalculates the entire subsequent schedule and shows the new payoff date and total interest saved. Adding a recurring extra payment shows the cumulative effect across all remaining payments.

---

## Correctness Bar

The final payment row must show a remaining balance of exactly $0.00. Any implementation that shows a residual positive or negative balance — even $0.01 — fails this requirement. Rounding accumulation over 360 payments is the common cause; the final payment must be adjusted to absorb any accumulated rounding difference.

The monthly payment amount must be correct to the cent and match the formula output for the given inputs.

Extra payment recalculation must be correct: adding a $1,000 extra payment at month 12 of a 30-year mortgage must reduce total interest paid by a calculable, verifiable amount (roughly $3,000–$5,000 depending on rate), and all subsequent payment rows must reflect the lower principal from that point forward. An implementation that subtracts the extra payment from the final balance without recalculating subsequent interest produces incorrect totals.

The stacked area chart must show principal and interest portions summing exactly to the total payment amount for every data point across all 360 rows.
