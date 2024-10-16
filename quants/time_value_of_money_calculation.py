from time_value_of_money_functions import *

another_calculation = True
annuity = ""
what_calculation = ""

while another_calculation:
    what_calculation = input("What would you like calculate the value, period or growth of cash flow? ")
    if what_calculation == "growth":
        growth_rate()
    elif what_calculation == "period":
        period_calculation()
    elif what_calculation == "value":
        future_or_present = input("Would you like to calculate the present or future value? ").lower()
        if future_or_present == "present":
            annuity = input("Is it a single cash flow or an annuity? ")
            if annuity == "annuity":
                annuity_present_value()
            else:
                present_value()
        elif future_or_present == "future":
            annuity = input("Is it a single cash flow or an annuity? ")
            if annuity == "annuity":
                annuity_future_value()
            else:
                future_value()
        else:
            print("Invalid option. Please enter either 'present' or 'future'")
            continue
    else:
        print("Invalid option. Please enter either 'growth', 'period' or 'value'")
        continue
    another = input("Would you like another calculation y/n? ").lower()
    if another == 'n':
        break