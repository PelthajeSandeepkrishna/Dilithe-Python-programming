num = int(input())
foo = [int(i) for i in input().split(" ") if i != ""]
foo2 = []
[foo2.append(x) for x in foo if x not in foo2]
if num == len(foo): foo2.remove(max(foo2))
print(max(foo2))
