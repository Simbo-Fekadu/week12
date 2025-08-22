import streamlit as st
import json
from pathlib import Path
import pandas as pd

st.set_page_config(page_title="Credit Risk Scoring Dashboard", layout="wide")
st.title("Credit Risk Scoring Dashboard")

cols = st.columns(4)
metrics_path = Path("artifacts/metrics.json")
if metrics_path.exists():
    with open(metrics_path) as f:
        data = json.load(f)
    auc = data.get("auc")
    ks = data.get("ks")
    brier = data.get("brier")
    cols[0].metric("AUC", f"{auc:.3f}" if isinstance(auc, (int, float)) else auc)
    cols[1].metric("KS", f"{ks:.3f}" if isinstance(ks, (int, float)) else ks)
    cols[2].metric("Brier", f"{brier:.3f}" if isinstance(brier, (int, float)) else brier)
    cols[3].metric("#Features", len(data.get("features", [])))
    st.write("Model Type:", data.get("model_type"))
else:
    st.warning("Metrics artifact not found. Run training script first.")

st.subheader("Feature List")
if metrics_path.exists():
    st.code(", ".join(data.get("features", [])) or "(none)")

st.subheader("Explainability (Planned)")
st.markdown("Global SHAP summary and local instance breakdown will appear here once generated.")

st.subheader("Roadmap")
st.markdown("- Add SHAP global summary plot\n- Add scenario explorer for applicant features\n- Add drift (PSI) visualization")
