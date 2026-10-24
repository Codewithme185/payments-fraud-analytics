import pandas as pd

df = pd.read_csv("/Users/rajaansari/Documents/Project 1/PS_20174392719_1491204439457_log.csv")

print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head().to_string(index=False))
print("\nColumn Names:")
print(df.columns.tolist())

print("\nTotal Fraud Cases:", df["isFraud"].sum())

print("\nFraud vs Normal Transactions:")
print(df["isFraud"].value_counts())

print("\nFraud by Transaction Type:")
print(df.groupby("type")["isFraud"].sum())

print("\nFraud Rate by Transaction Type (%):")
print(
    (df.groupby("type")["isFraud"].mean() * 100)
    .round(3)
)

summary = df.groupby("type").agg(
    total_transactions=("type", "count"),
    total_amount=("amount", "sum"),
    fraud_cases=("isFraud", "sum"),
    fraud_rate=("isFraud", "mean")
).reset_index()

summary["fraud_rate"] = (summary["fraud_rate"] * 100).round(3)

summary.to_csv("fraud_summary.csv", index=False)

print("\nSummary exported successfully!")
print(summary)
from sqlalchemy import create_engine

engine = create_engine("sqlite:///fraud_analysis.db")

df.to_sql(
    "transactions",
    engine,
    if_exists="replace",
    index=False,
    chunksize=100000
)

print("Data successfully loaded into SQL database!")

import sqlite3

conn = sqlite3.connect("fraud_analysis.db")

query = """
SELECT
    type,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount), 2) AS total_amount,
    SUM(isFraud) AS fraud_cases,
    ROUND(AVG(isFraud) * 100, 3) AS fraud_rate
FROM transactions
GROUP BY type
ORDER BY fraud_rate DESC;
"""

result = pd.read_sql_query(query, conn)
print(result)

conn.close()