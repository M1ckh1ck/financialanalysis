import math

def future_value():
    """Function to calculate the future value of a single cash flow"""
    present_value = float(input("What is the present value of the single cash flow? "))
    years = float(input("What is the the time period in years? "))
    rate = calculated_rate()
    value = present_value * (rate ** years)
    return print(f"The future value of this investment is {value:,.2f} in {years} years grown at {((rate-1)*100):.4f}% pa.")

def present_value():
    """Function to calculate the present value of a future single cash flow"""
    future_value = float(input("What is the future value of the cash flow? "))
    years = float(input("What is the the time period in years? "))
    rate = calculated_rate()
    value = future_value / (rate**years)
    return print(f"The present value of the cash flow is {value:,.2f} discounted at {((rate-1)*100):.4f}% pa for {years} years.")

def annuity_future_value():
    """Function to calculate the future value of an annuity"""
    present_value = float(input("What is the value of the annual payment? "))
    years = float(input("What is the the time period in years? "))
    rate = calculated_rate()
    value = present_value * ((rate ** years) - 1)/(rate-1)
    return print(f"The future value of the annuity payments is {value:,.2f} in {years} years grown at {((rate-1)*100):.4f}% pa.")

def annuity_present_value():
    """Function to calculate the present value of an annuity payments"""
    annuity_value = float(input("What is the value of the annuity payments? "))
    years = float(input("What is the the time period in years? "))
    rate = calculated_rate()
    value = annuity_value * (1 - (1/(rate ** years)))/(rate-1)
    return print(f"The present value of the annuity payments is {value:,.2f} discounted at {((rate-1)*100):.4f}% pa for {years} years.")

def calculated_rate():
    """Calutate the actual rate of return from the quoted rate and the compounding period"""
    quoted_rate = float(input("What is the quoted interest rate in decimals? "))
    compound_period = input("What is the compund period a/q/m/d/c? ").lower()

    if compound_period == "a":
        compound_period = 1
    elif compound_period == "q":
        compound_period = 4
    elif compound_period == "m":
        compound_period = 12
    elif compound_period == "d":
        compound_period = 365
    elif compound_period == "c":
        return (math.e)**quoted_rate
    actual_rate = (1 + (quoted_rate/compound_period))**compound_period
    return actual_rate

def growth_rate():
    """Calculate the growth rate of the cash investment"""
    future_value = float(input("What is the future value of the cash flow? "))
    present_value = float(input("What is the present value of the cash flow? "))
    years = float(input("What is the the time period in years? "))
    growth_rate = (future_value / present_value)**(1 / years)
    return print(f"The growth on the investment is {(growth_rate-1)*100:.4f}% pa.")

def period_calculation():
    """Calculate the period of time"""
    future_value = float(input("What is the future value of the cash flow? "))
    present_value = float(input("What is the present value of the cash flow? "))
    rate = calculated_rate()
    #Ln(x^N) = N.Ln(x)
    ln = math.log
    years = ln(future_value / present_value) / ln(rate)
    print(f"The period of time equals {years} years.")




