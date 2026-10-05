# Create a Pandas DataFrame containing monthly sales data for 12 months.
import pandas as pd
import matplotlib.pyplot as plt

monthly_sales_data = {
    "Month": [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ],
    "Sales": [
        10000,
        12000,
        15000,
        18000,
        20000,
        22000,
        25000,
        28000,
        30000,
        32000,
        35000,
        40000
    ]
}

monthly_sales_df = pd.DataFrame(monthly_sales_data)
print(monthly_sales_df)
print("-------------------------------------------------------------------")
print("total sales for the year:", monthly_sales_df["Sales"].sum())
print("highest sales month:", monthly_sales_df.loc[monthly_sales_df["Sales"].idxmax()]["Month"])
print("lowest sales month:", monthly_sales_df.loc[monthly_sales_df["Sales"].idxmin()]["Month"])

# Line plot for monthly sales trend
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales_df["Month"], monthly_sales_df["Sales"], marker="o", color="blue", linewidth=2)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

