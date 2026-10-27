
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv(
    "data/cleaned_online_retail.csv",
    parse_dates=["InvoiceDate"]
)

# Create a date-only column
df["Date"] = df["InvoiceDate"].dt.date

# Calculate total revenue for each day
daily_sales = df.groupby("Date")["Revenue"].sum()

# Save daily revenue
daily_sales.to_csv("data/daily_revenue.csv")

print("Total days:", len(daily_sales))
print("\nFirst 5 days of sales:")
print(daily_sales.head())

print("\nHighest revenue day:")
print(daily_sales.idxmax(), round(daily_sales.max(), 2))

print("\nLowest revenue day:")
print(daily_sales.idxmin(), round(daily_sales.min(), 2))

# Graph 1: Daily revenue trend
plt.figure(figsize=(12, 5))
daily_sales.plot()
plt.title("Daily Retail Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("graphs/graph1_daily_revenue.png")
plt.close()
plt.close()
print("Graph saved successfully!")

# Graph 2: Top 10 countries by revenue
country_sales = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

plt.figure(figsize=(10, 6))
country_sales.plot(kind="barh")
plt.title("Top 10 Countries by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("graphs/graph2_country_revenue.png")
plt.close()

# Graph 3: Top 10 products by revenue
product_sales = (
    df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

plt.figure(figsize=(10, 6))
product_sales.plot(kind="barh")
plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig("graphs/graph3_product_revenue.png")
plt.close()
print("\nAll 3 graphs saved in the graphs folder!")
