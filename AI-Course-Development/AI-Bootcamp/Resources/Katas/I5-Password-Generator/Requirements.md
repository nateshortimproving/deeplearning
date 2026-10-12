# I5: Password Generator with Entropy Meter — Requirements

**Difficulty:** Intermediate
**Primary challenge areas:** Math (high), Algorithm (medium), UI (medium), Visualization (medium)

---

## Challenge

Build a password generator with controls for total length and character set inclusion (uppercase letters, lowercase letters, digits, symbols). After generating a password, calculate and visualize its entropy in bits and display an estimated crack time against three attack scenarios: online attack (1,000 guesses/second), offline slow hash (100,000 guesses/second), and offline fast hash (10 billion guesses/second). Include a pronounceable mode that generates passwords using alternating consonant-vowel patterns while maintaining reasonable entropy.

---

## Key Technical Requirements

- Cryptographic randomness using `crypto.getRandomValues()` — `Math.random()` is not cryptographically secure and must not be used
- Entropy calculation in bits: `password_length × log₂(character_set_size)`
- Crack time estimation converting entropy to expected guesses at 50% probability (2^(entropy−1)) divided by the attack rate for each scenario
- Pronounceable generation algorithm using consonant-vowel alternation that produces human-readable output while remaining random

---

## Optional Stretch Goals

- Passphrase generation using a diceware-style word list with entropy calculated from list size and word count
- Memorable password generation using a word + number + symbol pattern with calculated entropy
- Have I Been Pwned API integration using the k-anonymity model (send only the first 5 characters of the SHA-1 hash) to check whether a generated password appears in known breach databases
