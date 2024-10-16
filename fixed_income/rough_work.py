#Calculate Macaulay duration 

coupon_rate = float(input("what is the coupon rate per period in decimals? "))
market_rate = float(input("What is the current market rate in decimals? "))
number_of_periods = int(input("What is the number of periods? "))
days_per_coupon = float(input("How many days per coupon period? "))
days_since_coupon =  float(input("How many days since last coupon? "))

mac_duration = (
    (((1 + market_rate) / market_rate) - 
                (1 + market_rate + (number_of_periods * (coupon_rate - market_rate))
                 ) / ((coupon_rate * (((1 + market_rate) ** number_of_periods) - 1)) + market_rate)
                ) / (days_since_coupon / days_per_coupon)
)
print(mac_duration)

mod_duration = mac_duration / (1 + market_rate)
print(mod_duration)