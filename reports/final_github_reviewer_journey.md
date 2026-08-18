# Public GitHub Reviewer Journey & Complexity Audit
## Navigating the Portfolio from 2 Minutes to 60 Minutes

**Audience**: Technical Recruiters, Basketball Analytics Directors, Head Coaches  
**Core Standard**: Minimizing Cognitive Overload while Demonstrating Deep Technical Competence  

---

# 1. The "Too Much Project" Complexity Audit

```
+----------------------------------------------------------------------------------------------------+
| POTENTIAL RISK / SYMPTOM      | REPOSITORY STATUS & REMEDIATION                                    |
+----------------------------------------------------------------------------------------------------+
| **Over-Advertising Test Count**| FIXED: 186 tests are kept as a quality badge and in the appendix, |
|                               | but are NOT used as the main headline value proposition.           |
+----------------------------------------------------------------------------------------------------+
| **Chronological Navigation    | FIXED: Public entry points lead with the Flagship Demonstration    |
| Overload (MVP-0 to MVP-14)**  | and Coaching Brief rather than forcing a 15-stage historical tour. |
+----------------------------------------------------------------------------------------------------+
| **Technical Jargon in Coaching| FIXED: Pre-game briefs use plain basketball terms (possession pace,|
| Context**                     | drop depth, foul rate); calibration curves remain in the appendix. |
+----------------------------------------------------------------------------------------------------+
| **Duplicate Reports**         | AUDITED: Earlier MVP reports are preserved in `reports/` for audit  |
|                               | integrity, but public navigation focuses on the top 5 assets.      |
+----------------------------------------------------------------------------------------------------+
```

---

# 2. The Step-by-Step GitHub Reviewer Journey

```
+----------------------------------------------------------------------------------------------------+
| REVIEW TIMELINE | WHAT THE REVIEWER SEES, UNDERSTANDS & INVESTIGATES                               |
+----------------------------------------------------------------------------------------------------+
| **2 Minutes**   | • **Sees**: Clean README with clear WHO / WHAT / WHY / LIMITATION positioning.   |
| (First Glance)  | • **Understands**: This is a basketball data analyst portfolio for coaching      |
|                 |   decision support spanning 20 years of international competitions (2005–2024).|
|                 | • **Action**: Clicks link to Flagship Beijing 2008 Demonstration.                |
+----------------------------------------------------------------------------------------------------+
| **5 Minutes**   | • **Sees**: Flagship Coaching Brief & Streamlit Workspace architecture.          |
| (Exploration)   | • **Understands**: How the analyst takes pre-game data, surfaces tactical        |
|                 |   contradictions (stats vs film), and formulates questions for coaching staff.   |
|                 | • **Action**: Reviews the 32-Question Interview Guide or runs Streamlit locally. |
+----------------------------------------------------------------------------------------------------+
| **15 Minutes**  | • **Investigates**: The underlying code in `src/analytics/` and DuckDB schemas.  |
| (Code Quality)  | • **Understands**: The candidate writes clean, modular Python, uses SQL CTEs,     |
|                 |   enforces strict chronological walk-forward splits, and avoids future leakage.  |
|                 | • **Action**: Inspects `fact_team_game` queries and model validation tests.      |
+----------------------------------------------------------------------------------------------------+
| **30 Minutes**  | • **Convinces**: Checks the 3-Tier Capability Matrix and Coach Pushback script.  |
| (Verification)  | • **Understands**: Candidate has genuine basketball intuition, understands       |
|                 |   shooting variance, respects coaching authority, and communicates with humility.|
|                 | • **Action**: Decides candidate is ready for an initial technical screen.        |
+----------------------------------------------------------------------------------------------------+
| **60 Minutes**  | • **Deep Audit**: Runs full pytest suite, reviews Econometric ITS study and      |
| (Due Diligence) |   double-coded qualitative film metrics ($\kappa = 0.80$).                       |
|                 | • **Conclusion**: Flawless execution. No data leakage or overclaims found.       |
+----------------------------------------------------------------------------------------------------+
```
