# Grounded Classical Mechanics

**A full year of physics — 365 daily lessons — taught with the objects Kenya already has.**

A jerrican is a pressure lab. A boda boda is a machine zoo. A swinging stone on a sisal
string is a clock, a gravity meter and a pendulum all at once. This course teaches the
complete classical mechanics spine of Kenya's Competency Based Education physics
curriculum to learners aged 10–17 using only what a homestead, market or jua kali
workshop can provide — no laboratory required.

## What Is This?

- **365 self-contained lessons**, one for every day of the year, each a complete
  45-minute plan.
- **Every lesson** carries a **pre-test and post-test** (so growth is measurable every
  single day), **advanced questions with worked answers for ages 14–17**, safety notes,
  and teacher notes.
- **222 hands-on lessons** include written build instructions: parts you can find in
  any market, step-by-step workflows, checkpoints, and the common mistakes.
- **16 units** build from measurement to a working **windmill water pump**, a
  **siphon garden**, **water rockets**, **bridges**, and a **class orchestra** of
  student-built instruments.
- **CBE-aligned** to the KICD Grade 10 Physics design (strand 1.0 Mechanics & Thermal
  Physics, waves 2.1, energy & climate 4.1) plus the Junior School Integrated Science
  and Upper Primary Science & Technology *Force & Energy* strands. See
  [docs/CBE_COVERAGE.md](docs/CBE_COVERAGE.md) for the full matrix.

## Who Is It For?

- **Teachers** in Kenyan primary, junior and senior schools — especially where the
  laboratory is a dream but the compound is full of physics.
- **Home-schooling families and community learning centres.**
- **Ages 10–13** learn by doing; the **Advanced Questions** carry ages **14–17** into
  senior-school mathematics.

## A Taste of the Year

| Unit | Lessons | Flagship builds |
|---|---|---|
| 01 Measurement & Scientific Skills | 26 | water clock, eureka can, sundial |
| 02 Forces in Everyday Life | 26 | rubber-strip force meter, balloon rocket |
| 03 Describing Motion | 26 | ticker timer, speed trap, journey graphs |
| 04 Gravity, Falling & Projectiles | 20 | egg drop, water rocket (3 days) |
| 05 Work, Energy & Power | 26 | home energy audit, Rube Goldberg chain |
| 06 Simple Machines | 32 | weighing beam, windlass, block & tackle, bicycle study |
| 07 Pressure & Fluids at Rest | 28 | water level, manometer, barometer, hydraulic lift, Cartesian diver |
| 08 Fluids in Motion, Siphons & Pumps | 22 | **siphon garden**, flap valves, diaphragm pump, ram pump |
| 09 Buoyancy & Floating | 18 | clay boats, pencil hydrometer |
| 10 Circular & Rotational Motion | 18 | sling, carousel, wheel balancing |
| 11 Oscillations & Pendulums | 18 | **pendulum clock**, metronome, shake table |
| 12 Momentum & Collisions | 16 | Newton's cradle, boda-safety campaign |
| 13 Elasticity, Materials & Structures | 24 | spring scale, **bridge challenge**, tower |
| 14 Wind & Water Power | 28 | anemometer, **the school windmill** (8 days), spoon turbine |
| 15 Sound & Mechanical Waves | 20 | bottle xylophone, one-string guitar, pan pipes, debe telephone |
| 16 Capstone & Community Science | 17 | team capstone + Community Science Day |

Full index: [CURRICULUM_MAP.md](CURRICULUM_MAP.md).

## Why "Grounded"?

Because a child who has felt a siphon start with her own tube, timed her own pendulum,
and watched her own windmill lift real water does not need to be persuaded that physics
is true — she has *used* it. Every concept here starts from an object the learner can
touch, and every build leaves the school more capable than it was: a water level for
the fundis, a hydrometer for the dairy, a garden that waters itself.

The materials are not a compromise. They are the curriculum.

## Repository Layout

```
lessons/                 365 lesson files, organised by unit
data/units/              curriculum source data (edit these!)
data/curriculum_map.json generated master map (365 lessons)
CURRICULUM_MAP.md        generated human-readable index
docs/
  MATERIALS_GUIDE.md     what to scavenge, buy and borrow — and where
  FLAGSHIP_PROJECTS.md   the multi-day build threads
  ASSESSMENT_GUIDE.md    pre/post growth model + CBE competency mapping
  CBE_COVERAGE.md        generated standards coverage matrix
templates/               lesson template, style guide, gold-standard example
tools/                   build_map / lint_lessons / coverage / build_index
tests/                   pytest suite validating all 365 lessons
```

## For Contributors

The curriculum is **data-driven**: lesson metadata lives in `data/units/*.json`, and
the map, index and coverage docs are generated:

```bash
python tools/build_map.py        # validate data, regenerate curriculum_map.json
python tools/build_index.py      # regenerate CURRICULUM_MAP.md
python tools/coverage.py         # regenerate docs/CBE_COVERAGE.md
python tools/lint_lessons.py --all   # structural check on all 365 lessons
python -m pytest tests/ -q       # the full verification suite
```

Every lesson must pass the linter: required sections, 45-minute timings that sum to 45,
pre/post answer keys, worked advanced answers, and hands-on build sections where the
map demands them.

## License

MIT — teach it, adapt it, translate it, build the windmill. Karibu.
