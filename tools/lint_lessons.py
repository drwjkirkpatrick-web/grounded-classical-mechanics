#!/usr/bin/env python3
"""lint_lessons.py — structural validation for Grounded Classical Mechanics lessons.

Usage:
    python tools/lint_lessons.py --all                 # all 365 lessons vs the map
    python tools/lint_lessons.py --unit 7              # one unit
    python tools/lint_lessons.py --files <paths...>    # specific files
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAP = ROOT / "data" / "curriculum_map.json"

REQUIRED_SECTIONS = [
    r"## Learning Outcomes",
    r"## Materials",
    r"## Vocabulary",
    r"## Pre-Test",
    r"## Lesson Flow \(45 Minutes\)",
    r"## Post-Test",
    r"## Advanced Questions \(Ages 14[–-]17\)",
    r"## Safety Notes",
    r"## Teacher Notes",
]
VALID_CBE = {
    "G10-PHY-1.1", "G10-PHY-1.2", "G10-PHY-1.3", "G10-PHY-1.4", "G10-PHY-1.5",
    "G10-PHY-1.6", "G10-PHY-2.1", "G10-PHY-2.2", "G10-PHY-3.1", "G10-PHY-3.2",
    "G10-PHY-3.3", "G10-PHY-4.1", "G10-PHY-4.2", "JS-FE", "UP-FE",
}
MIN_WORDS = 350


def section(text, header_regex, following):
    """Extract text between a section header and the next '## ' header."""
    m = re.search(header_regex + r".*?\n(.*?)(?=\n## |\Z)", text, re.S)
    return m.group(1) if m else ""


def numbered_items(block):
    return len(re.findall(r"^\d+\.\s", block, re.M))


def lint_file(path, entry, errors):
    text = path.read_text(encoding="utf-8")
    words = len(re.findall(r"\S+", text))

    h1 = re.search(r"^# Lesson (\d+): (.+)$", text, re.M)
    if not h1:
        errors.append("missing or malformed H1 '# Lesson NNN: Title'")
    else:
        if int(h1.group(1)) != entry["n"]:
            errors.append(f"H1 number {h1.group(1)} != map number {entry['n']}")
        if h1.group(2).strip() != entry["title"].strip():
            errors.append(f"H1 title '{h1.group(2).strip()}' != map title '{entry['title'].strip()}'")

    for sec_re in REQUIRED_SECTIONS:
        if not re.search(r"^" + sec_re, text, re.M):
            errors.append(f"missing section: {sec_re}")

    # CBE alignment line with valid codes
    cbe_line = re.search(r"\*\*CBE Alignment:\*\*(.+)", text)
    if not cbe_line:
        errors.append("missing **CBE Alignment:** line")
    else:
        codes = [c for c in VALID_CBE if c in cbe_line.group(1)]
        if not codes:
            errors.append("CBE Alignment line has no valid codes")

    # Lesson flow timings sum to 45
    flow = section(text, r"## Lesson Flow \(45 Minutes\)", None)
    if flow:
        times = [int(x) for x in re.findall(r"\((\d+)\s*min\)", flow)]
        if not times:
            errors.append("Lesson Flow has no (N min) timings")
        elif sum(times) != 45:
            errors.append(f"Lesson Flow timings sum to {sum(times)}, expected 45 (found {times})")

    # Pre-test
    pre = section(text, r"## Pre-Test", None)
    if pre:
        if numbered_items(pre.split("**Answer Key")[0]) < 3:
            errors.append("Pre-Test has fewer than 3 numbered questions")
        if "**Answer Key (Pre-Test):**" not in pre:
            errors.append("Pre-Test missing '**Answer Key (Pre-Test):**'")

    # Post-test
    post = section(text, r"## Post-Test", None)
    if post:
        if numbered_items(post.split("**Answer Key")[0]) < 4:
            errors.append("Post-Test has fewer than 4 numbered questions")
        if "**Answer Key (Post-Test):**" not in post:
            errors.append("Post-Test missing '**Answer Key (Post-Test):**'")

    # Advanced questions
    adv = section(text, r"## Advanced Questions \(Ages 14[–-]17\)", None)
    if adv:
        n_q = len(re.findall(r"\*\*Q:\*\*", adv))
        n_a = len(re.findall(r"\*\*Worked Answer:\*\*", adv))
        if n_q < 2:
            errors.append(f"Advanced Questions has {n_q} questions, need >= 2")
        if n_a < n_q:
            errors.append(f"Advanced Questions has {n_a} worked answers for {n_q} questions")

    # Hands-on build section presence
    has_build = bool(re.search(r"^## Hands-On Build", text, re.M))
    if entry["hands_on"] and not has_build:
        errors.append("map says hands_on=true but no '## Hands-On Build' section")
    if not entry["hands_on"] and has_build:
        errors.append("map says hands_on=false but file has '## Hands-On Build' section")
    if has_build:
        for sub in ("### Parts", "### Workflow", "### Common Mistakes"):
            if sub not in text:
                errors.append(f"Hands-On Build missing '{sub}'")

    if words < MIN_WORDS:
        errors.append(f"too short: {words} words < {MIN_WORDS}")

    return errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--unit", type=int)
    ap.add_argument("--files", nargs="*")
    args = ap.parse_args()

    data = json.loads(MAP.read_text(encoding="utf-8"))
    entries = [les for u in data["units"] for les in u["lessons"]]

    targets = []
    if args.files:
        by_file = {e["filename"]: e for e in entries}
        for f in args.files:
            rel = str(Path(f).resolve().relative_to(ROOT)) if Path(f).is_absolute() else str(f)
            if rel not in by_file:
                print(f"ERROR: {rel} not in curriculum map", file=sys.stderr)
                sys.exit(2)
            targets.append((ROOT / rel, by_file[rel]))
    else:
        for e in entries:
            if args.unit and e["unit"] != args.unit:
                continue
            targets.append((ROOT / e["filename"], e))

    n_fail_files = 0
    missing = 0
    for path, entry in targets:
        if not path.exists():
            print(f"MISSING: {entry['filename']}")
            missing += 1
            n_fail_files += 1
            continue
        errors = []
        lint_file(path, entry, errors)
        if errors:
            n_fail_files += 1
            print(f"FAIL: {entry['filename']}")
            for e in errors:
                print(f"   - {e}")

    n_ok = len(targets) - n_fail_files
    print(f"\n{n_ok}/{len(targets)} files pass" + (f", {missing} missing" if missing else ""))
    sys.exit(1 if n_fail_files else 0)


if __name__ == "__main__":
    main()
