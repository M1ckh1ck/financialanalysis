from fi_functions import *

another_calculation = True

while another_calculation:
    rate = input("Enter s if you want to use spot rate or r for market rate. ")
    if rate == "r":
        bond_pv = bond_pv_market()
    elif rate == "s":
        bond_pv = bond_pv_spot()
    
    print(f"The present value of your bond is {bond_pv:.4f}")

    duration_calc = input("Would you like calculate the Macualay Duration? y/n ")
    if duration_calc == "y":
        calc_mac_duration()

    another = input("Would you like another calculation y/n? ").lower()
    if another == 'n':
        break

