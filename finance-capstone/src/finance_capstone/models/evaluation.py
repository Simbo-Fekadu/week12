from __future__ import annotations
from sklearn.metrics import roc_auc_score, brier_score_loss
import pandas as pd
from typing import Dict


def compute_classification_metrics(y_true, y_prob) -> Dict[str, float]:
    return {
        "roc_auc": roc_auc_score(y_true, y_prob),
        "brier": brier_score_loss(y_true, y_prob),
    }


def ks_statistic(y_true, y_prob) -> float:
    df = pd.DataFrame({"y": y_true, "p": y_prob})
    df = df.sort_values("p", ascending=False)
    df["cum_event"] = (df["y"].cumsum() / df["y"].sum()).fillna(0)
    df["cum_non_event"] = ((1 - df["y"]).cumsum() / (1 - df["y"]).sum()).fillna(0)
    df["diff"] = (df["cum_event"] - df["cum_non_event"]).abs()
    return float(df["diff"].max())
