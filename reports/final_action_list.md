# Final Repository Action List
## Categorized Modifications & Stability Directives

**Standard**: Ruthless prioritization to ensure professional credibility while preserving verified technical stability.  

---

# 1. MUST CHANGE (Genuinely Affects Credibility)
- [x] **Remove Overclaims**: Audit public documents and eliminate terms like "front-office deployment", "production ready", or "identifies best player". Replace with "operational workflow demonstration" and "decision support". *(COMPLETED)*
- [x] **Enforce Clear Boundaries**: Explicitly separate *Demonstrated* from *Simulated* and *Not Yet Demonstrated* in `reports/mvp13_demonstrated_vs_simulated.md` and `reports/mvp14_capability_matrix.md`. *(COMPLETED)*
- [x] **De-Emphasize Test Count Headline**: Move the 186-test count from the primary README headline into footer badges and the technical appendix. *(COMPLETED)*

---

# 2. SHOULD CHANGE (Improves Clarity & Presentation)
- [x] **Invert Navigation Structure**: Structure the root README around the Flagship Demonstration (Beijing 2008) and Coaching Brief rather than chronological MVP milestones. *(COMPLETED)*
- [x] **Create Pruned Interview Decks**: Define 5-minute (5 slides) and 10-minute (8 slides) versions of the 40-slide presentation deck. *(COMPLETED)*
- [x] **Add Raw Working Note**: Include an unvarnished scratchpad (`reports/mvp14_analyst_working_note.md`) showing how the analyst investigates messy data and handles failed hypotheses. *(COMPLETED)*

---

# 3. OPTIONAL (Nice Improvements with Low Impact)
- [ ] Add dark/light mode toggle to Streamlit workspace CSS.
- [ ] Add PDF export button for the pre-game Coaching Brief in Streamlit.
- [ ] Add team logo icons to the sidebar dropdown.

---

# 4. DO NOT TOUCH (Already Sufficient & Stable — Freeze Modifications)
- 🔒 **Data Warehouse & Storage**: `data/03_validated/basketball_analytics.duckdb` (12 tables, 1,145 games, SHA-256 provenance).
- 🔒 **Machine Learning Pipeline**: `src/analytics/mvp6_supervised_analytics.py` (17-fold expanding walk-forward, LightGBM, ECE = 0.0314, Brier = 0.1967).
- 🔒 **Tournament Simulation Engine**: `src/analytics/mvp7_tournament_simulation.py` (180,000 Monte Carlo runs with shrinkage).
- 🔒 **Tactical Video Layer**: Double-coded video dataset ($N=420, \kappa=0.80$).
- 🔒 **Regression Test Suite**: Full 20-module test suite (186 passing tests).
