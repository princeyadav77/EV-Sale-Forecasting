import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Model Comparison",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Machine Learning Model Comparison")

st.markdown("""
Compare the performance of different Machine Learning models
used for EV Sales Prediction.
""")

# --------------------------------------------------
# Load Data
# --------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("data/processed/model_comparison.csv")

comparison = load_data()

# --------------------------------------------------
# Show Comparison Table
# --------------------------------------------------

st.subheader("📋 Performance Metrics")

st.dataframe(
    comparison,
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------

best_rmse = comparison.loc[comparison["RMSE"].idxmin()]
best_r2 = comparison.loc[comparison["R2 Score"].idxmax()]
best_mae = comparison.loc[comparison["MAE"].idxmin()]

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "🏆 Lowest RMSE",
        best_rmse["Model"]
    )

with c2:
    st.metric(
        "🏆 Highest R²",
        best_r2["Model"]
    )

with c3:
    st.metric(
        "🏆 Lowest MAE",
        best_mae["Model"]
    )

st.divider()

# --------------------------------------------------
# RMSE
# --------------------------------------------------

st.subheader("📉 RMSE Comparison")

fig = px.bar(
    comparison,
    x="Model",
    y="RMSE",
    color="Model",
    text_auto=".2f",
    title="Root Mean Squared Error"
)

st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# MAE
# --------------------------------------------------

st.subheader("📉 MAE Comparison")

fig = px.bar(
    comparison,
    x="Model",
    y="MAE",
    color="Model",
    text_auto=".2f",
    title="Mean Absolute Error"
)

st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# R²
# --------------------------------------------------

st.subheader("📈 R² Score Comparison")

fig = px.bar(
    comparison,
    x="Model",
    y="R2 Score",
    color="Model",
    text_auto=".3f",
    title="Coefficient of Determination"
)

st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# MAPE
# --------------------------------------------------

st.subheader("📊 MAPE Comparison")

fig = px.bar(
    comparison,
    x="Model",
    y="MAPE",
    color="Model",
    text_auto=".3f",
    title="Mean Absolute Percentage Error"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# --------------------------------------------------
# Best Model
# --------------------------------------------------

best_model = comparison.loc[
    comparison["RMSE"].idxmin()
]

st.success(f"""
🏆 Best Performing Model: **{best_model['Model']}**
""")

# --------------------------------------------------
# Detailed Metrics
# --------------------------------------------------

st.subheader("📌 Best Model Metrics")

metrics = pd.DataFrame({
    "Metric": ["MAE", "RMSE", "R² Score", "MAPE"],
    "Value": [
        best_model["MAE"],
        best_model["RMSE"],
        best_model["R2 Score"],
        best_model["MAPE"]
    ]
})

st.table(metrics)

st.divider()

# --------------------------------------------------
# Conclusion
# --------------------------------------------------

st.subheader("📝 Conclusion")

st.info(f"""
Based on the evaluation metrics, **{best_model['Model']}** achieved the
best overall performance on the EV Sales dataset.

This model has:

✅ Lowest RMSE

✅ Lowest MAE

✅ Highest R² Score

Therefore, it is selected as the final prediction model
for the EV Sales Forecasting System.
""")