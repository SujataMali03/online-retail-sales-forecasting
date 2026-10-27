
import pandas as pd

# Load cleaned transaction data
df = pd.read_csv(
    "data/cleaned_online_retail.csv",
    parse_dates=["InvoiceDate"]
)

# Aggregate transaction revenue by calendar day
df["Date"] = df["InvoiceDate"].dt.normalize()

daily = (
    df.groupby("Date")["Revenue"]
    .sum()
    .sort_index()
)

# Include days with no recorded sales
daily = daily.asfreq("D", fill_value=0)

# Create a DataFrame for forecasting
features = daily.to_frame(name="Revenue")

# Calendar features
features["DayOfWeek"] = features.index.dayofweek
features["Month"] = features.index.month
features["DayOfMonth"] = features.index.day

# Previous-day and previous-week revenue
features["Lag1"] = features["Revenue"].shift(1)
features["Lag7"] = features["Revenue"].shift(7)

# Previous seven days' average, excluding the current day
features["RollingMean7"] = (
    features["Revenue"].shift(1).rolling(7).mean()
)

print("First 10 rows of daily revenue:")
print(features.head(10))

print("\nFeature columns:")
print(features.columns.tolist())

# Save features for inspection
features.to_csv("data/forecast_features.csv")

print("\nFeature dataset saved successfully!")
