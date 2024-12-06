import yfinance as yf
import numpy as np
import pandas as pd

class Equity:
    def __init__(self, ticker, period= "5y"):
        """
        Initialising the attributes by downloading the data from Yahoo 
        to include daily price data, default period set to 5 years
        
        ticker (str): Stock ticker symbol.
        data (pd.DataFrame): Price data for the given period.
        adj_close (pd.Series): Adjusted close price.
        simple_daily_r (pd.Series): Daily simple returns.
        log_daily_r (pd.Series): Daily log returns.
        avg_daily_r (float): Average of daily log returns.
        annualised_return (float): Annualised log return (based on 252 trading days).
        """

        self.ticker = ticker
        self.data = yf.download(ticker, period= period)
        self.data.index = pd.to_datetime(self.data.index)
        self.adj_close = self.data["Adj Close"]
        self.simple_daily_r = ((self.adj_close / self.adj_close.shift()) - 1).dropna()
        self.log_daily_r = np.log(self.adj_close / self.adj_close.shift()).dropna()
        self.avg_daily_r = self.log_daily_r.mean()
        self.annualised_return = self.avg_daily_r * 252
        
    def download_data(self, ticker, period= "5y"):
        """Download price data for the given ticker"""
        price_data = yf.download(ticker, period= period)
        price_data.index = pd.to_datetime(price_data.index)
        adj_close = price_data["Adj Close"]
        log_daily_r = np.log(adj_close / adj_close.shift()).dropna()
        return adj_close, log_daily_r

    def convert_daily(self, return_data, period):
        """Convert the daily log returns to weekly, monthly and annual"""
        return_data = return_data.resample(period).sum()
        return return_data
    
    def calc_beta(self, benchmark= "^GSPC"):
        """Calculate the beta of a given stock against it's benchmark"""
        _, benchmark_return = self.download_data(benchmark)
        monthly_benchmark = self.convert_daily(benchmark_return, "M")
        monthly_stock = self.convert_daily(self.log_daily_r, "M")
        return_data = pd.concat([monthly_stock, monthly_benchmark], axis=1)
        return_data.columns = [self.ticker, benchmark]
        
        cov = np.cov(return_data[self.ticker], return_data[benchmark])[0][1]
        market_var = np.var(return_data[benchmark])
        beta = cov / market_var
        return beta

    def calc_capm(self, risk_free= "^TNX", market= "^GSPC"):
        """Calculate the CAPM, using the calculated beta"""
        risk_free_r ,_ = self.download_data(risk_free)
        risk_free_r = (risk_free_r.iloc[-1]) / 100
        _, market_r = self.download_data(market)
        market_r = market_r.mean() * 252

        capm = risk_free_r + self.calc_beta() * (market_r - risk_free_r)

        return capm


    def calc_sharpe_ratio(self, risk_free = "^TNX"):
        """Caculate the stocks Sharp Ratio using ten year treasury as risk free rate"""
        risk_free_r ,_ = self.download_data(risk_free)
        risk_free_r = (risk_free_r.iloc[-1]) / 100
        stdev = self.log_daily_r.std() * (250 ** 0.5)
        capm = self.calc_capm()

        sharpe_ratio = (capm - risk_free_r) / stdev

        return sharpe_ratio 





#Creating the object equity from the Equity class
equity = Equity("ppppp")
print(equity.adj_close)