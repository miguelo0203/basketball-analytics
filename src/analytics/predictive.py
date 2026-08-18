"""Predictive modeling engine with strict Leave-One-Tournament-Out (LOTO) validation."""

import numpy as np
import pandas as pd
from typing import Dict, Any, List, Tuple
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.metrics import brier_score_loss, log_loss, roc_auc_score, mean_absolute_error, mean_squared_error


class PredictiveEvaluation:
    """Evaluates prediction models using tournament-isolated splits to prevent data leakage."""

    def __init__(self, random_state: int = 42):
        self.random_state = random_state

    def leave_one_tournament_out_split(
        self,
        df: pd.DataFrame,
    ) -> List[Tuple[pd.DataFrame, pd.DataFrame, str]]:
        """Yield (train_df, test_df, tournament_id) folds held out atomically."""
        tournaments = df["tournament_id"].unique()
        splits = []
        for tourney in tournaments:
            train = df[df["tournament_id"] != tourney].copy()
            test = df[df["tournament_id"] == tourney].copy()
            splits.append((train, test, str(tourney)))
        return splits

    def evaluate_win_probability_models(
        self,
        df: pd.DataFrame,
        feature_cols: List[str],
        target_col: str = "home_win",
    ) -> Dict[str, Any]:
        """Train and evaluate win probability models across LOTO folds."""
        splits = self.leave_one_tournament_out_split(df)
        
        y_true_all = []
        y_pred_baseline = []
        y_pred_logistic = []

        for train_df, test_df, tourney_id in splits:
            if len(test_df) == 0:
                continue

            X_train = train_df[feature_cols].fillna(0.0).values
            y_train = train_df[target_col].values
            X_test = test_df[feature_cols].fillna(0.0).values
            y_test = test_df[target_col].values

            # 1. Baseline: 50% coin-flip
            base_prob = np.full(len(y_test), 0.5)

            # 2. Logistic Regression
            clf = LogisticRegression(random_state=self.random_state, max_iter=500)
            clf.fit(X_train, y_train)
            log_prob = clf.predict_proba(X_test)[:, 1]

            y_true_all.extend(y_test)
            y_pred_baseline.extend(base_prob)
            y_pred_logistic.extend(log_prob)

        y_true_arr = np.array(y_true_all)
        log_pred_arr = np.array(y_pred_logistic)
        base_pred_arr = np.array(y_pred_baseline)

        return {
            "n_evaluated_games": len(y_true_arr),
            "baseline_brier_score": round(float(brier_score_loss(y_true_arr, base_pred_arr)), 4),
            "logistic_brier_score": round(float(brier_score_loss(y_true_arr, log_pred_arr)), 4),
            "logistic_log_loss": round(float(log_loss(y_true_arr, log_pred_arr)), 4),
            "logistic_roc_auc": round(float(roc_auc_score(y_true_arr, log_pred_arr)), 4),
        }

    def evaluate_margin_models(
        self,
        df: pd.DataFrame,
        feature_cols: List[str],
        target_col: str = "margin_home",
    ) -> Dict[str, Any]:
        """Train and evaluate point margin prediction models across LOTO folds."""
        splits = self.leave_one_tournament_out_split(df)

        y_true_all = []
        y_pred_baseline = []
        y_pred_ridge = []

        for train_df, test_df, _ in splits:
            if len(test_df) == 0:
                continue

            X_train = train_df[feature_cols].fillna(0.0).values
            y_train = train_df[target_col].values
            X_test = test_df[feature_cols].fillna(0.0).values
            y_test = test_df[target_col].values

            # Baseline: 0 margin (even game)
            base_pred = np.zeros(len(y_test))

            # Ridge Regression
            reg = Ridge(alpha=1.0, random_state=self.random_state)
            reg.fit(X_train, y_train)
            ridge_pred = reg.predict(X_test)

            y_true_all.extend(y_test)
            y_pred_baseline.extend(base_pred)
            y_pred_ridge.extend(ridge_pred)

        y_true_arr = np.array(y_true_all)
        ridge_pred_arr = np.array(y_pred_ridge)
        base_pred_arr = np.array(y_pred_baseline)

        return {
            "n_evaluated_games": len(y_true_arr),
            "baseline_mae": round(float(mean_absolute_error(y_true_arr, base_pred_arr)), 2),
            "ridge_mae": round(float(mean_absolute_error(y_true_arr, ridge_pred_arr)), 2),
            "ridge_rmse": round(float(np.sqrt(mean_squared_error(y_true_arr, ridge_pred_arr))), 2),
        }
