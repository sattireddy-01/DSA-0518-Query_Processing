import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock ticker symbol, start date, and end date
ticker = "GOOGL"  # Alphabet Inc.
start_date = "2023-01-01"
end_date = "2023-12-31"

# Download stock data
stock_data = yf.download(ticker, start=start_date, end=end_date)

# Reset index to make the date a column
stock_data.reset_index(inplace=True)

# Scatter plot of Trading Volume vs Closing Price
plt.figure(figsize=(10, 6))
plt.scatter(stock_data["Volume"], stock_data["Close"], color="blue", alpha=0.6)

# Add titles and labels
plt.title(f"Trading Volume vs Stock Prices of Alphabet Inc. (GOOGL) from {start_date} to {end_date}", fontsize=14)
plt.xlabel("Trading Volume", fontsize=12)
plt.ylabel("Stock Price (Closing)", fontsize=12)
plt.grid(alpha=0.5)

# Show the plot
plt.tight_layout()
plt.show()
