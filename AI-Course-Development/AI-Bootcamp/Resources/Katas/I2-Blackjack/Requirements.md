# I2: Blackjack with Strategy Coach — Requirements

**Difficulty:** Intermediate
**Primary challenge areas:** Math (high), Algorithm (medium), State (medium), UI (medium)

---

## Challenge

Create a blackjack game against a dealer following standard casino rules: dealer hits on soft 16, stands on soft 17, blackjack pays 3:2, insurance available when dealer shows an ace. For every player decision point, display the mathematically optimal play (hit, stand, double down, or split) based on basic strategy charts. After each hand, track and display the player's decision accuracy — the percentage of decisions that matched the optimal strategy — across the session.

---

## Key Technical Requirements

- Complete basic strategy lookup table covering all hard hands, soft hands, and pair splits against all dealer up-cards — this is a 2D lookup table encoding a known correct reference, not a derived algorithm
- Multi-hand split logic supporting up to four simultaneous hands
- Correct soft hand vs. hard hand distinction for strategy lookups (an Ace can count as 1 or 11, and this determines which strategy row applies)
- Running decision accuracy statistics accumulated across multiple hands in a session

---

## Optional Stretch Goals

- Card counting simulation using the Hi-Lo system: display the running count and true count (running count divided by decks remaining) as the game progresses
- Configurable house rules: number of decks, whether dealer hits or stands on soft 17, whether surrender is allowed
- Expected value display showing the EV of each possible decision (hit, stand, double, split) in units of the original bet
- Training mode that replays hands where the player deviated from optimal strategy
