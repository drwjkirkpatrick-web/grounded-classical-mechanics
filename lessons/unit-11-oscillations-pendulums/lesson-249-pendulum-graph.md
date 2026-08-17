# Lesson 249: The Pendulum Graph: T² Against L

**Unit:** 11 — Oscillations & Pendulums  |  **Duration:** 45 minutes  |  **Ages:** 10–17 (differentiated)
**CBE Alignment:** G10-PHY-2.1; JS-FE  |  **Hands-On:** Yes  |  **Project:** —

## Learning Outcomes
By the end of the lesson, learners can:
1. Plot T² against L using the class dataset from Lesson 248.
2. Recognise that the graph is a straight line through the origin, confirming T² ∝ L.
3. Calculate the gradient and use it to find g (acceleration due to gravity).
4. Compare the pendulum-measured g with the drop-method result from Unit 4.

## Materials
- Class dataset from Lesson 248 (length | period table, copied by each learner)
- Graph paper (or squared notebook paper)
- Ruler
- Pencil and eraser
- Calculator (phone calculator is fine)
- A copy of the Unit 4 drop-method g result, if available

## Vocabulary
- **gradient** (mteremko) — the slope of a line: rise ÷ run (Δy/Δx)
- **straight-line graph** (grafu ya mstari) — a line where the gradient is constant
- **T² (T-squared)** — the period multiplied by itself; plotting this against L gives a straight line
- **g** — acceleration due to gravity, ≈ 9.8 m/s² (use 10 N/kg for quick estimates)

## Pre-Test
*5 minutes, individual, closed book.*

1. If T ∝ √L, what happens to the relationship when you square both sides? What is T² proportional to?
2. What shape is a graph of T² against L if T² ∝ L?
3. The formula for a pendulum is T = 2π√(L/g). Rearrange to show T² in terms of L and g.

**Answer Key (Pre-Test):**
1. Squaring both sides: T² ∝ L. The square root disappears — it becomes a direct proportion.
2. A straight line through the origin (y = mx, where m is the constant of proportionality).
3. T² = 4π²L/g. So T² = (4π²/g) × L — a straight line with gradient 4π²/g.

## Lesson Flow (45 Minutes)

1. **Settle and Pre-Test (5 min)** — collect slips.
2. **Engage (5 min)** — on the board, sketch what T vs L looks like (a curve — square-root shape). Ask: *how do we test if it is really √L?* The trick: square T and plot T² vs L. If the points fall on a straight line through the origin, the relationship is confirmed. Board the plan.
3. **Explore (15 min)** — each learner computes T² for each row of the class dataset, then plots T² (y-axis, in s²) against L (x-axis, in m). They draw the best-fit straight line, choose two points far apart on the line, and calculate the gradient = rise/run = ΔT²/ΔL. The gradient equals 4π²/g, so g = 4π²/gradient. Each learner computes their g value and writes it on the board.
4. **Explain (8 min)** — consolidate. The class g values should cluster around 9.5–10.2 m/s² (with some scatter from measurement error). Compare with the Unit 4 drop-method result (if available). The pendulum method is usually more accurate because timing 10 swings averages out reaction time, while the drop method requires timing a very short fall. Confront the misconception that "a curve can't tell us anything" — by transforming (squaring T), we turn a curve into a line and extract a physical constant (g) from the gradient.
5. **Post-Test (10 min)** — administer; collect or peer-mark.
6. **Wrap and Homework (2 min)** — takeaway: *straight lines hide inside curves*. Homework: complete the g calculation and compare your value with 9.8 m/s².

## Hands-On Build: T² vs L Graph
*Plot the class data and extract g from the gradient.*

### Parts
- Class dataset from Lesson 248 — copied into notebook
- Graph paper or squared notebook
- Ruler, pencil, eraser
- Calculator (phone)

### Workflow
1. Create a table with three columns: L (m) | T (s) | T² (s²). Fill in L and T from the class dataset.
2. Compute T² = T × T for each row. **Checkpoint:** the T² values should be 0.2–4.0 s² for lengths 0.2–1.0 m.
3. On graph paper, label the x-axis "L (m)" from 0 to 1.0 and the y-axis "T² (s²)" from 0 to 4.0. Choose a scale that fills the page.
4. Plot each (L, T²) point with a small cross. **Checkpoint:** do the points look roughly linear? If one point is far off, check the arithmetic.
5. Draw the best-fit straight line — it should pass through the origin (0, 0).
6. Choose two points on the line far apart (not data points). Calculate gradient = (y₂ − y₁)/(x₂ − x₁). Units: s²/m.
7. Compute g = 4π²/gradient = 39.48/gradient. Write g on the board.

### Common Mistakes
- **Mixing units** — L must be in metres, not cm. 50 cm = 0.50 m. If you plot cm, the gradient changes and g comes out wrong by a factor of 100.
- **Not starting axes at zero** — the line should go through the origin. If axes start at a non-zero value, the visual "through origin" check is lost.
- **Using data points for the gradient** — use two points *on the line*, not the plotted data points. This averages out scatter.
- **Forgetting to square** — T² means T × T, not 2 × T. A period of 1.5 s gives T² = 2.25 s², not 3.0 s.

## Post-Test
*10 minutes, individual.*

1. If T ∝ √L, what is T² proportional to? (mirrors pre-test)
2. What shape is the T² vs L graph? (mirrors pre-test)
3. Your gradient is 4.0 s²/m. Calculate g using g = 4π²/gradient.
4. Why is the pendulum method for finding g often more accurate than the drop method?
5. Challenge: the true value of g is 9.8 m/s². Your class got 9.6. Suggest one reason for the small difference.

**Answer Key (Post-Test):**
1. T² ∝ L — direct proportionality.
2. A straight line through the origin.
3. g = 4π²/4.0 = 39.48/4.0 = 9.87 m/s² ≈ 9.9 m/s².
4. The pendulum method times 10 swings (total ~15–20 s), so the reaction-time error is a small percentage. The drop method times a fall of ~1 m lasting ~0.45 s — the reaction-time error is a large fraction of the measured time.
5. Accept any valid source: air resistance slightly slowing the pendulum (making T slightly too long, so g slightly too small); string not perfectly flexible (stiffness adds a small restoring force); amplitude slightly too large (breaks small-angle approximation, increasing T); measurement error in length.

## Advanced Questions (Ages 14–17)

1. **Q:** Full computation: gradient 0.040 s²/cm → g in m/s². Compare with your Unit 4 drop result.
   **Worked Answer:** Gradient = 0.040 s²/cm = 0.040 × 100 = 4.0 s²/m. g = 4π²/4.0 = 39.48/4.0 = 9.87 m/s². This is within 0.7% of the standard 9.8 m/s². Compare with the Unit 4 drop result (typically 8–11 m/s² with larger scatter) — the pendulum method is more precise because the timing error is spread over many seconds.
2. **Q:** A group's line does not pass through the origin — it crosses the y-axis at 0.2 s². What systematic error could cause this?
   **Worked Answer:** A positive y-intercept means T² is non-zero when L = 0, which is unphysical. Likely cause: the measured length is too short — the pivot has finite size, or the bob's centre is below the point where the string was measured. The effective length is L + ΔL (the "effective pivot point" is above where you measured). The fix: measure from the actual pivot point to the centre of the bob, and account for the bob's radius.
3. **Q:** Explain why squaring T "linearises" the square-root relationship. What general principle does this illustrate?
   **Worked Answer:** If T = k√L, then T² = k²L. The square root is removed by squaring, converting a curve (T vs L) into a line (T² vs L). This illustrates the principle of linearisation: transform one or both variables so the relationship becomes linear, making it easy to extract the gradient and verify the proportionality. It is the same idea as plotting log(y) vs x to linearise an exponential.

## Safety Notes
- No physical hazards in this lesson (graphing only). Ensure pencils and rulers are used safely.

## Teacher Notes
- Prior knowledge: Lesson 248 collected the class dataset. This lesson analyses it graphically. Learners should have seen straight-line graphs in mathematics.
- Differentiation: ages 10–13 focus on plotting and seeing the straight line. Ages 14–17 compute the gradient, extract g, and compare methods.
- Local resource tips: graph paper is ideal, but squared notebook paper works. If neither is available, draw a grid on the board and have the class plot collectively.
- The g value from this lesson is used in Lesson 250 to compare the pendulum and drop methods side by side. Record the class average g on the board for reference.