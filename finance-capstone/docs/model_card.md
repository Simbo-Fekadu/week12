# Model Card: Credit Risk Scoring (PD Model)

## 1. Model Details

- **Model Type:** Logistic Regression (baseline, calibrated planned)
- **Version:** 0.1.0
- **Owner:** <Your Name>
- **Primary Use Case:** Predict probability of default within 12-month horizon.

## 2. Intended Use

- **Intended Users:** Credit risk analysts, underwriting automation services.
- **Intended Decisions:** Application approval, pricing, risk-based limit assignment.
- **Out of Scope:** Collections prioritization, fraud detection.

## 3. Data

- **Source:** Synthetic placeholder (to be replaced with internal lending dataset)
- **Target Variable:** `defaulted` (0/1)
- **Core Features:** age, income, loan_amount, employment_years, credit_score, existing_debt, engineered ratios.
- **Data Quality Controls:** Schema validation (pydantic), logical constraint checks.

## 4. Performance (Synthetic Baseline)

| Metric      | Value        | Target             |
| ----------- | ------------ | ------------------ |
| ROC AUC     | TBD          | ≥ 0.78             |
| KS          | TBD          | ≥ 0.35             |
| Brier       | TBD          | ≤ 0.18             |
| Calibration | Plot pending | Smooth reliability |

## 5. Limitations

- Synthetic data not representative of real credit distributions.
- No fairness / bias segmentation yet (to add with real data).
- Economic / macro factors excluded.

## 6. Ethical Considerations

- Ensure demographic parity assessment with real data.
- Monitor for proxy variables leading to indirect discrimination.

## 7. Explainability

- Planned: SHAP global summary & local waterfall for approved vs declined cases.
- Interim: Coefficient-based importance for logistic model.

## 8. Monitoring & Maintenance

| Aspect      | Metric | Threshold | Action                         |
| ----------- | ------ | --------- | ------------------------------ |
| Drift       | PSI    | > 0.2     | Investigate & possible retrain |
| Performance | AUC    | < 0.75    | Retrain & recalibrate          |
| Calibration | Brier  | > 0.20    | Recalibrate                    |

## 9. Security & Compliance

- Dependency scanning via pip-audit in CI.
- Reproducible environment pinned via requirements.txt.

## 10. Versioning

- Tagged releases (e.g., v0.1.0 baseline). Artifacts stored under `artifacts/`.

## 11. Change Log

| Version | Date       | Changes                         |
| ------- | ---------- | ------------------------------- |
| 0.1.0   | YYYY-MM-DD | Initial baseline logistic model |

## 12. Future Work

- Add gradient boosted model comparison.
- Implement fairness metrics & segment dashboards.
- Add real-time inference API + request logging.
