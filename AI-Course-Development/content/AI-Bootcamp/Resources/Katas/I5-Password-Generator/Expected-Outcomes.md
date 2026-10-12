# I5: Password Generator with Entropy Meter — Expected Outcomes

---

## What the Completed Application Delivers

A user selects a character set and length and generates a password. The entropy display shows the calculated bit strength. The crack time display shows three scenarios — online attack, offline slow hash, and offline fast hash — each with a human-readable time estimate (seconds, hours, years, centuries). Pronounceable mode generates passwords that read as syllable sequences.

Regenerating produces a different password each time. The entropy and crack time displays update immediately when any setting changes, before a new password is generated.

---

## Correctness Bar

Passwords must use `crypto.getRandomValues()`. Using `Math.random()` is a functional security failure, not a style issue.

The entropy formula must be correct: a 12-character password from a 72-character set has entropy = 12 × log₂(72) ≈ 75.6 bits. Crack time estimation must be based on the correct conversion: 2^(entropy−1) expected guesses to reach 50% probability, divided by the attack rate for each scenario. Crack times must be in the correct order of magnitude — a 75-bit password should show years for the offline fast hash scenario, not seconds or millennia. All three scenarios must produce distinct, meaningfully different time estimates that reflect the 7 orders of magnitude difference between online and fast offline attack rates.
