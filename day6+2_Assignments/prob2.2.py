# Read four integers from the keyboard a,b,c,d and those values in the following order.
# max > mid1 > mid2 > min

num = [int(i) for i in input("Enter four numbers : ").split(" ") if i != ""]
print(*num)
foo = []
if len(num) == 4:
    for i in range(4):
        foo.append(max(num))
        num.remove(max(num))
print(*foo,sep=" > ")
