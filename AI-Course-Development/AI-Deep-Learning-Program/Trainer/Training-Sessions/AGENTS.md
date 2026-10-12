# Agent Instructions — Training Sessions

## Deck Generation Workflow

**Decks are generated from `.deck.md` prompt files by a specialized design harness. There are no PPTX template files in this repository.**

### File Structure

Each session has two files:

| File | Purpose |
|------|---------|
| `Session-N.md` | Authoritative content source — the session content, agenda, labs, trainer notes |
| `Session-N.deck.md` | Deck structure prompt — describes the slides the design harness should generate |

The `.md` file is the source of truth for content. The `.deck.md` file is the source of truth for slide structure. The design harness reads both and generates the `.pptx` as a derived artifact.

### Deck Prompt Structure

Every deck prompt file specifies slides using these types:

**Required in every deck:**
- **Intro Slide** — Session title, week, loop, role focus, one-line framing
- **Check-In Slide** — Discussion question(s) connecting prior work to this session
- **Session Goals Slide** — Each goal annotated with relevance to Product/Process, Development, and Testing roles
- **Closing Slide** — Reviews goals and how they affected each role

**Content slides (used as needed):**
- **Exercise Slide** — Lab Name, Lab Timing, Lab Steps, "You'll know when you're done because..." footer
- **Demo Slide** — Description (what and why, not how) + "What to focus on" section
- **Compare/Contrast Slide** — Left-side bad behaviors → right-side good behaviors, hard limited to 5 items
- **Lecture Slide** — Only what students should learn; no layout or design instructions

### Content Source

When updating a deck prompt, always read the session's `.md` file first and reconcile any content differences. The markdown is the source of truth, the deck prompt is the structure specification, and the PPTX is the generated output.

### No PPTX Files in Repo

PPTX files are generated from `.deck.md` prompt files using a design tool (e.g., Claude Design). Generated PPTXs are committed to the repo so instructors don't need to regenerate them. To update or regenerate decks, use the `.deck.md` file as input to your design tool and commit the new PPTX.

The deck prompts are primarily for content maintainers. Instructors should use the committed PPTX files directly.