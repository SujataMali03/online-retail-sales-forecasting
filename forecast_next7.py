
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

# Load the feature dataset
df = pd.read_csv(
    "data/forecast_features.csv",
    parse_dates=["Date"],
    index_col="Date"
).sort_index()

# Remove rows with missing features
training_data = df.dropna()

feature_columns = [
    "DayOfWeek",
    "Month",
    "DayOfMonth",
    "Lag1",
    "Lag7",
    "RollingMean7"
]

X = training_data[feature_columns]
y = training_data["Revenue"]

# Train the model on all available historical data
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)
model.fit(X, y)

# Start forecasting after the last recorded date
history = df["Revenue"].copy()
last_date = history.index.max()

forecast_rows = []

for step in range(1, 8):
    next_date = last_date + pd.Timedelta(days=step)

    lag1 = history.iloc[-1]
    lag7 = history.iloc[-7]
    rolling_mean7 = history.iloc[-7:].mean()

    row = pd.DataFrame([{
        "DayOfWeek": next_date.dayofweek,
        "Month": next_date.month,
        "DayOfMonth": next_date.day,
        "Lag1": lag1,
        "Lag7": lag7,
        "RollingMean7": rolling_mean7
    }])

    prediction = model.predict(row[feature_columns])[0]

    # Revenue cannot be negative
    prediction = max(0, prediction)

    forecast_rows.append({
        "Date": next_date,
        "PredictedRevenue": round(prediction, 2)
    })

    # Add prediction to history for the next forecast
    history.loc[next_date] = prediction

# Save the seven-day forecast
forecast = pd.DataFrame(forecast_rows)
forecast.to_csv("data/next7day_forecast.csv", index=False)

print("Next 7 Days Sales Forecast")
print(forecast.to_string(index=False))

print("\nForecast saved to data/next7day_forecast.csv")

# Plot the predicted revenue
plt.figure(figsize=(10, 5))
plt.plot(
    forecast["Date"],
    forecast["PredictedRevenue"],
    marker="o"
)
plt.title("Next 7 Days Sales Revenue Forecast")
plt.xlabel("Date")
plt.ylabel("Predicted Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/graph4_next7day_forecast.png")
plt.close()

print("Forecast graph saved successfully!")
