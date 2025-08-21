# Finance Capstone: Credit Risk Scoring Platform

## Executive Summary

A robust, transparent credit risk scoring pipeline engineered for reliability, explainability, and monitoring. Targets improved risk-adjusted lending decisions by predicting probability of default (PD) and providing controls to reduce model and operational risk.

## Business Problem

Financial institutions must balance loan portfolio growth with default risk. Manual or ad‑hoc scoring increases unexpected loss, capital inefficiency, and compliance exposure. This project delivers a reproducible PD model + governance framework enabling:

- Faster credit decisions
- Better calibration of default probabilities for pricing / provisioning
- Ongoing monitoring to detect drift and maintain performance

## Core Objectives

1. Accurate & calibrated PD estimation (AUC ≥ 0.78, KS ≥ 0.35, Brier ≤ 0.18)
2. Reliability via data contracts, tests, CI/CD, and deterministic builds
3. Transparency with SHAP-based global & local explanations + model card
4. Monitoring for drift (PSI) & stability of feature importance
5. Deployable dashboard for stakeholder interaction

## Repository Layout

```
src/finance_capstone/
  config/            # Central settings & environment handling
  data/              # Loading, validation, preprocessing
  features/          # Feature engineering & selection
  models/            # Training, inference, evaluation, calibration
  explainability/    # SHAP utilities & reporting
  utils/             # Logging, IO helpers, timing, misc utilities
  api/               # (Planned) FastAPI service for inference
tests/               # Unit & integration tests
scripts/             # CLI entry points
dashboards/          # Streamlit app
notebooks/           # Exploration & analysis notebooks
ci/                  # CI workflow(s)
docs/                # Model card, governance docs
```

## Quick Start (Planned)

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest -q
python scripts/run_training.py --config configs/local.yaml
streamlit run dashboards/streamlit_app.py
```

## Success Metrics

| Dimension                  | Metric              | Target           |
| -------------------------- | ------------------- | ---------------- |
| Discrimination             | ROC AUC             | ≥ 0.78           |
| Rank Separation            | KS                  | ≥ 0.35           |
| Calibration                | Brier Score         | ≤ 0.18           |
| Stability                  | Feature PSI         | < 0.1            |
| Explainability Consistency | Top 10 SHAP overlap | ≥ 0.6            |
| Testing                    | Coverage            | ≥ 85% core logic |

## Planned Features (MVP Sprint)

- Data schema & validation (pydantic/pandera)
- Modular feature pipeline
- Baseline model (Logistic + XGBoost) & calibration
- Evaluation & drift monitoring module
- SHAP explainability utilities
- Streamlit dashboard (KPIs, scenario analysis, SHAP)
- CI: lint, tests, security scan, build
- Model Card & governance doc

## Roadmap (High Level)

| Day | Focus                                | Outputs                           |
| --- | ------------------------------------ | --------------------------------- |
| 1   | Structure + baseline data validation | Repo skeleton, schema tests       |
| 2   | Feature engineering & unit tests     | Feature modules + test coverage   |
| 3   | Modeling + calibration + eval        | Trained model artifacts + metrics |
| 4   | Monitoring + integration tests       | Drift detection, end-to-end test  |
| 5   | Dashboard + explainability           | Streamlit app, SHAP plots         |
| 6   | Hardening                            | CI green, coverage, security scan |
| 7   | Documentation & presentation         | Model card, blog draft, slides    |

## Governance Artifacts (Planned)

- docs/model_card.md
- docs/governance.md
- CI generated metrics badges

## License

TBD.
