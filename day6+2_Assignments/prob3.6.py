# PRINT THE BELOW MENTIONED PATTERN FOR ANY "N" VALUE. WHERE "N" INDICATES NO.OF ROWS.
#   Input Format: A SINGLE INTEGER DENOTING N VALUE
#   Constraints : 1<=N<=100
#   Output Format : PATTERN AS SHOWN IN SAMPLE TEST CASE

num = int(input())
if num >= 1 and num <= 100: 
    for i in range(num): print(" "*int(i)+str(i+1))
