import yfinance as yf
import numpy as np
import pandas as pd

class Equity:
    def __init__(self, ticker):
        """Initialising the attributes by downloading the data from Yahoo 
        to include price data and calculate both simple log daily returns"""

        self.ticker = ticker
        self.data = yf.download(ticker, period= "5y")
        self.data.index = pd.to_datetime(self.data.index)
        self.adj_close = self.data["Adj Close"]
        self.simple_daily_r = ((self.adj_close / self.adj_close.shift()) - 1).dropna()
        self.log_daily_r = np.log(self.adj_close / self.adj_close.shift()).dropna()
        self.avg_daily_r = self.log_daily_r.mean()
        self.annualised_return = self.avg_daily_r * 250
        
    def download_data(self, ticker, period= "5y"):
        """Download price data for the given ticker"""
        price_data = yf.download(ticker, period= period)
        price_data.index = pd.to_datetime(price_data.index)
        adj_close = price_data["Adj Close"]
        return adj_close
    
    def calc_beta(self, benchmark= "^GSPC"):
        """Calculate the beta of a given stock against it's benchmark"""
        benchmark_data = self.download_data(benchmark)
        benchmark_return = np.log(benchmark_data / benchmark_data.shift()).dropna()
        return_data = pd.concat([self.log_daily_r, benchmark_return], axis=1)
        return_data.columns = [self.ticker, benchmark]
        
        cov = np.cov(return_data[self.ticker], return_data[benchmark])[0][1]
        market_var = np.var(return_data[benchmark])
        beta = cov / market_var
        return beta

#Creating the object equity from the Equity class
equity = Equity("PG")
print(equity.calc_beta("^GSPC"))
