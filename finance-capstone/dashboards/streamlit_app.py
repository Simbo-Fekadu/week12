import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="Credit Risk Scoring Dashboard", layout="wide")

st.title("Credit Risk Scoring Dashboard")

metrics_path = Path("artifacts/metrics.json")
if metrics_path.exists():
    with open(metrics_path) as f:
        data = json.load(f)
    st.metric("Baseline AUC", f"{data.get('auc', 'NA'):.3f}" if isinstance(data.get('auc'), (int,float)) else data.get('auc'))
    st.write("Features:", ", ".join(data.get("features", [])))
else:
    st.warning("Metrics artifact not found. Run training script first.")

st.header("Next Features")
st.markdown("- Add SHAP global summary plot\n- Add scenario explorer for applicant features\n- Add drift (PSI) visualization")
