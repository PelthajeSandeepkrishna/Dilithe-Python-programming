# Day8 Report

### Pattern

​	Explained some pattern program.

### Nested loop

```python
for <iter_var> in <iterator>:
    for <iter_var> in <iterator>:
        <statements>
```

### Example Program

```python
# Pattern 1+3:
# Program to print the following pattern
# Input : Sam
# Output :
# S    S
# Sa  Sa
# SamSam

string = input()
size = len(string)
for index in range(1,size+1):
    # print(string[:index], end="")
    # print(" " * ((size-index)*2), end="")
    # print(string[:index])
    # print(string[:index] + " " * ((size-index)*2) + string[:index])
    print(string[:index] + " " * ((size-index)*2) + string[:index][::-1])
```

```python
# Diamond pattern1:
# Program to print the following pattern
# Input : Sam
# Output :
# SamSam
# Sa  aS
# S    S
# Sa  Sa
# SamSam

string = input()
size = len(string)
for index in range(size,0,-1):
    print(string[:index] + " " * ((size-index)*2) + string[:index][::-1])
for index in range(2,size+1):
    print(string[:index] + " " * ((size-index)*2) + string[:index][::-1])
```

```python
# Diamond pattern1:
# Program to print the following pattern
# Input : Sam
# Output :
# S    S
# Sa  Sa
# SamSam
# Sa  aS
# S    S

string = input()
size = len(string)
for index in range(1, size):
    print(string[:index] + " " * ((size-index)*2) + string[:index][::-1])
for index in range(size,0,-1):
    print(string[:index] + " " * ((size-index)*2) + string[:index][::-1])
```

```python
# Program to demonstrate nested for

n =int(input())
for i in range(n):
    for j in range(n):
        print("Sample ",end="")
    print()
```



```python
# program to print the following
# input
# 5
# output
# 1
# 12
# 123
# 1234
# 12345

n = int(input())
for i in range(1, n+1):
    for j in range(1,i+1):
        print(j,end="")
	print()