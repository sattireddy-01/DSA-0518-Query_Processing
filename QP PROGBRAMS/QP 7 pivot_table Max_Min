import pandas as pd

# Create sample sales data
data = {
    "Item": ["A", "B", "A", "C", "B", "C", "A"],
    "Sale_Value": [250, 300, 150, 400, 350, 200, 100],
    "Region": ["North", "East", "West", "North", "East", "West", "North"],
}
sales_data = pd.DataFrame(data)

# Create a Pivot table to find maximum and minimum sale value of items
pivot_table = sales_data.pivot_table(
    values="Sale_Value", index="Item", aggfunc=["max", "min"]
)

# Rename columns for clarity
pivot_table.columns = ["Max_Sale_Value", "Min_Sale_Value"]

# Display the Pivot table
print(pivot_table)
