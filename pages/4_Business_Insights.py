import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Business Insights",
    page_icon="💡",
    layout="wide"
)

st.title("💡 Business Insights")

st.markdown("""
This page highlights key business insights derived from the Electric Vehicle Sales dataset.
""")

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv(
        "data/processed/ev_sales_feature_engineered.csv",
        parse_dates=["Date"]
    )

df = load_data()

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------

total_sales = df["EV_Sales"].sum()
avg_sales = df["EV_Sales"].mean()
total_states = df["State"].nunique()
vehicle_types = df["Vehicle_Category"].nunique()

c1, c2, c3, c4 = st.columns(4)

c1.metric("🚗 Total EV Sales", f"{total_sales:,.0f}")
c2.metric("📊 Average Sales", f"{avg_sales:,.0f}")
c3.metric("🗺 States Covered", total_states)
c4.metric("🚘 Vehicle Categories", vehicle_types)

st.divider()

# --------------------------------------------------
# Top Performing State
# --------------------------------------------------

state_sales = (
    df.groupby("State")["EV_Sales"]
      .sum()
      .sort_values(ascending=False)
      .reset_index()
)

top_state = state_sales.iloc[0]
lowest_state = state_sales.iloc[-1]

left, right = st.columns(2)

with left:

    st.subheader("🏆 Top Performing States")

    fig = px.bar(
        state_sales.head(10),
        x="EV_Sales",
        y="State",
        orientation="h",
        color="EV_Sales",
        title="Top 10 States by EV Sales"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    st.subheader("📌 Key State Insights")

    st.success(f"""
Top State

**{top_state['State']}**

Total Sales

**{top_state['EV_Sales']:,.0f}**
""")

    st.error(f"""
Lowest Performing State

**{lowest_state['State']}**

Total Sales

**{lowest_state['EV_Sales']:,.0f}**
""")

st.divider()

# --------------------------------------------------
# Vehicle Category Analysis
# --------------------------------------------------

vehicle_sales = (
    df.groupby("Vehicle_Category")["EV_Sales"]
      .sum()
      .reset_index()
)

st.subheader("🚘 Vehicle Category Analysis")

fig = px.pie(
    vehicle_sales,
    names="Vehicle_Category",
    values="EV_Sales",
    hole=0.45
)

st.plotly_chart(fig, use_container_width=True)

best_vehicle = vehicle_sales.loc[
    vehicle_sales["EV_Sales"].idxmax()
]

st.info(
    f"🏆 Best Selling Vehicle Category: **{best_vehicle['Vehicle_Category']}**"
)

st.divider()

# --------------------------------------------------
# Monthly Trend
# --------------------------------------------------

monthly = (
    df.groupby("Month")["EV_Sales"]
      .sum()
      .reset_index()
)

st.subheader("📅 Monthly EV Sales")

fig = px.line(
    monthly,
    x="Month",
    y="EV_Sales",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

peak_month = monthly.loc[
    monthly["EV_Sales"].idxmax()
]

st.success(
    f"Highest Sales Month: **Month {int(peak_month['Month'])}**"
)

st.divider()

# --------------------------------------------------
# Yearly Growth
# --------------------------------------------------

yearly = (
    df.groupby("Year")["EV_Sales"]
      .sum()
      .reset_index()
)

st.subheader("📈 Yearly EV Sales")

fig = px.bar(
    yearly,
    x="Year",
    y="EV_Sales",
    color="EV_Sales",
    text_auto=True
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# --------------------------------------------------
# Business Recommendations
# --------------------------------------------------

st.subheader("📋 Business Recommendations")

recommendations = [
    "Expand charging infrastructure in high-growth states.",
    "Increase dealership presence in top-performing markets.",
    "Focus marketing campaigns on the highest-selling vehicle category.",
    "Prepare inventory before peak demand months.",
    "Offer incentives in low-performing states to improve adoption.",
    "Use sales trends to optimize production planning."
]

for rec in recommendations:
    st.write(f"✅ {rec}")

st.divider()

# --------------------------------------------------
# Executive Summary
# --------------------------------------------------

st.subheader("📑 Executive Summary")

st.success(f"""
• Total EV Sales: {total_sales:,.0f}

• Top State: {top_state['State']}

• Best Vehicle Category: {best_vehicle['Vehicle_Category']}

• Highest Sales Month: {int(peak_month['Month'])}

• States Covered: {total_states}

• Vehicle Categories: {vehicle_types}

The analysis shows steady EV market growth with significant variation across
states and vehicle categories. These insights can support better inventory,
marketing, and infrastructure planning.
""")