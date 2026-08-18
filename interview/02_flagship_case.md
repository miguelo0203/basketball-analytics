# 02 — Flagship Case Study Interview Walkthrough
## Talking Through the Beijing 2008 Spain vs. USA Olympic Final

---

### 1. How to Introduce the Case
- *"I chose the Beijing 2008 Olympic Final between Spain and the USA 'Redeem Team' because it perfectly illustrates how an analyst navigates extreme statistical priors, small-sample noise, and tactical contradictions."*

---

### 2. The Core Problem & Numbers
- **Prior Problem**: Spain lost by 37 points in group play. Public consensus was that Spain had no tactical path to victory.
- **Model Baseline**: Pre-game walk-forward LightGBM model favored USA at $73.2\%$ ($P(\text{ESP}) = 26.8\%$, Expected Margin: $-8.5$ pts).
- **Four Factors Discovery**: USA's scoring margin was driven by fast-break transition off live turnovers ($1.42$ pts/poss). In half-court set play, Spain held a $+4.2$ Net Rating advantage.

---

### 3. The Tactical Contradiction & Coaching Inquiry
- **Contradiction**: USA's center dropped deep in P&R coverage to protect the rim, which left wide-open pockets for pick-and-pop trailers.
- **Analyst Output**: Delivered a 1.5-page Pre-Game Brief asking the coaching staff:
  1. *Can we deploy a 2-3 zone to break USA's transition flow?*
  2. *Can Pau and Marc Gasol trail to the 3-point line to pull Howard out of the paint?*

---

### 4. The Outcome & Process Review
- **Final Result**: USA 118 – Spain 107 (11 pts). Spain cut the deficit to 4 points with 2:20 left using the 2-3 zone and pick-and-pop actions.
- **Key Takeaway**: The pre-game analysis did not guarantee a win, but it accurately isolated the critical tactical levers before the game was played.
