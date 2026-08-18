"""Publication-Quality Visual Analytics Engine for MVP-4.

Generates decision-support visual artifacts:
1. fig1_candidate_universe_funnel.png
2. fig2_recruitment_fit_matrix.png
3. fig3_shortlist_stability_heatmap.png
4. fig4_role_space_shortlist_scatter.png
5. fig5_reliability_vs_performance.png
6. fig6_candidate_profile_cards.png
"""

from pathlib import Path
from typing import Dict, List, Any
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from src.config import ANALYTICS_DATA_DIR, REPORTS_DIR

FIGURES_DIR = REPORTS_DIR / "figures" / "mvp4"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)


class ScoutingVisualAnalyticsEngine:
    """Generates publication-quality charts for decision support and shortlist validation."""

    def __init__(self, data_dir: Path = ANALYTICS_DATA_DIR):
        from src.analytics.mvp4_decision_support import ScoutingDecisionSupportEngine
        self.engine = ScoutingDecisionSupportEngine(data_dir=data_dir)
        self.df = self.engine.df

        plt.rcParams.update({
            "font.sans-serif": "Arial",
            "font.family": "sans-serif",
            "axes.edgecolor": "#333333",
            "axes.linewidth": 0.8,
            "grid.color": "#EAEAEA",
            "grid.linestyle": "--",
            "grid.linewidth": 0.5,
        })

    def generate_all_figures(self) -> Dict[str, Path]:
        """Generate all 6 required publication figures for MVP-4."""
        paths = {}

        # -------------------------------------------------------------
        # Figure 1: Candidate Universe Funnel
        # -------------------------------------------------------------
        stages = [
            "Total Database\nCampaigns\n(N = 4,350)",
            "Eligible Sample\n(MIN >= 40, G >= 3)\n(N = 3,767)",
            "Tactical Screen\n(Mandatory Criteria)\n(N = 142)",
            "Stage 1 Pool\n(Ranked Fit)\n(N = 20)",
            "Stage 2 Shortlist\n(Reliability Filter)\n(N = 10)",
            "Stage 3 Final Dossiers\n(Scouting Candidates)\n(N = 5)"
        ]
        counts = [4350, 3767, 142, 20, 10, 5]
        colors = ["#2b5c8f", "#386cb0", "#41b6c4", "#7fc97f", "#fdc086", "#d95f02"]

        fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
        y_pos = np.arange(len(stages))[::-1]
        bars = ax.barh(y_pos, counts, color=colors, edgecolor="#333333", height=0.65)

        for bar, count in zip(bars, counts):
            ax.text(bar.get_width() + 40, bar.get_y() + bar.get_height()/2, f"{count:,}",
                    va="center", ha="left", fontsize=9.5, fontweight="bold", color="#222222")

        ax.set_yticks(y_pos)
        ax.set_yticklabels(stages, fontsize=9, fontweight="semibold")
        ax.set_xlabel("Number of Player-Tournament Campaigns", fontsize=10, fontweight="bold")
        ax.set_title("Multi-Stage Scouting Decision Funnel: Candidate Selection (2005–2025)", fontsize=12, fontweight="bold", pad=12)
        ax.grid(True, axis="x")
        fig.tight_layout()
        f1_p = FIGURES_DIR / "fig1_candidate_universe_funnel.png"
        plt.savefig(f1_p)
        plt.close()
        paths["fig1"] = f1_p

        # -------------------------------------------------------------
        # Figure 2: Recruitment Fit Matrix Heatmap (Cases A, B, C)
        # -------------------------------------------------------------
        # Execute the 3 recruitment cases
        res_a = self.engine.execute_recruitment_workflow(
            case_name="Case A: Secondary Creation Wing",
            target_roles=["Wing", "Spacer"],
            min_age=20, max_age=32, min_height=192,
            mandatory_filters={"three_point_rate": 0.35, "ts_pct": 0.50, "ast_pct_est": 0.10, "stl_per_40": 0.8},
            weights={"z_dim_perimeter_orientation": 1.2, "z_dim_creation": 1.2, "z_dim_scoring_efficiency": 1.1, "z_dim_defense": 1.1, "z_dim_scoring_volume": 0.8},
            min_minutes=80.0
        )
        res_b = self.engine.execute_recruitment_workflow(
            case_name="Case B: Defensive / Spacing Guard",
            target_roles=["Spacer", "Initiator"],
            min_age=20, max_age=32, min_height=180,
            mandatory_filters={"three_point_rate": 0.45, "ts_pct": 0.52, "stl_per_40": 1.0},
            weights={"z_dim_perimeter_orientation": 1.5, "z_dim_scoring_efficiency": 1.3, "z_dim_defense": 1.3, "z_dim_creation": 0.6, "z_dim_scoring_volume": 0.8},
            min_minutes=80.0
        )
        res_c = self.engine.execute_recruitment_workflow(
            case_name="Case C: Stretch / Connector Forward",
            target_roles=["Stretch Big", "Interior"],
            min_age=21, max_age=34, min_height=202,
            mandatory_filters={"three_point_rate": 0.25, "ts_pct": 0.52},
            weights={"z_dim_perimeter_orientation": 1.3, "z_dim_rebounding": 1.3, "z_dim_scoring_efficiency": 1.2, "z_dim_defense": 0.8, "z_dim_scoring_volume": 0.9},
            min_minutes=80.0
        )

        matrix_data = []
        labels_y = []
        dim_headers = ["Scoring Vol", "Efficiency", "3P Gravity", "Creation", "Rebounding", "Defense", "Fit (0-100)"]

        for case_label, res in [("Case A (Wing)", res_a), ("Case B (Guard)", res_b), ("Case C (Big)", res_c)]:
            for d in res["stage3_dossiers"][:3]:
                labels_y.append(f"[{case_label[:6]}] {d['full_canonical_name']} ({d['team_id']})")
                p_row = self.df[self.df["player_tournament_id"] == d["player_tournament_id"]].iloc[0]
                matrix_data.append([
                    p_row["z_dim_scoring_volume"],
                    p_row["z_dim_scoring_efficiency"],
                    p_row["z_dim_perimeter_orientation"],
                    p_row["z_dim_creation"],
                    p_row["z_dim_rebounding"],
                    p_row["z_dim_defense"],
                    d["fit_index_100"] / 25.0 - 2.0  # normalized for visual scale
                ])

        fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
        cax = ax.imshow(matrix_data, cmap="coolwarm", aspect="auto", vmin=-2.5, vmax=2.5)

        for i in range(len(labels_y)):
            for j in range(len(dim_headers)):
                val = matrix_data[i][j]
                ax.text(j, i, f"{val:+.1f}", ha="center", va="center", color="#111111" if abs(val)<1.4 else "#ffffff", fontsize=8.5, fontweight="bold")

        ax.set_xticks(np.arange(len(dim_headers)))
        ax.set_xticklabels(dim_headers, fontsize=9.5, fontweight="bold")
        ax.set_yticks(np.arange(len(labels_y)))
        ax.set_yticklabels(labels_y, fontsize=9, fontweight="semibold")
        ax.set_title("Recruitment Candidate Multi-Dimensional Alignment Matrix", fontsize=12, fontweight="bold", pad=12)
        fig.colorbar(cax, ax=ax, label="Standardized Z-Score Deviation", fraction=0.03, pad=0.03)
        fig.tight_layout()
        f2_p = FIGURES_DIR / "fig2_recruitment_fit_matrix.png"
        plt.savefig(f2_p)
        plt.close()
        paths["fig2"] = f2_p

        # -------------------------------------------------------------
        # Figure 3: Shortlist Stability Heatmap
        # -------------------------------------------------------------
        top_candidates = [d["full_canonical_name"] for d in res_a["stage3_dossiers"]]
        stab_df = self.engine.evaluate_shortlist_robustness("Case A", ["Wing"], top_candidates)

        spec_cols = [
            "Baseline Specification", "Strict Efficiency (TS% >= 55%)",
            "High Sample Only (MIN >= 120)", "EuroBasket Only", "Post-2010 Era Only"
        ]
        stab_matrix = []
        for _, row in stab_df.iterrows():
            stab_matrix.append([1.0 if row[c] == "YES" else 0.0 for c in spec_cols])

        fig, ax = plt.subplots(figsize=(9, 4.5), dpi=300)
        cax = ax.imshow(stab_matrix, cmap="YlGn", aspect="auto", vmin=0, vmax=1)

        for i in range(len(top_candidates)):
            for j in range(len(spec_cols)):
                txt = "SURVIVES" if stab_matrix[i][j] == 1.0 else "EXCLUDED"
                col = "#00441b" if stab_matrix[i][j] == 1.0 else "#7f0000"
                ax.text(j, i, txt, ha="center", va="center", color=col, fontsize=8.5, fontweight="bold")

        ax.set_xticks(np.arange(len(spec_cols)))
        ax.set_xticklabels([c.replace(" ", "\n") for c in spec_cols], fontsize=8.5, fontweight="bold")
        ax.set_yticks(np.arange(len(top_candidates)))
        ax.set_yticklabels(top_candidates, fontsize=9.5, fontweight="bold")
        ax.set_title("Counterfactual Robustness: Candidate Shortlist Stability Across Specifications", fontsize=11, fontweight="bold", pad=12)
        fig.tight_layout()
        f3_p = FIGURES_DIR / "fig3_shortlist_stability_heatmap.png"
        plt.savefig(f3_p)
        plt.close()
        paths["fig3"] = f3_p

        # -------------------------------------------------------------
        # Figure 4: Role-Space Shortlist Scatter
        # -------------------------------------------------------------
        fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
        df_qual = self.df[self.df["reliability_tier"] != "INSUFFICIENT SAMPLE"]

        ax.scatter(df_qual["three_point_rate"] * 100, df_qual["ast_pct_est"] * 100,
                   color="#cccccc", alpha=0.35, s=20, label="International Population (N=3,767)")

        # Highlight shortlisted candidates
        for d in res_a["stage3_dossiers"]:
            m = d["metrics"]
            ax.scatter(m["three_point_rate"] * 100, m["ast_pct_est"] * 100, color="#d95f02", s=85, edgecolors="#000000", linewidth=1.2, zorder=5)
            ax.annotate(f"{d['full_canonical_name']}\n({d['team_id']} {d['year']})",
                        (m["three_point_rate"] * 100 + 1, m["ast_pct_est"] * 100 + 0.5),
                        fontsize=8, fontweight="bold", bbox=dict(boxstyle="round,pad=0.2", fc="#ffffff", ec="#333333", alpha=0.85))

        ax.set_title("Shortlisted Candidates in International Tactical Space (3PAr vs Creation)", fontsize=12, fontweight="bold", pad=12)
        ax.set_xlabel("3-Point Attempt Rate (3PAr %)", fontsize=10, fontweight="bold")
        ax.set_ylabel("Estimated Assist Rate (AST %)", fontsize=10, fontweight="bold")
        ax.legend(loc="upper left", fontsize=8.5)
        ax.grid(True)
        fig.tight_layout()
        f4_p = FIGURES_DIR / "fig4_role_space_shortlist_scatter.png"
        plt.savefig(f4_p)
        plt.close()
        paths["fig4"] = f4_p

        # -------------------------------------------------------------
        # Figure 5: Reliability vs Performance
        # -------------------------------------------------------------
        fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
        tier_colors = {
            "HIGH RELIABILITY": "#2ca02c",
            "MODERATE RELIABILITY": "#1f77b4",
            "LIMITED SAMPLE": "#ff7f0e",
        }

        stage1_df = res_a["stage1_top20_df"]
        for tier, grp in stage1_df.groupby("reliability_tier"):
            ax.scatter(grp["total_minutes"], grp["fit_index_100"],
                       color=tier_colors.get(tier, "#888888"), s=75, label=f"{tier} (N={len(grp)})", edgecolors="#333333", alpha=0.85)

        for _, r in stage1_df.head(5).iterrows():
            ax.annotate(f"{r['full_canonical_name']} ({r['team_id']})", (r["total_minutes"] + 2, r["fit_index_100"] - 0.5),
                        fontsize=8, fontweight="bold")

        ax.set_title("Candidate Recruitment Fit Index vs Sample Duration (Case A: Playmaking Wings)", fontsize=12, fontweight="bold", pad=12)
        ax.set_xlabel("Tournament Total Minutes Played", fontsize=10, fontweight="bold")
        ax.set_ylabel("Recruitment Fit Index (0–100)", fontsize=10, fontweight="bold")
        ax.axvline(150, color="#2ca02c", linestyle=":", label="High Reliability Threshold (150 MIN)")
        ax.axvline(90, color="#1f77b4", linestyle=":", label="Moderate Reliability Threshold (90 MIN)")
        ax.legend(loc="lower right", fontsize=8.5)
        ax.grid(True)
        fig.tight_layout()
        f5_p = FIGURES_DIR / "fig5_reliability_vs_performance.png"
        plt.savefig(f5_p)
        plt.close()
        paths["fig5"] = f5_p

        # -------------------------------------------------------------
        # Figure 6: Candidate Profile Cards (Spider Radar for Case Winners)
        # -------------------------------------------------------------
        categories = ["Scoring Vol", "Efficiency", "3P Gravity", "Creation", "Rebounding", "Defense", "Usage"]
        N_cat = len(categories)
        angles = [n / float(N_cat) * 2 * np.pi for n in range(N_cat)]
        angles += angles[:1]

        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(14, 5), subplot_kw=dict(polar=True), dpi=300)
        cand_axes = [(res_a["stage3_dossiers"][0], ax1, "#d62728", "Case A: Creation Wing"),
                     (res_b["stage3_dossiers"][0], ax2, "#1f77b4", "Case B: Spacing Guard"),
                     (res_c["stage3_dossiers"][0], ax3, "#2ca02c", "Case C: Stretch Big")]

        feature_cols = [
            "z_dim_scoring_volume", "z_dim_scoring_efficiency",
            "z_dim_perimeter_orientation", "z_dim_creation",
            "z_dim_rebounding", "z_dim_defense", "z_dim_usage"
        ]

        for d, ax, col, title in cand_axes:
            p_row = self.df[self.df["player_tournament_id"] == d["player_tournament_id"]].iloc[0]
            vals = list(p_row[feature_cols].values)
            vals += vals[:1]
            ax.plot(angles, vals, linewidth=2.2, color=col)
            ax.fill(angles, vals, color=col, alpha=0.2)
            ax.set_xticks(angles[:-1])
            ax.set_xticklabels(categories, fontsize=7.5, fontweight="bold")
            ax.set_title(f"{title}\n{d['full_canonical_name']} ({d['team_id']})", fontsize=9.5, fontweight="bold", pad=12)

        plt.suptitle("Tactical Profile Fingerprints: #1 Candidates Across Recruitment Briefs", fontsize=12, fontweight="bold", y=1.02)
        fig.tight_layout()
        f6_p = FIGURES_DIR / "fig6_candidate_profile_cards.png"
        plt.savefig(f6_p)
        plt.close()
        paths["fig6"] = f6_p

        return paths


def main():
    vis = ScoutingVisualAnalyticsEngine()
    paths = vis.generate_all_figures()
    print("MVP-4 Visual Analytics Figures Generated:")
    for k, p in paths.items():
        print(f"  {k}: {p}")


if __name__ == "__main__":
    main()
