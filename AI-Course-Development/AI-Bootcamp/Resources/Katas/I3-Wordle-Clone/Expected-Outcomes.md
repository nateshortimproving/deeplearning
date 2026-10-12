# I3: Wordle Clone with Analysis — Expected Outcomes

---

## What the Completed Application Delivers

A user plays a Wordle game. Each guess is validated against the dictionary. After submission, each letter is colored: green for correct position, yellow for correct letter in wrong position, gray for not in the word. The on-screen keyboard updates to reflect the best-known status of each letter. The remaining candidates count updates after each guess.

In solver mode, the application suggests the optimal next guess from the remaining candidate words based on letter frequency across remaining candidates. The suggestion is drawn only from words consistent with all revealed constraints.

---

## Correctness Bar

The multi-letter constraint is the critical correctness requirement. If the target word is LEVER and the player guesses ENTER: the E at position 4 is green (correct position), and the E at position 2 must be colored correctly based on whether a second E exists in the target beyond what is already accounted for by the green E. Implementations that treat each letter independently fail this case and produce incorrect colorings for multi-letter words.

The remaining candidates count must decrease monotonically after each guess — it cannot increase. It must reach 1 when all constraints uniquely identify the target word. The solver must never suggest a word that is inconsistent with the revealed constraints.
