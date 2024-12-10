import yfinance as yf
import numpy as np
import pandas as pd

class Equity:
    def __init__(self, ticker, period= "5y"):
        """
        Initialising the attributes by downloading the data from Yahoo 
        to include daily price data, default period set to 5 years
        
        Parameters:
        ticker: str, the ticker for the stock
        period: str, default set to 5y

        Attributes:
        ticker (str): Stock ticker symbol.
        information (object): Stock information based on ticker
        data (pd.DataFrame): Price data for the given period.
        adj_close (pd.Series): Adjusted close price.
        simple_daily_r (pd.Series): Daily simple returns.
        log_daily_r (pd.Series): Daily log returns.
        avg_daily_r (float): Average of daily log returns.
        annualised_return (float): Annualised log return (based on 252 trading days).
        """

        self.ticker = ticker
        self.information = yf.Ticker(ticker)
        self.sector = self.information.info.get("sector")
        self.data = yf.download(ticker, period= period)
        self.data.index = pd.to_datetime(self.data.index)
        self.adj_close = self.data["Adj Close"]
        self.simple_daily_r = ((self.adj_close / self.adj_close.shift()) - 1).dropna()
        self.log_daily_r = np.log(self.adj_close / self.adj_close.shift()).dropna()
        self.avg_daily_r = self.log_daily_r.mean()
        self.annualised_return = self.avg_daily_r * 252

    def sector_benchmark(self):
        """
        Using the sector to decide specific benchmark

        Returns:
        Sector specific benchmark
        """
        sector_benchmark = {
            "Communication Services": "XLC",
            "Consumer Cyclical": "XLY",
            "Consumer Defensive": "XLP",
            "Energy": "XLE",
            "Financial Services": "XLF",
            "Healthcare": "XLV",
            "Industrials": "XLI",
            "Technology": "XLK",
            "Materials": "XLB",
            "Real Estate": "XLRE",
            "Utilities": "XLU",
        }

        benchmark = sector_benchmark[self.sector]
        return benchmark




    def download_data(self, ticker, period= "5y"):
        """
        Download price data for the given ticker
        
        Parameters:
        ticker: str, the ticker for the stock
        period: str, default set to 5y

        Returns: 
        adj_close: pandas DataFrame with daily close
        log_daily_r: pandas DataFrame with log daily return
        """
        price_data = yf.download(ticker, period= period)
        price_data.index = pd.to_datetime(price_data.index)
        adj_close = price_data["Adj Close"]
        log_daily_r = np.log(adj_close / adj_close.shift()).dropna()
        return adj_close, log_daily_r

    def convert_daily(self, return_data, period= "D"):
        """
        Convert daily log returns to weekly, monthly, or annual.
        
        Parameters:
        return_data: pandas DataFrame or Series with daily data.
        period: str, frequency for resampling 
        ('W' for weekly, 'ME' for monthly, 'A' for annual).

        Returns:
        Resampled data with the specified frequency.
        """

        if period.upper() == "D":
            return return_data
        elif period.upper() in ["W", "ME", "A"]:
            return_data = return_data.resample(period).sum()
        else:
            raise ValueError("""Invalid period. Use "W", "ME", "A".""")

        return return_data
    
    def calc_beta(self, benchmark= "^GSPC"):
        """Calculate the beta of a given stock against it's benchmark"""
        _, benchmark_return = self.download_data(benchmark)
        monthly_benchmark = self.convert_daily(benchmark_return, "ME")
        monthly_stock = self.convert_daily(self.log_daily_r, "ME")
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


    def historical_var(self, confidence_level=0.95, period="D"):
        """
        Calculates the historical on the stock using the historical returns at a 
        given level of confidence.

        Parametres:
        confidence_level: int, default set to 0.95
        period: str, default set to daily

        returns:
        Historical Var for a give period
        """
        log_daily_r = self.convert_daily(self.log_daily_r, period)
        h_var = np.percentile(log_daily_r, 100 * (1 - confidence_level))
        print(
        f"At a {confidence_level *100:.0f}% confidence level, "
        f"{self.ticker} has a maximum {period} loss of {h_var * 100:.2f}%"
        )
        return h_var


    def parametric_var(self, confidence_level= 0.95, period= "D"):
        """
        Calculates the VaR using the parametric method for a given stock 
        using the mean and standard deviation at a given level of confidence

        Parametres:
        confidence_level: int, default set to 0.95
        period: str, default set to daily

        returns:
        Parametric Var for a give period
        """
        log_daily_r = self.convert_daily(self.log_daily_r, period)
        mean = np.mean(log_daily_r)
        std = np.mean(log_daily_r)

        if confidence_level == 0.90:
            z_score = 1.645
        elif confidence_level == 0.95:
            z_score = 1.960
        elif confidence_level == 0.99:
            z_score = 2.567

        p_var = mean - (z_score * std)
        print(
            f"At a {confidence_level *100:.0f}% confidence level, "
            f"{self.ticker} has a maximum {period} loss of {p_var * 100:.2f}%"
            )
        return p_var

#Creating the object equity from the Equity class
equity = Equity("AMT")

benchmark = equity.sector_benchmark()

print(equity.calc_beta(benchmark))