import yfinance as yf
import numpy as np

class Equity:
    def __init__(self, ticker):
        self.ticker = ticker
        self.company_name = None
        self.price_per_share = None
        self.historical_data = None

    def download_information(self):
        """Download information about the company from Yahoo Finance"""
        info = yf.Ticker(self.ticker).info

        self.company_name = info.get('longName', 'N/A')
        self.price_per_share = info.get('currentPrice', 0)
        print(f"{self.company_name} has a most recent price of {self.price_per_share}")

    def download_historical_data(self, period= None, start= None, end= None, interval="1d"):
        """Download historical entering start and end date, interval set to 1 d as default"""

        self.data = yf.download(self.ticker)
        self.daily_return = (self.data("Adj Close") / self.data("Adj Close").shift()) - 1
        


equity = Equity("PG")
equity.download_information()
equity.download_historical_data(period= "1y")