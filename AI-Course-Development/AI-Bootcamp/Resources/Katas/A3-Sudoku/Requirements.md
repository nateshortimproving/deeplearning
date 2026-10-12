# A3: Sudoku Generator and Solver — Requirements

**Difficulty:** Advanced
**Primary challenge areas:** Algorithm (high), UI (high), State (medium), Visualization (medium)

---

## Challenge

Create a Sudoku game that generates valid puzzles at three difficulty levels (easy, medium, hard) with unique solutions. Include a hint button that reveals the value of one cell using the solver's logic. Include a solve button that animates the backtracking algorithm's execution: show cells being filled in, show the backtracking when a contradiction is reached, and highlight the final solution. Validate user input in real-time, highlighting conflicting cells immediately.

---

## Key Technical Requirements

- Puzzle generation that produces boards with exactly one solution — requires the solver to verify uniqueness after each cell removal during generation, since a valid filled board is not the same as a valid puzzle
- Difficulty estimation based on which solving techniques are required (easy: naked singles only; medium: hidden singles; hard: advanced techniques) — not just the count of given cells
- Solving animation with intelligent throttling — the backtracking algorithm may make thousands of recursive calls; showing every step would be either too fast to follow or too slow to complete
- Real-time conflict highlighting covering same row, same column, and same 3×3 box simultaneously when any value is placed

---

## Optional Stretch Goals

- Pencil marks (candidate values) with automatic constraint elimination: placing a value removes it from candidates in the same row, column, and box
- Advanced technique visualization for naked pairs, hidden singles, and X-wing patterns with explanatory text
- "Rate my puzzle" mode analyzing a user-provided puzzle and reporting which solving techniques are required
- Variant sudoku support: killer sudoku (caged cells with sum constraints), thermometer sudoku, diagonal sudoku
