# Governance & Risk Management

## Overview

This document outlines the governance, control framework, and operational processes supporting the Credit Risk Scoring Model.

## Control Matrix

| Control                  | Objective                      | Mechanism                      | Evidence                        |
| ------------------------ | ------------------------------ | ------------------------------ | ------------------------------- |
| Data Schema Validation   | Prevent malformed inputs       | Pydantic models + unit tests   | tests/unit/test_validation\*.py |
| Feature Drift Monitoring | Detect population shifts       | PSI per feature vs baseline    | monitoring PSI report           |
| Performance Monitoring   | Ensure discrimination retained | AUC, KS periodic recompute     | metrics artifacts               |
| Calibration Monitoring   | Maintain probability accuracy  | Brier score & reliability plot | calibration artifacts           |
| Explainability           | Transparency of decisions      | SHAP plots + coefficient table | explainability reports          |
| Dependency Security      | Reduce supply-chain risk       | pip-audit in CI                | CI logs                         |
| Reproducibility          | Deterministic builds           | requirements.txt + seeds       | training script output          |
| Coverage & Testing       | Reduce regression risk         | pytest + coverage threshold    | CI status                       |

## Lifecycle

1. Development: Feature engineering, experimentation (notebooks tracked, no secrets).
2. Validation: Metrics reviewed vs acceptance thresholds; calibration verified.
3. Deployment: Tagged release; artifact stored and hashed.
4. Monitoring: Scheduled job computes drift & performance; alerts if thresholds breached.
5. Retraining: Triggered by threshold breach or quarterly cadence.

## Roles & Responsibilities

| Role         | Responsibility                             |
| ------------ | ------------------------------------------ |
| Model Owner  | Performance, documentation, approvals      |
| Risk Analyst | Independent validation & monitoring review |
| Engineering  | CI/CD, infrastructure, logging             |

## Retraining Triggers

- PSI > 0.2 for any major feature
- AUC degradation > 0.03 absolute vs baseline
- Significant macroeconomic regime change (analyst judgment)

## Documentation Artifacts

- Model Card (`model_card.md`)
- Governance (this file)
- Metrics snapshots (`artifacts/metrics.json`)

## Audit Readiness Checklist

- [ ] Tagged release present
- [ ] All tests green
- [ ] Coverage report archived
- [ ] Latest drift report under threshold
- [ ] Calibration plot current
- [ ] SHAP feature importance stable vs prior period

## Incident Response

If drift or performance breach detected:

1. Log incident with timestamp & metric delta.
2. Assess data pipeline integrity (schema + volume).
3. Run expedited retrain on updated dataset.
4. Recalibrate & regenerate explainability artifacts.
5. Update model card with new version + change log.
