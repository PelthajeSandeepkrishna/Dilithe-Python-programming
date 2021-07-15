while True:
    foo = input()
    if len(foo) >= 3 and len(foo) <= 10**5:
        break
moo = []
j = ""
for i in foo:
    if i in "aeiou":
        moo.append(j)
        j = ""
        moo.append(i)
    else :
        j += i
if j != "": moo.append(j)
print(*moo[::-1],sep="")
