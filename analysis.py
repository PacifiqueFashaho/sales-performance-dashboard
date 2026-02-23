import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales_data.csv")

# Convert Date
df["Date"] = pd.to_datetime(df["Date"])

# Create columns
df["Revenue"] = df["Quantity"] * df["Price"]
df["Profit"] = (df["Price"] - df["Cost"]) * df["Quantity"]
df["Month"] = df["Date"].dt.month

# =============================
# GROUP DATA
# =============================

monthly_revenue = df.groupby("Month")["Revenue"].sum()
monthly_profit = df.groupby("Month")["Profit"].sum()
top_products = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)

# =============================
# PLOT 1 — Monthly Revenue
# =============================

plt.figure()
monthly_revenue.plot(kind="line")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

# =============================
# PLOT 2 — Top Products
# =============================

plt.figure()
top_products.plot(kind="bar")
plt.title("Top Products by Quantity Sold")
plt.xlabel("Product")
plt.ylabel("Total Quantity")
plt.show()

# =============================
# PLOT 3 — Monthly Profit
# =============================

plt.figure()
monthly_profit.plot(kind="line")
plt.title("Monthly Profit Trend")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()