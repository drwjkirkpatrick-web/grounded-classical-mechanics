# RESUME.md — How to Finish Grounded Classical Mechanics

**Written for the next session (Kimi K3 or any Hermes agent). Read this first.**

## Where the Project Stands

- **56 of 365 lessons are written, lint-clean and committed** (as of 2026-08-16).
  - Unit 1 (Measurement & Scientific Skills): complete, lessons 001–026
  - Unit 2 (Forces in Everyday Life): complete, lessons 027–052
  - Unit 3 (Describing Motion): only lessons 065–068 exist
- The full 365-lesson plan is DONE and correct: `data/units/*.json` →
  `data/curriculum_map.json` (generated). **Do not re-plan. The map is the spec.**
- Tooling is DONE: `tools/build_map.py`, `make_batches.py`, `lint_lessons.py`,
  `coverage.py`, `build_index.py`, `make_quiz.py`; `tests/test_curriculum.py`.
- Docs are DONE: README, MATERIALS_GUIDE, FLAGSHIP_PROJECTS, ASSESSMENT_GUIDE,
  TEACHING_NOTES, CBE_COVERAGE, CURRICULUM_MAP.
- **What remains is pure production: write the 309 missing lesson files.**

## The Production Pipeline (repeat until 365/365)

1. `cd ~/projects/grounded-classical-mechanics`
2. `python3 tools/make_batches.py` — regenerates `data/batches/batch-NN.json` from the
   map MINUS lesson files already on disk (self-healing after failures). Batch size: 4.
   **Only run this when no subagent wave is in flight** (batch files shift).
3. Dispatch a wave: `delegate_task` with **tasks = up to 6 batches** (batches 01–06).
   Each task's goal: "Write the 4 lesson files in batch NN. Batch file:
   /home/walker/projects/grounded-classical-mechanics/data/batches/batch-NN.json"
   Use the subagent brief from the section below verbatim.
4. When the wave completes: verify with `python3 tools/lint_lessons.py --all`
   (missing files are expected; FAIL lines are what matters — re-queue failed unit's
   lessons by just re-running make_batches.py), then commit:
   `git add lessons && git commit -m "Lessons: <units covered> (wave N)"`
5. Repeat from step 2. ~21 waves of 6 remain at batch size 4.

## Subagent Brief (copy verbatim into each task's context)

```
You are writing lessons for 'Grounded Classical Mechanics': daily 45-min physics lessons for Kenyan learners aged 10-17 using only objects found in Kenyan homes/markets/farms/jua kali workshops. Project root: /home/walker/projects/grounded-classical-mechanics.

PROCEDURE (no detours, no exploration):
1. Read ONLY your batch file (path in goal) — it embeds the full template digest. Batch lines are pipe-delimited: filename | n | title | cbe | hands_on | project | materials | focus | advanced.
2. Write each lesson with write_file to its exact filename, following the embedded template digest EXACTLY (same headers, same order). Straight through the batch, one write per lesson.
3. Then run once via terminal: cd /home/walker/projects/grounded-classical-mechanics && python3 tools/lint_lessons.py --files <your files> ; fix until 'N/N files pass'.

KEY RULES: H1 '# Lesson NNN: <exact title>'; sections exactly as in the embedded digest; Lesson Flow (N min) markers sum to EXACTLY 45; Pre-Test 3-4 numbered Qs + '**Answer Key (Pre-Test):**'; Post-Test 4-5 numbered Qs with Q1-2 marked as mirroring pre-test + '**Answer Key (Post-Test):**'; Advanced Questions section header EXACTLY '## Advanced Questions (Ages 14–17)' with 2-3 items each '**Q:**' + '**Worked Answer:**'; hands_on=yes includes '## Hands-On Build' (### Parts / ### Workflow with a **Checkpoint:** step / ### Common Mistakes), hands_on=no omits it; '**CBE Alignment:**' line uses exact codes from the batch line. ~450-700 words/lesson. Only write your own lesson files; if a call fails, retry it; files persist.
```

## Hermes Config Already Applied (do not redo)

- `delegation.child_timeout_seconds = 1800`
- `delegation.max_concurrent_children = 6`

## Known Failure Mode (2026-08-16)

The kimi-coding provider intermittently stalls: "Non-streaming API call timed out after
90s" — the subagent then burns iterations and dies having written zero or few files.
**This is why batches are size 4.** When a wave reports API-timeout failures, the files
simply don't exist; re-running `make_batches.py` re-queues them automatically. If the
provider is stalling badly, pause and resume later rather than burning tokens — a good
wave writes ~24 lessons, a bad wave writes ~4.

## Finishing Checklist (when lint says 365/365)

1. `python3 tools/lint_lessons.py --all` → "365/365 files pass"
2. `python3 -m pytest tests/ -q` → all pass
3. `python3 tools/coverage.py && python3 tools/build_index.py` (regen docs)
4. Update `Project_state.md` (phase: complete) and this file's status.
5. Final commit. **The user pushes to GitHub** (`git push origin main`) — do not push.
6. Report: lessons count, hands-on count, CBE coverage summary.

## Hard Rules (user's, from memory)

- One subagent per file; subagents write ONLY their own lesson files. Parent owns all
  shared files (tools/, data/, docs/, README).
- Default branch `main`. Commit as you go; user pushes.
- README audience-facing voice: Phosphorus (warm, charismatic) — already written.
