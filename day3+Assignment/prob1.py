# Write a prorgram to calculate simple interest.
#   formula to calculate simple interest : PNR/100

# Getting input from user
principal = int(input("princial amount :"))
rate = int(input("Interest rate :"))
years = float(input("Number of years :"))

# Calculating Simple interest
interest = (principal*years*rate)/100

# Printing the result 
print("Compound Interest :",round(interest,2)) #gives two digits after decimal
