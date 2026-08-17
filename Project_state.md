# Project State: Grounded Classical Mechanics

> **Last updated:** 2026-08-16
> **Current phase:** PAUSED (mid-production) — see RESUME.md to continue
> **Overall health:** green (plan + tooling complete; 56/365 lessons written)

---

## 1. Goal
365 daily 45-minute classical-mechanics lessons for Kenyan learners aged 10–17, taught with common Kenyan physical objects, aligned to KICD CBE physics strands, each with pre/post tests and 14–17 advanced questions, plus hands-on build instructions where possible.

## 2. Current Status
### Done
- [x] CBE research: Grade 10 Physics strands confirmed (KICD 2025 design)
- [x] 16-unit / 365-lesson curriculum map (`data/units/*.json` → `data/curriculum_map.json`) — exactly 365 verified
- [x] Lesson template + style guide + gold-standard example (lesson 051)
- [x] Tooling: build_map, make_batches, lint_lessons, coverage, build_index, make_quiz
- [x] Pytest suite (tests/test_curriculum.py)
- [x] Docs: README (Phosphorus), MATERIALS_GUIDE, FLAGSHIP_PROJECTS, ASSESSMENT_GUIDE, TEACHING_NOTES, CBE_COVERAGE, CURRICULUM_MAP
- [x] **56 lessons written & lint-clean:** Units 1–2 complete (001–052); Unit 3 has 065–068
- [x] Hermes config tuned for production: delegation.child_timeout_seconds=1800, max_concurrent_children=6

### In Progress
- [ ] Lesson production: **309 remaining** (units 3–16). Pipeline documented in RESUME.md.

### Not Started
- [ ] Final verification (lint 365/365 + pytest), regen index/coverage, final commit; user pushes to GitHub

## 3. Architecture & Key Decisions
| Decision | Rationale | Date |
|---|---|---|
| Mechanics spine only (CBE 1.x, 2.1, 4.1); electricity/optics/radioactivity for companion volume | Project name + CBE G10 strand 1.0 is mechanics-heavy | 2026-08-16 |
| Data-driven: `data/units/*.json` → generated map/index/coverage | Single source of truth; lint-able at scale | 2026-08-16 |
| Subagents write lesson files only; parent owns shared files | One-subagent-per-file hard rule | 2026-08-16 |
| Batch size 4, disk-based re-queue (make_batches recomputes from disk) | Provider (kimi-coding) intermittently stalls 90s; small batches = cheap failures | 2026-08-16 |
| 45-min skeleton 5+5+15+8+10+2 | Pre/post tests fit inside the period | 2026-08-16 |

## 4. Blockers & Risks
- **Blocker (transient):** kimi-coding provider 90s API stalls killed 5/6 subagents in the last wave. Resume when the provider is healthy; the pipeline self-heals via make_batches.py.
- **Risk:** CBE sub-strand codes are strand-level (public designs) → documented as such in docs/CBE_COVERAGE.md.

## 5. Next Step (only ONE)
> **Next:** Follow RESUME.md: run `python3 tools/make_batches.py`, dispatch a 6-batch wave with the verbatim brief, lint, commit. Repeat until 365/365.

## 6. Environment & Tooling Notes
- Python 3 stdlib only; pytest for the suite
- GitHub: drwjkirkpatrick-web/grounded-classical-mechanics — **user pushes**; `gh` authenticated
- Git author for commits: Walker Kirkpatrick <walker@example.com> (via `git -c`)

## 7. Recent Session Log
- 2026-08-16: Scaffolded; CBE researched; 365-map authored; tooling + docs built; waves 1–6 wrote 56 lessons (Units 1–2 complete); provider stalls prompted pause. RESUME.md written for continuation.

## 8. References
- RESUME.md — the continuation runbook (start here next session)
- KICD Grade 10 Physics Curriculum Design (2025): strands 1.0 Mechanics & Thermal Physics, 2.0 Waves & Optics, 3.0 Electricity & Magnetism, 4.0 Environmental & Space Physics
