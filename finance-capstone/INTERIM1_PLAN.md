# Interim Submission 1

## Project Chosen

Credit Risk Scoring Platform – engineered probability of default (PD) model + monitoring & explainability framework enabling better lending decisions and risk governance.

## Business Understanding (Summary)

Banks and digital lenders must decide which applicants to approve and at what credit terms. Inaccurate or opaque risk assessment increases unexpected credit losses, capital allocation inefficiency, regulatory scrutiny, and missed growth. A robust PD scoring system with continuous validation reduces loss volatility and supports compliant decisioning.

## Objectives (This Improvement Sprint)

- Lift baseline discriminatory power & maintain calibration
- Enforce data contracts & validation for input reliability
- Provide transparent global & local explanations (SHAP)
- Add drift & stability monitoring (PSI + feature importance overlap)
- Deliver an interactive dashboard for non-technical review
- Achieve engineering reliability (tests, CI, reproducibility)

## What Was Accomplished Previously

- Initial exploratory data analysis & baseline logistic regression (uncalibrated)
- Basic feature list crafted (demographics, credit bureau signals)
- Manual notebook experimentation for AUC estimation (~0.74 preliminary)
- Informal feature importance review (coefficient magnitudes)

## Planned Extensions (High-Level)

1. Formalize schema & validation (reject malformed inputs)
2. Modularize feature engineering & add derived ratios
3. Implement calibrated modeling pipeline (LogReg + XGBoost comparison)
4. Evaluation module (ROC, KS, Brier, calibration curve)
5. Monitoring (PSI drift + SHAP stability) offline job
6. Explainability utilities (global summary, local waterfall)
7. Streamlit dashboard (KPIs, scenario explorer, drift panel)
8. CI/CD (lint, tests, security scan, build artifact)
9. Model Card & governance docs

## Detailed Week Plan

| Day | Task                           | Definition of Done                            | Risk                   | Mitigation                      |
| --- | ------------------------------ | --------------------------------------------- | ---------------------- | ------------------------------- |
| 1   | Repo restructure & config      | New modular folders + settings module         | Scope creep            | Freeze structure after day 1    |
| 1   | Data schema & validation tests | Pydantic models + failing invalid sample test | Ambiguous field ranges | Confirm with assumptions doc    |
| 2   | Feature engineering module     | Functions pure + unit tests                   | Feature leakage        | Exclude target in builder tests |
| 2   | Baseline training script       | Re-runnable, outputs metrics.json             | Data imbalance         | Use stratified split            |
| 3   | Add XGBoost + calibration      | Calibrated probabilities & comparison table   | Overfitting            | Cross-validate & early stopping |
| 3   | Evaluation metrics module      | KS, Brier, calibration plot saved             | Metric miscalc         | Cross-check small manual calc   |
| 4   | Drift monitoring (PSI)         | Function + test with synthetic shift          | False alerts           | Set sensible PSI thresholds     |
| 4   | SHAP explainability utils      | Global summary + sample local plot            | Perf cost              | Cache model & background set    |
| 5   | Streamlit dashboard            | Sections: KPIs, scenario, drift, SHAP         | Time overrun           | Build minimal MVP first         |
| 5   | Integration test (E2E train)   | Test passes with synthetic data               | Flaky randomness       | Fix seed                        |
| 6   | CI workflow + coverage         | GitHub Actions YAML + badge                   | Tool version conflicts | Pin versions                    |
| 6   | Security & quality gates       | pip-audit, ruff, black CI success             | New vulns              | Document allowlist if needed    |
| 7   | Model card & governance        | docs complete, reviewed                       | Missing sections       | Use template checklist          |
| 7   | Presentation & blog draft      | Slide deck outline + narrative                | Scope expansion        | Prioritize core story first     |

## Assumptions

- Synthetic / sample dataset used for development; real data accessible later under compliance constraints.
- Binary target `defaulted` is 0/1 without severe label noise.
- Class imbalance manageable (<25% default rate) allowing standard logistic baseline.

## Risks & Mitigations

| Risk                      | Impact              | Likelihood | Mitigation                    |
| ------------------------- | ------------------- | ---------- | ----------------------------- |
| Data schema changes late  | Rework              | Medium     | Lock contract & version it    |
| Feature drift undetected  | Performance decay   | Medium     | Implement daily PSI check job |
| Slow SHAP computations    | Dashboard lag       | Medium     | Use sampled background set    |
| Overfitting boosted model | Poor generalization | Medium     | Early stopping + calibration  |
| CI pipeline time >10m     | Developer friction  | Low        | Parallelize jobs & cache deps |

## Success Metrics (Sprint)

- AUC uplift ≥ +0.03 over original baseline or documented reason
- Calibration Brier ≤ 0.18
- PSI for synthetic stable set < 0.1
- ≥ 85% unit test coverage (core modules)
- CI end-to-end < 10 minutes
- Dashboard delivers inference + explanation under 2s per query (synthetic)

## Tools & Stack

Python 3.11, pandas, scikit-learn, XGBoost, SHAP, Streamlit, pytest, ruff, black, pip-audit.

## Next Immediate Actions

- Fix unit test syntax issue and add minimal training test
- Implement evaluation utilities
- Add CI workflow stub
