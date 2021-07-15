# Q1:  Some prime numbers can be expressed as a sum of other consecutive prime numbers.
# For example
#   5 = 2 + 3,
#   17 = 2 + 3 + 5 + 7,
#   41 = 2 + 3 + 5 + 7 + 11 + 13.
# Your task is to find out how many prime numbers which satisfy this property are present in the range 3 to N subject to a constraint that summation should always start with number 2.
# Write code to find out the number of prime numbers that satisfy the above-mentioned property in a given range.
#   Input Format: First line contains a number N
#   Output Format: Print the total number of all such prime numbers which are less than or equal to N.
#   Constraints: 2<N<=12,000,000,000

def isPrime(num):
    val = True
    if num > 1:
        for i in range(2, num):
            if (num%i) == 0:
                val = False
                break
        else:
            val = True
    return val

# print(isPrime(int(input())))
while(True):
    zee = int(input())
    if isPrime(zee):
        break
# zee = int(input())
bar = [int(i) for i in range(2, zee) if isPrime(i)]
x = 0
tmp = []
for i in bar:
    x+=i
    if x <= zee:    tmp.append(i)
print(*tmp,sep=' + ')
