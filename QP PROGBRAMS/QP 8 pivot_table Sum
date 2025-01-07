import pandas as pd

# Create sample sales data
data = {
    "Item": ["A", "B", "A", "C", "B", "C", "A"],
    "Units_Sold": [5, 8, 3, 7, 10, 4, 6],
    "Region": ["North", "East", "West", "North", "East", "West", "North"],
}
sales_data = pd.DataFrame(data)

# Create Pivot table to find item-wise units sold
pivot_table = sales_data.pivot_table(
    values="Units_Sold", index="Item", aggfunc="sum"
)

# Rename column for clarity
pivot_table.columns = ["Total_Units_Sold"]

# Display the Pivot table
print(pivot_table)
