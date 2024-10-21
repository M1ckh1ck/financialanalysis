def pv_bond(coupon, number_of_periods, market_rate, face_value, days_since_last_coupon, days_in_the_period):
    """Calculate the present value of the bond including days since last coupon payment"""
    pv_principal = face_value / ((1 + market_rate) ** number_of_periods)

    #This loop can be cleaned up to one line
    pv_coupons = 0
    for i in range(1, number_of_periods + 1):
        pv_coupon = coupon / ((1 + market_rate)**i)
        pv_coupons += pv_coupon

    total_pv = (pv_coupons + pv_principal) * ((1 + market_rate) ** (days_since_last_coupon / days_in_the_period))
    return(total_pv)

def pv_bond_plus_rate_change(coupon, number_of_periods, market_rate_up, face_value, days_since_last_coupon, days_in_the_period):
    """Calculate the present value of the bond including days since last coupon payment"""
    #Can use the PV-Bond function in here to clean up 
    pv_principal = face_value / ((1 + market_rate_up) ** number_of_periods)

    pv_coupons = 0
    for i in range(1, number_of_periods + 1):
        pv_coupon = coupon / ((1 + market_rate_up)**i)
        pv_coupons += pv_coupon

    total_pv = (pv_coupons + pv_principal) * ((1 + market_rate_up) ** (days_since_last_coupon / days_in_the_period))
    return(total_pv)

def pv_bond_minus_rate_change(coupon, number_of_periods, market_rate_down, face_value, days_since_last_coupon, days_in_the_period):
    """Calculate the present value of the bond including days since last coupon payment"""
    pv_principal = face_value / ((1 + market_rate_down) ** number_of_periods)

    pv_coupons = 0
    for i in range(1, number_of_periods + 1):
        pv_coupon = coupon / ((1 + market_rate_down)**i)
        pv_coupons += pv_coupon

    total_pv = (pv_coupons + pv_principal) * ((1 + market_rate_down) ** (days_since_last_coupon / days_in_the_period))
    return(total_pv)

#Inputs for the present value calculation
face_value = float(input("What is the par value of the bond? "))

#Calculate the coupon per period
coupon_rate = float(input("How much is the coupon in bps? "))

#This can be cleaned up 
period = input("Is the coupon paid quarterly, semi-annually or annually? q/s/a ")
if period == "q":
    period = 4
if period == "s":
    period = 2
if period == "a":
    period = 1 

coupon = ((coupon_rate / 10000) * face_value) / period

#calculate the market rate (YTM) period
# This can be cleaned up 
market_rate = float(input("What is the current market in bps? "))
rate_change = float(input("What is the change market rate in bps? "))
current_market_rate = (market_rate / 10000) / period
market_rate_plus = ((market_rate + rate_change)/ 10000) / period
market_rate_minus = ((market_rate - rate_change)/ 10000) / period

#Calculate number of periods
number_of_years = int(input("What is the number of years? "))
number_of_periods = number_of_years * period

days_since_last_coupon = int(input("How many days since last coupon payment? "))
days_in_the_period = int(input("How many days in the period? "))

current_pv_dond = pv_bond(coupon= coupon, 
        number_of_periods= number_of_periods, 
        market_rate= current_market_rate, 
        face_value= face_value, 
        days_in_the_period= days_in_the_period, 
        days_since_last_coupon= days_since_last_coupon
        )

up_pv_dond = pv_bond_plus_rate_change(coupon= coupon, 
        number_of_periods= number_of_periods, 
        market_rate_up= market_rate_plus, 
        face_value= face_value, 
        days_in_the_period= days_in_the_period, 
        days_since_last_coupon= days_since_last_coupon
        )

down_pv_dond = pv_bond_minus_rate_change(coupon= coupon, 
        number_of_periods= number_of_periods, 
        market_rate_down= market_rate_minus, 
        face_value= face_value, 
        days_in_the_period= days_in_the_period, 
        days_since_last_coupon= days_since_last_coupon
        )

approx_mod_duration = (down_pv_dond - up_pv_dond) / (2 * (rate_change / 10000)* current_pv_dond)
approx_convexity = ((down_pv_dond - up_pv_dond - (2 * current_pv_dond)) / (((rate_change / 10000)**2) * current_pv_dond))
print(f"The current PV of the bond is {current_pv_dond} with approximate modified duration of {approx_mod_duration} years and convexity of {approx_convexity}.")