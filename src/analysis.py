import pandas as pd
import matplotlib.pyplot as plt

print("Future Interns Task 1")
print("Business Sales Performance Analytics")

# Load dataset
df = pd.read_csv(
    "data/Sample - Superstore.csv",
    encoding="latin1"
)

# Show first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Show column names
print("\nColumns:")
print(df.columns)

# Dataset information
print("\nDataset Info:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Dataset statistics
print("\nDataset Statistics:")
print(df.describe())

# Total Sales
print("\nTotal Sales:")
print(df["Sales"].sum())

#Data Cleaning Code
# Remove duplicate rows
df.drop_duplicates(inplace=True)

print("\nDuplicates Removed!")

# Check shape of dataset
print("\nDataset Shape:")
print(df.shape)

#Regional Sales Analysis
# Sales by Region
print("\nSales by Region:")

region_sales = df.groupby("Region")["Sales"].sum()

print(region_sales)

#Analyze Top Categories
# Sales by Category
print("\nSales by Category:")

category_sales = df.groupby("Category")["Sales"].sum()

print(category_sales)

#Find Top 10 Products
# Top Products
print("\nTop 10 Products:")

top_products = df.groupby("Product Name")["Sales"].sum()

print(top_products.sort_values(ascending=False).head(10))

#Create Region Sales Chart
# Sales by Region Chart

region_sales = df.groupby("Region")["Sales"].sum()

region_sales.plot(kind="bar")

plt.title("Sales by Region")

plt.xlabel("Region")

plt.ylabel("Sales")

plt.show()

#Create Category Chart
# Sales by Category Chart

category_sales = df.groupby("Category")["Sales"].sum()

category_sales.plot(kind="bar")

plt.title("Sales by Category")

plt.xlabel("Category")

plt.ylabel("Sales")

plt.show()

#Create Top Products Chart
# Top 10 Products Chart

top_products = df.groupby("Product Name")["Sales"].sum()

top_10 = top_products.sort_values(ascending=False).head(10)

top_10.plot(kind="bar")

plt.title("Top 10 Products")

plt.xlabel("Products")

plt.ylabel("Sales")

plt.show()

