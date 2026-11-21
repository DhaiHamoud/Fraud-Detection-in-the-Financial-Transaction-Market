import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Fraud Model Monitoring", layout="wide")
st.title("Fraud Detection Model Monitoring")
st.caption("Placeholder data for now")

page = st.sidebar.radio("Page", ["Model performance", "Data drift", "Check a transaction"])

# placeholder data, will be replaced with real results
months = pd.period_range("2020-01", "2020-12", freq="M").astype(str)
rng = np.random.default_rng(0)
performance = pd.DataFrame({
    "month": months,
    "precision": rng.uniform(0.6, 0.9, 12).round(2),
    "recall": rng.uniform(0.6, 0.9, 12).round(2),
}).set_index("month")

drift = pd.DataFrame({
    "feature": ["amt", "age", "hour", "amt_to_customer_avg", "hours_since_prev"],
    "psi": [0.02, 0.08, 0.01, 0.15, 0.30],
})
drift["status"] = np.select([drift["psi"] < 0.1, drift["psi"] < 0.25],
                            ["Stable", "Moderate change"], "Major change")

if page == "Model performance":
    st.subheader("Monthly performance (2020)")
    col1, col2 = st.columns(2)
    col1.metric("Average precision", f"{performance['precision'].mean():.2f}")
    col2.metric("Average recall", f"{performance['recall'].mean():.2f}")
    st.line_chart(performance)

elif page == "Data drift":
    st.subheader("Feature drift vs 2019 (PSI)")
    st.dataframe(drift, hide_index=True)
    st.caption("Below 0.1 stable, 0.1 to 0.25 moderate, above 0.25 major")

else:
    st.subheader("Check a transaction")
    amt = st.number_input("Amount ($)", min_value=1.0, value=100.0)
    category = st.selectbox("Category", ["shopping_net", "grocery_pos", "misc_net", "food_dining", "travel"])
    hour = st.slider("Hour", 0, 23, 12)
    if st.button("Check"):
        st.info("Fraud probability: 12% (placeholder)")
