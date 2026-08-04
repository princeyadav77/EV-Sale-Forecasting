import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------
# Page Configuration
# ----------------------------------

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 EV Sales Dashboard")

# ----------------------------------
# Load Dataset
# ----------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv(
        "data/processed/ev_sales_feature_engineered.csv",
        parse_dates=["Date"]
    )
    return df

df = load_data()

# ----------------------------------
# Sidebar Filters
# ----------------------------------

st.sidebar.header("Filters")

state = st.sidebar.selectbox(
    "Select State",
    ["All"] + sorted(df["State"].unique().tolist())
)

vehicle = st.sidebar.selectbox(
    "Vehicle Category",
    ["All"] + sorted(df["Vehicle_Category"].unique().tolist())
)

year = st.sidebar.selectbox(
    "Year",
    ["All"] + sorted(df["Year"].unique().tolist())
)

# ----------------------------------
# Apply Filters
# ----------------------------------

filtered_df = df.copy()

if state != "All":
    filtered_df = filtered_df[
        filtered_df["State"] == state
    ]

if vehicle != "All":
    filtered_df = filtered_df[
        filtered_df["Vehicle_Category"] == vehicle
    ]

if year != "All":
    filtered_df = filtered_df[
        filtered_df["Year"] == year
    ]

# ----------------------------------
# KPI Cards
# ----------------------------------

total_sales = filtered_df["EV_Sales"].sum()
average_sales = filtered_df["EV_Sales"].mean()
max_sales = filtered_df["EV_Sales"].max()
min_sales = filtered_df["EV_Sales"].min()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Sales", f"{total_sales:,.0f}")
c2.metric("Average Sales", f"{average_sales:,.2f}")
c3.metric("Highest Sales", f"{max_sales:,.0f}")
c4.metric("Lowest Sales", f"{min_sales:,.0f}")

st.divider()

# ----------------------------------
# Sales Trend
# ----------------------------------

st.subheader("📈 EV Sales Trend")

trend = (
    filtered_df
    .groupby("Date")["EV_Sales"]
    .sum()
    .reset_index()
)

fig = px.line(
    trend,
    x="Date",
    y="EV_Sales",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------
# Two Charts
# ----------------------------------

left, right = st.columns(2)

with left:

    state_sales = (
        filtered_df
        .groupby("State")["EV_Sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        state_sales,
        x="State",
        y="EV_Sales",
        title="State-wise Sales"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    vehicle_sales = (
        filtered_df
        .groupby("Vehicle_Category")["EV_Sales"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        vehicle_sales,
        names="Vehicle_Category",
        values="EV_Sales",
        title="Vehicle Category Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

# ----------------------------------
# Monthly Sales
# ----------------------------------

st.subheader("📅 Monthly Sales")

monthly = (
    filtered_df
    .groupby("Month")["EV_Sales"]
    .sum()
    .reset_index()
)

fig = px.bar(
    monthly,
    x="Month",
    y="EV_Sales"
)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------
# Show Dataset
# ----------------------------------

st.subheader("📄 Dataset Preview")

st.dataframe(
    filtered_df,
    use_container_width=True
)