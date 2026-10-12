# E1: Texas Hold'em Probability Simulator — Expected Outcomes

---

## What the Completed Application Delivers

A user sees nine player hands dealt face-up and a community card area showing the flop, turn, and river positions. Before the flop, all nine players show win probability percentages. As each community card is revealed, all nine probabilities update. By the river, probabilities have converged — typically one player is near 100% and the rest near 0%, unless there is a split pot.

The interface remains responsive during simulation — card reveals do not freeze the UI while recalculating.

---

## Correctness Bar

Probability accuracy is the primary requirement. With no community cards dealt, the displayed probabilities should be within ±2% of known equity calculations for any given set of hole cards. Running the simulation at 10,000 iterations per board state is a reasonable baseline for real-time accuracy.

Tie handling is the most common failure mode: in a three-way tie, each player must receive 1/3 of a win, not 0 wins and not 1 win. The probabilities for all nine players must always sum to exactly 100% at every board state — any deviation indicates a tie handling or rounding error.

Performance must be acceptable: updated probabilities must appear within 500ms of each card reveal on a modern browser. Simulations that block the UI thread produce a frozen interface during calculation, which is a functional failure.
