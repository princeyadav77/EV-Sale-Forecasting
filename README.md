# 🚗 EV Sales Forecasting & Analysis System

An end-to-end Machine Learning project that analyzes historical Electric Vehicle (EV) sales data, predicts EV sales using Machine Learning models, and provides interactive business insights through a Streamlit dashboard.

---

## 📌 Project Overview

The EV Sales Forecasting & Analysis System helps users:

- 📊 Analyze historical EV sales trends
- 📈 Visualize state-wise and category-wise sales
- 🤖 Predict EV sales using Machine Learning
- 📉 Compare multiple ML models
- 💡 Generate business insights for decision-making

This project demonstrates the complete Machine Learning workflow, from data preprocessing to model deployment.

---

## 🚀 Features

- ✅ Data Cleaning & Preprocessing
- ✅ Exploratory Data Analysis (EDA)
- ✅ Feature Engineering
- ✅ Linear Regression Model
- ✅ Random Forest Regression Model
- ✅ Model Performance Comparison
- ✅ Interactive Streamlit Dashboard
- ✅ Business Insights Dashboard

---

## 📂 Project Structure

```text
EV_Sales_Forecasting/
│
├── app.py
│
├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_Prediction.py
│   ├── 3_Model_Comparison.py
│   └── 4_Business_Insights.py
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_preparation.ipynb
│   ├── 05_linear_regression.ipynb
│   ├── 06_random_forest.ipynb
│   └── 09_model_comparison.ipynb
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│
├── assets/
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🛠 Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Scikit-learn
- Plotly
- Joblib
- Streamlit

### Development Tools

- Jupyter Notebook
- Visual Studio Code
- Git & GitHub

---

## 📊 Machine Learning Models

### Linear Regression

Used as the baseline regression model for EV sales prediction.

### Random Forest Regression

A tree-based ensemble learning model used to improve prediction accuracy.

---

## 📈 Dashboard Pages

### 🏠 Home

- Project Overview
- Technologies Used
- Navigation

### 📊 Dashboard

- KPI Cards
- Sales Trend
- State-wise Sales
- Vehicle Category Distribution
- Monthly Sales Analysis

### 🔮 Prediction

- Predict EV Sales
- Model Selection
- Prediction Summary

### 📈 Model Comparison

- Performance Metrics
- RMSE Comparison
- MAE Comparison
- R² Score Comparison
- Best Model Selection

### 💡 Business Insights

- Top Performing State
- Best Selling Vehicle Category
- Monthly Sales Trend
- Business Recommendations

---

## 📉 Evaluation Metrics

The models were evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score
- Mean Absolute Percentage Error (MAPE)

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/EV_Sales_Forecasting.git
```

Move into the project directory:

```bash
cd EV_Sales_Forecasting
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📸 Screenshots

Add screenshots of:

- Home Page
- Dashboard
- Prediction Page
- Model Comparison
- Business Insights

---

## 📚 Future Improvements

- Add XGBoost Regression
- Add ARIMA Time Series Forecasting
- Add LSTM Deep Learning Model
- Deploy on AWS/Azure
- Add Real-Time EV Sales Data
- Add Interactive Maps
- Improve Forecast Accuracy

---

## 👨‍💻 Author

**Priyanshu Kumar Prasad**

B.Tech – Computer Science & Engineering

Machine Learning Enthusiast

---

## ⭐ If you found this project useful, consider giving it a star!