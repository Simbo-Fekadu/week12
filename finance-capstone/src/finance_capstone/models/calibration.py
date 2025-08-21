from __future__ import annotations
from sklearn.calibration import CalibratedClassifierCV
from sklearn.base import BaseEstimator


def calibrate_model(model: BaseEstimator, X, y, method: str = "isotonic", cv: int = 3):
    """Wrap model with probability calibration.

    Parameters
    ----------
    model : fitted estimator supporting predict_proba
    X, y : training data
    method : 'isotonic' or 'sigmoid'
    cv : cross-validation folds
    """
    calibrated = CalibratedClassifierCV(base_estimator=model, method=method, cv=cv)
    calibrated.fit(X, y)
    return calibrated
