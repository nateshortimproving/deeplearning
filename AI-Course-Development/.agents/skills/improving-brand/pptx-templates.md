# Improving PPTX Template Catalog

## Template Files

Stored at: `~/.claude/branding/improving/templates/`

| Template | File | Style | Best For |
|----------|------|-------|----------|
| **Primary** | `PRESO-THEME-WIDE-NOV 2025.pptx` | Clean, corporate, geometric. White backgrounds with blue-teal gradient bar at bottom. Logo bottom-right on content slides. | Client presentations, proposals, formal deliverables |
| **Alternative** | `Starter Preso Alternative Style NOV 2025.pptx` | Softer, modern, organic. Pastel abstract backgrounds with dot grid and blob shapes. Logo upper-right on content slides. | Internal presentations, workshops, lighter tone |

Both templates share the same theme colors and Poppins + Khula fonts. Default to the **Primary** template unless the user requests the alternative style.

## How to Use Templates

When creating a PPTX, **clone** the appropriate template file and modify it:
1. Copy the template to the output location
2. Delete the example slides you don't need
3. Add new slides using the defined layouts
4. Populate placeholders with content
5. **DELETE unused placeholder shapes** from each slide's XML (see SKILL.md for the `delete_unused_placeholders` function)

This preserves the slide masters, theme colors, fonts, and decorative elements.

> **WARNING**: Step 5 is non-negotiable. Skipping it causes ghost text ("JOHN DOE", "Click to edit Master subtitle style") to render from the slide layout defaults. python-pptx's `tf.clear()` does NOT prevent this — you must remove the XML element entirely.

## Placeholder Index Map (Primary Template)

These are the **actual placeholder indices** from the template OOXML. Use these when calling `slide.placeholders[idx]`.

| Layout | idx | Name | Default Ghost Text | Notes |
|--------|-----|------|--------------------|-------|
| **0 - Principal Title** | 0 | Title | "Click to edit..." | Presentation title |
| | 1 | Subtitle | "Click to edit..." | Client name / date |
| | **13** | **Text Placeholder** | **"JOHN DOE"** | **ALWAYS DELETE — presenter name trap** |
| **1 - Title Page** | 0 | Title | "Click to edit..." | Section title |
| | 1 | Subtitle | "Click to edit..." | Section subtitle |
| **2 - Text Slide** | 0 | Title | "Click to edit..." | Slide title |
| | 10 | Content | "Click to edit..." | Main body area |
| | 11 | Subtitle | "Click to edit..." | Subtitle line — fill or delete |
| **3 - 2 Text Boxes** | 0 | Title | "Click to edit..." | Slide title |
| | 11 | Left Content | "Click to edit..." | Left column body |
| | 12 | Right Content | "Click to edit..." | Right column body |
| | 13 | Subtitle | "Click to edit..." | Subtitle line — fill or delete |
| **4 - Text Box Left** | 0 | Title | "Click to edit..." | Title (left half only) |
| | 11 | Left Content | "Click to edit..." | Left body text area |
| | 12 | Subtitle | "Click to edit..." | Subtitle — fill or delete |
| **5 - Text Box Right** | 0 | Title | "Click to edit..." | Title (right half only) |
| | 12 | Right Content | "Click to edit..." | Right body text area |
| | 11 | Subtitle | "Click to edit..." | Subtitle — fill or delete |
| **6 - Quote Slide** | 0 | Title/Attribution | **"John Doe"** | **ALWAYS overwrite with attribution** |
| | 10 | Quote Body | "Click to edit..." | The quote text |
| **7 - Bullet Slide (3)** | 0 | Title | "Click to edit..." | Slide title |
| | 1 | Body Area 1 | "Click to edit..." | First item content |
| | 11 | Body Area 2 | "Click to edit..." | Second item content |
| | 12 | Body Area 3 | "Click to edit..." | Third item content |
| | 13 | Badge 1 | "01" | Keep default or overwrite |
| | 14 | Badge 2 | "02" | Keep default or overwrite |
| | 15 | Badge 3 | "03" | Keep default or overwrite |
| | 16 | Subtitle | "Click to edit..." | Subtitle — fill or delete |
| **8 - Bullet 2 (4)** | 0 | Title | "Click to edit..." | Slide title |
| | 1 | Body Area 1 | "Click to edit..." | Top-left quadrant |
| | 11 | Body Area 2 | "Click to edit..." | Top-right quadrant |
| | 12 | Body Area 3 | "Click to edit..." | Bottom-left quadrant |
| | 13 | Body Area 4 | "Click to edit..." | Bottom-right quadrant |
| | 14 | Subtitle | "Click to edit..." | Subtitle — fill or delete |
| **9 - Contact Slide** | 0 | Title | "Click to edit..." | "Contact" |
| | 1 | Contact Text | *(empty)* | Name, title, email, phone |
| | 10 | Picture | *(image placeholder)* | Headshot — insert image or delete |
| **10 - Custom Layout** | 0 | Title | "Click to edit..." | Title only |
| **11 - Blank** | 5 | Footer Holder | *(empty)* | |
| | 6 | Date Holder | "11/14/2025" | |
| | 7 | Slide Number | "\u2039#\u203a" | |

## Template 1 (Primary): Slide Layouts

### Layout 1: Principal Title Slide
- **When to use**: First slide of every presentation (cover)
- **Background**: Full-bleed blue-to-teal gradient (image-based)
- **Logo**: White Improving logo with starburst, upper-left (~1.0", 1.8"), ~3.5" x 1.6"
- **Placeholders**: Center Title, Subtitle, copyright bar at bottom
- **Fonts**: Title inherits theme major; Subtitle: Poppins ~20pt, gray
- **Notes**: Always use this for the opening slide. Enter presentation title and client name in subtitle.

### Layout 2: Title Page (Section Divider)
- **When to use**: Section dividers between major presentation sections
- **Background**: Full-bleed blue-to-teal gradient (same as cover)
- **Logo**: None
- **Placeholders**: Title, Subtitle
- **Notes**: Use to visually break the presentation into sections (e.g., "Current State", "Recommendations", "Next Steps")

### Layout 3: Text Slide (Standard Content)
- **When to use**: Most slides - the workhorse layout
- **Background**: White, with gradient bar at very bottom from master
- **Logo**: Blue full-color Improving logo, bottom-right (~11.3", 7.0"), ~1.5" x 0.5"
- **Placeholders**: Title (32pt Poppins), Subtitle (20pt), Body content (14pt Khula)
- **Notes**: Title + subtitle + body. Use for narrative content, bullet points, descriptions.

### Layout 4: 2 Text Boxes (Two-Column)
- **When to use**: Side-by-side comparisons, before/after, pros/cons
- **Background**: White
- **Logo**: Blue logo, bottom-right
- **Placeholders**: Title, Subtitle, Left body, Right body

### Layout 5: Text Box Left
- **When to use**: Content with supporting image on the right
- **Background**: White fill rectangle on left half, right half open for images
- **Logo**: Blue logo, bottom-right
- **Placeholders**: Title (left-half), Subtitle, Left body
- **Notes**: Add image on right side manually

### Layout 6: Text Box Right
- **When to use**: Content with supporting image on the left
- **Background**: White fill rectangle on right half, left half open for images
- **Logo**: Blue logo, bottom-right
- **Placeholders**: Title (right-half), Subtitle, Right body

### Layout 7: Quote Slide
- **When to use**: Client testimonials, executive quotes, key statements, callout insights
- **Background**: White
- **Decorative**: Large blue-to-teal gradient speech bubble quotation marks
- **Logo**: Blue logo, bottom-right
- **Placeholders**: Title, Quote body text
- **Notes**: Great for emphasizing a key finding or client voice

### Layout 8: Bullet Slide (Three Items)
- **When to use**: Three key features, recommendations, or numbered highlights
- **Background**: White with full-width gradient bar across middle
- **Logo**: Blue logo, bottom-right
- **Placeholders**: Title, Subtitle, 3 numbered badge areas + 3 text areas in a row
- **Notes**: Perfect for "Top 3 Recommendations" or "3 Key Findings"

### Layout 9: Bullet 2 Slide (Four Items)
- **When to use**: Four-item grid, 2x2 comparison matrix
- **Background**: White
- **Logo**: Blue logo, bottom-right
- **Placeholders**: Title, Subtitle, 4 body areas in 2x2 grid

### Layout 10: Contact Slide
- **When to use**: Contact info, team bios, closing "get in touch" slide
- **Background**: White
- **Logo**: Blue logo, bottom-right
- **Placeholders**: Title, Contact body text, Picture placeholder (headshot)

### Layout 11: Custom Layout
- **When to use**: Freeform content that doesn't fit other layouts
- **Placeholders**: Title only

### Layout 12: Blank
- **When to use**: Fully custom slides, complex diagrams, infographics
- **Placeholders**: Footer elements only

## Template 2 (Alternative): Slide Layouts

### Layout 1: Principal Title Slide (Standard Content)
- **When to use**: Most slides (this template's workhorse layout)
- **Background**: Soft pastel abstract (pale blue-lavender with dot grid and organic blobs)
- **Logo**: Blue Improving logo, upper-right (~11.1", 0.4"), ~2.1" x 0.8"
- **Placeholders**: Title (29pt), Body (subtitle), Body (content)
- **Notes**: In Template 2, the content layout is Layout 1 (not Layout 3 like Template 1)

### Layout 2: Title Page (Cover & Section Divider)
- **When to use**: Cover slide and section dividers
- **Background**: Full-bleed blue-to-teal gradient with organic blob shapes and dot pattern
- **Logo**: White Improving logo, upper-right (~10.8", 0.3"), ~2.4" x 0.8"
- **Placeholders**: Title (29pt), Subtitle
- **Decorative**: Two small rectangles at bottom

### Layout 3: Text Slide
- **When to use**: Title + subtitle + body content (alternative to Layout 1)
- **Logo**: Blue Improving logo, upper-LEFT (0.4", 0.4") - note different position
- **Placeholders**: Title, Subtitle, Body

### Layout 4: 2 Text Boxes
- **When to use**: Two-column content
- **Logo**: Blue logo, upper-right

### Layout 5: Bullet Slide (Text + Image)
- **When to use**: Text on left with picture placeholder on right
- **Logo**: Blue logo, upper-right
- **Placeholders**: Title, Subtitle, Left body, Picture placeholder (~6.3" x 4.6")

### Layout 6: Quote Slide
- **When to use**: Quotes, testimonials, key statements
- **Decorative**: Large gradient teardrop quotation mark + rounded-rectangle attribution frame
- **Logo**: Blue logo, upper-right
- **Placeholders**: Title, Label, Quote text (Poppins 28pt bold italic, `#2297D5`), Attribution (Poppins 18pt, `#4597D3`)

### Layout 7: Custom Layout / Layout 8: Blank
- Same as Template 1 equivalents

## Layout Selection Design Guide

Choosing the right layout is a presentation design decision, not just a formatting one. Each layout creates a different cognitive effect on the audience. Here's how to think about it in the context of consulting deliverables.

### Principal Title Slide (Layout 1)
**The contract.** This slide sets expectations. It tells the audience what this presentation is, who it's for, and signals professionalism. Every presentation starts here -- no exceptions.
- Title = the deliverable name (e.g., "DevOps Maturity Assessment", "Cloud Migration Proposal")
- Subtitle = client name and/or date
- Never put content here. If you're tempted to add bullet points to the cover, you need a Text Slide after it instead.

### Title Page / Section Divider (Layout 2)
**The mental reset.** Use this when the audience needs to shift gears entirely. The gradient background creates a visual break that says "we're done with that topic, here's a new one." This is critical for longer presentations.
- **Use it** when moving between fundamentally different topics: "Current State" → "Recommendations" → "Next Steps"
- **Don't use it** between sub-topics within the same section. If you're going from "Infrastructure Findings" to "Security Findings," that's still within "Current State" -- use a bold heading on a Text Slide instead.
- **Rule of thumb**: A 20-slide deck should have 3-4 section dividers. More than that and the presentation feels choppy. Fewer and the audience loses track of where they are.
- Good section divider titles are short and action-oriented: "What We Found", "What We Recommend", "What Happens Next" -- not "Section 3: Detailed Analysis of Current State Infrastructure"

### Text Slide (Layout 3)
**The workhorse.** 70-80% of your slides will be this layout. It carries the substance of your message.
- **Use it for**: Narrative explanations, bullet-point findings, process descriptions, detailed recommendations, risk analysis, anything that's primarily text-driven
- **Structure matters more than layout here**: Use the title as a complete thought or assertion (e.g., "Legacy deployment process adds 3 weeks to every release" not "Deployment Process"). The subtitle can add context. The body carries the evidence.
- **When NOT to use it**: If your content is purely a comparison between two things (use Two-Column), if you're showing data alongside an image/diagram (use Text+Image), or if you have a single powerful statement (use Quote).

### 2 Text Boxes / Two-Column (Layout 4)
**The comparison.** Use this when you're asking the audience to evaluate two things of roughly equal importance side by side.
- **Best for**: Current state vs. future state, Option A vs. Option B, before/after, risks vs. mitigations, client perspective vs. industry benchmark
- **Both columns should have parallel structure**: same heading pattern, similar depth. If one side is 3 bullets and the other is 15 lines, the visual imbalance signals that one option is clearly more developed -- which may or may not be your intent.
- **Don't use it for**: Content that's just long and needs two columns to fit. If the two sides aren't being compared, use a Text Slide with structured bullets instead.

### Text Box Left / Text Box Right (Layouts 5 & 6)
**The evidence slide -- Jake's preferred content layout.** When in doubt about how to present a content slide, default to this pattern: high-level bullet points on one side, supporting image on the other. This is more visually engaging than a full-text slide and forces you to keep the text concise.

> **CRITICAL: These layouts REQUIRE an actual image.** Without one, the slide is half-empty whitespace and looks terrible. If you don't have an image to insert (AI-generated, diagram, screenshot, or placeholder), use a Text Slide (Layout 2) instead. Never use these layouts for text-only content.

- **Text Box Left** (bullets left, image right): **The default choice.** The eye reads left-to-right, so the audience processes your key points first, then sees the supporting visual. Use this most of the time.
  - Great for: Architecture diagrams with explanation, screenshot evidence with annotations, process flows with narrative, data charts with bullet-point interpretation, current-state photos with findings
  - The bullets should be high-level takeaways (3-5 bullets max), not dense paragraphs. Let the image carry the detail.
- **Text Box Right** (image left, bullets right): Use when the image is the primary hook and the text explains it. The image catches attention first, then the text provides context.
  - Great for: Dashboard screenshots that speak for themselves, team photos with bios, product demos, before/after visuals
- **Don't use it for**: Stock photos or decorative images. If the image doesn't carry real informational value, it's wasting half your slide. Use a Text Slide instead.
- **Preference note**: When building presentations for Jake, prefer Text Box Left (bullets + image) over plain Text Slides for most content. Reserve full-text Text Slides for when the content genuinely needs more space or there's no meaningful image to pair with it.
- **Visual alternation**: When consecutive slides use the bullet+image pattern, alternate between Text Box Left (Layout 5) and Text Box Right (Layout 6) to create visual rhythm and prevent the audience's eye from glazing over. Don't put 3+ slides in a row with the same side layout. Text Box Left remains the default for any single slide in isolation; Text Box Right is the variation you introduce for consecutive sequences. However, if the image is clearly the primary hook for a specific slide, let that override the alternation pattern -- content logic beats visual rhythm.

### Quote Slide (Layout 7)
**The emotional anchor.** This layout is dramatically different from content slides -- the large quotation mark graphics signal "pay attention, this is someone's actual words." Use it to create impact.
- **Use it for**:
  - A client stakeholder's own words describing their pain point ("We spend 40% of our sprint just fighting the deployment pipeline")
  - An executive sponsor's endorsement or vision statement
  - A key finding that's more powerful stated as a direct observation than as a bullet point
  - Industry authority quotes that validate your recommendation
- **How many per deck**: 1-2 maximum. If every other slide is a quote, the impact is diluted. Save it for the moment that matters most.
- **MUST be an actual quote**: The quotation mark graphics signal "these are someone's real words." Never use this layout for paraphrased findings, summaries, or fabricated text — that's misleading. If you don't have a real quote from a stakeholder, use a Text Slide with visual emphasis instead.
- **Don't use it for**: Long paragraphs. Quotes on this layout should be 1-3 sentences. If it's longer, put it on a Text Slide with visual emphasis instead.
- **Pro tip**: Place the Quote Slide right before or after a Section Divider for maximum dramatic effect. It works as either the culmination of a section ("here's what the current state means in human terms") or the opening of a new section ("this is why we need to act").

### Bullet Slide - Three Items (Layout 8)
**The power of three.** Humans remember things in threes. This layout with its numbered badges and gradient bar is designed to make three items feel equally important and memorable.
- **Use it for**:
  - Top 3 recommendations
  - 3 key findings / takeaways
  - 3 workstreams or phases
  - 3 options being proposed
  - Executive summary (3 things to remember from this presentation)
- **Each item should be roughly equal in weight and depth.** If one of your three items needs a paragraph of explanation and the others are one-liners, the layout will feel unbalanced -- break the complex item into its own Text Slide instead.
- **Don't use it for**: Lists of 3 things that aren't equally important. If it's really "1 critical thing and 2 minor things," use a Text Slide where you can visually emphasize the important one.

### Bullet 2 Slide - Four Items (Layout 9)
**The framework.** The 2x2 grid naturally suggests a matrix or framework. It implies structure and completeness.
- **Use it for**:
  - 2x2 priority matrices (urgent/important)
  - Four-quadrant assessments (e.g., cost vs. effort)
  - Four pillars / capabilities / workstreams
  - SWOT-style analysis
- **The spatial position matters**: Top-left is perceived as "first" or "most important." Be intentional about which item goes where.
- **Don't use it for**: A list of 4 things that don't relate to each other as a group. If they're sequential steps, use a Text Slide with numbered bullets instead.

### Contact Slide (Layout 10)
**The closer.** Always the last slide. It tells the audience who to reach out to and puts a face to the name.
- **Use it for**: Final slide with consultant name, title, email, phone, and headshot
- **Keep it simple**: Name, role, email, phone. Don't clutter it with social media links or lengthy bios.
- **In team presentations**: If multiple consultants presented, consider one Contact Slide per person, or a single slide with names/emails and the primary contact's photo.

### Custom Layout (Layout 11) and Blank (Layout 12)
**The escape hatches.** Use these when no structured layout fits your content.
- **Custom Layout**: When you need a title but want full control over the body. Good for complex diagrams you're building from shapes, org charts, or multi-element infographics.
- **Blank**: When you need complete creative control. Good for full-bleed images, complex data visualizations, or slides where the template elements would just get in the way.
- **Use sparingly**: More than 2-3 custom/blank slides in a deck suggests the template doesn't fit the content, or the content needs restructuring. These layouts lose the visual consistency that makes a branded deck look polished.

## Image Strategy

When building slides that need images (especially the preferred bullet+image layouts), use this decision tree:

### 1. Generate with AI (preferred when possible)
Use the available image generation tools to create professional supporting visuals:
- **`z-image` skill**: Best for photorealistic, 16:9 presentation images. Optimized for professional photography styles. Use for conceptual/metaphorical images (e.g., "modern cloud infrastructure", "agile team collaboration", "digital transformation").
- **`nanobanana` skill**: Best when the image needs text rendered in it (infographics, labeled diagrams, process charts with text).
- **`gemini-image` skill**: General-purpose generation for anything else.

**Good candidates for AI generation:**
- Conceptual images that illustrate a theme (security = shield/lock imagery, speed = motion imagery)
- Professional "stock photo" style scenes (teams at whiteboards, server rooms, office environments)
- Simple process diagrams and flowcharts
- Technology concept art (cloud architecture, data pipelines, CI/CD)
- Abstract visuals for section dividers or background texture

**Always generate at 16:9 aspect ratio** for presentation slides. Request professional, clean, corporate-appropriate imagery that complements Improving's blue-teal brand palette when possible.

### 2. Leave labeled placeholders
For images that must come from the real world, insert a placeholder shape with a clear description of what's needed. Format: light gray rectangle with centered text describing the image.

**Must be placeholders:**
- Screenshots from the client's actual systems, dashboards, or tools
- Client-specific photos (their office, team, product, environment)
- Data visualizations / charts built from real client data
- Architecture diagrams that must precisely reflect the client's actual environment
- Photos from on-site assessments or observations

**Placeholder text format**: `[IMAGE: Description of what goes here]` -- e.g., `[IMAGE: Screenshot of client's current CI/CD pipeline in Jenkins]` or `[IMAGE: Client org chart showing reporting structure]`

### 3. Reuse existing Improving assets
The official templates already contain reusable branded images:
- World map with office locations
- Award badges and certifications
- Guiding Principles interconnected circles
- Stakeholder model diagram
- Service offerings category layout
- Company timeline infographic

These are embedded in the template slides. When building a deck that includes an "About Improving" section, clone those slides directly from the template rather than recreating them.

### Decision flow
```
Need an image for a slide?
  |
  ├─ Is it client-specific data/screenshots? → PLACEHOLDER
  ├─ Is it a standard Improving asset (logo, map, awards)? → REUSE FROM TEMPLATE
  ├─ Is it a conceptual/thematic image? → GENERATE WITH AI
  └─ Is it a precise technical diagram? → PLACEHOLDER (unless simple enough to generate)
```

## Recommended Presentation Structure

For a typical client engagement presentation:

| Slide # | Layout | Content |
|---------|--------|---------|
| 1 | **Principal Title** (cover) | Presentation title, client name, date |
| 2 | **Text Slide** | Agenda / Table of Contents |
| 3 | **Title Page** (section divider) | "About Improving" |
| 4-6 | **Text Slide** | Company overview, capabilities, relevant experience |
| 7 | **Title Page** (section divider) | "Current State Assessment" / main topic |
| 8-12 | **Text Slide** / **2 Text Boxes** / **Text Box Left/Right** | Findings, analysis, data |
| 13 | **Quote Slide** | Key client quote or critical finding |
| 14 | **Title Page** (section divider) | "Recommendations" |
| 15-17 | **Bullet Slide** / **Text Slide** | Recommendations with detail |
| 18 | **Title Page** (section divider) | "Next Steps" |
| 19 | **Text Slide** | Timeline, action items |
| 20 | **Contact Slide** | Presenter contact info |

## Font Usage in Presentations

| Element | Font | Weight | Size | Color |
|---------|------|--------|------|-------|
| Slide Title | Poppins | SemiBold/Bold | 29-32pt | `#005596` or theme default |
| Subtitle | Poppins | Medium | 18-20pt | Gray (50% luminance) |
| Body Text | Khula or Poppins | Regular | 12-14pt | `#58595A` (dark gray) |
| Stats / Big Numbers | Poppins | ExtraBold | 44pt | `#1E5690` |
| Stat Labels | Poppins | SemiBold | 28pt | `#1E5690` |
| Quote Text | Poppins | Bold Italic | 28pt | `#2297D5` |
| Attribution | Poppins | Regular | 18pt | `#4597D3` |
| Category Headers | Poppins | ExtraBold | 10pt | White on colored bg |
| Category Detail | Khula | Regular | 10pt | White on colored bg |
| Copyright | Khula | Bold | 9pt | White at 28% opacity |
| Location/Secondary | Poppins | Regular | 12pt | `#8D8D8D` |

## Service Category Colors

These specific colors are used when presenting Improving's service areas:

| Service | Color |
|---------|-------|
| Community | `#A4228E` (purple) |
| Training & Coaching | `#2297D5` (blue) |
| Consulting Services | `#FAA51A` (gold/orange) |
| Software Development | `#005696` (deep blue) |
| Outsourcing | `#27BCA2` (teal) |

## Guiding Principles Value Colors

| Value | Color |
|-------|-------|
| Excellence - Rise Above | `#F4BA41` (gold) |
| Involvement - Go Beyond | `#5BC1A6` (teal) |
| Dedication - Give Freely | `#005596` (deep blue) |
