#!/usr/bin/env python3
"""build_index.py — generate CURRICULUM_MAP.md from data/curriculum_map.json.

The generated file is committed to the repo; regenerate after any data change:
    python tools/build_index.py
"""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAP = ROOT / "data" / "curriculum_map.json"
OUT = ROOT / "CURRICULUM_MAP.md"


def main():
    data = json.loads(MAP.read_text(encoding="utf-8"))
    lines = [
        "# Curriculum Map — 365 Lessons",
        "",
        "One lesson per day for a full year. Each lesson is a self-contained 45-minute plan",
        "with pre-test, post-test, advanced questions (ages 14–17) and — where the concept",
        "allows — a hands-on build with parts list and workflow.",
        "",
        "**Generated file — edit `data/units/*.json` instead, then run `tools/build_index.py`.**",
        "",
    ]
    total_hands_on = 0
    for u in data["units"]:
        first, last = u["lessons"][0]["n"], u["lessons"][-1]["n"]
        ho = sum(1 for l in u["lessons"] if l["hands_on"])
        total_hands_on += ho
        lines += [
            f"## Unit {u['unit']:02d}: {u['title']} — lessons {first}–{last}",
            "",
            f"*{u['intro']}*",
            "",
            f"{len(u['lessons'])} lessons · {ho} hands-on · CBE: {', '.join('`%s`' % c for c in u['cbe_strands'])}",
            "",
            "| # | Lesson | Hands-on | Project |",
            "|---|---|---|---|",
        ]
        for l in u["lessons"]:
            lines.append(
                f"| {l['n']} | [{l['title']}]({l['filename']}) | {'🔧' if l['hands_on'] else ''} | {l['project'] or ''} |"
            )
        lines.append("")
    projects = Counter(l["project"] for u in data["units"] for l in u["lessons"] if l["project"])
    lines += [
        "## Project Threads",
        "",
        "Lessons sharing a project tag build one artifact across multiple days:",
        "",
        "| Project | Lessons |",
        "|---|---|",
    ]
    for slug, count in sorted(projects.items(), key=lambda kv: -kv[1]):
        lines.append(f"| `{slug}` | {count} |")
    lines += [
        "",
        f"**Totals:** {data['total']} lessons · {total_hands_on} hands-on · {len(projects)} project threads",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT} ({data['total']} lessons, {total_hands_on} hands-on, {len(projects)} projects)")


if __name__ == "__main__":
    main()
