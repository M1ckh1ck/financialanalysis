from equity_class import Equity

ticker = input("What is the ticker you would like to look up?")
equity = Equity(ticker)

equity.download_data()
equity.print_data()