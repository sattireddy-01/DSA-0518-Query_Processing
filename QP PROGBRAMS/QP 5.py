import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame to simulate stock data
data = {
    "Date": pd.date_range(start="2023-01-01", periods=12, freq="M"),
    "Volume": [1200000, 1500000, 1300000, 1400000, 1600000, 1550000, 1450000, 1480000, 1620000, 1700000, 1800000, 1900000]
}

df = pd.DataFrame(data)

# Define the start and end dates
start_date = "2023-03-01"
end_date = "2023-09-30"

# Filter the DataFrame for rows between the specified dates
filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

# Create a bar plot for the trading volume
plt.figure(figsize=(10, 6))
plt.bar(filtered_df["Date"], filtered_df["Volume"], color="blue", edgecolor="black")
plt.title("Trading Volume of Alphabet Inc. Stock", fontsize=16)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Trading Volume", fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
