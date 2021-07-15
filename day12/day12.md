# Day12 Report



### Example Problems

```python
string = "sample"
print("{} is an example".format(string))
print(f"{} is an example")
```

```python
# List function
lst = [1,2,3,4,5,6]
max(lst)	# 6
min(lst)	# 1
len(lst)	# 6
sum(lst)	# 21
all(lst)	# True if non-zero
any(lst)	# If all zero return False
```

```python
# List method
lst = [1,2,3,4,5]
lst.append(6)	# [1,2,3,4,5,6]
lst2 = [7,8,9]
lst.append(lst2)	# [1,2,3,4,5,[7,8,9]]
lst.extend(lst2)	# [1,2,3,4,5,7,8,9]
lst.insert(0,"txt")		# ['txt',1,2,3,4,5]
lst.pop(1)	# 1
lst.remove("txt")	# no return 
print(lst)	# [2,3,4,5]
lst.count(4) 	#	1
lst.reverse()
print(lst)	# [5,4,3,2]
lst.sort()	# [2,3,4,5] all items should be str or int
lst.sort(reverse=True)	#  [5,4,3,2]
lst2.clear() 	# []
lst3 = lst.copy()	# [5,4,3,2]
```

```python
# List comprehension
# program to find a square of list of elements
print(*[int(i)**2 for i in input().split(" ") if i != "" and int(i)%2 == 0])
# some random if statements in one line
print(*[int(i)**2 if int(i)%2 == 0 else int(i) for i in input().split(" ") if i != "" and int(i) >= 1 and int(i) <= 100])
```

