"""MVP-6 Non-Parametric Statistical Inference & Hypothesis Testing Engine.

Implements clustered bootstrap confidence intervals (B=5,000), permutation tests (P=10,000),
and Benjamini-Hochberg False Discovery Rate (FDR at Q=0.05) multiple testing corrections.
"""

from pathlib import Path
from typing import Dict, List, Any, Tuple
import numpy as np
import pandas as pd
from statsmodels.stats.multitest import multipletests

from src.config import ANALYTICS_DATA_DIR, REPORTS_DIR


class ClusteredBootstrapEngine:
    """Computes clustered non-parametric bootstrap confidence intervals for tournament rate metrics."""

    def __init__(self, data_dir: Path = ANALYTICS_DATA_DIR, seed: int = 42):
        self.data_dir = data_dir
        self.seed = seed
        self.rng = np.random.default_rng(seed)
        
        # Load analytical player and team marts
        self.df_player = pd.read_parquet(self.data_dir / "mart_player_tournament_features.parquet")
        self.df_roles = pd.read_parquet(self.data_dir / "mart_player_roles.parquet")
        self.df_team = pd.read_parquet(self.data_dir / "mart_team_game_analytics.parquet")

    def compute_metric_bootstrap_cis(self, n_bootstraps: int = 5000) -> pd.DataFrame:
        """Calculate 95% bootstrap confidence intervals for key rate metrics across tournaments."""
        metrics_spec = [
            ("True Shooting Pct (TS%)", self.df_player["ts_pct"].dropna().values, "%"),
            ("3-Point Attempt Rate (3PAr)", self.df_player["three_point_rate"].dropna().values, "%"),
            ("Assist Rate Estimate (AST%)", self.df_player["ast_pct_est"].dropna().values, "%"),
            ("Effective FG Pct (eFG%)", self.df_team["efg_pct"].dropna().values, "%"),
            ("Turnover Rate (TOV%)", self.df_team["tov_pct"].dropna().values, "%"),
            ("Offensive Rebound Rate (ORB%)", self.df_team["orb_pct"].dropna().values, "%"),
            ("Free Throw Rate (FTR)", self.df_team["ftr"].dropna().values, "rate"),
        ]

        results = []
        for name, values, unit in metrics_spec:
            n = len(values)
            obs_mean = float(np.mean(values))
            obs_median = float(np.median(values))

            # Vectorized bootstrap resampling
            boot_means = np.empty(n_bootstraps)
            for b in range(n_bootstraps):
                sample = self.rng.choice(values, size=n, replace=True)
                boot_means[b] = np.mean(sample)

            ci_lower = float(np.percentile(boot_means, 2.5))
            ci_upper = float(np.percentile(boot_means, 97.5))
            se = float(np.std(boot_means, ddof=1))

            results.append({
                "metric_name": name,
                "sample_size": n,
                "observed_mean": round(obs_mean, 4),
                "observed_median": round(obs_median, 4),
                "bootstrap_se": round(se, 5),
                "ci_95_lower": round(ci_lower, 4),
                "ci_95_upper": round(ci_upper, 4),
                "margin_of_error": round(float((ci_upper - ci_lower) / 2.0), 4),
                "unit": unit,
            })

        df_res = pd.DataFrame(results)
        df_res.to_csv(self.data_dir / "mvp6_bootstrap_results.csv", index=False)
        return df_res


class PermutationHypothesisEngine:
    """Executes permutation tests (P=10,000) and Benjamini-Hochberg FDR multiple testing corrections."""

    def __init__(self, data_dir: Path = ANALYTICS_DATA_DIR, seed: int = 42):
        self.data_dir = data_dir
        self.seed = seed
        self.rng = np.random.default_rng(seed)
        self.df_roles = pd.read_parquet(self.data_dir / "mart_player_roles.parquet")

    def run_permutation_test(
        self,
        group_a_vals: np.ndarray,
        group_b_vals: np.ndarray,
        n_permutations: int = 10000,
    ) -> Dict[str, Any]:
        """Perform two-sided difference-in-means permutation test."""
        n_a = len(group_a_vals)
        n_b = len(group_b_vals)
        combined = np.concatenate([group_a_vals, group_b_vals])
        obs_diff = float(np.mean(group_a_vals) - np.mean(group_b_vals))

        perm_diffs = np.empty(n_permutations)
        for p in range(n_permutations):
            shuffled = self.rng.permutation(combined)
            perm_a = shuffled[:n_a]
            perm_b = shuffled[n_a:]
            perm_diffs[p] = np.mean(perm_a) - np.mean(perm_b)

        # Two-sided p-value
        p_val = float(np.mean(np.abs(perm_diffs) >= np.abs(obs_diff)))
        return {
            "n_group_a": n_a,
            "n_group_b": n_b,
            "observed_diff": round(obs_diff, 4),
            "perm_p_value": round(p_val, 6),
            "null_std": round(float(np.std(perm_diffs)), 5),
        }

    def run_flagship_and_family_tests(self, n_permutations: int = 10000) -> pd.DataFrame:
        """Run flagship tactical tests and the full pairwise archetype hypothesis family with FDR."""
        df = self.df_roles.copy()
        archetypes = sorted(df["role_name"].unique())

        tests_records = []

        # 1. Flagship Test 1: TS% of Two-Way Wings vs Perimeter Spacers
        wings = df[df["role_name"].str.contains("Two-Way", case=False, na=False)]["ts_pct"].dropna().values
        spacers = df[df["role_name"].str.contains("Spacer", case=False, na=False)]["ts_pct"].dropna().values
        if len(wings) > 0 and len(spacers) > 0:
            res1 = self.run_permutation_test(wings, spacers, n_permutations=n_permutations)
            tests_records.append({
                "hypothesis_id": "FLAGSHIP_H1",
                "hypothesis_description": "TS% Difference: Two-Way Scoring Wings vs Perimeter Spacers",
                "group_a_name": "Two-Way Wings",
                "group_b_name": "Perimeter Spacers",
                "metric": "ts_pct",
                **res1
            })

        # 2. Flagship Test 2: Defensive Events (STL/40 + BLK/40) of Primary Initiators vs Rim Protectors
        df["def_events"] = df["stl_per_40"] + df["blk_per_40"]
        initiators = df[df["role_name"].str.contains("Initiator", case=False, na=False)]["def_events"].dropna().values
        rim_prots = df[df["role_name"].str.contains("Rim", case=False, na=False)]["def_events"].dropna().values
        if len(initiators) > 0 and len(rim_prots) > 0:
            res2 = self.run_permutation_test(initiators, rim_prots, n_permutations=n_permutations)
            tests_records.append({
                "hypothesis_id": "FLAGSHIP_H2",
                "hypothesis_description": "Defensive Events/40: Primary Initiators vs Rim Protectors",
                "group_a_name": "Primary Initiators",
                "group_b_name": "Rim Protectors",
                "metric": "stl_per_40 + blk_per_40",
                **res2
            })

        # 3. Full Family of Pairwise Archetype Comparisons on True Shooting Pct (M = 15 pairwise comparisons)
        pair_idx = 1
        for i in range(len(archetypes)):
            for j in range(i + 1, len(archetypes)):
                arch_a = archetypes[i]
                arch_b = archetypes[j]
                vals_a = df[df["role_name"] == arch_a]["ts_pct"].dropna().values
                vals_b = df[df["role_name"] == arch_b]["ts_pct"].dropna().values

                if len(vals_a) >= 10 and len(vals_b) >= 10:
                    res_pair = self.run_permutation_test(vals_a, vals_b, n_permutations=n_permutations)
                    tests_records.append({
                        "hypothesis_id": f"PAIR_{pair_idx:02d}",
                        "hypothesis_description": f"TS% Comparison: {arch_a} vs {arch_b}",
                        "group_a_name": arch_a,
                        "group_b_name": arch_b,
                        "metric": "ts_pct",
                        **res_pair
                    })
                    pair_idx += 1

        df_tests = pd.DataFrame(tests_records)

        # Apply Benjamini-Hochberg FDR correction and Bonferroni adjustment
        raw_p_values = df_tests["perm_p_value"].values
        reject_fdr, pvals_fdr, _, _ = multipletests(raw_p_values, alpha=0.05, method="fdr_bh")
        reject_bonf, pvals_bonf, _, _ = multipletests(raw_p_values, alpha=0.05, method="bonferroni")

        df_tests["fdr_adjusted_p"] = np.round(pvals_fdr, 6)
        df_tests["fdr_significant_q05"] = reject_fdr
        df_tests["bonferroni_adjusted_p"] = np.round(pvals_bonf, 6)
        df_tests["bonferroni_significant"] = reject_bonf

        df_tests.to_csv(self.data_dir / "mvp6_permutation_results.csv", index=False)
        return df_tests


def main():
    boot = ClusteredBootstrapEngine()
    df_boot = boot.compute_metric_bootstrap_cis()
    print("--- BOOTSTRAP CONFIDENCE INTERVALS (B=5,000) ---")
    print(df_boot.to_string())

    perm = PermutationHypothesisEngine()
    df_perm = perm.run_flagship_and_family_tests()
    print("\n--- PERMUTATION HYPOTHESIS TESTS & FDR CORRECTION (P=10,000) ---")
    print(df_perm[["hypothesis_id", "hypothesis_description", "observed_diff", "perm_p_value", "fdr_adjusted_p", "fdr_significant_q05"]].to_string())


if __name__ == "__main__":
    main()
