# I3: Wordle Clone with Analysis — Requirements

**Difficulty:** Intermediate
**Primary challenge areas:** UI (high), State (medium), Algorithm (medium), Math (medium)

---

## Challenge

Build a Wordle clone with a dictionary of 5-letter words. After each guess, show which letters are correct and in the right position (green), correct but in the wrong position (yellow), and not in the word (gray) using standard Wordle coloring rules. After each guess, display the number of words from the dictionary that are still possible given all revealed constraints. Include a solver mode that suggests the optimal next guess from the remaining possible words based on letter frequency analysis.

---

## Key Technical Requirements

- Word filtering logic that correctly eliminates candidates after each guess, including the multi-letter case — a letter appearing more than once in a guess has non-obvious constraint implications that must be handled correctly
- On-screen keyboard reflecting the best-known status of each letter (green supersedes yellow, yellow supersedes gray)
- Letter frequency analysis across remaining candidates to drive solver suggestions without excessive computation
- Dictionary large enough to be a real game, curated enough that target words are reasonable

---

## Optional Stretch Goals

- Information theory scoring measuring each guess's value in bits gained (how much it narrows the possibility space)
- Hard mode enforcement requiring revealed green letters to stay in position and revealed yellow letters to appear somewhere in subsequent guesses
- Adversarial mode that changes the target word after each guess to maximize guesses required while remaining consistent with all revealed constraints
- Variable word lengths supporting 4- through 7-letter modes
