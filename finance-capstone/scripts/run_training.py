from __future__ import annotations
import json
from pathlib import Path
from finance_capstone.config.settings import settings
from finance_capstone.data.schemas import ApplicantRecord
from finance_capstone.data.validation import validate_records
from finance_capstone.features.engineering import basic_feature_frame, add_engineered_features
from finance_capstone.models.train import train_baseline

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
    result = train_baseline(df)
    artifact_dir = Path(settings.ARTIFACT_DIR)
    artifact_dir.mkdir(parents=True, exist_ok=True)
    with open(artifact_dir / "metrics.json", "w") as f:
        json.dump({"auc": result.auc, "features": result.feature_list}, f, indent=2)
    print(f"Baseline model AUC: {result.auc:.4f}")

if __name__ == "__main__":
    main()
