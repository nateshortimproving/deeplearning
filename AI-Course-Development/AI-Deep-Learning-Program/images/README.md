# Images Directory

This directory contains SVG diagrams generated from Mermaid source for the DLP curriculum.

## Standard

All workflow and pipeline diagrams in the DLP are:

1. **Authored as Mermaid** — the source of truth is the `.mmd` file in this directory
2. **Exported as SVG** — the rendered SVG lives alongside the `.mmd` file
3. **Referenced in docs** — markdown files reference the SVG using relative paths: `![Pipeline](../images/sdlc-pipeline.svg)`

## Why Mermaid → SVG?

- Mermaid is text-based, so diagrams are diffable and versionable
- SVGs render cleanly in GitHub, IDEs, and most markdown viewers
- No binary artifacts to manage — the SVG is XML, also diffable
- Changes to diagrams follow the same review workflow as code

## How to Regenerate

If you have the Mermaid CLI (`mmdc`) installed:

```bash
npx @mermaid-js/mermaid-cli -i images/sdlc-pipeline.mmd -o images/sdlc-pipeline.svg
```

Or use the Mermaid Live Editor (https://mermaid.live) — paste the `.mmd` content and export as SVG.

## Files

| File | Description | Use In |
|------|-------------|--------|
| `sdlc-pipeline.mmd` / `.svg` | Full pipeline showing structured YAML data flow, Loop 1/Loop 2 phases, evaluation/adversarial/harness layers | @Overview.md, EE curriculum @Overview — internal/trainer reference |
| `sdlc-pipeline-simple.mmd` / `.svg` | Simplified student-facing flow: PRD/Architecture/UX → epics-and-stories → plan-story → implement-story → review-implementation → (next story) | Session slides, student handouts, deck prompts |