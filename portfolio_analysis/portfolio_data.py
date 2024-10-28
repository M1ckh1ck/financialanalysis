import pandas as pd
import numpy as np
import yfinance as yf

#Starting with one holding, will expand analysis    
portfolio = ["MCD"]


# Download historical data for a stock
price_data = yf.download(portfolio, start='2023-10-24', end='2024-10-25')
price_data.to_csv("finance_projects/financialanalysis/portfolio_analysis/mcd_data.csv")

