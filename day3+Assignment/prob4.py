# Read three integers from the keyboard a,b,c and those values in the following order.
# max > mid > min

# Get input from user
num = [int(i) for i in input("Input three digits: ").split(" ") if i != ""]

# Print output
if len(num) == 3:
    for i in num:
        if i < max(num) and i > min(num):
            print(str(max(num)) + ' > ' + str(i) + " > " + str(min(num)))
