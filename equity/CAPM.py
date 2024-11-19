import numpy as np 
import pandas as pd
import yfinance as yf

#Create portfolio
portfolio = ["PG", "^GSPC"]

#Download required data for analysis, and create a DataFrame for Adjust Close
pfolio_data = yf.download(portfolio, start= "2012-1-1", end= "2016-12-31")
pfolio_adj_close = pfolio_data["Adj Close"]

#Calculate daily returns and annualised Covariance
pfolio_returns = np.log( pfolio_adj_close / pfolio_adj_close.shift())
pfolio_cov = pfolio_returns.cov() * 250
cov_market = pfolio_cov.iloc[0, 1]

market_var = pfolio_returns["^GSPC"].var() * 250

pg_beta = cov_market / market_var

#Downloading 10 year yield to be used as the risk free rate
ten_year_info = yf.Ticker("^TNX").info
ten_year_yield = ten_year_info.get("previousClose", "N/A") /100

market_return = pfolio_returns["^GSPC"].mean() * 250

pg_capm = ten_year_yield + pg_beta * (market_return - ten_year_yield)


#Sharp Ratio
pg_std = pfolio_returns["PG"].std() * (250 ** 0.5)

sharp_ratio = (pg_capm - ten_year_yield) / pg_std


print(sharp_ratio)