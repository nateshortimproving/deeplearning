---
name: improving-brand
description: Apply Improving brand standards to deliverable artifacts (PDFs, PPTX, DOCX). Use when creating client-facing documents, reports, assessments, proposals, or any professional deliverable that should carry Improving branding. Automatically applies correct colors, fonts, logos, gradients, and layout patterns.
---

# Improving Brand Standards Skill

This skill ensures all client-facing deliverables follow Improving's official brand guidelines.

## When to Use This Skill

- Creating PDFs for client engagements (assessments, reports, proposals, recommendations)
- Building PowerPoint presentations
- Generating Word documents (SOWs, charters, handoff docs)
- Any professional artifact that needs Improving branding
- When user mentions "branded" or requests a deliverable for a client

## Instructions

1. **Always reference** [brand-config.md](brand-config.md) for colors, fonts, gradients, and logo paths.
2. **Default to Improving branding** unless user specifies client-only or co-branded.
3. **Apply the branding mode** based on context:
   - `improving` (default): Improving brand on all deliverables you present to clients
   - `client`: Client's brand only, for handoff artifacts the client will own
   - `co-branded`: Both logos on title page, Improving brand on interior pages
4. **Always include a branded title page** with gradient background and white logo for PDFs and PPTX.
5. **Always include branded headers/footers** on interior pages with the blue logo.
6. **Use Poppins** for all headings and **Khula** for body text.
7. **Install fonts** if needed: both are Google Fonts, available at `~/.claude/branding/improving/logos/` alongside the logos.

## Branding Mode Quick Reference

| Mode | Title Page | Interior Header | Footer | When to Use |
|------|-----------|----------------|--------|-------------|
| `improving` | Improving gradient + white logo | Blue logo top-right | "Confidential - Improving" + page num | Assessments, proposals, status reports |
| `client` | Client's brand | Client's logo | Client's footer | Handoff docs, internal client artifacts |
| `co-branded` | Both logos on gradient | Improving logo | Both company names | Partnership deliverables |

## PDF Generation Pattern

When generating PDFs using the `document-skills:pdf` skill, apply branding by following the layout patterns in [brand-config.md](brand-config.md). The key elements are:

1. **Title page**: Full-bleed gradient background (#005596 to #5BC2A7 diagonal), white logo top-right, document title in Poppins Bold white, subtitle/client name below, date at bottom
2. **Interior pages**: White background, blue logo (small) in header right, blue accent line below header, Poppins headings in Improving Blue (#005596), Khula body text in dark gray, page numbers in footer
3. **Section dividers** (optional): Blue-to-teal gradient bar across top of page with white Poppins section title
4. **Tables**: Header row in Improving Blue (#005596) with white text, alternating light blue (#4597D3 at 10% opacity) row striping
5. **Accent elements**: Use Green accent (#5BC2A7) for callout boxes, Orange (#F5BB41) for warnings, Purple (#9D1D96) sparingly for highlights

## PPTX Generation Pattern

> **For markdown-to-PPTX generation**: Use the `improving-powerpoint` skill instead. It handles parsing markdown outlines, selecting layouts, and running the full template workflow automatically. This skill (`improving-brand`) provides the underlying brand standards that `improving-powerpoint` references.

When generating PPTX using the `document-skills:pptx` skill, **always clone an official template** rather than building from scratch. See [pptx-templates.md](pptx-templates.md) for the complete slide layout catalog.

### Template Selection
- **Primary** (`PRESO-THEME-WIDE-NOV 2025.pptx`): Clean corporate style, white backgrounds, logo bottom-right. Use for client presentations, proposals, formal deliverables.
- **Alternative** (`Starter Preso Alternative Style NOV 2025.pptx`): Softer modern style, pastel backgrounds, logo upper-right. Use for internal presentations, workshops.

Templates stored at: `~/.claude/branding/improving/templates/`

### Workflow
1. Copy the template file to the output location
2. Delete example slides you don't need
3. Add new slides using the defined layouts (see catalog for layout names and indices)
4. Populate placeholders with content
5. **CRITICAL: Delete unused placeholder shapes** from each slide's XML (see Ghost Text Prevention below)

### PPTX Critical: Ghost Text Prevention

**Problem**: PowerPoint placeholders inherit default text from the slide master/layout. Calling `tf.clear()` or `clear_placeholder()` does NOT prevent this — an empty text frame still inherits and renders the layout's default text (e.g., "JOHN DOE", "Click to edit Master subtitle style").

**The ONLY reliable fix**: Delete unused placeholder shapes from the slide XML entirely.

```python
def delete_unused_placeholders(slide, used_indices):
    """Delete any placeholder not in used_indices from the slide XML."""
    spTree = slide.shapes._spTree
    to_remove = []
    for sp in spTree.iterchildren():
        ph_elem = sp.find('.//{http://schemas.openxmlformats.org/presentationml/2006/main}ph')
        if ph_elem is not None:
            idx = int(ph_elem.get('idx', '0'))
            if idx not in used_indices:
                to_remove.append(sp)
    for sp in to_remove:
        spTree.remove(sp)
```

**Usage**: After populating content on each slide, call `delete_unused_placeholders(slide, {set of indices you filled})`.

**Known ghost text traps** (Primary Template):
- Layout 0 (Principal Title): PH idx=13 defaults to **"JOHN DOE"** — always delete
- Layout 6 (Quote): PH idx=0 defaults to **"John Doe"** — always overwrite with attribution text
- All layouts with subtitle placeholders: default to "Click to edit Master subtitle style" — fill or delete

### PPTX Layout Selection Rules

- **Never use Text Box Left/Right (layouts 4/5) without an actual image** — creates a half-empty slide with massive whitespace. If you don't have an image, use Text Slide (layout 2) instead.
- **2 Text Boxes (layout 3) works great for phase comparisons** where both sides have equal content density.
- **Bullet Slide / Bullet 2 (layouts 7/8) have built-in visual elements** (gradient bars, badge numbers) — use these for key highlights and KPIs.
- **Delete template slides** using this pattern (python-pptx doesn't have a clean API for this):
```python
while len(prs.slides) > 0:
    rId = prs.slides._sldIdLst[0].get(
        '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
    if rId:
        prs.part.drop_rel(rId)
    prs.slides._sldIdLst.remove(prs.slides._sldIdLst[0])
```

### Key Slide Types (Primary Template)
| Layout | Name | When to Use |
|--------|------|-------------|
| 1 | **Principal Title Slide** | Cover slide (gradient bg, white logo) |
| 2 | **Title Page** | Section dividers (gradient bg) |
| 3 | **Text Slide** | Standard content - the workhorse (white bg, blue logo bottom-right) |
| 4 | **2 Text Boxes** | Two-column comparisons, side-by-side |
| 5/6 | **Text Box Left/Right** | Content with image on opposite side |
| 7 | **Quote Slide** | Testimonials, key findings, callout statements |
| 8 | **Bullet Slide** | Three key items with numbered badges |
| 9 | **Bullet 2 Slide** | Four-item 2x2 grid |
| 10 | **Contact Slide** | Closing contact info with headshot |

See [pptx-templates.md](pptx-templates.md) for full details on each layout including placeholder positions, decorative elements, and font specs.

## Recipe Persistence

Every branded artifact should have a saved "recipe" so future modifications reuse the original content and generation script rather than starting from scratch.

### Recipe Location

```
~/.claude/projects/-Users-jakes/recipes/<slug>/
  ├── recipe.md       # Metadata + full markdown content
  ├── generate.py     # (or generate.js for PPTX) exact generation script
  └── assets/         # Referenced images/logos (optional)
```

Slug is derived from the artifact name: lowercase, spaces to hyphens (e.g., `acme-security-assessment`).

### After Every Artifact Generation

1. Create `~/.claude/projects/-Users-jakes/recipes/<slug>/` directory
2. Write `recipe.md` with YAML frontmatter:
   ```yaml
   ---
   output_path: ~/Work/Clients/Acme/Acme-Security-Assessment.pdf
   created: 2026-03-04
   updated: 2026-03-04
   type: pdf          # pdf, pptx, or docx
   description: Security assessment report for Acme Corp
   branding_mode: improving
   ---
   ```
   Followed by the full markdown content used to generate the artifact.
3. Write `generate.py` (or `generate.js` for PPTX) containing the exact generation code that was executed. Include a header comment with the output path and re-run instructions.

### When User Asks to Modify an Existing Deliverable

1. Search `~/.claude/projects/-Users-jakes/recipes/` for a matching recipe (match by output path or slug)
2. Read the existing `recipe.md` and `generate.py`/`generate.js`
3. Apply the requested changes to content and/or script
4. Regenerate the artifact by running the updated script
5. Update recipe files with new versions (bump `updated` date)

### Important

- **Only regenerate when the user explicitly asks** — never auto-regenerate
- When regenerating, always update both `recipe.md` and the generation script
- If the output path changes, update `output_path` in the frontmatter

## Logo Selection

- **Light backgrounds**: Use `Improving Full Logo.png` (with tagline) or `Improving Simple Logo.png` (without tagline, for small spaces like headers)
- **Dark/gradient backgrounds**: Use `improving_logo_white.svg` (convert to PNG if needed with cairosvg or similar)
- **Header placement**: Simple Logo (no tagline), scaled to ~120px wide, top-right corner
- **Title page placement**: Full Logo or White Logo, scaled to ~250px wide
