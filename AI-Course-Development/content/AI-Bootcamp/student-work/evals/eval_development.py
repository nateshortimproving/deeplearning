#!/usr/bin/env python3
"""
Evaluation script for the development skill.

Reads each test case's post.md output and applies the EC from
development-tests.md:

DETERMINISTIC CHECKS (pure Python, no model call):
  1. length_in_range        - platform-appropriate length:
                               LinkedIn 100-300 words, X <=280 chars,
                               Instagram 50-125 words
  2. hashtag_count_in_range - platform-appropriate count in #format:
                               LinkedIn 3-5, X 1-2, Instagram 5-10
  3. cta_present            - post ends with a clear call to action
                               (CTA marker in the last non-hashtag lines)
  4. imagery_when_appropriate - Instagram posts include a visual cue
                               (image/carousel/reel suggestion); other
                               platforms auto-pass

LLM JUDGE CHECK (qualitative EC from development-tests.md):
  5. llm_judge_quality      - a model grades the output against a rubric:
        a) tone sounds human, not salesy or obviously AI-generated
        b) first line hooks into the trend
        c) post is self-contained (no unseen trend context needed)
        d) CTA is appropriate for the platform
      The script reads verdicts from judge_verdicts_dev.json so the judge
      can be any model (or Devin acting as the judge). Run with
      --write-judge-prompts to generate the prompts file for a judge
      to fill in.

Usage:
  python3 eval_development.py                          # run all checks
  python3 eval_development.py --write-judge-prompts    # emit judge_prompts_dev.md
"""

import json
import os
import re
import sys
import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUTS_DIR = os.path.join(HERE, "..", "development-outputs")
VERDICTS_FILE = os.path.join(HERE, "judge_verdicts_dev.json")
PROMPTS_FILE = os.path.join(HERE, "judge_prompts_dev.md")

HASHTAG_RE = re.compile(r"#[A-Za-z0-9_]+")

# Platform rules encoded from the EC. "length" is words for LinkedIn and
# Instagram, characters for X.
PLATFORMS = {
    "linkedin":  {"min_len": 100, "max_len": 300, "unit": "words",
                  "min_tags": 3, "max_tags": 5,  "imagery_required": False},
    "x":         {"min_len": 1,   "max_len": 280, "unit": "chars",
                  "min_tags": 1, "max_tags": 2,  "imagery_required": False},
    "instagram": {"min_len": 50,  "max_len": 125, "unit": "words",
                  "min_tags": 5, "max_tags": 10, "imagery_required": True},
}

# CTA markers: phrases that signal a call to action. EC requires the post to
# END with a CTA, so only the tail of the post is scanned.
CTA_RE = re.compile(
    r"comment|reply|retweet|\bRT\b|share|tag someone|tag a friend|save this|"
    r"link in bio|follow|connect|join|tell me|what do you think|your take|"
    r"your thoughts|let me know|drop a|sound off|have you tried|try it|"
    r"check it out|give it a try|let's hear|share your|below\b",
    re.I,
)

IMAGERY_RE = re.compile(
    r"\b(image|photo|picture|carousel|reel|graphic|visual|infographic|"
    r"video|screenshot|illustration)\b",
    re.I,
)

JUDGE_RUBRIC = """You are grading output from a "development" skill that turns a trend
into a social media post.

Platform under test: {platform}
Input prompt: {input_prompt}

Grade the post.md content below against these criteria:
1. TONE: the post sounds human and platform-native — not like a salesman,
   not obviously AI-generated (no "game-changer", "in today's fast-paced
   world", em-dash abuse, or hype stacking).
2. HOOK: the first line hooks into the trend — a reader immediately knows
   what this post is about.
3. SELF-CONTAINED: the post stands alone — someone who never saw the
   underlying trend entry understands the angle.
4. CTA FIT: the post ends with a call to action that is appropriate for
   {platform} (e.g., question/comment on LinkedIn, reply on X,
   save/tag/link-in-bio on Instagram).
5. ON-TOPIC: the post is clearly about the trend named in the input prompt.

Respond with exactly this JSON on one line:
{{"pass": true/false, "tone": true/false, "hook": true/false, "self_contained": true/false, "cta_fit": true/false, "on_topic": true/false, "notes": "one sentence"}}

--- BEGIN post.md ---
{content}
--- END post.md ---
"""

# Inputs mirror development-tests.md so judge prompts can show them.
TEST_INPUTS = {
    "test-1-linkedin-ux":          "Write a LinkedIn post based on this trend: AI co-pilots for UX design",
    "test-2-x-minecraft":          "Write an X/Twitter post based on this trend: AI use in Minecraft",
    "test-3-instagram-meal-planning": "Write an Instagram post based on this trend: AI-powered personalized meal planning",
    "test-4-linkedin-nfl":         "Write a LinkedIn post based on this trend: AI-powered player performance analytics in the NFL",
    "test-5-x-minecraft-npcs":     "Write an X/Twitter post based on this trend: AI NPC companions in Minecraft servers",
}


def platform_of(case_name):
    if "linkedin" in case_name:
        return "linkedin"
    if "instagram" in case_name:
        return "instagram"
    return "x"


def find_cases():
    cases = []
    for name in sorted(os.listdir(OUTPUTS_DIR)):
        path = os.path.join(OUTPUTS_DIR, name, "post.md")
        if os.path.isfile(path):
            cases.append((name, path))
    return cases


def body_without_hashtag_runs(content):
    """Return post text with pure hashtag lines removed (for length checks)."""
    lines = []
    for line in content.splitlines():
        tokens = line.split()
        if tokens and all(t.startswith("#") for t in tokens):
            continue
        lines.append(line)
    return "\n".join(lines)


def check_length(content, rules):
    body = body_without_hashtag_runs(content)
    if rules["unit"] == "chars":
        n = len(body.strip())
    else:
        n = len(body.split())
    ok = rules["min_len"] <= n <= rules["max_len"]
    return ok, f"{n} {rules['unit']} (need {rules['min_len']}-{rules['max_len']})"


def check_hashtag_count(content, rules):
    tags = HASHTAG_RE.findall(content)
    n = len(tags)
    ok = rules["min_tags"] <= n <= rules["max_tags"]
    return ok, f"{n} hashtags (need {rules['min_tags']}-{rules['max_tags']})"


def check_cta(content):
    # Scan the last 3 non-empty lines — EC requires the post to END with a CTA.
    tail = [l for l in content.splitlines() if l.strip()][-3:]
    joined = "\n".join(tail)
    ok = bool(CTA_RE.search(joined))
    return ok, "CTA marker found in closing lines" if ok else "no CTA marker in last 3 lines"


def check_imagery(content, rules):
    if not rules["imagery_required"]:
        return True, "imagery not required on this platform"
    ok = bool(IMAGERY_RE.search(content))
    return ok, ("visual cue present" if ok
                else "Instagram post suggests no visual (image/carousel/reel)")


def write_judge_prompts(cases):
    today = datetime.date.today().isoformat()
    with open(PROMPTS_FILE, "w") as f:
        for name, path in cases:
            content = open(path).read()
            f.write(f"## {name}\n\n")
            f.write(JUDGE_RUBRIC.format(
                platform=platform_of(name),
                input_prompt=TEST_INPUTS.get(name, "(see test file)"),
                today=today, content=content))
            f.write("\n\n")
    print(f"Wrote {PROMPTS_FILE}. Have a judge answer each section, then "
          f"save verdicts to judge_verdicts_dev.json as:")
    print('  {"test-1-linkedin-ux": {"pass": true, "tone": true, '
          '"hook": true, "self_contained": true, "cta_fit": true, '
          '"on_topic": true, "notes": "..."}, ...}')


def run_llm_judge(case_name):
    if not os.path.isfile(VERDICTS_FILE):
        return None, "no judge_verdicts_dev.json (run --write-judge-prompts first)"
    verdicts = json.load(open(VERDICTS_FILE))
    v = verdicts.get(case_name)
    if v is None:
        return None, "no verdict recorded for this case"
    return v["pass"], v.get("notes", "")


def evaluate(case_name, path):
    content = open(path).read()
    rules = PLATFORMS[platform_of(case_name)]
    checks = {
        "length_in_range": check_length(content, rules),
        "hashtag_count_in_range": check_hashtag_count(content, rules),
        "cta_present": check_cta(content),
        "imagery_when_appropriate": check_imagery(content, rules),
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

    out = os.path.join(HERE, "eval_results_dev.json")
    with open(out, "w") as f:
        json.dump({k: {c: {"pass": ok, "detail": d} for c, (ok, d) in v.items()}
                   for k, v in results.items()}, f, indent=2)
    print(f"Machine-readable results written to {out}")


if __name__ == "__main__":
    main()
