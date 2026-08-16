#!/usr/bin/env python3
"""coverage.py — CBE coverage matrix: which standards each unit/lesson serves.

Usage:
    python tools/coverage.py            # print matrix + write docs/CBE_COVERAGE.md
    python tools/coverage.py --check    # exit 1 if any CBE code has < 5 lessons
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAP = ROOT / "data" / "curriculum_map.json"
OUT = ROOT / "docs" / "CBE_COVERAGE.md"

CBE_NAMES = {
    "G10-PHY-1.1": "Introduction to Physics (Senior School G10)",
    "G10-PHY-1.2": "Pressure (Senior School G10)",
    "G10-PHY-1.3": "Mechanical Properties of Materials (Senior School G10)",
    "G10-PHY-1.4": "Temperature and Thermal Expansion (Senior School G10)",
    "G10-PHY-1.5": "Moments and Equilibrium (Senior School G10)",
    "G10-PHY-1.6": "Energy, Work, Power and Machines (Senior School G10)",
    "G10-PHY-2.1": "Properties of Waves (Senior School G10)",
    "G10-PHY-4.1": "Greenhouse Effect and Climate Change (Senior School G10)",
    "G10-PHY-4.2": "Introduction to Space Physics (Senior School G10)",
    "JS-FE": "Junior School Integrated Science — Force & Energy (G7–9)",
    "UP-FE": "Upper Primary Science & Technology — Force & Energy (G4–6)",
}
MIN_LESSONS_PER_CODE = 5
# Bridge-only codes: touched where they meet mechanics (altitude boiling, hot-air
# lift, satellites) but owned by the companion volume. Exempt from the minimum.
BRIDGE_ONLY = {"G10-PHY-1.4", "G10-PHY-4.2"}


def main():
    data = json.loads(MAP.read_text(encoding="utf-8"))
    by_code = defaultdict(list)
    for u in data["units"]:
        for les in u["lessons"]:
            for code in les["cbe"]:
                by_code[code].append(les["n"])

    lines = [
        "# CBE Coverage Matrix",
        "",
        "How the 365 lessons of Grounded Classical Mechanics map to Kenya's Competency",
        "Based Education (CBE) curriculum designs (KICD). Senior School references are the",
        "Grade 10 Physics Curriculum Design (KICD, 2025); Junior School and Upper Primary",
        "references are the Integrated Science and Science & Technology designs (Force &",
        "Energy strands).",
        "",
        "> **Scope note.** This course is the *mechanics spine* of CBE physics. Strand 1.0",
        "> (Mechanics and Thermal Physics), wave motion under 2.1, and the energy/climate",
        "> outcomes of 4.1 are covered directly through daily hands-on lessons. Electricity",
        "> & Magnetism (3.x), Optics, Radioactivity (2.2) and Thermal Physics (1.4) are",
        "> touched only where they meet mechanics (altitude boiling, hot-air buoyancy,",
        "> dynamo teaser) and are flagged for the companion volume.",
        "",
        "| CBE code | Strand / sub-strand | Lessons | Count |",
        "|---|---|---|---|",
    ]
    weak = []
    for code in sorted(CBE_NAMES, key=lambda c: (c not in by_code, c)):
        nums = sorted(by_code.get(code, []))
        if code not in by_code:
            weak.append(code)
        show = ", ".join(str(n) for n in nums)
        if len(show) > 160:
            show = show[:157] + "…"
        lines.append(f"| `{code}` | {CBE_NAMES[code]} | {show} | {len(nums)} |")
    lines += [
        "",
        "## Reading the matrix",
        "",
        "- Every lesson carries at least one code; most carry two (a senior-school anchor",
        "  plus the junior/primary strand it consolidates).",
        "- `JS-FE` and `UP-FE` appear throughout by design: the course spirals, revisiting",
        "  junior concepts with senior-school mathematics in the Advanced Questions.",
        "- Generate this file: `python tools/coverage.py` (do not edit by hand).",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT}")
    for code in sorted(CBE_NAMES):
        print(f"  {code:<12} {len(by_code.get(code, [])):>3} lessons  {CBE_NAMES[code]}")

    if "--check" in sys.argv:
        thin = [c for c in CBE_NAMES
                if c not in BRIDGE_ONLY and len(by_code.get(c, [])) < MIN_LESSONS_PER_CODE]
        if thin:
            print(f"WEAK COVERAGE (<{MIN_LESSONS_PER_CODE} lessons): {thin}", file=sys.stderr)
            sys.exit(1)
        print("coverage check OK")


if __name__ == "__main__":
    main()
