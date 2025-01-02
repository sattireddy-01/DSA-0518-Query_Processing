import pandas as pd
import matplotlib.pyplot as plt

# Sample financial data as a dictionary
data = {
    'Date': ['10-03-16', '10-04-16', '10-05-16', '10-06-16', '10-07-16'],
    'Open': [774.25, 776.030029, 779.309998, 779.0, 779.659973],
    'High': [776.065002, 778.710022, 782.070007, 780.47998, 779.659973],
    'Low': [769.5, 772.890015, 775.650024, 775.539978, 770.75],
    'Close': [772.559998, 776.429993, 776.469971, 776.859985, 775.080017]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert the Date column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%m-%d-%y')

# Plotting the Close prices
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Close'], marker='o', label='Close Price', color='blue')

# Adding labels, title, and legend
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price', fontsize=12)
plt.title('Alphabet Inc. Financial Data (October 3, 2016 - October 7, 2016)', fontsize=14)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Display the plot
plt.show()
