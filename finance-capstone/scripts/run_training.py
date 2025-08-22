from __future__ import annotations
import json
from pathlib import Path
from finance_capstone.config.settings import settings
from finance_capstone.data.schemas import ApplicantRecord
from finance_capstone.data.validation import validate_records
from finance_capstone.features.engineering import basic_feature_frame, add_engineered_features
from finance_capstone.models.train import train_baseline
from finance_capstone.models.evaluation import compute_classification_metrics, ks_statistic
from finance_capstone.models.calibration import calibrate_model
from joblib import dump

# Temporary synthetic data generator
SYNTHETIC_SAMPLE = [
    {
        "applicant_id": f"A{i}",
        "age": 25 + i % 10,
        "income": 3000 + (i * 150),
        "loan_amount": 5000 + (i * 200),
        "loan_term_months": 36,
        "employment_years": 1 + i % 5,
        "credit_score": 600 + (i * 2),
        "existing_debt": 1000 + (i * 50),
        "defaulted": 1 if i % 4 == 0 else 0,
    }
    for i in range(60)
]

def main():
    records = validate_records(SYNTHETIC_SAMPLE)
    df = basic_feature_frame(records)
    df = add_engineered_features(df)
    # Train baseline logistic regression
    result = train_baseline(df)

    # Prepare calibration dataset (reuse training frame; in real scenario use holdout)
    feature_df = df[[c for c in df.columns if c not in ("defaulted", "applicant_id")]].fillna(0)
    target = df["defaulted"].fillna(0)
    calibrated_model = calibrate_model(result.model, feature_df, target, method="isotonic", cv=3)

    # Compute probabilities on full set for synthetic metrics
    probs = calibrated_model.predict_proba(feature_df)[:, 1]
    metrics_core = compute_classification_metrics(target, probs)
    ks = ks_statistic(target, probs)

    artifact_dir = Path(settings.ARTIFACT_DIR)
    artifact_dir.mkdir(parents=True, exist_ok=True)

    # Persist model & feature snapshot
    dump(calibrated_model, artifact_dir / "model.joblib")
    feature_df.to_parquet(artifact_dir / "baseline_features.parquet")

    metrics_payload = {
        "auc": metrics_core["roc_auc"],
        "brier": metrics_core["brier"],
        "ks": ks,
        "features": result.feature_list,
        "model_type": "logistic_regression_calibrated",
        "version": "0.1.0",
    }
    with open(artifact_dir / "metrics.json", "w") as f:
        json.dump(metrics_payload, f, indent=2)
    print(
        "Baseline calibrated model metrics: AUC={auc:.4f} KS={ks:.4f} Brier={brier:.4f}".format(
            **metrics_payload
        )
    )

if __name__ == "__main__":
    main()
