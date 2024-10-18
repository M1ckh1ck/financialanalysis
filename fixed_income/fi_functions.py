
def bond_pv_market():
    coupon = float(input("How much is the coupon? "))
    face_value = float(input("What is the par value of the bond? "))
    market_rate = float(input("What is the current market rate in decimals? "))
    number_of_periods = int(input("What is the number of periods? "))

    pv_principal = face_value / ((1 + market_rate) ** number_of_periods)

    pv_coupons = 0
    for i in range(1, number_of_periods + 1):
        pv_coupon = coupon / ((1 + market_rate)**i)
        pv_coupons += pv_coupon
    
    total_pv = pv_coupons + pv_principal
    return total_pv

def bond_pv_spot():
    coupon = float(input("How much is the coupon? "))
    face_value = float(input("What is the par value of the bond? "))
    number_of_periods = int(input("What is the number of periods? "))

    spot_rates = []
    pv_coupons = 0

    for i in range(0, number_of_periods):
        spot_rate = float(input(f"What is the spot rate for year {i + 1} in decimals? "))
        spot_rates.append(spot_rate)

    for i in range(1, number_of_periods + 1):
        pv_coupon = coupon / ((1 + spot_rates[i - 1])**i)
        pv_coupons += pv_coupon

    pv_principal = face_value / ((1 + spot_rates[number_of_periods - 1]) ** number_of_periods)

    total_pv = pv_coupons + pv_principal
    return total_pv

def calc_mac_duration():
    """Function to calculate the Macaulay Duration for a bond using user inputs"""
    coupon_rate = float(input("what is the coupon rate per period in decimals? "))
    market_rate = float(input("What is the current market rate in decimals? "))
    number_of_periods = int(input("What is the number of periods? "))
    days_per_coupon = float(input("How many days per coupon period? "))
    days_since_coupon =  float(input("How many days since last coupon? "))

    mac_duration = (
        (((1 + market_rate) / market_rate) - 
                    (1 + market_rate + (number_of_periods * (coupon_rate - market_rate))
                    ) / ((coupon_rate * (((1 + market_rate) ** number_of_periods) - 1)) + market_rate)
                    ) - (days_since_coupon / days_per_coupon)
    )
    print(f"The Macaulay Duration is {mac_duration} years")

    #Macaulay duration uses per period values, this needs to annualised i.e. semi annual coupons would be 2 periods per year 
    mod_duration = mac_duration / (1 + market_rate)
    print(f"The Modified duration is {mod_duration} years.")

    price_change = True
    calc_change = input("Would you like to know the change of price based on change in yield? y/n ")
    if calc_change == "y":
        yield_change = float(input("What is the percentage change in the yield? "))
        #Linear estimation of the price change
        delta_full_price = (-1 * mod_duration) * yield_change
    else:
        price_change = False