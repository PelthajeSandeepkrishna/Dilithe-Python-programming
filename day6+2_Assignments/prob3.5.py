# PRINT THE BELOW MENTIONED PATTERN FOR ANY "N" VALUE. WHERE "N" INDICATES NO.OF ROWS.
#   Input Format : A SINGLE INTEGER DENOTING N VALUE
#   Constraints : 1<=N<=100 ; N is only odd
#   Output Format : PATTERN AS SHOWN IN SAMPLE TEST CASE

num = int(input())
if num % 2 != 0 and num >= 1 and num <= 100:
    foo = (num / 2)+1
    count = [int(i) for i in range(num) if i % 2 != 0][::-1]
    rnum = num
    #print(count)
    for i in range(num):
        print(" "*int(i),end='')
        print(i+1,end="")
        if int(foo) == i+1: 
            print("")
            break
        else:
            print(" "*int(count[i]),end="")
            print(int(rnum))
        rnum -= 1
