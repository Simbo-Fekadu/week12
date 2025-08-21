from __future__ import annotations
import numpy as np
import pandas as pd
from typing import Dict


def population_stability_index(expected: pd.Series, actual: pd.Series, bins: int = 10) -> float:
    """Compute PSI between two distributions.

    expected: baseline feature values
    actual: current feature values
    """
    e, a = expected.dropna(), actual.dropna()
    quantiles = np.linspace(0, 1, bins + 1)
    cuts = e.quantile(quantiles).values
    cuts[0] = -np.inf
    cuts[-1] = np.inf
    e_counts = np.histogram(e, bins=cuts)[0]
    a_counts = np.histogram(a, bins=cuts)[0]
    e_perc = np.where(e_counts == 0, 1e-6, e_counts / e_counts.sum())
    a_perc = np.where(a_counts == 0, 1e-6, a_counts / a_counts.sum())
    psi_values = (a_perc - e_perc) * np.log(a_perc / e_perc)
    return float(np.sum(psi_values))


def feature_psi_report(baseline_df: pd.DataFrame, current_df: pd.DataFrame, features: list[str]) -> Dict[str, float]:
    return {f: population_stability_index(baseline_df[f], current_df[f]) for f in features if f in baseline_df.columns and f in current_df.columns}
