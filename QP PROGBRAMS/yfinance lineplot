import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch historical stock data for Alphabet Inc. (ticker symbol: GOOGL)
ticker = "GOOGL"
start_date = "2023-01-01"
end_date = "2023-12-31"

# Download stock data
stock_data = yf.download(ticker, start=start_date, end=end_date)

# Create a line plot for the 'Close' prices
plt.figure(figsize=(10, 6))
plt.plot(stock_data.index, stock_data["Close"], label="Close Price", color="blue")
plt.title(f"Alphabet Inc. (GOOGL) Stock Prices from {start_date} to {end_date}")
plt.xlabel("Date")
plt.ylabel("Close Price (USD)")
plt.legend()
plt.grid()
plt.show()
 
