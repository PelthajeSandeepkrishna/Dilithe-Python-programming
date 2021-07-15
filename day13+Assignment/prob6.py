foo = [i for i in input().split(" ") if i != ""]
wd = input()
num = int(input())
count = 1
for i in range(len(foo)):
    if foo[i] == wd:
        print(foo[i],wd)
        if num == count:
            foo.pop(i)
            break
        count += 1
print(foo)
