#!/usr/bin/env python3
"""Generate AI Bootcamp branded PDFs using improving-pdf CLI."""
import re
import os
import subprocess
import tempfile
from pathlib import Path

BOOTCAMP_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BOOTCAMP_DIR / "PDFs"

WEEK_DAYS = {
    1: [
        ("Monday",    "EDD-Prompt-Harness-Model-and-RTCC"),
        ("Tuesday",   "Trend-Identification-Skill"),
        ("Wednesday", "Ideation-Skill"),
        ("Thursday",  "Development-Skill"),
        ("Friday",    "Graphics-Skill-and-Pipeline"),
    ],
    2: [
        ("Monday",    "Pipeline-Orientation-and-Baseline-Run"),
        ("Tuesday",   "Create-PRD-Full-EDD-Iteration"),
        ("Wednesday", "Create-Architecture-and-Create-UX"),
        ("Thursday",  "Create-Epics-Stories-and-Plan-Story"),
        ("Friday",    "Implement-Review-and-Week-Synthesis"),
    ],
    3: [
        ("Monday",    "Spectrum-and-Invocation-Decision"),
        ("Tuesday",   "Enabling-Model-Invocation"),
        ("Wednesday", "Adversarial-Agents"),
        ("Thursday",  "Bounded-Agents"),
        ("Friday",    "Synthesis-and-Artifacts-Review"),
    ],
    4: [
        ("Monday",    "Player-Coach-Model"),
        ("Tuesday",   "Resistance-Scenarios"),
        ("Wednesday", "DLP-Operating-Model-and-Artifact-Handoff"),
        ("Thursday",  "Rehearsal-Engagement"),
        ("Friday",    "Certification-Gate"),
    ],
}


def strip_instructor_content(content: str) -> str:
    """Remove all instructor-facing content from a markdown document."""
    # 1. Remove Coaching Notes section and everything after it
    content = re.sub(
        r'\n---\n\n## Coaching Notes.*$',
        '',
        content,
        flags=re.DOTALL,
    )
    content = re.sub(
        r'\n## Coaching Notes.*$',
        '',
        content,
        flags=re.DOTALL,
    )

    # 2. Remove "Key insight to surface:" blocks (bold label + rest of paragraph)
    content = re.sub(
        r'\*\*Key insight to surface:\*\*[^\n]*(?:\n(?!\n)[^\n]*)?\n',
        '',
        content,
    )

    # 3. Remove "Debrief focus:" blocks
    content = re.sub(
        r'\*\*Debrief focus:\*\*[^\n]*(?:\n(?!\n)[^\n]*)?\n',
        '',
        content,
    )

    # 4. Remove sentences where instructor demonstrates
    content = re.sub(
        r'The instructor demonstrates[^.]*\.\s*',
        '',
        content,
    )

    # 5. Fix instructor-provision language for students
    content = content.replace(
        'are provided by the instructor. Participants are not expected to invent them.',
        'will be provided to you.',
    )

    return content.strip()


def extract_intro(content: str) -> str:
    """Return everything before the first day heading."""
    match = re.search(r'\n## (?:Monday|Tuesday|Wednesday|Thursday|Friday)\b', content)
    if match:
        return content[: match.start()].strip()
    return content


def extract_objectives(intro: str) -> str:
    """Pull just the Objectives block from the intro."""
    match = re.search(
        r'(## Objectives.*?)(?=\n## |\Z)',
        intro,
        re.DOTALL,
    )
    return match.group(1).strip() if match else ''


def extract_day_section(content: str, day_name: str) -> str:
    """Extract a named day's section."""
    pattern = (
        rf'(## {day_name}\b.*?)'
        r'(?=\n## (?:Monday|Tuesday|Wednesday|Thursday|Friday|Week \d|Coaching)|\Z)'
    )
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1).strip() if match else ''


def extract_deliverables(content: str) -> str:
    """Extract the week deliverables checklist section."""
    match = re.search(
        r'(## Week \d+ Deliverables.*?)(?=\n## |\Z)',
        content,
        re.DOTALL,
    )
    return match.group(1).strip() if match else ''


def run_improving_pdf(markdown_content: str, output_pdf: Path):
    """Write markdown to a temp file and invoke improving-pdf."""
    with tempfile.NamedTemporaryFile(
        mode='w', suffix='.md', delete=False, dir='/tmp', encoding='utf-8'
    ) as f:
        f.write(markdown_content)
        temp_path = f.name

    try:
        result = subprocess.run(
            ['improving-pdf', temp_path, '-o', str(output_pdf)],
            capture_output=True,
            text=True,
            timeout=180,
        )
        if result.returncode != 0:
            print(f'  ERROR {output_pdf.name}:\n    {result.stderr[:300]}')
        else:
            print(f'  ✓  {output_pdf.relative_to(OUTPUT_DIR)}')
    except subprocess.TimeoutExpired:
        print(f'  TIMEOUT {output_pdf.name}')
    finally:
        os.unlink(temp_path)


# ── Create output directory structure ────────────────────────────────────────
OUTPUT_DIR.mkdir(exist_ok=True)
for wk in range(1, 5):
    (OUTPUT_DIR / f'Week-{wk}').mkdir(exist_ok=True)
    (OUTPUT_DIR / f'Week-{wk}' / 'Exercises').mkdir(exist_ok=True)


# ── Full PDFs for every source MD file ───────────────────────────────────────
print('=== Full Branded PDFs ===')

overview_md = (BOOTCAMP_DIR / '@Overview.md').read_text(encoding='utf-8')
run_improving_pdf(overview_md, OUTPUT_DIR / 'Overview.pdf')

for wk in range(1, 5):
    raw = (BOOTCAMP_DIR / f'Week-{wk}.md').read_text(encoding='utf-8')
    run_improving_pdf(raw, OUTPUT_DIR / f'Week-{wk}' / f'Week-{wk}.pdf')


# ── Student exercise PDFs (one per day, no instructor content) ────────────────
print('\n=== Student Exercise PDFs ===')

for wk in range(1, 5):
    raw = (BOOTCAMP_DIR / f'Week-{wk}.md').read_text(encoding='utf-8')
    student = strip_instructor_content(raw)

    intro = extract_intro(student)
    objectives = extract_objectives(intro)
    deliverables = extract_deliverables(student)

    # Extract week title from first H1
    title_match = re.match(r'# (.+)', intro)
    week_title = title_match.group(1) if title_match else f'AI Bootcamp — Week {wk}'

    # Extract timing block for context
    timing_match = re.search(r'(## Timing.*?)(?=\n## )', intro + '\n## ', re.DOTALL)
    timing_section = timing_match.group(1).strip() if timing_match else ''

    days = WEEK_DAYS[wk]
    for idx, (day_name, slug) in enumerate(days):
        day_section = extract_day_section(student, day_name)
        if not day_section:
            print(f'  WARN: no section for {day_name} in Week {wk}')
            continue

        is_last_day = idx == len(days) - 1

        parts = [
            f'# {week_title}',
            f'*{day_name} — Student Exercise Guide*',
            '---',
        ]
        if objectives:
            parts.append(objectives)
            parts.append('---')
        if timing_section:
            parts.append(timing_section)
            parts.append('---')
        parts.append(day_section)
        if is_last_day and deliverables:
            parts.append('---')
            parts.append(deliverables)

        exercise_md = '\n\n'.join(parts)
        out_path = (
            OUTPUT_DIR
            / f'Week-{wk}'
            / 'Exercises'
            / f'Week-{wk}-Day-{idx + 1}-{slug}.pdf'
        )
        run_improving_pdf(exercise_md, out_path)

print(f'\n=== Complete. Output: {OUTPUT_DIR} ===')
