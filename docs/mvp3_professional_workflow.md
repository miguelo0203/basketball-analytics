# Professional Basketball Analytics & Scouting Workflow
## End-to-End Decision-Support Pipeline from Raw Data to Scouting Decision

```
QUESTION
   ↓
DATA ACQUISITION & RAW PROVENANCE (SHA-256)
   ↓
ENTITY RESOLUTION & DETERMINISTIC CANONICAL IDENTITIES
   ↓
ACCOUNTING & BALL-MATH VALIDATION (SUM(Player) == Team Total)
   ↓
DIMENSIONAL FEATURE ENGINEERING & NORMALIZATION
   ↓
FUNCTIONAL ROLE DISCOVERY (Hybrid Domain Clustering)
   ↓
MULTI-DIMENSIONAL COMPARABLES & SIMILARITY DECOMPOSITION
   ↓
RECRUITMENT FIT SCORING & TRADE-OFF EXPOSURE
   ↓
SAMPLE-SIZE CONFIDENCE & UNCERTAINTY GOVERNANCE
   ↓
STRUCTURED VIDEO SCOUTING HYPOTHESES ("What Data Says" vs "What Requires Video")
   ↓
FINAL FRONT-OFFICE / COACHING DECISION
```

---

## 1. Stage-by-Stage Operational Protocol

### Stage 1: Tactical Question Definition
- **Objective**: Translate a coaching or front-office need into measurable basketball hypotheses.
- **Example**: *"We need a secondary playmaker who spaces the floor and defends opposing primary guards without fouling."*

### Stage 2: Data Acquisition & Accounting Gatekeeper
- **Standard**: Ingest real tournament squad rosters and match records with immutable SHA-256 provenance.
- **Validation**: Enforce ball-math accounting ($\sum PTS = Team\_PTS$) and exact minute reconciliation ($(200 + 25 \times OT) \times 60$ seconds).

### Stage 3: Player Representation & Dimension Engineering
- **Standard**: Convert raw boxscore counting numbers into pace-adjusted per-40 rates ($PTS/40, FGA/40, STL/40, BLK/40$) and normalized percentage efficiencies ($TS\%, eFG\%, 3PAr, AST\%, TOV\%, ORB\%, DRB\%$).
- **Context**: Standardize metrics across qualified rotation players ($MIN \ge 40, G \ge 3$) to prevent noise from end-of-bench garbage time stints.

### Stage 4: Functional Role Discovery
- **Standard**: Discard nominal positions (1–5) and classify players into 6 functional archetypes based on on-court actions:
  - *Primary Initiator / Floor General*
  - *Two-Way Scoring Wing / Slasher*
  - *Perimeter Movement Shooter / Spacer*
  - *Stretch Big / Pick-and-Pop Forward*
  - *Low-Block Anchor / Interior Scorer*
  - *Rim Protector / Roll Threat & Anchor*

### Stage 5: Similarity Engine & Historical Comparables
- **Standard**: Given a target player, calculate weighted multi-dimensional distance against the historical international player universe ($N = 3,767$ qualified campaigns) and decompose the primary alignment drivers.

### Stage 6: Recruitment Shortlisting & Trade-Off Exposure
- **Standard**: Filter candidates by age, role, and minimum minutes, score them via weighted multi-attribute utility functions, and highlight trade-offs (e.g. Volume vs Efficiency, Playmaking vs Turnovers).

### Stage 7: The Scouting Bridge & Video Sampling
- **Standard**: Formulate structured **Video Scouting Hypotheses** (`[HIPÓTESIS PARA VÍDEO]`) specifying exact clip sampling criteria (e.g. pick-and-roll coverage reads, contested catch-and-shoot mechanics, screen navigation).

### Stage 8: Decision Support
- **Standard**: Deliver an evidence-based Player Evaluation Dossier explicitly separating quantitative evidence from qualitative film study.
