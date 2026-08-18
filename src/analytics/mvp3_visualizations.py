"""Publication-Quality Visual Analytics Engine for MVP-3.

Generates high-resolution figures for player roles, PCA spaces,
spider comparables, recruitment trade-offs, and sample size confidence.
"""

from pathlib import Path
from typing import Dict, List, Any
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

from src.config import ANALYTICS_DATA_DIR, REPORTS_DIR

FIGURES_DIR = REPORTS_DIR / "figures" / "mvp3"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)


class PlayerVisualAnalyticsEngine:
    """Generates publication-quality charts for player evaluation and scouting."""

    def __init__(self, data_dir: Path = ANALYTICS_DATA_DIR):
        self.roles_path = data_dir / "mart_player_roles.parquet"
        self.df = pd.read_parquet(self.roles_path)
        self.df_qual = self.df[self.df["is_qualified_sample"] == 1].copy()

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
        """Generate all 5 publication figures."""
        paths = {}
        feature_cols = [
            "z_dim_scoring_volume", "z_dim_scoring_efficiency",
            "z_dim_perimeter_orientation", "z_dim_creation",
            "z_dim_rebounding", "z_dim_defense", "z_dim_usage"
        ]

        # -------------------------------------------------------------
        # Figure 1: 2D PCA Player Role Space
        # -------------------------------------------------------------
        pca = PCA(n_components=2, random_state=42)
        coords = pca.fit_transform(self.df_qual[feature_cols].values)
        self.df_qual["pca_x"] = coords[:, 0]
        self.df_qual["pca_y"] = coords[:, 1]

        fig, ax = plt.subplots(figsize=(11, 7), dpi=300)
        roles = self.df_qual["role_name"].unique()
        colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]

        for idx, r in enumerate(roles):
            sub = self.df_qual[self.df_qual["role_name"] == r]
            ax.scatter(sub["pca_x"], sub["pca_y"], label=r, color=colors[idx % len(colors)], alpha=0.45, s=28)

        # Annotate Key International Stars
        notable = [
            ("pau_gasol_1980", "Pau Gasol (ESP)", 12),
            ("ricky_rubio_1990", "Ricky Rubio (ESP)", -15),
            ("rudy_fernandez_1985", "Rudy Fernández (ESP)", 10),
            ("bogdan_bogdanovic_1992", "Bogdan Bogdanović (SRB)", 10),
            ("luka_doncic_1999", "Luka Dončić (SLO)", -15),
            ("rudy_gobert_1992", "Rudy Gobert (FRA)", 12),
            ("dirk_nowitzki_1978", "Dirk Nowitzki (GER)", 10),
            ("kevin_durant_1988", "Kevin Durant (USA)", -12),
        ]
        for slug, label, offset in notable:
            match = self.df_qual[self.df_qual["canonical_player_id"] == slug]
            if not match.empty:
                row = match.iloc[0]
                ax.scatter(row["pca_x"], row["pca_y"], color="#000000", s=80, edgecolors="#ffffff", linewidth=1.5, zorder=5)
                ax.annotate(label, (row["pca_x"], row["pca_y"]), xytext=(row["pca_x"] + 0.15, row["pca_y"] + offset*0.02),
                            fontsize=8.5, fontweight="bold", bbox=dict(boxstyle="round,pad=0.2", fc="#ffffff", ec="#333333", alpha=0.85))

        ax.set_title(f"2D PCA Projection of International Player Roles (2005–2025, N={len(self.df_qual)})", fontsize=13, fontweight="bold", pad=12)
        ax.set_xlabel(f"Principal Component 1 (Variance Expl: {pca.explained_variance_ratio_[0]*100:.1f}%)", fontsize=10, fontweight="bold")
        ax.set_ylabel(f"Principal Component 2 (Variance Expl: {pca.explained_variance_ratio_[1]*100:.1f}%)", fontsize=10, fontweight="bold")
        ax.legend(loc="upper right", fontsize=8, framealpha=0.9)
        ax.grid(True)
        fig.tight_layout()
        f1_p = FIGURES_DIR / "fig1_player_role_map_pca.png"
        plt.savefig(f1_p)
        plt.close()
        paths["fig1"] = f1_p

        # -------------------------------------------------------------
        # Figure 2: Role Profiles Across 7 Dimensions
        # -------------------------------------------------------------
        role_means = self.df_qual.groupby("role_name")[feature_cols].mean()
        dim_labels = ["Scoring Volume", "Efficiency", "3P Attempt Rate", "Creation/AST%", "Rebounding", "Defense", "Usage Rate"]

        fig, ax = plt.subplots(figsize=(12, 6), dpi=300)
        x = np.arange(len(dim_labels))
        width = 0.13

        for idx, (r_name, row) in enumerate(role_means.iterrows()):
            ax.bar(x + idx * width, row.values, width, label=r_name, color=colors[idx % len(colors)], alpha=0.85)

        ax.set_title("Standardized Dimensional Profiles Across Discovered Roles", fontsize=13, fontweight="bold", pad=12)
        ax.set_xticks(x + width * 2.5)
        ax.set_xticklabels(dim_labels, fontsize=9.5, fontweight="bold")
        ax.set_ylabel("Standard Deviations (Z-Score)", fontsize=10, fontweight="bold")
        ax.axhline(0, color="#333333", linewidth=0.8, linestyle="--")
        ax.legend(loc="upper left", fontsize=7.5, ncol=2)
        ax.grid(True)
        fig.tight_layout()
        f2_p = FIGURES_DIR / "fig2_role_radar_profiles.png"
        plt.savefig(f2_p)
        plt.close()
        paths["fig2"] = f2_p

        # -------------------------------------------------------------
        # Figure 3: Target Player Comparables Spider Radar
        # -------------------------------------------------------------
        from src.analytics.player_comparables import PlayerComparablesEngine
        comp_engine = PlayerComparablesEngine()
        target_res = comp_engine.find_comparables("ricky_rubio_1990", top_n=3)

        categories = ["Scoring Vol", "Efficiency", "3P Attempt Rate", "Creation", "Rebounding", "Defense", "Usage"]
        N_cat = len(categories)
        angles = [n / float(N_cat) * 2 * np.pi for n in range(N_cat)]
        angles += angles[:1]

        fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True), dpi=300)

        # Target player vector
        t_row = self.df_qual[self.df_qual["canonical_player_id"] == "ricky_rubio_1990"].iloc[0]
        t_vals = list(t_row[feature_cols].values)
        t_vals += t_vals[:1]
        ax.plot(angles, t_vals, linewidth=2.5, color="#d62728", label=f"TARGET: {target_res['target_player']['full_canonical_name']}")
        ax.fill(angles, t_vals, color="#d62728", alpha=0.15)

        # Top 2 Comparators
        comp_colors = ["#1f77b4", "#2ca02c"]
        for c_idx, c_info in enumerate(target_res["comparables"][:2]):
            c_row = self.df_qual[self.df_qual["player_tournament_id"] == c_info["player_tournament_id"]].iloc[0]
            c_vals = list(c_row[feature_cols].values)
            c_vals += c_vals[:1]
            ax.plot(angles, c_vals, linewidth=1.5, linestyle="--", color=comp_colors[c_idx],
                    label=f"COMP #{c_idx+1}: {c_info['full_canonical_name']} ({c_info['similarity_score']:.2f})")

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories, fontsize=9, fontweight="bold")
        ax.set_title(f"Multi-Dimensional Alignment: Ricky Rubio vs Top Historical Comparators", fontsize=11, fontweight="bold", pad=15)
        ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1), fontsize=8)
        fig.tight_layout()
        f3_p = FIGURES_DIR / "fig3_target_player_comparables_spider.png"
        plt.savefig(f3_p)
        plt.close()
        paths["fig3"] = f3_p

        # -------------------------------------------------------------
        # Figure 4: Production vs Efficiency Recruitment Trade-Offs
        # -------------------------------------------------------------
        fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
        sc = ax.scatter(
            self.df_qual["pts_per_40"],
            self.df_qual["ts_pct"] * 100,
            s=self.df_qual["total_minutes"] * 0.8,
            c=self.df_qual["cluster_id"],
            cmap="tab10",
            alpha=0.6,
            edgecolors="#ffffff",
            linewidth=0.5
        )

        ax.set_title("Player Production vs Scoring Efficiency (Bubble Size = Tournament Minutes)", fontsize=12, fontweight="bold", pad=12)
        ax.set_xlabel("Points Per 40 Minutes (PTS / 40m)", fontsize=10, fontweight="bold")
        ax.set_ylabel("True Shooting Percentage (TS %)", fontsize=10, fontweight="bold")
        ax.axhline(55.0, color="#888888", linestyle=":", label="International League Avg TS (55%)")
        ax.axvline(20.0, color="#888888", linestyle=":", label="High-Volume Threshold (20 PTS/40m)")
        ax.legend(loc="lower left", fontsize=8.5)
        ax.grid(True)
        fig.tight_layout()
        f4_p = FIGURES_DIR / "fig4_recruitment_shortlist_tradeoffs.png"
        plt.savefig(f4_p)
        plt.close()
        paths["fig4"] = f4_p

        # -------------------------------------------------------------
        # Figure 5: Sample Size vs Estimation Confidence
        # -------------------------------------------------------------
        fig, ax = plt.subplots(figsize=(9, 5), dpi=300)
        minutes = np.linspace(10, 300, 100)
        # Standard error of rate estimator shrinks proportionally to 1/sqrt(minutes)
        std_error = 1.0 / np.sqrt(minutes / 40.0)

        ax.plot(minutes, std_error, color="#1f77b4", linewidth=2.2, label="Relative Estimation Error (SE ∝ 1/√MIN)")
        ax.axvline(40, color="#d62728", linestyle="--", linewidth=1.5, label="Minimum Sample Threshold (40 MIN)")
        ax.axvline(100, color="#2ca02c", linestyle=":", linewidth=1.5, label="High-Confidence Sample (100 MIN)")

        ax.fill_between(minutes, 0, std_error, color="#1f77b4", alpha=0.1)
        ax.set_title("Statistical Estimation Uncertainty vs Tournament Sample Minutes", fontsize=12, fontweight="bold", pad=12)
        ax.set_xlabel("Total Tournament Minutes Played", fontsize=10, fontweight="bold")
        ax.set_ylabel("Relative Parameter Standard Error", fontsize=10, fontweight="bold")
        ax.legend(loc="upper right", fontsize=8.5)
        ax.grid(True)
        fig.tight_layout()
        f5_p = FIGURES_DIR / "fig5_sample_size_confidence_curve.png"
        plt.savefig(f5_p)
        plt.close()
        paths["fig5"] = f5_p

        return paths


def main():
    engine = PlayerVisualAnalyticsEngine()
    paths = engine.generate_all_figures()
    print("MVP-3 Visualizations generated:")
    for k, p in paths.items():
        print(f"  {k}: {p}")


if __name__ == "__main__":
    main()
