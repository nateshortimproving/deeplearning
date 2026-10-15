# Improving Brand Configuration

## Company Info

- **Name**: Improving
- **Tagline**: "It's what we do."
- **Values**: Excellence, Dedication, Involvement
- **Brand Voice**: Approachable, modern, trustworthy, professional

## Logo Assets

All logos stored at: `~/.claude/branding/improving/logos/`

| File | Use Case | Background |
|------|----------|------------|
| `Improving Full Logo.png` | Title pages, large placements | Light/white backgrounds |
| `Improving Simple Logo.png` | Headers, small placements (no tagline) | Light/white backgrounds |
| `improving_logo_white.svg` | Title pages on gradients | Dark/gradient backgrounds |

### Logo Rules
- Never use the "splash" (starburst) icon standalone without marketing approval
- Maintain clear space around logo (at least 1x the height of the "i" in "improving")
- Never distort, recolor, or add effects to the logo

## Color Palette

### Primary Colors

| Name | HEX | Pantone | CMYK | Usage |
|------|-----|---------|------|-------|
| **Improving Blue** | `#005596` | 2945 C | 100,73,20,6 | Primary brand color, headings, header bars, logo |
| **Improving Light Blue** | `#4597D3` | 7688 C | 71,28,4,0 | Secondary headers, links, lighter accents |

### Accent Colors

| Name | HEX | Pantone | CMYK | Usage |
|------|-----|---------|------|-------|
| **Green Accent** | `#5BC2A7` | 7472 C | 64,7,34,0 | Callout boxes, success indicators, gradient endpoint |
| **Orange Accent** | `#F5BB41` | 142 C | 4,27,83,0 | Warnings, attention items, highlight badges |
| **Gray Accent** | `#A7A8A9` | Cool Gray 6C | 36,29,28,0 | Subtle text, borders, dividers |
| **Purple Accent** | `#9D1D96` | 254 C | 45,99,0,0 | Sparingly for special highlights |

### Neutral Colors (for document layouts)

| Name | HEX | Usage |
|------|-----|-------|
| White | `#FFFFFF` | Page backgrounds, reversed text on dark |
| Near Black | `#1A1A2E` | Body text (preferred over pure black) |
| Light Gray | `#F5F5F5` | Alternate table row background |
| Medium Gray | `#E0E0E0` | Borders, divider lines |

## Brand Gradients

Used for title pages, section dividers, and accent elements. Always diagonal (top-left to bottom-right).

| Gradient | From | To | Usage |
|----------|------|----|-------|
| **Primary** | `#005596` (Blue) | `#4597D3` (Light Blue) | Headers, conservative layouts |
| **Extended** | `#005596` (Blue) | `#5BC2A7` (Green) | Title pages, hero sections |
| **Accent** | `#4597D3` (Light Blue) | `#5BC2A7` (Green) | Secondary sections, callout backgrounds |

### CSS Gradient Examples
```css
/* Primary gradient */
background: linear-gradient(135deg, #005596 0%, #4597D3 100%);

/* Extended gradient (title pages) */
background: linear-gradient(135deg, #005596 0%, #4597D3 50%, #5BC2A7 100%);

/* Accent gradient */
background: linear-gradient(135deg, #4597D3 0%, #5BC2A7 100%);
```

## Typography

### Fonts

| Role | Font Family | Source | Weights Available |
|------|------------|--------|-------------------|
| **Headings / Titles** | **Poppins** | Google Fonts | 300 Light, 400 Regular, 500 Medium, 600 SemiBold, 700 Bold |
| **Body / Primary** | **Khula** | Google Fonts | 300 Light, 400 Regular, 600 SemiBold, 700 Bold, 800 ExtraBold |

### Font files
Available at: `~/.claude/branding/improving/logos/` (see SharePoint > Marketing Assets > Font folders for TTF/OTF files if needed)

### Typography Scale (for PDF/document generation)

| Element | Font | Weight | Size | Color |
|---------|------|--------|------|-------|
| Document Title | Poppins | Bold (700) | 36pt | White (on gradient) or Improving Blue |
| Subtitle | Poppins | Medium (500) | 18pt | White (on gradient) or Light Blue |
| H1 - Section Title | Poppins | SemiBold (600) | 24pt | Improving Blue `#005596` |
| H2 - Subsection | Poppins | Medium (500) | 18pt | Improving Blue `#005596` |
| H3 - Sub-subsection | Poppins | Medium (500) | 14pt | Improving Light Blue `#4597D3` |
| Body Text | Khula | Regular (400) | 11pt | Near Black `#1A1A2E` |
| Body Bold | Khula | SemiBold (600) | 11pt | Near Black `#1A1A2E` |
| Caption / Footer | Khula | Light (300) | 9pt | Gray Accent `#A7A8A9` |
| Table Header | Poppins | SemiBold (600) | 10pt | White `#FFFFFF` on Blue `#005596` |
| Table Body | Khula | Regular (400) | 10pt | Near Black `#1A1A2E` |

### Table Column Width Guidelines

- **Always ensure column headers fit on a single line** -- wrapped headers (e.g., "Speedu\np") look unprofessional
- When using reportlab's `make_table()` with proportional widths (e.g., `W*0.12`), verify that the header text fits at the table header font size (Poppins SemiBold 10pt)
- **Minimum column widths by content type:**
  - Single number (#, Cx): `W*0.05` minimum
  - Short word (Files, Count): `W*0.08` minimum
  - Medium word (Priority, Effort, Usages): `W*0.11` minimum
  - Two words (AI Automatable?, Est. Duration): `W*0.15` minimum
  - Long text (File Path, Description): use remaining width
- If total proportions exceed 1.0, reduce the widest column (usually the description/path column) rather than squeezing headers
- **Test rule of thumb:** header text character count x 7pt should be less than the column pixel width

## Font Unicode Limitations

> **WARNING:** Poppins and Khula (Google Fonts) do not include the full Unicode character set. When generating PDFs with reportlab, missing characters render as a blank square (replacement character). Always use the ASCII substitutions listed below.

### Characters MISSING from Poppins and Khula (DO NOT USE in PDFs)

| Character | Unicode | Name | Safe Substitution |
|-----------|---------|------|-------------------|
| `→` | U+2192 | Right Arrow | `->` |
| `∼` | U+223C | Tilde Operator | `~` |
| `█` | U+2588 | Full Block | `\|` or `#` |
| `░` | U+2591 | Light Shade | `:` or `.` |

### Characters PRESENT in Poppins and Khula (safe to use)

| Character | Unicode | Name |
|-----------|---------|------|
| `–` | U+2013 | En-dash |
| `—` | U+2014 | Em-dash |
| `‘` | U+2018 | Left Single Quotation Mark |
| `’` | U+2019 | Right Single Quotation Mark |
| `•` | U+2022 | Bullet |

### Guidance

- Before using any special Unicode character in a reportlab PDF, verify it appears in the "safe" list above.
- If a character is missing, replace it with the ASCII substitution **before** passing text to the PDF builder.
- This applies to all text rendered with Poppins or Khula, including headings, body text, tables, and callout boxes.

## Page Layout Templates

### Title Page (PDF)

```
+--------------------------------------------------+
|                                                    |
|  [Gradient background: #005596 → #5BC2A7]         |
|                                                    |
|                          [White Logo - top right]  |
|                                                    |
|                                                    |
|   DOCUMENT TITLE                                   |
|   (Poppins Bold 36pt, white)                       |
|   ─────────────── (thin teal accent line)          |
|   Subtitle / Client Name                           |
|   (Poppins Medium 18pt, white)                     |
|                                                    |
|                                                    |
|                                                    |
|                                                    |
|   Date                                             |
|   (Khula Regular 11pt, white)                      |
|   CONFIDENTIAL                                     |
|   (Khula Light 9pt, white/80% opacity)             |
+--------------------------------------------------+
```

### Interior Page (PDF)

```
+--------------------------------------------------+
|                          [Simple Blue Logo 120px]  |
|  ─────────────────────────────────────────────── |
|  (thin line in Improving Blue)                     |
|                                                    |
|  Section Heading                                   |
|  (Poppins SemiBold 24pt, Improving Blue)           |
|                                                    |
|  Body text in Khula Regular 11pt. Lorem ipsum      |
|  dolor sit amet, consectetur adipiscing elit.      |
|                                                    |
|  +----------------------------------------------+ |
|  | Table Header | Col 2      | Col 3            | |
|  | (Blue bg)    |            |                   | |
|  |──────────────|────────────|───────────────────| |
|  | Row 1        | Data       | Data              | |
|  | Row 2 (alt)  | Data       | Data              | |
|  +----------------------------------------------+ |
|                                                    |
|  ─────────────────────────────────────────────── |
|  Confidential - Improving                Page X   |
+--------------------------------------------------+
```

### Section Divider (optional, for multi-section reports)

```
+--------------------------------------------------+
|  ================================================ |
|  [Gradient bar: Blue → Teal, ~80px tall]          |
|  SECTION TITLE (Poppins Bold 28pt, white)         |
|  ================================================ |
|                                                    |
|  Section intro text...                             |
|                                                    |
+--------------------------------------------------+
```

## Table Page-Break Prevention

> **RULE:** Tables must never be split across page boundaries in PDFs. Always wrap each table (and its immediately-preceding heading) inside a `KeepTogether` block.

### reportlab Pattern

```python
from reportlab.platypus import KeepTogether

# Wrap heading + table so they stay on the same page
story.append(KeepTogether([
    Paragraph("Section Heading", styles['h2']),
    Spacer(1, 6),
    make_table(data, col_widths),
]))
```

### Guidelines

- **Always wrap heading + table** in a single `KeepTogether`. A heading orphaned on one page with its table on the next looks broken.
- **Small tables (2-6 rows)** should ALWAYS stay on one page with their heading. `KeepTogether` guarantees this.
- **Large tables (10+ rows)** that exceed a full page height: `KeepTogether` will gracefully allow splitting. Ensure `repeatRows=1` is set on the `Table` object so the header row repeats on the continuation page.
- **Custom tables** (built inline with `Table()` instead of a `make_table` helper) need the same treatment — define the table object first, then wrap in `KeepTogether`.
- **Multi-table groups** (e.g., a heading + small data table + timeline table): wrap the entire group in one `KeepTogether` if the combined height is under ~70% of the page frame.
- If a `KeepTogether` block contains content too tall for one page, reportlab automatically falls back to normal splitting — so wrapping is always safe.

## Callout Box Styles

| Type | Background | Border-Left | Icon Color | Usage |
|------|-----------|-------------|------------|-------|
| Info | `#4597D3` at 8% | `#4597D3` 4px | Light Blue | General information |
| Success | `#5BC2A7` at 8% | `#5BC2A7` 4px | Green | Positive findings, recommendations met |
| Warning | `#F5BB41` at 8% | `#F5BB41` 4px | Orange | Risks, areas of concern |
| Critical | `#9D1D96` at 8% | `#9D1D96` 4px | Purple | Urgent items |

## Client Co-Branding

When co-branded mode is requested:
1. Title page: Client logo LEFT, Improving logo RIGHT, neutral gradient or split design
2. Interior pages: Improving branding (headers/footers), client name in subtitle
3. Footer: "Prepared by Improving for [Client Name]"

Store client brand configs at: `~/.claude/branding/clients/[client-name]/config.md`
