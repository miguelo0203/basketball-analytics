# Final Pre-Publication Action List
## Strategic Roadmap for Job Applications & Repository Maintenance

**Status**: Formally Certified Release Action List  

---

# 1. MUST DO BEFORE PUBLICATION (Completed)
- [x] **Remove All Overclaims**: Eliminate terms like "production deployment" or "AI coach"; ensure only GREEN and qualified YELLOW claims appear. *(COMPLETED)*
- [x] **Deploy Public Career & Interview Packages**: Populate `career/` and `interview/` directories with CV bullets, LinkedIn posts, and Q&A guides. *(COMPLETED)*
- [x] **Verify 100% Test Pass Rate**: Ensure all 186 unit/regression tests pass deterministically. *(COMPLETED)*
- [x] **Curate Public Figures**: Place 5 high-impact public figures in `portfolio/figures/` with `portfolio/figure_guide.md`. *(COMPLETED)*

---

# 2. SHOULD DO BEFORE FIRST APPLICATION (Completed)
- [x] **Publish LinkedIn Case Study**: Post `portfolio/linkedin_case_study.md` on LinkedIn targeting sports analytics directors. *(READY)*
- [x] **Add GitHub Badges**: Ensure public README contains verified DuckDB, Python 3.14, and Pytest passing badges. *(COMPLETED)*
- [x] **Verify Streamlit Demo Command**: Confirm `streamlit run src/analytics/mvp10_analyst_workspace.py -- streamlit` launches smoothly. *(COMPLETED)*

---

# 3. CAN DO LATER (Low Priority / Post-Interview)
- [ ] Record a 3-minute Loom / YouTube video walkthrough embedded in `portfolio/README.md`.
- [ ] Connect DuckDB warehouse to a sample public EuroLeague play-by-play scraper for modern 2025 matches.
- [ ] Add PDF export button to the Streamlit workspace.

---

# 4. DO NOT SPEND MORE TIME ON (Diminishing-Return Traps)
- ❌ **DO NOT build MVP-15 or MVP-16**: The analytical stack is complete; adding more MVPs creates complexity fatigue.
- ❌ **DO NOT train Deep Learning / Neural Network models**: Adding PyTorch/TensorFlow adds zero credibility for a junior basketball analytics role where tabular Four Factors and calibrated tree models are industry standard.
- ❌ **DO NOT fabricate live optical tracking / player coordinates**: Second Spectrum telemetry without real club licensing damages candidate credibility.
- ❌ **DO NOT create fake domestic club salary cap / transfer market tools**: The dataset is senior national team tournament basketball.
- ❌ **DO NOT write additional tests solely to inflate test count**: 186 tests already establishes engineering discipline.
