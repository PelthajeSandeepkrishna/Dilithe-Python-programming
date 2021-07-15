s1 = input()
s2 = [i for i in input().split(" ") if i != ""]
count = 0
foo = "No"
for i in s2:
    if len(i) >= len(s1):
        for j in range(len(s1)):
            if s1[j] == i[j]:
                # print(s1[j],i[j])
                count += 1
            if count == len(s1):
                # print(count,len(s1))
                foo = "Yes"
        count = 0
print(foo)
