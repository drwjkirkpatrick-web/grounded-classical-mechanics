# Lesson 252: Build: The One-Second Pendulum Clock II — Calibrate

**Unit:** 11 — Oscillations & Pendulums  |  **Duration:** 45 minutes  |  **Ages:** 10–17 (differentiated)
**CBE Alignment:** JS-FE; G10-PHY-1.1  |  **Hands-On:** Yes  |  **Project:** pendulum-clock

## Learning Outcomes
By the end of the lesson, learners can:
1. Calibrate the pendulum clock from Lesson 251 against a reference clock over 5 minutes.
2. Log the drift (gain or loss) and calculate the fractional time error.
3. Compute the length correction needed to bring the clock within target accuracy.
4. Identify environmental effects (temperature, wind, pivot wear) that cause drift.

## Materials
- The pendulum clock built in Lesson 251 (stand, string, bob at tuned length)
- A reference clock: a phone clock, a wall clock, or a watch
- Stopwatch (phone) — for counting swings
- A log sheet: a table with columns for time interval | expected swings | actual swings | drift
- Pencil and notebook
- Calculator (phone)

## Vocabulary
- **drift** (bwawa) — the accumulated time error of the pendulum clock vs a reference
- **calibration** (upimaji) — comparing the pendulum against a known clock and correcting
- **gain** (kukimbia) — the clock runs fast (reads ahead of real time)
- **loss** (chelewa) — the clock runs slow (reads behind real time)
- **fractional error** (hitilafu ya sehemu) — drift divided by total time; dimensionless

## Pre-Test
*5 minutes, individual, closed book.*

1. Your pendulum clock counts 300 swings in 5 minutes. How many swings should it count if T = 1.000 s?
2. If it counts 305 swings in 5 minutes, is the clock fast or slow?
3. If the clock gains 2 s in 10 min, what is the fractional error?

**Answer Key (Pre-Test):**
1. 5 minutes = 300 s. At T = 1.000 s, 300/1.000 = 300 swings. Exactly 300.
2. 305 swings in 300 s means T = 300/305 = 0.984 s — the period is too short (too fast). The clock is fast (gaining).
3. 2 s / 600 s = 0.00333 = 0.333% fractional error (fast).

## Lesson Flow (45 Minutes)

1. **Settle and Pre-Test (5 min)** — collect slips.
2. **Engage (5 min)** — recap: last lesson we tuned the pendulum to T ≈ 1 s. But is it accurate over a long run? Ask: *if your clock is off by 0.01 s per swing, how much does it drift in 5 minutes?* (0.01 × 300 = 3 s). Board: small errors accumulate. Today we measure and correct the drift.
3. **Explore (15 min)** — pairs run the 5-minute calibration (see Hands-On Build). Each pair: starts the pendulum and the reference clock simultaneously, counts swings for 5 minutes (or counts total swings at the 5-minute mark), computes the drift, and calculates the length correction. They apply the correction (adjust the string by the calculated amount), re-run for 2–3 minutes, and check if the drift is reduced. Results go on a class table: pair | drift before | correction | drift after.
4. **Explain (8 min)** — consolidate. The drift is caused by T being slightly off. If the clock gains (fast), T is too short — lengthen the string. If it loses (slow), T is too long — shorten. The correction: ΔT/T = drift/total_time, and ΔL/L = 2 × ΔT/T (since T ∝ √L). So ΔL = 2L × (drift/total_time). Environmental effects: temperature expands the string (longer L → slower clock → loses time); wind pushes the bob (adds a random force, destabilising the period); pivot wear increases friction (more damping → eventually stops). Confront the misconception that "a tuned clock stays accurate forever" — real clocks need regular calibration because temperature, humidity, and wear all shift the period.
5. **Post-Test (10 min)** — administer; collect or peer-mark.
6. **Wrap and Homework (2 min)** — takeaway: *small errors grow — calibrate regularly*. Homework: name your clock and write a one-sentence care instruction (e.g., "Keep away from wind; check weekly").

## Hands-On Build: Five-Minute Calibration
*Calibrate the pendulum clock against a reference and correct the drift.*

### Parts
- Pendulum clock from Lesson 251
- Reference clock (phone, wall clock, watch)
- Stopwatch (phone) — for counting or timing
- Log sheet — table: time | expected swings | actual swings | drift
- Calculator (phone)

### Workflow
1. Start the pendulum swinging gently (~10°). Start the reference clock timer at the same moment. **Checkpoint:** the pendulum and the timer start simultaneously.
2. Let the pendulum run for exactly 5 minutes (300 s). Count the total swings, or note the swing count at the 5-minute mark. **Checkpoint:** use the 10-swing counting method from Lesson 245 for accuracy.
3. Expected swings = 300 (at T = 1.000 s). Actual swings = your count. Drift = actual − expected. **Checkpoint:** if actual > 300, the clock is fast (gaining); if actual < 300, it is slow (losing).
4. Compute the fractional error: drift/300. Compute the length correction: ΔL/L = 2 × drift/300 → ΔL = 2 × L × (drift/300). **Checkpoint:** if drift = +3 (fast), ΔL = 2 × 0.248 × (3/300) = +0.005 m = +5 mm. Lengthen the string by 5 mm.
5. Apply the correction. Re-run for 2–3 minutes and check if the drift is reduced. **Checkpoint:** the residual drift should be under 1 swing per 2–3 minutes.
6. Record: drift_before | correction | drift_after. Write the clock's name on the stand.

### Common Mistakes
- **Not running long enough** — 1 minute is too short to see small drift. Run at least 5 minutes for the first calibration.
- **Counting errors** — use the 10-swing method (count in groups of 10) to avoid losing track. Have one partner count, one partner time.
- **Overcorrecting** — if drift is 2 swings in 300, the correction is tiny (~3 mm). Do not adjust by 1 cm — that overshoots.
- **Ignoring amplitude decay** — if the pendulum slows to a stop before 5 minutes, the amplitude was too small or the pivot is too rough. Re-start with a slightly larger amplitude or fix the pivot.
- **Wind or vibration** — calibrate indoors, away from wind and passing traffic. Any external disturbance adds noise.

## Post-Test
*10 minutes, individual.*

1. Your clock counts 300 swings in 5 minutes. What does this tell you? (mirrors pre-test)
2. If the clock counts 296 swings in 5 minutes, is it fast or slow? What is the drift? (mirrors pre-test)
3. The clock gains 2 s per 10 min. Calculate the fractional error and the length correction (L = 25 cm). (mirrors pre-test)
4. A hot day makes the string expand. Will the clock gain or lose? Why?
5. Challenge: your clock drifts 5 s in 10 min. Calculate ΔL. Should you shorten or lengthen? (L = 25 cm, g = 9.8.)

**Answer Key (Post-Test):**
1. T = 300/300 = 1.000 s exactly. The clock is perfectly calibrated — drift is zero.
2. Slow (losing). Drift = 296 − 300 = −4 swings. T = 300/296 = 1.014 s — the period is too long. The clock is 4 swings short, meaning it has counted 4 s less than it should.
3. Fractional error = 2/600 = 0.00333 (fast). ΔL/L = 2 × 0.00333 = 0.00667. ΔL = 0.25 × 0.00667 = 0.00167 m = 1.7 mm. Lengthen by 1.7 mm (the clock is fast → T is too short → L is too short → lengthen).
4. Lose (run slow). Longer L → longer T → fewer swings per minute → the clock falls behind. Heat expands the string, effectively lengthening the pendulum. This is why precision clocks use temperature-compensated pendulums (e.g., mercury or invar).
5. Drift = 5 s in 600 s → fractional error = 5/600 = 0.00833 (fast, assuming positive drift). ΔL/L = 2 × 0.00833 = 0.01667. ΔL = 0.25 × 0.01667 = 0.00417 m = 4.2 mm. Lengthen by 4.2 mm. (If the drift is negative — losing — then shorten by 4.2 mm instead.)

## Advanced Questions (Ages 14–17)

1. **Q:** Clock gains 2 s per 10 min. Compute the length correction with direction (L = 0.248 m).
   **Worked Answer:** Drift = +2 s in 600 s → fractional error = 2/600 = 0.00333 (fast). ΔT/T = 0.00333 → ΔT = 1.0 × 0.00333 = 0.00333 s (T is too short by 0.00333 s). Since T ∝ √L: ΔL/L = 2ΔT/T = 2 × 0.00333 = 0.00667. ΔL = 0.248 × 0.00667 = 0.00165 m = 1.65 mm. The clock is fast, so T is too short, meaning L is too short. Lengthen by 1.65 mm. Verification: new L = 0.2497 m → T = 2π√(0.2497/9.8) = 2π × 0.15967 = 1.0033 s. Old T = 2π × 0.15915 = 0.9967 s. Correction: 1.0033 − 0.9967 = 0.0066 s — wait, let me recalculate. Actually if the clock gains 2 s in 600 s, it means it counted 600+2 = 602 effective seconds. So T_actual = 600/602 × T_target = 0.99668 × 1.000 = 0.99668 s. T is too short by 0.00332 s. ΔL = 2L × ΔT/T = 2 × 0.248 × 0.00332 = 0.00165 m. Lengthen by 1.65 mm.
2. **Q:** A brass pendulum (α = 19×10⁻⁶ /°C) is calibrated at 20°C. At 35°C, how much time does it lose per day?
   **Worked Answer:** ΔL/L = αΔT = 19×10⁻⁶ × 15 = 2.85×10⁻⁴. ΔT/T = ½ΔL/L = 1.425×10⁻⁴. In 86400 s: drift = 86400 × 1.425×10⁻⁴ = 12.3 s/day slow. The clock loses about 12 seconds per day due to thermal expansion.
3. **Q:** Design a calibration procedure that achieves accuracy within 30 s/day. How long must you run the test?
   **Worked Answer:** 30 s/day = 30/86400 = 3.47×10⁻⁴ fractional error. To measure drift at this level, the drift must exceed the counting uncertainty. If we count N swings, the counting uncertainty is ~1 swing. So we need N such that 1/N < 3.47×10⁻⁴ → N > 2882 swings. At T = 1 s, that's 2882 s ≈ 48 minutes. So run the calibration for about 50 minutes, count total swings, and compare to the expected count. Correct the length by ΔL = 2L × (drift/expected_swings). A second 50-minute run confirms the correction. Total: ~2 hours for full calibration to 30 s/day.

## Safety Notes
- Same as Lesson 251: secure stand, clear swing area, no fragile bobs.
- Long calibration runs (5+ minutes) — ensure the pendulum doesn't wander into other learners or objects.

## Teacher Notes
- Prior knowledge: Lesson 251 built and tuned the pendulum to T ≈ 1 s. This lesson checks long-term accuracy and corrects residual drift.
- Differentiation: ages 10–13 focus on the 5-minute run and the idea of drift. Ages 14–17 compute the length correction, explore thermal expansion, and design a precision calibration.
- Local resource tips: a phone clock is the best reference. If counting swings for 5 minutes is difficult, time 100 swings and compare to 100 s — the drift is proportional.
- The "name your clock" activity is a fun closing that personalises the project. Display the named clocks in the classroom.