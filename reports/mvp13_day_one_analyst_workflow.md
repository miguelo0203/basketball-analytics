# The First 30 Days: Professional Club Analyst Integration Plan
## Operational Roadmap for a Basketball Data Analyst Joining a Coaching Staff

**Status**: Formally Certified Operational Integration Plan  
**Core Philosophy**: Integration with coaching staff and practical tactical utility over technology for technology's sake.  

---

# Phase 1: Days 1–3 — Listen, Learn & Establish Common Language

- **Understand Coaching Philosophy**: Meet with the Head Coach and lead assistants to understand their core offensive/defensive principles (e.g. drop vs. switch P&R, transition pace, offensive rebounding philosophy).
- **Adopt Coaching Terminology**: Align analytical metrics with the staff's existing vocabulary (e.g. if the coach calls middle P&R "side roll" or "flat hedge", the analyst's briefs must adopt those exact terms).
- **Map Decision Cadence**: Identify when the staff needs opponent scouting reports (e.g. 48 hours pre-game), when video meetings happen, and how half-time debriefs operate.
- **Audit Existing Reporting**: Review the reports the staff currently receives to identify what they find useful and what they ignore due to information overload.

---

# Phase 2: Week 1 — Data Infrastructure & Workflow Audit

- **Audit Available Data Feeds**: Inspect current club data sources (Synergy, Second Spectrum optical tracking, domestic league play-by-play, Catapult GPS load data).
- **Check Data Quality & Integrity**: Verify data pipeline latency, missing game entries, and coordinate tracking accuracy.
- **Map Player Evaluation Processes**: Understand how the sporting director and scouting staff evaluate domestic and international targets.
- **Identify Tactical Blind Spots**: Note areas where the coaching staff expresses frustration (e.g. *"We don't know why our bench lineup gives up runs in the 2nd quarter"*).

---

# Phase 3: Week 2 — Deliver One High-Impact Repeatable Pipeline

- **Automate One Repeatable Opponent Brief**: Build a clean, automated 2-page pre-game scouting template integrating Four Factors baselines and P&R tendencies.
- **Create a Reliable Data Pipeline**: Connect raw league play-by-play feeds into an internal DuckDB/Parquet feature store with automated daily updates.
- **Build One Simple Rotation Dashboard**: Implement a clean lineup Net Rating dashboard that explicitly displays possession-level sample size confidence intervals ($\text{Poss} \ge 100$ vs. $<30$).

---

# Phase 4: Week 3 — Coaching Feedback & Usability Validation

- **Observe Brief Usage**: Sit in pre-game scouting meetings to see which sections of the brief the coaching staff references during film sessions.
- **Prune Unnecessary Complexity**: If the staff ignores synthetic advanced metrics (e.g. composite fit scores), immediately replace them with concrete basketball possession counts (e.g. points per P&R possession).
- **Validate Uncertainty Communication**: Ensure coaches understand that a 65% win probability represents a baseline model expectation with natural shooting variance, not a guaranteed victory.

---

# Phase 5: Week 4 — Institutionalize the Workflow & Plan Future Roadmap

- **Standardize the Game-Week Workflow**:
  * $T-2$ Days: Opponent Scouting Profile delivered to lead assistant.
  * $T-1$ Day: Matchup Brief & P&R tactical video notes reviewed in coaching meeting.
  * Game Day: 1-page starting lineup and variance cheat sheet on the coach's desk.
  * Post-Game: Objective process review evaluating deviation from pre-game priors.
- **Deliver Documented Methodology**: Hand off documentation ensuring all pipelines and metric definitions are fully auditable.
- **Present 6-Month Roadmap**: Propose future analytics developments (e.g. integrating optical tracking defensive contest metrics, custom shot quality models).
