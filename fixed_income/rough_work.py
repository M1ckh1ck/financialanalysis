#Calculate the full price of the bond including days since coupon payment

face_value = float(input("What is the par value of the bond? "))

coupon_rate = float(input("How much is the coupon in bps? "))

period = input("Is the coupon paid quarterly, semi-annually or annually? q/s/a ")
if period == "q":
    period = 4
if period == "s":
    period = 2
if period == "a":
    period = 1 

coupon = ((coupon_rate / 10000) * face_value) / period

market_rate = float(input("What is the current market rate in bps? "))
market_rate = (market_rate / 10000) / period

number_of_years = int(input("What is the number of years? "))
number_of_periods = number_of_years * period

days_since_last_coupon = int(input("How many days since last coupon payment? "))
days_in_the_period = int(input("How many days in the period? ")) 

pv_principal = face_value / ((1 + market_rate) ** number_of_periods)

pv_coupons = 0
for i in range(1, number_of_periods + 1):
    pv_coupon = coupon / ((1 + market_rate)**i)
    pv_coupons += pv_coupon

total_pv = (pv_coupons + pv_principal) * ((1 + market_rate) ** (days_since_last_coupon / days_in_the_period))
print(total_pv)