# Write a program to calculate the EB Bill.
# The tariff rate for all division is the same. Karnataka electricity board single slaps for the domestic LT supply such as for 0 to 30 units the per-unit cost will be ? 3.75/-, from 31 to 100 the per-unit cost will be ? 5.20, from 101 to 200, the per-unit cost will be ? 6.75 and above 201 units you have to pay ? 7.8 per unit.
# Additionally, the consumer will pay fixed charges as ? 60/- and electricity tax of 5% extra.

units = int(input("Enter unit : "))
if units in range(0,31):
    bill_amount = units * 3.75
if units in range(31,101):
    bill_amount = units * 5.20
if units in range(101,201):
    bill_amount = units * 6.75
if units >= 201:
    bill_amount = units * 7.8
print("Units        : %10.f"%units)
print("Amount       : %10.2f"%bill_amount)
tax = bill_amount*5/100
print("Tax amount   : %10.2f"%tax)
bill_amount = bill_amount + tax + 60
print("Total amount : %10.2f"%bill_amount)
