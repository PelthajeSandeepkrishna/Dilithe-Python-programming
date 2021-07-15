# Day10 Report

### Break statement

​	It is used to break the loop.

### Continue

​	It is to continue loop.

### Functions

+ Pre-defined
  + string functions : max(), min(), len().

+ User defined 

### Example Problem

```python
# Program to terminate the itertion
for i in range(10):
    if i % 2:
        break
    print(i)
# Output : 0
```

```python
# Program to terminate the itertion
for i in range(10):
    if i % 2:
        continue
    print(i)
# Output : 0 2 4 6 8
```

```python
# Program to check prime number
n = int(input())
for foo in range(2, n//2+1):
    if n % foo == 0:
        print("Not Prime")
        break
else:
    print("Prime")
```

```python
n = int(input())
if n% 2 == 0:
    pass
else:
    print("This is example for pass statement")
```

```python
# Program to demo the ternary operator
n = int(input())
if n % 2:
    print("odd")
else:
    print("Even")
# In single line 
print("odd") if int(input()) % 2 else print("even")
# Or
print("odd" if int(input()) % 2 else "even")
```

