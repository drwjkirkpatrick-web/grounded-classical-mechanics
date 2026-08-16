#!/usr/bin/env python3
"""make_quiz.py — build a printable quiz from a range of lessons.

Usage:
    python tools/make_quiz.py 45 52              # questions only (student sheet)
    python tools/make_quiz.py 45 52 --answers    # with answer keys (teacher sheet)
    python tools/make_quiz.py 45 52 --advanced   # advanced (14-17) questions instead

Pulls Pre-Test/Post-Test items (or Advanced Questions) from lesson files and
assembles one markdown document. Stdlib only.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAP = ROOT / "data" / "curriculum_map.json"


def extract(text, start_re, stop_re=r"\n## "):
    m = re.search(start_re + r"\n(.*?)(?=" + stop_re + r"|\Z)", text, re.S)
    return m.group(1).strip() if m else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("start", type=int, help="first lesson number")
    ap.add_argument("end", type=int, help="last lesson number")
    ap.add_argument("--answers", action="store_true", help="include answer keys")
    ap.add_argument("--advanced", action="store_true", help="use Advanced Questions")
    args = ap.parse_args()

    data = json.loads(MAP.read_text(encoding="utf-8"))
    lessons = [l for u in data["units"] for l in u["lessons"]
               if args.start <= l["n"] <= args.end]
    if not lessons:
        sys.exit(f"no lessons in range {args.start}..{args.end}")

    kind = "Advanced Questions (Ages 14–17)" if args.advanced else "Pre/Post Tests"
    out = [f"# Quiz — Lessons {args.start}–{args.end} ({kind})", ""]
    for l in lessons:
        path = ROOT / l["filename"]
        if not path.exists():
            print(f"warning: missing {l['filename']}", file=sys.stderr)
            continue
        text = path.read_text(encoding="utf-8")
        if args.advanced:
            block = extract(text, r"## Advanced Questions \(Ages 14[–-]17\)")
            # strip worked answers unless requested
            if not args.answers:
                block = re.sub(r"\n\s*\*\*Worked Answer:\*\*[^\n]*(\n(?!\d+\. \*\*Q:)[^\n]*)*", "", block)
        else:
            pre = extract(text, r"## Pre-Test")
            post = extract(text, r"## Post-Test")
            def strip_key(b):
                return re.split(r"\*\*Answer Key[^\n]*\*\*:?", b)[0].strip()
            def keys(b):
                m = re.search(r"(\*\*Answer Key[^\n]*\*\*:?.*)", b, re.S)
                return m.group(1).strip() if m else ""
            block = "**From the pre-tests:**\n\n" + strip_key(pre) + "\n\n**From the post-tests:**\n\n" + strip_key(post)
            if args.answers:
                block += "\n\n" + keys(pre) + "\n\n" + keys(post)
        out += [f"## Lesson {l['n']}: {l['title']}", "", block, ""]

    doc = "\n".join(out)
    print(doc)


if __name__ == "__main__":
    main()
