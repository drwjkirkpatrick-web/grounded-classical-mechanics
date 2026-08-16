# Teaching Notes: Running the Course

## The Daily 45 Minutes

Every lesson follows the same skeleton, so learners know the rhythm by heart:

| Block | Minutes | What happens |
|---|---|---|
| Settle + Pre-Test | 5 | Baseline questions, individual, no shame in "don't know yet" |
| Engage | 5 | A demo, story or mystery object that raises the question |
| Explore | 15 | The experiment, demo or build — hands on objects |
| Explain | 8 | Board work: name the concept, confront the misconception |
| Post-Test | 10 | Mirrored items measure the day's growth |
| Wrap + Homework | 2 | One-line takeaway; a tiny home task |

## Multi-Grade Classrooms

The course assumes mixed ages (10–17) in one room:

- **Ages 10–13** do the core lesson: build, observe, talk, pre/post tests.
- **Ages 14–17** also take the **Advanced Questions** (quantitative, senior-school level)
  and act as **build captains** for the hands-on workflows — leading a pair is itself
  assessed under the communication competency.
- Pre/post tests are written so a 10-year-old can attempt every item; the advanced
  section is where the older cohort stretches.

## When You Can't Do the Build

Every hands-on lesson names substitutes in its Parts list. If even those fail, run the
lesson as a demo-and-discussion: the pre/post tests still work. Mark the build as
"weathered out" and return to it — project threads are designed to absorb a lost day.

## Safety Governance

- **Teacher-handled items:** panga, jembe blade, hot jiko, steam crush-can, ladder drops.
- **Student builds:** no glass under pressure, no mains electricity anywhere, sling and
  rocket work only in the designated open field with a safety arc.
- Each lesson's **Safety Notes** are specific — read them the day before, not in the moment.
- Water hygiene: mouth-start siphons with clean drinking water only; better, teach the
  fill-the-tube-first method from day one (Lesson 180).

## Preparation Rhythm

- **Friday (15 min):** scan next week's five lessons; drop needed parts into the unit debe.
- **The scavenging calendar** in [MATERIALS_GUIDE.md](MATERIALS_GUIDE.md) keeps the kit
  stocked without a budget line.
- **Data logs:** units 8, 11, 13 and 14 reuse earlier measurements — keep class logbooks
  where learners can retrieve them.

## Assessment

See [ASSESSMENT_GUIDE.md](ASSESSMENT_GUIDE.md). The short version: record pre and post
scores per learner per lesson; growth is the mark that matters; project rubrics score
investigation, data honesty, iteration and communication.

## Using the Tools

```bash
python tools/lint_lessons.py --unit 7     # check a unit's lesson files
python tools/make_quiz.py 45 52           # printable quiz from a week's lessons
python tools/coverage.py                  # regenerate the CBE coverage doc
```

## Adapting

- **Two terms instead of three?** Units 1–8 form a coherent first course; 9–16 the second.
- **Only senior students?** Compress Units 1–4 to the advanced tracks and labs.
- **Only juniors?** Run the core lessons and treat advanced questions as extension work.
