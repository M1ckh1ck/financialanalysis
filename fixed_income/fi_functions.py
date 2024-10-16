
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