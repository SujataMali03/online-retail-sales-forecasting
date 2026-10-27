
import pandas as pd

# 1. Load the original dataset
df = pd.read_excel("data/Online Retail.xlsx")

print("Original rows:", len(df))

# 2. Remove duplicate rows
df = df.drop_duplicates()
print("After removing duplicates:", len(df))

# 3. Remove rows with missing essential transaction details
df = df.dropna(
    subset=["InvoiceNo", "StockCode", "InvoiceDate",
            "Quantity", "UnitPrice"]
)

# 4. Ensure correct data types
df["InvoiceNo"] = df["InvoiceNo"].astype(str)
df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"], errors="coerce"
)
df["Quantity"] = pd.to_numeric(
    df["Quantity"], errors="coerce"
)
df["UnitPrice"] = pd.to_numeric(
    df["UnitPrice"], errors="coerce"
)

# 5. Remove invalid dates and numeric values
df = df.dropna(
    subset=["InvoiceDate", "Quantity", "UnitPrice"]
)

df = df[
    (df["Quantity"] > 0) &
    (df["UnitPrice"] > 0)
]

# 6. Exclude cancelled invoices
df = df[
    ~df["InvoiceNo"].str.startswith("C", na=False)
]

# 7. Calculate revenue
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# 8. Show the cleaning results
print("\nCleaned rows:", len(df))
print("Columns:", df.columns.tolist())
print("Remaining duplicates:", df.duplicated().sum())
print("Total sales revenue:", round(df["Revenue"].sum(), 2))

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# 9. Save the cleaned dataset
df.to_csv("data/cleaned_online_retail.csv", index=False)

print("\nCleaned dataset saved successfully!")
