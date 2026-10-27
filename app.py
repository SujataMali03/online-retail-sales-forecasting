
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(
    page_title="Online Retail Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("Online Retail Sales Analysis & Revenue Forecasting")
st.write(
    "Explore historical retail sales, product performance, "
    "country-wise revenue, and the seven-day sales forecast."
)

# Check project files
cleaned_file = Path("data/cleaned_online_retail.csv")
daily_file = Path("data/daily_revenue.csv")
forecast_file = Path("data/next7day_forecast.csv")

if not cleaned_file.exists():
    st.error("Cleaned dataset not found. Please run data_analysis.py first.")
    st.stop()

df = pd.read_csv(cleaned_file, parse_dates=["InvoiceDate"])

# Summary metrics
total_revenue = df["Revenue"].sum()
total_transactions = df["InvoiceNo"].nunique()
total_products = df["StockCode"].nunique()
total_countries = df["Country"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"{total_revenue:,.2f}")
col2.metric("Transactions", f"{total_transactions:,}")
col3.metric("Products", f"{total_products:,}")
col4.metric("Countries", f"{total_countries:,}")

st.divider()

# Daily revenue chart
st.subheader("Daily Revenue Trend")

if daily_file.exists():
    daily = pd.read_csv(daily_file, index_col=0, parse_dates=True)
    daily.columns = ["Revenue"]

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(daily.index, daily["Revenue"])
    ax.set_xlabel("Date")
    ax.set_ylabel("Revenue")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
else:
    st.warning("Daily revenue file not found. Run sales_analysis.py first.")

# Country analysis
st.subheader("Top 10 Countries by Revenue")

country_sales = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

fig, ax = plt.subplots(figsize=(10, 5))
country_sales.plot(kind="barh", ax=ax)
ax.set_xlabel("Revenue")
ax.set_ylabel("Country")
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# Product analysis
st.subheader("Top 10 Products by Revenue")

product_sales = (
    df.groupby("Description")["Revenue"]
    .sum()
    .nlargest(10)
    .sort_values()
)

fig, ax = plt.subplots(figsize=(10, 5))
product_sales.plot(kind="barh", ax=ax)
ax.set_xlabel("Revenue")
ax.set_ylabel("Product")
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# Seven-day forecast
st.subheader("Next 7 Days Revenue Forecast")

if forecast_file.exists():
    forecast = pd.read_csv(forecast_file, parse_dates=["Date"])
    st.dataframe(forecast, use_container_width=True)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(
        forecast["Date"],
        forecast["PredictedRevenue"],
        marker="o"
    )
    ax.set_xlabel("Date")
    ax.set_ylabel("Predicted Revenue")
    ax.grid(True, alpha=0.3)
    fig.autofmt_xdate()
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
else:
    st.warning("Forecast file not found. Run forecast_next7.py first.")

st.caption(
    "Note: The dataset contains historical transactions from 2010–2011. "
    "Forecasts are estimates and may not represent current retail conditions."
)
