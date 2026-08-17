#!/usr/bin/env python3
"""make_batches.py — split remaining (not-yet-written) lessons into subagent batches.

Re-run any time: batches are computed from the curriculum map MINUS lesson files
already present on disk, so re-dispatching after failures is automatic.

Writes data/batches/batch-NN.json and prints the wave plan.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAP = ROOT / "data" / "curriculum_map.json"
OUT = ROOT / "data" / "batches"
TEMPLATE_DIGEST = """\
EMBEDDED TEMPLATE — use these section headers in this exact order (replace {placeholders}):
# Lesson {NNN}: {exact title}
**Unit:** {unit line}  |  **Duration:** 45 minutes  |  **Ages:** 10-17 (differentiated)
**CBE Alignment:** {codes}  |  **Hands-On:** {Yes/No}  |  **Project:** {slug or —}
## Learning Outcomes         (3-4 numbered, action verbs)
## Materials                 (bulleted, local objects + substitutes)
## Vocabulary                (4-7 terms: **term** (Kiswahili) — meaning)
## Pre-Test                  (3-4 numbered Qs; then line '**Answer Key (Pre-Test):**' + numbered answers)
## Lesson Flow (45 Minutes)  (numbered steps with (N min) markers summing to EXACTLY 45:
                             5 settle+pre-test, 5 engage, 15 explore, 8 explain, 10 post-test, 2 wrap)
## Hands-On Build: {name}    (ONLY if hands_on=yes) with:
### Parts                    (part — qty — source/substitute)
### Workflow                 (numbered steps; include a **Checkpoint:** step)
### Common Mistakes          (mistake + fix bullets)
## Post-Test                 (4-5 numbered Qs, Q1-2 marked as mirroring pre-test; then '**Answer Key (Post-Test):**' + answers with working)
## Advanced Questions (Ages 14–17)   (2-3 items, each '**Q:** ...' then '   **Worked Answer:** ...' with full working and units)
## Safety Notes              (specific hazards of THIS activity)
## Teacher Notes             (prior knowledge, differentiation 10-13 vs 14-17, local sourcing tips, CBE assessment note)
Body ~450-700 words. Physics: g=10 N/kg, water 1000 kg/m3, 1 L water = 1 kg, sound ~340 m/s.
Ground everything in Kenyan objects: boda, matatu, mkokoteni, jerrican, debe, sufuria, sisal, mabati, jembe, jiko, posho mill, jua kali.
"""

BATCH_SIZE = 4  # lessons per subagent (small chunks: fast, low failure blast radius)


def done_lessons():
    done = set()
    for p in (ROOT / "lessons").rglob("lesson-*.md"):
        m = re.match(r"lesson-(\d{3})-", p.name)
        if m:
            done.add(int(m.group(1)))
    return done


def main():
    data = json.loads(MAP.read_text(encoding="utf-8"))
    done = done_lessons()
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("batch-*.json"):
        old.unlink()

    batches = []
    for unit in data["units"]:
        remaining = [l for l in unit["lessons"] if l["n"] not in done]
        for i in range(0, len(remaining), BATCH_SIZE):
            batches.append(remaining[i:i + BATCH_SIZE])

    index = []
    for bi, batch in enumerate(batches, 1):
        path = OUT / f"batch-{bi:02d}.json"
        # Compact line format: one line per lesson + embedded template digest,
        # so a subagent needs exactly ONE file read before writing.
        lines = [
            f"BATCH {bi:02d} — Unit {batch[0]['unit']}: {batch[0]['unit_title']}",
            f"Write {len(batch)} lesson files at the exact paths below.",
            "",
            TEMPLATE_DIGEST,
            "filename | n | title | cbe | hands_on | project | materials | focus | advanced",
        ]
        for l in batch:
            lines.append(
                f"{l['filename']} | {l['n']} | {l['title']} | {';'.join(l['cbe'])} | "
                f"{'yes' if l['hands_on'] else 'no'} | {l['project'] or '-'} | "
                f"{'; '.join(l['materials'])} | {l['focus']} | {l['advanced']}"
            )
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        index.append({"batch": bi, "unit": batch[0]["unit"],
                      "range": [batch[0]["n"], batch[-1]["n"]], "count": len(batch)})

    (OUT / "index.json").write_text(json.dumps(index, indent=1) + "\n", encoding="utf-8")
    total = sum(len(b) for b in batches)
    print(f"{len(done)} lessons already on disk; {len(batches)} batches for remaining {total}")
    for w in range(0, len(batches), 3):
        wave = index[w:w + 3]
        print(f"wave {w // 3 + 1}: " + ", ".join(f"b{b['batch']}(u{b['unit']}, {b['count']})" for b in wave))


if __name__ == "__main__":
    main()
