# MVP-14 Pre-Implementation Adversarial Gap Analysis
## Professional Basketball Club Analyst Employability Audit

**Status**: Formally Certified Gap Analysis  
**Audit Question**: *"If an experienced basketball club analyst, coach, or data science director reviewed this repository tomorrow, what would convince them I can contribute, and what would make them doubt?"*  
**Date**: 2026-08-18  

---

# 1. What Convinces a Professional Basketball Organization?

```
+----------------------------------------------------------------------------------------------------+
| CONVINCING CAPABILITY DEMONSTRATED          | EVIDENCE IN REPOSITORY                               |
+----------------------------------------------------------------------------------------------------+
| **1. Complete Data Pipeline Competence**    | Provenance from immutable raw files (SHA-256) to     |
|                                             | DuckDB relational tables and Parquet feature stores. |
+----------------------------------------------------------------------------------------------------+
| **2. Basketball Domain Fluency**            | Deep understanding of Four Factors, Net Rating,      |
|                                             | True Shooting, P&R drop coverage, and floor spacing. |
+----------------------------------------------------------------------------------------------------+
| **3. Methodological Rigor & No Leakage**    | Expanding 17-fold chronological walk-forward ML;     |
|                                             | out-of-sample probability calibration (ECE = 0.0314).|
+----------------------------------------------------------------------------------------------------+
| **4. Tactical-Quantitative Synergy**        | Double-coded qualitative film coding (N=420, κ=0.80) |
|                                             | integrated with statistical models.                  |
+----------------------------------------------------------------------------------------------------+
| **5. Humility & Decision-Support Framing**  | Rejects AI replacement claims; delivers structured   |
|                                             | coaching questions; quarantines anti-hindsight state.|
+----------------------------------------------------------------------------------------------------+
```

---

# 2. What Would Make Them Doubt? (Remaining Risks)

```
+----------------------------------------------------------------------------------------------------+
| POTENTIAL SKEPTICISM / DOUBT                | ADVERSARIAL ROOT CAUSE & HOW WE ADDRESS IT           |
+----------------------------------------------------------------------------------------------------+
| **"Is this purely academic modeling?"**     | Risk that the analyst only cares about Brier scores. |
|                                             | *Fix*: Deliver standardized 1–2 page Coaching Briefs |
|                                             | focused on possession counts and tactical matchups.  |
+----------------------------------------------------------------------------------------------------+
| **"Can the candidate handle coach pushback?"| Risk that the analyst will argue stubbornly over ML. |
|                                             | *Fix*: Create a realistic Coach Pushback Simulation  |
|                                             | showing how to investigate discrepancies with film.  |
+----------------------------------------------------------------------------------------------------+
| **"Does the candidate know their limits?"**  | Risk of confusing portfolio work with club work.     |
|                                             | *Fix*: Publish an explicit 3-tier Capability Matrix. |
+----------------------------------------------------------------------------------------------------+
```

---

# 3. The Single Biggest Remaining Weakness

The remaining weakness was not technical—it was **demonstrating the internal investigation process**:
- Previous MVPs showcased polished conclusions, calibrated tables, and automated briefs.
- What hiring managers want to see is **how the analyst thinks when the data is messy, when an initial hypothesis fails, and when numbers contradict intuition**.
- **Solution in MVP-14**: Create an unpolished **Analyst Working Note** detailing initial assumptions, surprising discoveries, and what was intentionally left out of the coaching brief.

---

# 4. What Should NOT Be Built

- **NO New ML Models / Deep Learning**: Adding neural nets or XGBoost adds zero domain credibility.
- **NO Fabricated Live Club Telemetry**: Faking Second Spectrum XYZ tracking without proprietary data damages trust.
- **NO Transfer Market Scenarios**: Spanish national team tournament data cannot legitimately model domestic club contract buyouts or salary caps.
- **NO Additional Test Count Inflation**: The existing 169-test suite already proves engineering rigor.
