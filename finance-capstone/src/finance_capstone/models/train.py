from __future__ import annotations
from dataclasses import dataclass
from typing import Tuple
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
from ..features.engineering import feature_columns, TARGET_COL

@dataclass
class TrainResult:
    model: LogisticRegression
    auc: float
    feature_list: list[str]


def train_baseline(df: pd.DataFrame, test_size: float = 0.2, random_state: int = 42) -> TrainResult:
    df_clean = df.dropna(subset=[TARGET_COL])
    X = df_clean[feature_columns(df_clean)].fillna(0)
    y = df_clean[TARGET_COL]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    model = LogisticRegression(max_iter=500, n_jobs=1)
    model.fit(X_train, y_train)
    preds = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, preds)
    return TrainResult(model=model, auc=auc, feature_list=list(X.columns))
