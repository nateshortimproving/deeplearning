# I4: Color Palette Generator — Expected Outcomes

---

## What the Completed Application Delivers

A user selects a base color using a color picker. The application generates four palettes — one per harmony rule — each showing the derived colors with hex codes, RGB values, and WCAG contrast ratios against white and black backgrounds. A live preview panel applies the current palette to a sample UI showing text, buttons, and background colors.

Switching between harmony types updates all palettes instantly. The WCAG contrast ratios indicate which color pairs meet AA or AAA accessibility standards for normal and large text.

---

## Correctness Bar

Color harmony correctness is verifiable against the color wheel. A complementary color must be exactly 180° opposite on the hue wheel. Triadic colors must be exactly 120° apart. Analogous colors must be within a ±30° range of the base. Any hue offset error of more than ±2° is visible as a noticeably off-harmony color.

The WCAG contrast ratio formula must be correctly implemented. The relative luminance calculation requires linearizing RGB channel values (applying inverse gamma correction before weighting), not simply normalizing to 0–1. A contrast ratio of 4.5:1 indicates AA compliance for normal text; this threshold must be correctly calculated and labeled. An incorrect linearization step produces systematically wrong contrast ratios across all color pairs.
