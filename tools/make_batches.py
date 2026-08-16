#!/usr/bin/env python3
"""make_batches.py — split the curriculum map into subagent batch files.

Writes data/batches/batch-NN.json (one per work package) and prints the wave
plan. Lesson 051 is already written by hand (gold standard) and is excluded.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAP = ROOT / "data" / "curriculum_map.json"
OUT = ROOT / "data" / "batches"
DONE = {51}  # lesson numbers already complete

# batch sizes per unit (unit -> list of batch sizes)
PLAN = {
    1: [13, 13], 2: [13, 12], 3: [13, 13], 4: [10, 10], 5: [13, 13],
    6: [11, 11, 10], 7: [10, 9, 9], 8: [11, 11], 9: [9, 9], 10: [9, 9],
    11: [9, 9], 12: [8, 8], 13: [12, 12], 14: [10, 10, 8], 15: [10, 10],
    16: [8, 9],
}


def main():
    data = json.loads(MAP.read_text(encoding="utf-8"))
    OUT.mkdir(parents=True, exist_ok=True)
    batches = []
    for unit in data["units"]:
        lessons = [l for l in unit["lessons"] if l["n"] not in DONE]
        sizes = PLAN[unit["unit"]]
        assert sum(sizes) == len(lessons), f"unit {unit['unit']}: plan {sum(sizes)} != lessons {len(lessons)}"
        i = 0
        for size in sizes:
            batches.append(lessons[i:i + size])
            i += size

    index = []
    for bi, batch in enumerate(batches, 1):
        path = OUT / f"batch-{bi:02d}.json"
        payload = {
            "batch": bi,
            "unit": batch[0]["unit"],
            "unit_title": batch[0]["unit_title"],
            "unit_slug": batch[0]["unit_slug"],
            "n_lessons": len(batch),
            "lessons": batch,
        }
        path.write_text(json.dumps(payload, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        index.append({"batch": bi, "unit": batch[0]["unit"],
                      "range": [batch[0]["n"], batch[-1]["n"]], "count": len(batch)})

    (OUT / "index.json").write_text(json.dumps(index, indent=1) + "\n", encoding="utf-8")
    total = sum(len(b) for b in batches)
    print(f"{len(batches)} batches, {total} lessons (+1 pre-written = {total + 1})")
    for w in range(0, len(batches), 3):
        wave = index[w:w + 3]
        print(f"wave {w // 3 + 1}: " + ", ".join(f"b{b['batch']}(u{b['unit']}, {b['count']} lessons)" for b in wave))


if __name__ == "__main__":
    main()
