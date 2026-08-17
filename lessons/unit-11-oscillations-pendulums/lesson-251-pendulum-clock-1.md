# Lesson 251: Build: The One-Second Pendulum Clock I

**Unit:** 11 — Oscillations & Pendulums  |  **Duration:** 45 minutes  |  **Ages:** 10–17 (differentiated)
**CBE Alignment:** JS-FE; G10-PHY-2.1  |  **Hands-On:** Yes  |  **Project:** pendulum-clock

## Learning Outcomes
By the end of the lesson, learners can:
1. Use T = 2π√(L/g) to calculate the length needed for a target period.
2. Build a rigid stand and pendulum assembly that holds a stable pivot.
3. Approach the target length by tuning — shortening or lengthening the string incrementally.
4. Verify the tuned period to within ±0.05 s using the 10-swing method.

## Materials
- Stand materials: a retort stand, or a stick clamped to a desk, or a door frame with a nail
- String or sisal twine — ~50 cm (non-stretchy)
- Bob: a stone, bunch of keys, or a large nut (50–200 g)
- Tape measure or ruler
- Stopwatch (phone)
- Protractor card (to set ~10° release angle)

## Vocabulary
- **target period** (kipindi lengwa) — the period you want the pendulum to have (here 1.000 s)
- **tuning** (kupanga) — adjusting the length incrementally until the measured period matches the target
- **calibration** (upimaji) — comparing your pendulum against a known clock to check accuracy
- **seconds pendulum** (ratili) — a pendulum with T = 2 s; here we build T = 1 s (half-second)

## Pre-Test
*5 minutes, individual, closed book.*

1. Using T = 2π√(L/g) with g = 9.8 m/s², find L for T = 1.000 s.
2. If your measured period is too long (too slow), should you shorten or lengthen the string?
3. Why should the stand be rigid and the pivot smooth?

**Answer Key (Pre-Test):**
1. L = g(T/2π)² = 9.8 × (1.000/6.283)² = 9.8 × 0.02533 = 0.248 m ≈ 25 cm.
2. Shorten — shorter L gives shorter T (T ∝ √L).
3. A wobbly stand leaks energy and changes the effective length; a rough pivot adds friction (damping). Both make the period unreliable.

## Lesson Flow (45 Minutes)

1. **Settle and Pre-Test (5 min)** — collect slips.
2. **Engage (5 min)** — challenge the class: *build a pendulum that ticks exactly once per second — T = 1.000 s.* The formula tells us the length; the build tells us whether reality matches theory. Board the target: L ≈ 25 cm, T = 1.000 s.
3. **Explore (15 min)** — pairs build the stand and pendulum (see Hands-On Build). Each pair: (a) calculates L from the formula, (b) sets the string to that length, (c) times 20 swings and computes T, (d) compares to 1.000 s, (e) adjusts the length by 1–2 mm and re-tests. Repeat until T = 1.000 ± 0.05 s. Record the final length — it should be close to 25 cm but may differ slightly due to local g, string mass, or pivot friction.
4. **Explain (8 min)** — consolidate. The formula gives a starting length, but real-world factors (string mass, pivot friction, air resistance, local g) shift the result slightly. Tuning closes the gap between theory and reality. The key insight: small length changes produce small period changes (T ∝ √L, so ΔT/T = ½ ΔL/L). A 1% length change gives only 0.5% period change — so tune patiently, 1–2 mm at a time. Confront the misconception that "the formula gives the exact length" — it gives the theoretical length; the real pendulum needs calibration.
5. **Post-Test (10 min)** — administer; collect or peer-mark.
6. **Wrap and Homework (2 min)** — takeaway: *theory gives the start; tuning gives the finish*. Homework: record your final length and period. Next lesson (252) calibrates against a real clock over 5 minutes.

## Hands-On Build: One-Second Pendulum Stand
*Build a rigid stand, hang the pendulum, and tune to T = 1.000 s.*

### Parts
- Stand: a retort stand, or a stick clamped firmly to a desk edge, or a nail in a door frame
- String: ~50 cm of non-stretchy string or sisal twine
- Bob: a stone, bunch of keys, or a large nut (50–200 g — mass doesn't matter, Lesson 246)
- Tape measure or ruler
- Stopwatch (phone)
- Protractor card (for 10° release)

### Workflow
1. Calculate L for T = 1.000 s: L = g(T/2π)² ≈ 0.248 m ≈ 25 cm. **Checkpoint:** write the calculation in your notebook, showing every step.
2. Build the stand: clamp the stick or secure the nail so it does not wobble. **Checkpoint:** push the top of the stand sideways — it should not move.
3. Tie the string to the pivot and the bob. Set the length from pivot to centre of bob to 25 cm. **Checkpoint:** measure to the centre of the bob, not the top. The bob hangs straight down without touching anything.
4. Pull to ~10° and release. Time 20 swings. Divide by 20 for T. **Checkpoint:** T should be close to 1.000 s but may be off by 0.02–0.05 s.
5. If T is too long (slow), shorten the string by 1–2 mm. If too short (fast), lengthen by 1–2 mm. Re-time 20 swings. **Checkpoint:** repeat until T = 1.000 ± 0.05 s.
6. Mark the final length on the string with a pen. Record: L_final = ___ cm, T = ___ s.

### Common Mistakes
- **Stand wobbles** — energy leaks into the stand, changing the period. Clamp firmly or use a heavier base.
- **String stretches** — sisal and cotton can stretch under load. Pull the string taut before measuring; use a non-stretchy material if available.
- **Measuring to the top of the bob** — the effective length includes half the bob's height. Measure to the centre.
- **Large amplitude** — at >15° the period increases (Lesson 247). Keep at 10°.
- **Impatient tuning** — changing the length by 1 cm at a time overshoots. Adjust 1–2 mm per iteration.

## Post-Test
*10 minutes, individual.*

1. Calculate L for T = 1.000 s using g = 9.8 m/s². (mirrors pre-test)
2. If T is too long, do you shorten or lengthen the string? Why? (mirrors pre-test)
3. Your 20-swing time is 19.8 s. What is T? Is it too fast or too slow?
4. By what fraction must you change L to change T by 1%? (Hint: T ∝ √L.)
5. Challenge: your tuned L is 24.5 cm but the formula says 24.8 cm. Suggest one reason for the difference.

**Answer Key (Post-Test):**
1. L = g(T/2π)² = 9.8 × (1.0/6.283)² = 9.8 × 0.02533 = 0.248 m ≈ 25 cm.
2. Shorten. T ∝ √L, so shorter L gives shorter T. If T is too long, L is too large — shorten it.
3. T = 19.8/20 = 0.99 s. This is too fast (T < 1.000 s) — the pendulum is too short. Lengthen slightly.
4. ΔT/T = ½ ΔL/L. For ΔT/T = 1% = 0.01: ΔL/L = 0.02 = 2%. So change L by 2% to change T by 1%.
5. Accept any valid reason: local g may differ slightly from 9.8; string mass adds to the effective length (the string itself oscillates, raising the effective centre of mass); pivot friction slightly increases the period; air resistance on a large bob.

## Advanced Questions (Ages 14–17)

1. **Q:** Use T = 2π√(L/g) to predict L for T = 1.000 s at g = 9.8. Compare with your tuned result.
   **Worked Answer:** L = g(T/2π)² = 9.8 × (1.000/6.2832)² = 9.8 × (0.15915)² = 9.8 × 0.025330 = 0.2482 m = 24.8 cm. Typical tuned result: 24.5–25.5 cm. The difference (~1–3 mm) comes from string mass, pivot friction, and local g variations.
2. **Q:** A learner uses a thick string. Explain why the effective length is longer than the measured length.
   **Worked Answer:** A thick, heavy string has its own mass distributed along its length. The centre of mass of the string-bob system is above the centre of the bob (the string's mass pulls the effective centre upward). The pendulum acts as if it has a shorter effective length — wait, actually: the string's mass adds inertia without adding proportionally to the restoring force, which effectively increases the period as if L were longer. More precisely, the formula T = 2π√(L/g) assumes a point mass on a massless string. A heavy string adds a correction: the effective length is L_eff = L + (string_mass × L)/(3 × bob_mass) for a uniform string. This makes T slightly longer than the simple formula predicts, so the tuned L is slightly shorter than 24.8 cm.
3. **Q:** If g in Nairobi (altitude ~1800 m) is 9.78 m/s² instead of 9.8, how much does the target L change?
   **Worked Answer:** L = g(T/2π)². At g = 9.80: L = 24.82 cm. At g = 9.78: L = 9.78 × 0.025330 = 0.2477 m = 24.77 cm. Difference: 24.82 − 24.77 = 0.05 mm — negligible for a classroom build. At much higher altitude (e.g., 4000 m, g = 9.79): still only ~0.1 mm difference. Altitude barely matters for a 1-second pendulum.

## Safety Notes
- Secure the stand firmly — a falling bob can injure feet.
- Do not use a glass or ceramic bob (breakage risk on a hard floor).
- Keep the swing area clear of other learners.

## Teacher Notes
- Prior knowledge: Lessons 248–250 established T ∝ √L, the graph method, and g measurement. This lesson applies the formula to a real build target.
- Differentiation: ages 10–13 focus on building, measuring, and tuning to get close to 1 s. Ages 14–17 should predict L, compare with the tuned result, and explain discrepancies using the string-mass correction and local g.
- Local resource tips: a stick clamped to a desk or a nail in a door frame works as the pivot. A stone or keys are fine bobs. Non-stretchy string is important — test by hanging the bob and checking the length doesn't creep.
- This is the build lesson for the pendulum-clock project. Lesson 252 is the calibration lesson — learners check their clock against a real clock over 5 minutes and correct for drift.