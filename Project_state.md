# Project State: Grounded Classical Mechanics

> **Last updated:** 2026-08-16
> **Current phase:** build
> **Overall health:** green

---

## 1. Goal
365 daily 45-minute classical-mechanics lessons for Kenyan learners aged 10–17, taught with common Kenyan physical objects, aligned to KICD CBE physics strands, each with pre/post tests and 14–17 advanced questions, plus hands-on build instructions where possible.

## 2. Current Status
### Done
- [x] CBE research: Grade 10 Physics strands confirmed (KICD 2025 design)
- [x] 16-unit / 365-lesson curriculum map authored (`data/units/*.json`, generated `data/curriculum_map.json`)
- [x] Lesson template + style guide + gold-standard example (lesson 051)
- [x] Tooling: build_map.py, make_batches.py, lint_lessons.py, coverage.py, build_index.py
- [x] Pytest suite (tests/test_curriculum.py)

### In Progress
- [ ] 35 subagent batches writing lessons (12 waves of 3); lesson 051 pre-written

### Not Started
- [ ] Docs: README (Phosphorus voice), MATERIALS_GUIDE, FLAGSHIP_PROJECTS, ASSESSMENT_GUIDE
- [ ] Full lint + pytest run, fixes
- [ ] Commit; user pushes to origin main

## 3. Architecture & Key Decisions
| Decision | Rationale | Date |
|---|---|---|
| Mechanics spine only (CBE 1.x, 2.1, 4.1); electricity/optics/radioactivity flagged for companion volume | Project name + CBE G10 strand 1.0 is mechanics-heavy | 2026-08-16 |
| Data-driven: `data/units/*.json` → generated map/index/coverage | Single source of truth; lint-able at scale | 2026-08-16 |
| Subagents write lesson files only; parent owns shared files | Walker's one-subagent-per-file hard rule | 2026-08-16 |
| Lesson 051 hand-written as gold standard | Anchors subagent style; lint-verified | 2026-08-16 |
| 45-min skeleton 5+5+15+8+10+2 | Pre/post tests fit inside the period | 2026-08-16 |

## 4. Blockers & Risks
- **Risk:** subagent quality drift across 35 batches → lint gates + spot-checks each wave; re-dispatch failures.
- **Risk:** CBE sub-strand codes are strand-level (public designs) → documented as such in CBE_COVERAGE.md.

## 5. Next Step (only ONE)
> **Next:** Run waves 1–12 of lesson-writing subagents; then docs + README; then verify + commit.

## 6. Environment & Tooling Notes
- Python 3 stdlib only; pytest for the suite
- No external services; offline-friendly repo
- GitHub: drwjkirkpatrick-web/grounded-classical-mechanics (user pushes)

## 7. Recent Session Log
- 2026-08-16: Project scaffolded, CBE researched, 365-lesson map authored, tooling built, subagent waves launched.

## 8. References
- KICD Grade 10 Physics Curriculum Design (2025): strands 1.0 Mechanics & Thermal Physics, 2.0 Waves & Optics, 3.0 Electricity & Magnetism, 4.0 Environmental & Space Physics
