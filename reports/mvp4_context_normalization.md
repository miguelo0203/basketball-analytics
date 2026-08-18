# MVP-4 Context Normalization & Tournament Environment Adjustments
## International Basketball Historical Analytics (2005–2025)

---

## 1. The Rationale for Context Normalization

In international tournament basketball, comparing unadjusted boxscore statistics across different competitions, eras, and federations introduces severe contextual bias:
1. **Competition Pace Variations**: EuroBasket 2007 operated at an average pace of $71.7\text{ poss/40m}$, whereas the Paris 2024 Olympic tournament operated at $83.7\text{ poss/40m}$ ($+16.7\%$ more possession opportunities per 40 minutes).
2. **Regulatory Era Shifts**: The 2010 3-point line shift (6.25m to 6.75m) and the 2014 shot-clock reset modification (14 seconds on offensive rebounds) structurally altered shooting and turnover baselines.
3. **Competition Tier Talent Density**: Olympic rosters (12 elite nations) have higher talent concentration than 24-team EuroBaskets or 32-team World Cups.

---

## 2. Implemented Context Transformations

For every player campaign in `mart_player_roles.parquet`, we computed **tournament-relative standardized deviations** ($Z_{\text{tourney}}$) and **competition-year percentile ranks**:

$$Z_{\text{tourney}}(X_{it}) = \frac{X_{it} - \bar{X}_t}{\sigma_t}$$

Where:
- $X_{it}$: Observed metric value for player $i$ in tournament edition $t$.
- $\bar{X}_t$: Mean metric value across all qualified rotation players in tournament $t$.
- $\sigma_t$: Standard deviation across all qualified rotation players in tournament $t$.

---

## 3. Preserved Provenance & Data Integrity

```
+---------------------------------------------------------------------------------------------------+
| RAW VARIABLE            | TRANSFORMED CONTEXT VARIABLE      | TRANSFORMATION METHOD               |
+---------------------------------------------------------------------------------------------------+
| `ts_pct`                | `z_tourney_ts_pct`, `pctile_ts_pct`| Tournament Z-score & Edition Rank   |
| `three_point_rate`      | `z_tourney_three_point_rate`      | Tournament Z-score & Edition Rank   |
| `ast_pct_est`           | `z_tourney_ast_pct_est`           | Tournament Z-score & Edition Rank   |
| `stl_per_40`            | `z_tourney_stl_per_40`            | Tournament Z-score & Edition Rank   |
| `pts_per_40`            | `z_tourney_pts_per_40`            | Tournament Z-score & Edition Rank   |
+---------------------------------------------------------------------------------------------------+
```

> [!IMPORTANT]
> Context-normalized transformations do NOT overwrite the raw observed variables. Both layers exist simultaneously in `mart_player_roles.parquet` to allow transparent auditing.
