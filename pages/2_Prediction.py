import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="EV Sales Prediction",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 EV Sales Prediction")

st.info(
    """
This page predicts EV Sales using the trained Machine Learning models.

Available Models:
- Linear Regression
- Random Forest
"""
)

# ----------------------------------------------------
# Load Dataset
# ----------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv(
        "data/processed/ev_sales_feature_engineered.csv"
    )


df = load_data()

# ----------------------------------------------------
# Load Models
# ----------------------------------------------------

lr_model = joblib.load("models/linear_regression.pkl")
rf_model = joblib.load("models/random_forest.pkl")

feature_columns = joblib.load("models/feature_columns.pkl")

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

st.sidebar.header("Prediction Settings")

selected_model = st.sidebar.selectbox(
    "Select Model",
    (
        "Random Forest",
        "Linear Regression"
    )
)

selected_year = st.sidebar.selectbox(
    "Select Year",
    sorted(df["Year"].unique())
)

selected_month = st.sidebar.selectbox(
    "Select Month",
    sorted(df["Month"].unique())
)

selected_state = st.sidebar.selectbox(
    "Select State",
    sorted(df["State"].unique())
)

selected_vehicle = st.sidebar.selectbox(
    "Vehicle Category",
    sorted(df["Vehicle_Category"].unique())
)

# ----------------------------------------------------
# Input Summary
# ----------------------------------------------------

st.subheader("📋 Selected Inputs")

c1, c2 = st.columns(2)

with c1:
    st.write("**Model** :", selected_model)
    st.write("**Year** :", selected_year)

with c2:
    st.write("**Month** :", selected_month)
    st.write("**State** :", selected_state)
    st.write("**Vehicle** :", selected_vehicle)

st.divider()

# ----------------------------------------------------
# Prepare Input Data
# ----------------------------------------------------

input_data = {
    "Year": selected_year,
    "Month": selected_month,
    "Quarter": (selected_month - 1) // 3 + 1,
    "Lag_1": 0,
    "Lag_2": 0,
    "Lag_3": 0,
    "Rolling_3": 0,
    "Rolling_STD_3": 0,
    "MoM_Growth": 0
}

input_df = pd.DataFrame([input_data])

# One-Hot Encode
input_df = pd.get_dummies(input_df)

# Add Missing Columns

for column in feature_columns:
    if column not in input_df.columns:
        input_df[column] = 0

# Set Selected State

state_column = f"State_{selected_state}"

if state_column in input_df.columns:
    input_df[state_column] = 1

# Set Selected Vehicle

vehicle_column = f"Vehicle_Category_{selected_vehicle}"

if vehicle_column in input_df.columns:
    input_df[vehicle_column] = 1

# Arrange Columns

input_df = input_df.reindex(
    columns=feature_columns,
    fill_value=0
)

# ----------------------------------------------------
# Prediction
# ----------------------------------------------------

if st.button("🚀 Predict EV Sales"):

    if selected_model == "Random Forest":
        prediction = rf_model.predict(input_df)[0]
    else:
        prediction = lr_model.predict(input_df)[0]

    prediction = max(0, prediction)

    st.success("Prediction Completed Successfully!")

    st.metric(
        label="Predicted EV Sales",
        value=f"{prediction:,.0f}"
    )

    st.divider()

    st.subheader("📈 Prediction Summary")

    summary = pd.DataFrame({
        "Parameter": [
            "Model",
            "Year",
            "Month",
            "State",
            "Vehicle Category",
            "Predicted Sales"
        ],
        "Value": [
            selected_model,
            selected_year,
            selected_month,
            selected_state,
            selected_vehicle,
            round(prediction)
        ]
    })

    st.table(summary)

    st.divider()

    st.subheader("📊 Prediction Visualization")

    chart_df = pd.DataFrame({
        "Category": ["Predicted EV Sales"],
        "Sales": [prediction]
    })

    st.bar_chart(chart_df.set_index("Category"))

# ----------------------------------------------------
# Information
# ----------------------------------------------------

st.divider()

with st.expander("ℹ️ About This Prediction"):

    st.write("""
The prediction is generated using trained Machine Learning models.

Current Models:
- Linear Regression
- Random Forest

Features Used:
- Year
- Month
- Quarter
- State
- Vehicle Category
- Historical engineered features

**Note:**

This prediction is based on the available historical dataset and engineered features. Since the current application sets lag-based features to default values, predictions are intended for demonstration purposes. A production-grade forecasting system would automatically compute historical lag features before generating predictions.
""")