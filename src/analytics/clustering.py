"""Unsupervised player archetype clustering engine with formal mathematical evaluation of k."""

import numpy as np
import pandas as pd
from typing import Dict, Any, List, Tuple
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score, adjusted_rand_score

# Non-redundant functional rate features (excluding raw height and redundant volume features)
CLUSTERING_FEATURES = [
    "usg_pct_avg",
    "ts_pct",
    "three_point_rate",
    "free_throw_rate",
    "fg2_pct",
    "fg3_pct",
    "ft_pct",
    "orb_pct_est",
    "drb_pct_est",
    "ast_pct_est",
    "tov_pct_est",
    "stl_per_40",
    "blk_per_40",
    "pf_per_40",
]


class PlayerClusteringPipeline:
    """Clustering pipeline evaluating functional archetypes without morphological bias."""

    def __init__(self, random_state: int = 42):
        self.random_state = random_state
        self.scaler = StandardScaler()
        self.best_model: Any = None
        self.best_k: int = 5

    def prepare_features(self, df: pd.DataFrame) -> Tuple[np.ndarray, pd.DataFrame]:
        """Impute missing rate values and scale features."""
        feature_df = df[CLUSTERING_FEATURES].copy()
        # Fill rate nulls (e.g. 0 3P attempts -> 0 3P%)
        feature_df = feature_df.fillna(0.0)
        scaled = self.scaler.fit_transform(feature_df)
        return scaled, feature_df

    def evaluate_k_range(
        self,
        X: np.ndarray,
        k_min: int = 3,
        k_max: int = 10,
    ) -> List[Dict[str, Any]]:
        """Evaluate cluster quality across k values using multiple mathematical metrics."""
        results = []
        for k in range(k_min, k_max + 1):
            km = KMeans(n_clusters=k, random_state=self.random_state, n_init=10)
            labels = km.fit_predict(X)

            sil = float(silhouette_score(X, labels))
            ch = float(calinski_harabasz_score(X, labels))
            db = float(davies_bouldin_score(X, labels))

            # GMM BIC
            gmm = GaussianMixture(n_components=k, random_state=self.random_state)
            gmm.fit(X)
            bic = float(gmm.bic(X))

            results.append({
                "k": k,
                "silhouette": round(sil, 4),
                "calinski_harabasz": round(ch, 2),
                "davies_bouldin": round(db, 4),
                "gmm_bic": round(bic, 2),
                "inertia": round(km.inertia_, 2),
            })
        return results

    def evaluate_bootstrap_stability(
        self,
        X: np.ndarray,
        k: int = 5,
        n_bootstraps: int = 50,
        subsample_ratio: float = 0.8,
    ) -> float:
        """Evaluate cluster stability via bootstrap resampling and Adjusted Rand Index."""
        n_samples = int(len(X) * subsample_ratio)
        base_km = KMeans(n_clusters=k, random_state=self.random_state, n_init=10)
        base_labels = base_km.fit_predict(X)

        ari_scores = []
        rng = np.random.default_rng(self.random_state)

        for _ in range(n_bootstraps):
            indices = rng.choice(len(X), size=n_samples, replace=False)
            sub_X = X[indices]
            sub_km = KMeans(n_clusters=k, random_state=int(rng.integers(0, 10000)), n_init=10)
            sub_labels = sub_km.fit_predict(sub_X)

            # Compare sub-model predictions against base model predictions on sub_X
            pred_base = base_km.predict(sub_X)
            ari = adjusted_rand_score(pred_base, sub_labels)
            ari_scores.append(ari)

        return float(round(np.mean(ari_scores), 4))

    def fit(self, df: pd.DataFrame, k: int = 5) -> Tuple[np.ndarray, KMeans]:
        """Fit final K-Means model on prepared player tournament dataset."""
        X, _ = self.prepare_features(df)
        self.best_k = k
        self.best_model = KMeans(n_clusters=k, random_state=self.random_state, n_init=20)
        labels = self.best_model.fit_predict(X)
        return labels, self.best_model
