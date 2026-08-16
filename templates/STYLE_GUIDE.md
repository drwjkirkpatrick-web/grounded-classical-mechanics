# Grounded Classical Mechanics — Lesson Authoring Style Guide

You are writing lessons for **Grounded Classical Mechanics**: 365 daily 45-minute physics
lessons for Kenyan learners aged 10–17, taught with objects found in Kenyan homes,
markets, farms and jua kali workshops. Alignment: Kenya CBE (KICD) curriculum.

## Voice and Audience

- Written for the **teacher**, in clear instructional English. Learners speak English and
  Kiswahili; sprinkle Kiswahili terms in Vocabulary where natural.
- Concrete before abstract: every concept starts from a real object, demo or story.
- Kenyan context is not decoration — it IS the curriculum's grounding: boda bodas,
  matatus, mkokoteni handcarts, jerricans, debes, sufurias, mabati, jembes, pangas,
  jikos, posho mills, sisal rope, inner-tube rubber, water tanks, wells, jua kali artisans,
  Lake Victoria boats, Kenyan athletics (Kipchoge, Yego), Kijito windmills, Olkaria
  geothermal, Lake Turkana wind, Seven Forks hydro.
- Ages 10–13 learn through doing and talking; the **Advanced Questions (Ages 14–17)**
  carry the quantitative load (algebra, multi-step, g = 10 N/kg unless stated).

## Hard Rules (lint-enforced)

1. Use `templates/lesson_template.md` EXACTLY — same section headers, same order.
2. H1 must be `# Lesson NNN: Title` matching the assigned number and title from the map.
3. All `(N min)` timings inside `## Lesson Flow (45 Minutes)` must sum to exactly 45.
   Recommended skeleton: 5 (settle+pre-test) + 5 (engage) + 15 (explore) + 8 (explain)
   + 10 (post-test) + 2 (wrap) = 45.
4. Pre-Test: 3–4 numbered questions + `**Answer Key (Pre-Test):**`.
5. Post-Test: 4–5 numbered questions + `**Answer Key (Post-Test):**`. Q1–2 must mirror
   the pre-test so growth is measurable.
6. `## Advanced Questions (Ages 14–17)`: exactly 2–3 items, each `**Q:** … **Worked Answer:** …`
   with full working and units.
7. If the map says `hands_on: true`, include the `## Hands-On Build` section with
   `### Parts`, `### Workflow` (numbered, with a checkpoint step), `### Common Mistakes`.
   If `hands_on: false`, OMIT the Hands-On Build section entirely.
8. `**CBE Alignment:**` line must include the codes given in the lesson's map entry.
9. `## Safety Notes` must be specific to this lesson's real hazards (sharps, heat,
   falling loads, flying objects, water, mouth-siphon hygiene, traffic observation).
10. Length: 400–700 words of body text per lesson (roughly 170–280 lines is too long;
    keep it tight and teachable). Do NOT pad.
11. Numbers must be physically correct. g = 10 N/kg, ρ(water) = 1000 kg/m³, 1 L water ≈ 1 kg,
    speed of sound ≈ 340 m/s. Show working in worked answers.
12. Answer keys must actually answer the questions asked. Cross-check each one.

## CBE Codes (use exactly as given in the map)

- `G10-PHY-1.1` Introduction to Physics (Senior School Physics, KICD 2025)
- `G10-PHY-1.2` Pressure
- `G10-PHY-1.3` Mechanical Properties of Materials
- `G10-PHY-1.4` Temperature and Thermal Expansion
- `G10-PHY-1.5` Moments and Equilibrium
- `G10-PHY-1.6` Energy, Work, Power and Machines
- `G10-PHY-2.1` Properties of Waves
- `G10-PHY-4.1` Greenhouse Effect and Climate Change
- `G10-PHY-4.2` Introduction to Space Physics
- `JS-FE` Junior School Integrated Science, Force & Energy strand (Grades 7–9)
- `UP-FE` Upper Primary Science & Technology, Force & Energy strand (Grades 4–6)

## Pre/Post Test Design

- Pre-test: what a 10-year-old could attempt before the lesson (prediction, opinion,
  recall of prior lessons). Not trick questions.
- Post-test: 1–2 mirrored items (growth), then application items; final item may stretch.
- Mix formats lightly: short answer, calculate, draw/diagram, explain, multiple choice
  (sparingly — at most one MCQ per test).

## Multi-Lesson Projects

Lessons tagged with the same `project` slug continue one build. Respect continuity:
- Later project lessons reference what was built earlier ("the diaphragm pump from Unit 8").
- Project lessons still need complete pre/post tests and advanced questions.
- The final lesson of a project includes presentation/measurement of results.
