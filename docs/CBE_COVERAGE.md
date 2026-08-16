# CBE Coverage Matrix

How the 365 lessons of Grounded Classical Mechanics map to Kenya's Competency
Based Education (CBE) curriculum designs (KICD). Senior School references are the
Grade 10 Physics Curriculum Design (KICD, 2025); Junior School and Upper Primary
references are the Integrated Science and Science & Technology designs (Force &
Energy strands).

> **Scope note.** This course is the *mechanics spine* of CBE physics. Strand 1.0
> (Mechanics and Thermal Physics), wave motion under 2.1, and the energy/climate
> outcomes of 4.1 are covered directly through daily hands-on lessons. Electricity
> & Magnetism (3.x), Optics, Radioactivity (2.2) and Thermal Physics (1.4) are
> touched only where they meet mechanics (altitude boiling, hot-air buoyancy,
> dynamo teaser) and are flagged for the companion volume.

| CBE code | Strand / sub-strand | Lessons | Count |
|---|---|---|---|
| `G10-PHY-1.1` | Introduction to Physics (Senior School G10) | 1, 2, 3, 5, 7, 10, 16, 17, 18, 19, 24, 26, 31, 131, 135, 136, 146, 200, 211, 245, 250, 252, 280, 282, 296, 303, 313, 315, 320, 323, 333, 350, 356, 357, 360, … | 37 |
| `G10-PHY-1.2` | Pressure (Senior School G10) | 13, 14, 15, 25, 92, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 18… | 79 |
| `G10-PHY-1.3` | Mechanical Properties of Materials (Senior School G10) | 29, 37, 43, 105, 256, 259, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 294, 295, 296, 297, 298, 299, 300, 310, 355, 359 | 31 |
| `G10-PHY-1.4` | Temperature and Thermal Expansion (Senior School G10) | 117, 167, 181, 222 | 4 |
| `G10-PHY-1.5` | Moments and Equilibrium (Senior School G10) | 9, 33, 42, 49, 50, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 150, 152, 156, 239, 291, 292, 293, 294, 297, 300, 352 | 27 |
| `G10-PHY-1.6` | Energy, Work, Power and Machines (Senior School G10) | 36, 48, 89, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 117, 118, 119, 120, 121, 123, 124, 125, 126, 134, 137, 138, 139, 1… | 91 |
| `G10-PHY-2.1` | Properties of Waves (Senior School G10) | 243, 249, 251, 254, 256, 257, 258, 259, 260, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 354, 355 | 31 |
| `G10-PHY-4.1` | Greenhouse Effect and Climate Change (Senior School G10) | 107, 111, 113, 114, 115, 116, 122, 168, 188, 204, 205, 299, 301, 302, 303, 305, 317, 323, 325, 326, 327, 328, 345, 363 | 24 |
| `G10-PHY-4.2` | Introduction to Space Physics (Senior School G10) | 96 | 1 |
| `JS-FE` | Junior School Integrated Science — Force & Energy (G7–9) | 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,… | 208 |
| `UP-FE` | Upper Primary Science & Technology — Force & Energy (G4–6) | 2, 4, 6, 8, 11, 12, 20, 22, 23, 24, 26, 27, 28, 30, 32, 34, 35, 38, 39, 41, 45, 51, 52, 53, 55, 60, 66, 69, 74, 75, 76, 78, 80, 85, 86, 87, 95, 112, 115, 141… | 55 |

## Reading the matrix

- Every lesson carries at least one code; most carry two (a senior-school anchor
  plus the junior/primary strand it consolidates).
- `JS-FE` and `UP-FE` appear throughout by design: the course spirals, revisiting
  junior concepts with senior-school mathematics in the Advanced Questions.
- Generate this file: `python tools/coverage.py` (do not edit by hand).
