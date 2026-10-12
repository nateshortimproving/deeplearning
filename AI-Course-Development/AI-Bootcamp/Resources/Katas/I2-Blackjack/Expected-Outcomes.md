# I2: Blackjack with Strategy Coach — Expected Outcomes

---

## What the Completed Application Delivers

A user plays blackjack against a dealer following standard casino rules. At each decision point, the application displays the recommended action (hit, stand, double down, or split) based on the mathematically correct basic strategy for the current hand against the dealer's up-card.

After each hand, the accuracy display shows what percentage of the user's decisions matched optimal strategy. A session accuracy tracker accumulates across hands. After splitting, each hand is played independently with its own strategy recommendation.

---

## Correctness Bar

The basic strategy lookup must be correct. A complete basic strategy chart is publicly verifiable — every recommended action for every hand combination against every dealer up-card must match the standard chart.

The most common failure modes are: incorrect soft hand handling (a hand with an Ace that can be 1 or 11 maps to a different strategy row than the same total as a hard hand), incorrect pair splitting recommendations, and off-by-one errors in hand value calculation when an Ace changes value. Dealer rules must be strictly implemented: hits on soft 16, stands on soft 17, no deviation.
