
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load the feature dataset
df = pd.read_csv(
    "data/forecast_features.csv",
    parse_dates=["Date"],
    index_col="Date"
)

# Remove rows with missing lag or rolling features
df = df.dropna()

# Features used by the model
X = df[
    [
        "DayOfWeek",
        "Month",
        "DayOfMonth",
        "Lag1",
        "Lag7",
        "RollingMean7"
    ]
]

# Target: daily revenue
y = df["Revenue"]

# Chronological train-test split (last 20% for testing)
split_index = int(len(df) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))

# Train the Random Forest model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# Generate predictions
predictions = model.predict(X_test)

# Baseline: predict revenue using the previous day's revenue
baseline_predictions = X_test["Lag1"].to_numpy()

# Evaluate both approaches
model_mae = mean_absolute_error(y_test, predictions)
model_rmse = np.sqrt(mean_squared_error(y_test, predictions))

baseline_mae = mean_absolute_error(
    y_test, baseline_predictions
)
baseline_rmse = np.sqrt(
    mean_squared_error(y_test, baseline_predictions)
)

print("\nRandom Forest Model Results")
print("MAE:", round(model_mae, 2))
print("RMSE:", round(model_rmse, 2))

print("\nBaseline Results")
print("MAE:", round(baseline_mae, 2))
print("RMSE:", round(baseline_rmse, 2))

# Save actual and predicted revenue for later analysis
results = pd.DataFrame({
    "ActualRevenue": y_test,
    "ModelPrediction": predictions,
    "BaselinePrediction": baseline_predictions
}, index=y_test.index)

results.to_csv("data/model_results.csv")

print("\nModel results saved to data/model_results.csv")
