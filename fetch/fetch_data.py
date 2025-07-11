
import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start="2023-01-01", end="2024-01-01"):
    data = yf.download(ticker, start=start, end=end)
    data.to_csv(f"data/{ticker}.csv")
    return data

