# E1: Texas Hold'em Probability Simulator — Requirements

**Difficulty:** Expert
**Primary challenge areas:** Math (high), State (medium), Algorithm (medium), UI (medium)

---

## Challenge

Simulate a full 9-handed Texas Hold'em table without betting or folding. Deal a hand to each of the nine players and display each hand. Show live win probability percentages for each player that update as community cards are revealed through the flop (three cards), turn (one card), and river (one card). Probabilities must be calculated using Monte Carlo simulation — repeatedly simulating the remainder of the hand with random card draws and counting outcomes.

---

## Key Technical Requirements

- Correct card deck management: a standard 52-card deck dealt without replacement, tracking which cards are in community, in player hands, and remaining in the deck
- Monte Carlo simulation running thousands of completions of the hand for each revealed board state, balancing simulation count against acceptable accuracy and performance
- Tie handling in probability calculation: ties count as fractional wins split among tied players, not as losses for all tied players
- Non-blocking UI: re-running the simulation after each card reveal must not freeze the interface; use Web Workers or a chunked async approach

---

## Optional Stretch Goals

- Hand strength classification labels (high card through royal flush) updating in real time for each player's current holding against the current board
- Exact odds for all-in scenarios (enumerate all remaining card combinations) with comparison against Monte Carlo estimates showing accuracy vs. speed tradeoff
- "What if" mode allowing the user to set specific cards for any player or community position and recalculate
- Outs count and percentage for drawing hands showing how many remaining cards complete each player's draw
