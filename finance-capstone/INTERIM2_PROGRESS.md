# Interim Submission 2 Progress Report

## Project Recap

**Title:** Credit Risk Scoring Platform (Probability of Default Modeling & Monitoring)
**Sprint Goal:** Strengthen reliability, transparency, and monitoring for a finance-ready PD scoring pipeline.

## Original Plan vs Progress Snapshot

| Area                       | Planned (Interim 1 Plan)    | Status          | Notes                                            |
| -------------------------- | --------------------------- | --------------- | ------------------------------------------------ |
| Repo Restructure & Config  | Complete by Day 1           | ✅ Done         | Folder skeleton + settings module in place       |
| Data Schema & Validation   | Pydantic model + tests      | ✅ Done         | Added success & failing tests                    |
| Feature Engineering Module | Basic transforms + tests    | ✅ Base Done    | Engineered ratios added; selection pending       |
| Baseline Training Script   | Logistic baseline + metrics | ✅ Done         | Synthetic data AUC stored (metrics JSON planned) |
| XGBoost + Calibration      | Model + comparison          | ⏳ Pending      | Await dependency install (network issue)         |
| Evaluation Module          | KS, Brier, calibration plot | ✅ Metrics core | Plotting/calibration not yet implemented         |
| Drift Monitoring (PSI)     | Function + test             | ⏳ Pending      | To implement after eval plots                    |
| SHAP Explainability        | Global + local utilities    | ⏳ Pending      | Will follow model finalization                   |
| Streamlit Dashboard        | KPIs, scenario, drift, SHAP | ⏳ Pending      | Scaffold not yet added                           |
| Integration Test (E2E)     | Synthetic end-to-end        | ⏳ Pending      | Blocked until modeling stabilized                |
| CI Workflow & Coverage     | Actions YAML + badge        | ⏳ Pending      | To add next iteration                            |
| Security & Quality Gates   | pip-audit, ruff, black      | ⏳ Pending      | Network install issue paused                     |
| Model Card & Governance    | Draft docs                  | ⏳ Pending      | Template planned Day 6–7                         |
| Presentation & Blog Draft  | Outline                     | ⏳ Pending      | To start after core features                     |

## Detailed Daily Log

| Date  | Planned                      | Done                                                     | Variance | Reason                             | Reschedule Action                                         |
| ----- | ---------------------------- | -------------------------------------------------------- | -------- | ---------------------------------- | --------------------------------------------------------- |
| Day 1 | Structure + schema           | Structure + schema + success test                        | 0        | -                                  | -                                                         |
| Day 2 | Feature eng + baseline       | Feature eng + baseline training script + eval metrics fn | + Extra  | Added eval earlier                 | Shift calibration to Day 3                                |
| Day 3 | XGBoost + calibration        | (Blocked)                                                | -1 Task  | Dependency install network failure | Retry install; fallback to pure sklearn stack if persists |
| Day 4 | Drift + SHAP                 | Not started                                              | -        | Pre-req models incomplete          | Move drift to Day 5                                       |
| Day 5 | Dashboard + integration test | Not started                                              | -        | Upstream tasks pending             | Compress dashboard + SHAP Day 6                           |

## Variances & Root Causes

- External: Package installation via conda timing out (network).
- Internal: Added evaluation earlier than scheduled (positive variance) but delayed advanced modeling.

## Mitigation & Adjusted Plan

| Issue                                              | Mitigation                                                    | New Target        |
| -------------------------------------------------- | ------------------------------------------------------------- | ----------------- |
| Network dependency install failures                | Retry with pip wheels; reduce deps temporarily                | Next work session |
| Modeling delay impacts SHAP & dashboard            | Implement temporary logistic-only explainability (coef-based) | Interim +1 day    |
| Drift monitoring depends on baseline reference set | Generate synthetic stable baseline now                        | Immediate         |

## Updated Upcoming Tasks (Next 48h)

1. Add CI workflow skeleton (lint + tests) and run locally.
2. Implement PSI drift function & unit test with shifted synthetic feature.
3. Add calibration (isotonic or Platt) wrapper for logistic model.
4. Create minimal Streamlit scaffold with KPI placeholders pulling `metrics.json`.
5. Draft model card template file.

## Current Metrics (Synthetic Placeholder)

Pending execution of training to capture AUC & Brier in `artifacts/metrics.json` (not yet written to disk). Evaluation function logic prepared.

## Risks Emerging

| Risk                                      | Severity | Action                                               |
| ----------------------------------------- | -------- | ---------------------------------------------------- |
| Continued dependency installation failure | Medium   | Use alternative mirror / pip only                    |
| Scope compression (dashboard + SHAP late) | Medium   | Prioritize global SHAP after calibration only        |
| Lack of real dataset for drift realism    | Low      | Use parameterized synthetic generator for simulation |

## Evidence Links

- Codebase: (repo main branch) – ensure commit hash after each major module.
- Tests: Located under `tests/unit/` (validation, evaluation, failure case)

## Next Report Focus

Show concrete metrics (AUC, KS, Brier), calibration plot artifact, PSI example, CI run screenshot.

## Support Needed

- (If available) Alternative Python package index / allow pip wheels
- Clarify acceptable minimum for interim if XGBoost delayed

---

Prepared for Interim Submission 2; will update metrics & artifacts once dependency installation succeeds.
