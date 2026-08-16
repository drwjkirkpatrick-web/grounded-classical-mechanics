#!/usr/bin/env python3
"""build_map.py — validate unit data files and generate data/curriculum_map.json.

Usage:
    python tools/build_map.py            # validate + regenerate map
    python tools/build_map.py --check    # validate only (CI-friendly)

Each unit file in data/units/ contributes its lessons in order; global lesson
numbers 1..N are assigned across units in filename order.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UNITS_DIR = ROOT / "data" / "units"
OUT = ROOT / "data" / "curriculum_map.json"

REQUIRED_LESSON_KEYS = {"slug", "title", "focus", "cbe", "materials", "hands_on", "project", "advanced"}
VALID_CBE = {
    "G10-PHY-1.1", "G10-PHY-1.2", "G10-PHY-1.3", "G10-PHY-1.4", "G10-PHY-1.5",
    "G10-PHY-1.6", "G10-PHY-2.1", "G10-PHY-2.2", "G10-PHY-3.1", "G10-PHY-3.2",
    "G10-PHY-3.3", "G10-PHY-4.1", "G10-PHY-4.2", "JS-FE", "UP-FE",
}


def fail(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def main():
    check_only = "--check" in sys.argv
    unit_files = sorted(UNITS_DIR.glob("unit-*.json"))
    if not unit_files:
        fail(f"no unit files found in {UNITS_DIR}")

    units, all_slugs, errors = [], set(), []
    n_total = 0
    for uf in unit_files:
        data = json.loads(uf.read_text(encoding="utf-8"))
        uslug = data.get("slug", uf.stem)
        lessons = data.get("lessons", [])
        for i, les in enumerate(lessons, 1):
            missing = REQUIRED_LESSON_KEYS - set(les)
            if missing:
                errors.append(f"{uf.name} lesson {i} ({les.get('slug','?')}): missing {missing}")
            bad_cbe = [c for c in les.get("cbe", []) if c not in VALID_CBE]
            if bad_cbe:
                errors.append(f"{uf.name} lesson {i} ({les['slug']}): unknown CBE codes {bad_cbe}")
            if les["slug"] in all_slugs:
                errors.append(f"{uf.name} lesson {i}: duplicate slug {les['slug']}")
            all_slugs.add(les["slug"])
        units.append(data)
        n_total += len(lessons)

    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    # Assign global lesson numbers
    n = 0
    for data in units:
        for les in data["lessons"]:
            n += 1
            les["n"] = n
            les["unit_slug"] = data["slug"]
            les["unit_title"] = data["title"]
            les["unit"] = data["unit"]
            les["filename"] = f"lessons/unit-{data['unit']:02d}-{data['slug']}/lesson-{n:03d}-{les['slug']}.md"

    if n_total != 365:
        fail(f"expected 365 lessons, found {n_total}")

    if not check_only:
        OUT.write_text(json.dumps({"total": n_total, "units": units}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"wrote {OUT} with {n_total} lessons across {len(units)} units")
    else:
        print(f"OK: {n_total} lessons across {len(units)} units (validation only)")

    for data in units:
        first = data["lessons"][0]["n"]
        last = data["lessons"][-1]["n"]
        print(f"  unit {data['unit']:02d} {data['title']:<38} lessons {first:>3}-{last:<3} ({len(data['lessons'])})")


if __name__ == "__main__":
    main()
