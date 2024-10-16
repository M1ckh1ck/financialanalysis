from ib_insync import *

# Connect to IBKR TWS or IB Gateway
ib = IB()
ib.connect('127.0.0.1', 7496, clientId=1)

# Define the Apple stock contract
contract = Stock('AAPL', 'SMART', 'USD')

# Request historical data for Apple stock (AAPL)
# This example retrieves 1 year of daily data.
bars = ib.reqHistoricalData(
    contract,
    endDateTime='',  # Leave blank for current time
    durationStr='1 d',  # 1 year of data
    barSizeSetting='1 day',  # Daily bars
    whatToShow='TRADES',  # Show trades
    useRTH=True,  # Use Regular Trading Hours only
    formatDate=1
)

# # Print the historical data
for bar in bars:
    print(f'Date: {bar.date}, Open: {bar.open}, High: {bar.high}, Low: {bar.low}, Close: {bar.close}, Volume: {bar.volume}')
