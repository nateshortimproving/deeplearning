#!/usr/bin/env python3
"""
Evaluation script for the trend-identification skill.

Reads each test case's trends.md output and applies:

DETERMINISTIC CHECKS (pure Python, no model call):
  1. topic_count_in_range   - numbered list contains 5-8 topics
  2. hashtags_per_topic     - each topic has 3-5 hashtags matching #Word format
  3. rationale_per_topic    - each topic has a "why trending" explanation
  4. platform_per_topic     - each topic names LinkedIn, X/Twitter, or Instagram
  5. source_citation_per_topic - each topic cites a real, named source
  6. content_hook_per_topic   - each topic includes a content angle / hook
  7. momentum_signal_per_topic - each topic quantifies trend momentum
  8. audience_segment_per_topic - each topic identifies a primary audience segment
  9. confidence_level_per_topic - each topic includes High/Medium/Low confidence

LLM JUDGE CHECK (qualitative EC from trend-identification-tests.md):
  10. llm_judge_quality      - a model grades the output against a rubric:
        a) every trend is specific to BOTH the subject and AI
        b) no two topics are the same thing reworded
        c) trends are plausibly current (last ~2 months)
        d) source citations name real, credible sources
        e) momentum signals are plausible and specific
        f) audience segments are concrete and relevant
      The script reads verdicts from judge_verdicts.json so the judge
      can be any model (or Devin acting as the judge). Run with
      --write-judge-prompts to generate the prompts file for a judge
      to fill in.

Usage:
  python3 eval_trends.py                          # run all checks
  python3 eval_trends.py --write-judge-prompts    # emit judge_prompts.md
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUTS_DIR = os.path.join(HERE, "..", "trend-identification-outputs")
VERDICTS_FILE = os.path.join(HERE, "judge_verdicts.json")
PROMPTS_FILE = os.path.join(HERE, "judge_prompts.md")

MIN_TOPICS, MAX_TOPICS = 5, 8
MIN_HASHTAGS, MAX_HASHTAGS = 3, 5

PLATFORM_LINE_RE = re.compile(r"(?im)^\s*-?\s*platform\s*:\s*(\S.*)$")
SOURCE_LINE_RE = re.compile(r"(?im)^\s*-?\s*source\s*:\s*(\S.*)$")
HOOK_LINE_RE = re.compile(r"(?im)^\s*-?\s*(?:content\s+)?(?:angle|hook)\s*:\s*(\S.*)$")
MOMENTUM_LINE_RE = re.compile(r"(?im)^\s*-?\s*momentum\s*:\s*(\S.*)$")
AUDIENCE_LINE_RE = re.compile(r"(?im)^\s*-?\s*audience\s*:\s*(\S.*)$")
CONFIDENCE_LINE_RE = re.compile(r"(?im)^\s*-?\s*confidence\s*:\s*(high|medium|low)\b.*$")

HASHTAG_RE = re.compile(r"#[A-Za-z0-9_]+")

# The rubric text sent to the LLM judge. Built directly from the most
# qualitative Expected Criteria in the hand-written test file.
JUDGE_RUBRIC = """You are grading output from a "trend identification" skill.

Subject under test: {subject}

Grade the trends.md content below against these criteria:
1. SUBJECT FIT: every trend must be specific to BOTH "{subject}" and AI.
2. NO DUPLICATES: no two topics may be the same thing reworded.
3. CURRENCY: each trend must be plausibly current (within ~2 months of today: {today}).
4. SOURCE QUALITY: each topic's "Source:" line names a real, credible, named source (publication, report, platform trend tool, or expert) — not a generic phrase like "social media" or "industry reports".
5. MOMENTUM PLAUSIBILITY: each topic's "Momentum:" line gives a specific, plausible quantitative or strong qualitative signal.
6. AUDIENCE RELEVANCE: each topic's "Audience:" line names a concrete, relevant segment for the trend.
7. CONFIDENCE JUSTIFICATION: each topic's "Confidence:" line states High/Medium/Low and gives a one-sentence justification tied to recency or evidence strength.

Respond with exactly this JSON on one line:
{{"pass": true/false, "subject_fit": true/false, "no_duplicates": true/false, "currency": true/false, "source_quality": true/false, "momentum_plausibility": true/false, "audience_relevance": true/false, "confidence_justification": true/false, "notes": "one sentence"}}

--- BEGIN trends.md ---
{content}
--- END trends.md ---
"""


def find_cases():
    cases = []
    for name in sorted(os.listdir(OUTPUTS_DIR)):
        path = os.path.join(OUTPUTS_DIR, name, "trends.md")
        if os.path.isfile(path):
            cases.append((name, path))
    return cases


def subject_of(case_name, content):
    """Derive the subject, e.g. 'test-3-ai-nfl' -> 'the NFL' (from the H1 if present)."""
    m = re.search(r"^#\s+Trending Topics:\s*AI in (.+)$", content, re.M)
    if m:
        return m.group(1).strip()
    return case_name.replace("test-", "").replace("-", " ")


def parse_topics(content):
    """Split the file into per-topic blocks keyed by the numbered item."""
    blocks = re.split(r"(?m)^\s*\d+\.\s", content)
    # blocks[0] is the header before item 1; the rest are topic bodies
    return blocks[1:]


def check_topic_count(topics):
    ok = MIN_TOPICS <= len(topics) <= MAX_TOPICS
    return ok, f"{len(topics)} topics (need {MIN_TOPICS}-{MAX_TOPICS})"


def check_hashtags(topics):
    bad = []
    for i, t in enumerate(topics, 1):
        # Count hashtags on the "Hashtags:" line so a #tag mentioned inside
        # the rationale prose doesn't inflate the count.
        line = next((l for l in t.splitlines() if "hashtag" in l.lower()), t)
        n = len(HASHTAG_RE.findall(line))
        if not (MIN_HASHTAGS <= n <= MAX_HASHTAGS):
            bad.append(f"topic {i} has {n}")
    return not bad, "; ".join(bad) if bad else f"all topics have {MIN_HASHTAGS}-{MAX_HASHTAGS} hashtags"


def check_rationale(topics):
    bad = [i for i, t in enumerate(topics, 1)
           if not re.search(r"why.{0,10}trend", t, re.I)]
    return not bad, ("missing rationale on topics " + ", ".join(map(str, bad))) if bad else "every topic has a why-trending line"


def check_platform(topics):
    # EC requires each topic to note its platform; any non-empty value counts.
    bad = [i for i, t in enumerate(topics, 1)
           if not PLATFORM_LINE_RE.search(t)]
    return not bad, ("missing platform on topics " + ", ".join(map(str, bad))) if bad else "every topic names a platform"


def check_source_citation(topics):
    bad = [i for i, t in enumerate(topics, 1)
           if not SOURCE_LINE_RE.search(t)]
    return not bad, ("missing source citation on topics " + ", ".join(map(str, bad))) if bad else "every topic cites a named source"


def check_content_hook(topics):
    bad = [i for i, t in enumerate(topics, 1)
           if not HOOK_LINE_RE.search(t)]
    return not bad, ("missing content hook on topics " + ", ".join(map(str, bad))) if bad else "every topic includes a content hook"


def check_momentum_signal(topics):
    bad = [i for i, t in enumerate(topics, 1)
           if not MOMENTUM_LINE_RE.search(t)]
    return not bad, ("missing momentum signal on topics " + ", ".join(map(str, bad))) if bad else "every topic quantifies momentum"


def check_audience_segment(topics):
    bad = [i for i, t in enumerate(topics, 1)
           if not AUDIENCE_LINE_RE.search(t)]
    return not bad, ("missing audience segment on topics " + ", ".join(map(str, bad))) if bad else "every topic identifies an audience segment"


def check_confidence_level(topics):
    bad = [i for i, t in enumerate(topics, 1)
           if not CONFIDENCE_LINE_RE.search(t)]
    return not bad, ("missing confidence level on topics " + ", ".join(map(str, bad))) if bad else "every topic states High/Medium/Low confidence"


def write_judge_prompts(cases):
    import datetime
    today = datetime.date.today().isoformat()
    with open(PROMPTS_FILE, "w") as f:
        for name, path in cases:
            content = open(path).read()
            f.write(f"## {name}\n\n")
            f.write(JUDGE_RUBRIC.format(subject=subject_of(name, content),
                                       today=today, content=content))
            f.write("\n\n")
    print(f"Wrote {PROMPTS_FILE}. Have a judge answer each section, then "
          f"save verdicts to judge_verdicts.json as:")
    print('  {"test-1-ai-ux-design": {"pass": true, "subject_fit": true, '
          '"no_duplicates": true, "currency": true, "source_quality": true, '
          '"momentum_plausibility": true, "audience_relevance": true, '
          '"confidence_justification": true, "notes": "..."}, ...}')


def run_llm_judge(case_name):
    """Look up this case's verdict in judge_verdicts.json."""
    if not os.path.isfile(VERDICTS_FILE):
        return None, "no judge_verdicts.json (run --write-judge-prompts first)"
    verdicts = json.load(open(VERDICTS_FILE))
    v = verdicts.get(case_name)
    if v is None:
        return None, "no verdict recorded for this case"
    return v["pass"], v.get("notes", "")


def evaluate(case_name, path):
    content = open(path).read()
    topics = parse_topics(content)

    checks = {
        "topic_count_in_range": check_topic_count(topics),
        "hashtags_per_topic": check_hashtags(topics),
        "rationale_per_topic": check_rationale(topics),
        "platform_per_topic": check_platform(topics),
        "source_citation_per_topic": check_source_citation(topics),
        "content_hook_per_topic": check_content_hook(topics),
        "momentum_signal_per_topic": check_momentum_signal(topics),
        "audience_segment_per_topic": check_audience_segment(topics),
        "confidence_level_per_topic": check_confidence_level(topics),
    }
    checks["llm_judge_quality"] = run_llm_judge(case_name)
    return checks


def main():
    cases = find_cases()
    if not cases:
        sys.exit(f"No cases found under {OUTPUTS_DIR}")

    if "--write-judge-prompts" in sys.argv:
        write_judge_prompts(cases)
        return

    results = {}
    for name, path in cases:
        checks = evaluate(name, path)
        passed = sum(1 for ok, _ in checks.values() if ok)
        skipped = sum(1 for ok, _ in checks.values() if ok is None)
        results[name] = checks
        print(f"\n=== {name} ===")
        for check, (ok, detail) in checks.items():
            mark = "SKIP" if ok is None else ("PASS" if ok else "FAIL")
            print(f"  [{mark}] {check}: {detail}")
        print(f"  -> {passed}/{len(checks)} checks passed"
              + (f" ({skipped} skipped)" if skipped else ""))

    n_pass = sum(1 for c in results.values() if all(ok for ok, _ in c.values()))
    print(f"\nSummary: {n_pass}/{len(results)} cases fully passed")

    out = os.path.join(HERE, "eval_results.json")
    with open(out, "w") as f:
        json.dump({k: {c: {"pass": ok, "detail": d} for c, (ok, d) in v.items()}
                   for k, v in results.items()}, f, indent=2)
    print(f"Machine-readable results written to {out}")


if __name__ == "__main__":
    main()
