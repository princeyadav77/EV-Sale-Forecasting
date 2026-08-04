import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="EV Sales Forecasting",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# Title
# -------------------------------
st.title("🚗 EV Sales Forecasting & Analysis System")

st.markdown("""
Welcome to the **Electric Vehicle Sales Forecasting and Analysis System**.

This application analyzes historical EV sales data and predicts future sales using Machine Learning.

---
""")

# -------------------------------
# Project Overview
# -------------------------------

st.header("📌 Project Overview")

st.write("""
This project provides:

- 📈 EV Sales Analysis
- 📊 Interactive Dashboard
- 🤖 Machine Learning Prediction
- 📉 Model Comparison
- 💡 Business Insights
""")

# -------------------------------
# Technologies
# -------------------------------

st.header("🛠 Technologies Used")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("Python")
    st.success("Pandas")
    st.success("NumPy")

with col2:
    st.success("Scikit-Learn")
    st.success("Plotly")
    st.success("Streamlit")

with col3:
    st.success("Random Forest")
    st.success("Linear Regression")
    st.success("Joblib")

# -------------------------------
# Sidebar
# -------------------------------

st.sidebar.title("Navigation")

st.sidebar.info("""
Use the pages on the left sidebar:

📊 Dashboard

🔮 Prediction

📈 Model Comparison

💡 Business Insights
""")

# -------------------------------
# Footer
# -------------------------------

# st.markdown("---")

# st.caption("Developed by Priyanshu Kumar Prasad")