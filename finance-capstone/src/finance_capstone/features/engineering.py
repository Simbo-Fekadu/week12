from __future__ import annotations
import pandas as pd
from typing import List

NUMERIC_FEATURES = [
    "age",
    "income",
    "loan_amount",
    "loan_term_months",
    "employment_years",
    "credit_score",
    "existing_debt",
]

TARGET_COL = "defaulted"
ID_COL = "applicant_id"


def basic_feature_frame(records) -> pd.DataFrame:
    df = pd.DataFrame([r.dict() for r in records])
    return df


def add_engineered_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if {"income", "loan_amount"}.issubset(out.columns):
        out["loan_income_ratio"] = out["loan_amount"] / out["income"].replace({0: pd.NA})
    if {"existing_debt", "income"}.issubset(out.columns):
        out["debt_income_ratio"] = out["existing_debt"] / out["income"].replace({0: pd.NA})
    return out


def feature_columns(df: pd.DataFrame) -> List[str]:
    exclude = {TARGET_COL, ID_COL}
    return [c for c in df.columns if c not in exclude]
