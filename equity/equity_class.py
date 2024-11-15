import yfinance as yf
from datetime import datetime

class Equity:
    def __init__(self, ticker):
        self.ticker = yf.Ticker(ticker)
        self.company_name = None
        self.price_per_share = None
        self.historical_data = None

    def download_information(self):
        """Download information about the company from Yahoo Finance"""
        info = self.ticker.info

        self.company_name = info.get('longName', 'N/A')
        self.price_per_share = info.get('currentPrice', 0)
        print(f"{self.company_name} has a most recent price of {self.price_per_share}")

    def download_historical_data(self, period= None, start= None, end= None, interval="1d"):
        """Download historical entering start and end date, interval set to 1 d as default"""

        date_range = input("Enter d for date range or p for period: ")

        if date_range.lower() == "p":
            period = input("Enter the period 1mo, 3mo, 1y, 5y, max: ")
            self.historical_data = self.ticker.history(period= period)
            return self.historical_data
        
        else:
            start = input("What is the start date? YYYY/MM/DD: ")
            start_date = datetime.strptime(start, "%Y/%m/%d").strftime("%Y-%m-%d")
            end = input("What is the end date? YYYY/MM/DD: ")
            end_date = datetime.strptime(end, "%Y/%m/%d").strftime("%Y-%m-%d")
            self.historical_data = self.ticker.history(start= start, end= end)
            return self.historical_data