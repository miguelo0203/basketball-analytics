# Comprehensive 32-Question Interview Preparation Master List
## International Basketball Historical Analytics (2005–2025)

**Status**: Formally Certified Interview Question Package  
**Target Roles**: Basketball Data Analyst, Analytics Manager, Data Scientist, Sporting Decision Support Lead  

---

# Category 1: Basketball & Coaching Staff Interaction (8 Questions)

1. What would you actually deliver to a Head Coach on match eve?
2. How do you translate a complex predictive model into an actionable coaching brief?
3. What do you do when your statistical model and your video film observations disagree?
4. Why should an experienced basketball coach trust your analysis over their own intuition?
5. What do you do if the coaching staff completely rejects your pre-game recommendation?
6. How do you communicate statistical uncertainty without making the staff lose confidence in the numbers?
7. Which single metric would you remove from your report if the coaching staff told you it was too complicated?
8. How does your system evaluate a player who has low boxscore scoring volume but elite defensive spacing gravity?

---

# Category 2: Data Science & Quantitative Methodology (8 Questions)

9. Why did you select LightGBM over Deep Learning, Logistic Regression, or XGBoost?
10. Why did you use an expanding 17-fold chronological walk-forward cross-validation scheme?
11. What is the Brier Score, and why is it superior to classification accuracy in basketball modeling?
12. What is Expected Calibration Error (ECE), and how did you calibrate your probabilities?
13. Why did you use a non-parametric clustered bootstrap instead of standard parametric confidence intervals?
14. What is the purpose of permutation testing and Benjamini-Hochberg False Discovery Rate (FDR) control?
15. What does TreeSHAP feature importance tell us, and why is it NOT a causal treatment effect?
16. How did you verify that zero future tournament or post-game target leakage entered your feature store?

---

# Category 3: Data Engineering & Systems Architecture (8 Questions)

17. Why did you build the core warehouse using DuckDB and Parquet instead of PostgreSQL, SQLite, or Pandas?
18. How did you validate data provenance and ensure that historical FIBA records remained immutable?
19. How did you handle duplicate player records and entity resolution across international tournaments?
20. How do you ensure mathematical reconciliation between game boxscores and player-game sums?
21. What data quality constraints prevent incomplete or corrupted tournament games from entering production?
22. How did you achieve 100% deterministic reproducibility across your entire pipeline?
23. How would you scale this pipeline if you were suddenly given millions of optical tracking telemetry rows?
24. Why did you write 160 automated pytest regression tests for an analytics portfolio?

---

# Category 4: Professional Realism & Organizational Context (8 Questions)

25. What data and infrastructure would you need from a real club on Day 1 to deploy this workflow?
26. What analytical systems would you build in your first 30 days on the job?
27. What are the key things this historical national team project CANNOT demonstrate?
28. How does your communication style change when briefing a Head Coach vs. a Sporting Director?
29. How do you handle missing player availability information (e.g. late injury scratch 10 minutes before tip-off)?
30. How do you evaluate your own performance after a game if your favored team loses an upset?
31. Why did you choose K=6 player archetypes, and how do you prevent post-clustering double-dipping?
32. What is the central value proposition of a basketball data analyst in a professional sports franchise?
