from __future__ import annotations
from typing import Any, Dict
import numpy as np

try:
    import shap  # type: ignore
except ImportError:  # graceful degradation
    shap = None  # type: ignore


def compute_global_shap(model, background_X, sample_X, max_display: int = 10) -> Dict[str, float]:
    """Return mean absolute SHAP values per feature (limited) as dict.
    If SHAP not installed, returns empty dict.
    """
    if shap is None:
        return {}
    explainer = shap.Explainer(model, background_X)
    shap_values = explainer(sample_X)
    mean_abs = np.abs(shap_values.values).mean(axis=0)
    ranked = sorted(zip(sample_X.columns, mean_abs), key=lambda x: x[1], reverse=True)
    return {k: float(v) for k, v in ranked[:max_display]}


def compute_local_shap(model, background_X, single_row) -> Dict[str, float]:
    if shap is None:
        return {}
    explainer = shap.Explainer(model, background_X)
    sv = explainer(single_row)
    return {f: float(v) for f, v in zip(single_row.columns, sv.values[0])}
