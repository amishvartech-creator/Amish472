# Create a Pandas DataFrame containing at least 8 products and their sales quantities.
import pandas as pd
import matplotlib.pyplot as plt

product_data = {
    "Product": [
        " Amul",
        " Britania",
        " Cadbury",
        " Dabur",
        " Earpods",
        " Facewash",
        " Glucose",
        " Horlicks"
    ],
    "Sales": [
        100000,
        150000,
        250000,
        180000,
        120000,
        160000,
        140000,
        190000
    ]

}

product_df = pd.DataFrame(product_data)
print(product_df)
print("-------------------------------------------------------------------")
print("Total Sales Quantity:", product_df["Sales"].sum())
print("the top three best selling products:", product_df.nlargest(3, "Sales"))

plt.title("Display Data in Pie Chart")
plt.pie(product_df["Sales"], labels=product_df["Product"], autopct="%1.1f%%")
plt.show()
