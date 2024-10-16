from ib_insync import *

# Connect to IBKR TWS or IB Gateway
ib = IB()
ib.connect('127.0.0.1', 7496, clientId=1)

#Creating a portfolio with the tickers
portfolio = ["AAPL", "NVDA", "PFE", "UNH", "JPM", 
             "BAC", "AMZN", "HD", "PG", "KO", 
             "XOM", "CVX", "NEE", "DUK", "NEM", 
             "DOW", "HON", "MMM", "AMT", "PLD"]

#Creating an empty list for the contracts and a dictionary for the historical data
contracts = []
historical_data = {}

#Create a loop through each stock symbol and request historical data 
for holding in portfolio:
    #Define a contract for each holding and store contract for reference
    contract = Stock(holding, "SMART", "USD")
    contracts.append(contract)

    #Request data from IB for each holding
    bars = ib.reqHistoricalData(
        contract,
        endDateTime='',  # Leave blank for current time
        durationStr='2 D',  # 1 day of data
        barSizeSetting='1 day',  # Daily bars
        whatToShow='TRADES',  # Show trades
        useRTH=True,  # Use Regular Trading Hours only
        formatDate=1
    )
    # Store the historical data for each symbol in a dictionary
    historical_data[holding] = bars

# Disconnect from IBKR after all requests are completed
ib.disconnect()

# Print the historical data for each stock
for symbol, data in historical_data.items():
    print(f"\nHistorical data for {symbol}:")
    for bar in data:
        print(bar)