from finance_capstone.models.evaluation import compute_classification_metrics, ks_statistic
import numpy as np

def test_metrics_shapes():
    y_true = np.array([0,1,0,1,0,1])
    y_prob = np.array([0.1,0.9,0.2,0.8,0.3,0.7])
    metrics = compute_classification_metrics(y_true, y_prob)
    assert "roc_auc" in metrics and "brier" in metrics
    ks = ks_statistic(y_true, y_prob)
    assert 0 <= ks <= 1
