import pandas as pd

# Define the sales data as a dictionary (example data based on the screenshot)
data = {
    "OrderDate": ["1-6-18", "1-23-18", "2-9-18", "2-26-18", "3-15-18", "4-1-18", "4-18-18", "5-5-18", "5-22-18", "6-8-18"],
    "Region": ["East", "Central", "Central", "Central", "West", "East", "Central", "Central", "West", "East"],
    "Manager": ["Martha", "Hermann", "Hermann", "Timothy", "Timothy", "Martha", "Hermann", "Hermann", "Douglas", "Martha"],
    "SalesMan": ["Alexander", "Shelli", "Luis", "David", "Stephen", "Alexander", "Steven", "Luis", "Michael", "Alexander"],
    "Item": ["Television", "Home Theater", "Television", "Cell Phone", "Television", "Home Theater", "Television", "Television", "Television", "Home Theater"],
    "Units": [95, 50, 36, 27, 56, 60, 75, 90, 32, 60],
    "Unit_price": [1198.00, 500.00, 1198.00, 225.00, 1198.00, 500.00, 1198.00, 1198.00, 1198.00, 500.00],
    "Sale_amt": [113810.00, 25000.00, 43128.00, 6075.00, 67088.00, 30000.00, 89850.00, 107820.00, 38336.00, 30000.00],
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Create a pivot table
pivot_table = pd.pivot_table(
    df,
    values="Sale_amt",  # Column to aggregate
    index=["Region", "Manager", "SalesMan"],  # Grouping columns
    aggfunc="sum"  # Aggregation function
)

# Display the pivot table
print(pivot_table)
