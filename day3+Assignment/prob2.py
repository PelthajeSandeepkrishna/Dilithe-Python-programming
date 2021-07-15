# Program to find sum and average of 3 values

# Get input from user
num = [float(i) for i in input('Input there digits with space : ').split(' ') if i != '']
# Calculate
foo = sum(num)
avg = foo/2
# Print output
print("Sum of digits: "+ str(foo) +" and average of digits: "+ str(avg))
