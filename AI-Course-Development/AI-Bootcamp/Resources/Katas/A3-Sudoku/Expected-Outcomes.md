# A3: Sudoku Generator and Solver — Expected Outcomes

---

## What the Completed Application Delivers

A user selects a difficulty level and receives a puzzle with some cells pre-filled. They fill in the remaining cells; conflicts are highlighted in red immediately when a value violates a row, column, or box constraint. The hint button fills in one cell using the solver's logic, not a random choice. The solve button animates the backtracking process: cells fill in, and when a contradiction is reached, the animation backtracks and tries a different value, continuing until the solution is found.

Generated puzzles at each difficulty level feel distinct — easy puzzles are solvable by direct elimination; hard puzzles require more deliberate reasoning.

---

## Correctness Bar

Every generated puzzle must have exactly one solution. This is verifiable by running the solver twice with different tie-breaking order and confirming both produce the same result. A puzzle that has multiple solutions is not a valid Sudoku puzzle.

The solver animation must be correct: the final highlighted solution must match the puzzle's unique solution. The animation must not skip valid backtracking steps or show a solution that was reached without backtracking when backtracking was required.

Real-time conflict detection must fire immediately on input and must correctly identify all three constraint types simultaneously — a value that conflicts in its row, its column, and its box must trigger all three highlights at once.
