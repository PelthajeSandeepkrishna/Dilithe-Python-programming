# Day6 Report

### Iterative control structure

There are two type

- while

  - syntax:

  - ```python
    while <expression>:
        <statements>
    ```

- for

  - ```python
    for <iter_variable> in <iterator/sequence>:
        <statements>
    ```

### Range

range() - used to generate sequenced numbers. 

```python
range(<start>,<end>,<step>)
```

### Example Problems

```python
# Program to print a message for 100 times
count = 1
while count < 100:
    print("Sample")
    count += 1 # count = count + 1
```

```python
# Program to reverse the number
# Method 1
num = int(input("Enter number : "))
reverse = 0
while num:
    remainder = num % 10
    reverse = reverse * 10 + remainder
    num //= 10  # num = num // 10
print(reverse)

# Method 2
print(input("Enter number : ")[::-1]) # Single line

# Method 3
num = int(input("Enter number : "))
print(num.zfill(len(num)))
#print("%*0d"%(len(num),int(num)))
```

```python
# Program to print even numbers
list1 = list(map(int,input().split()))
for elements in list1:
    if not element % 2 :
        print(element)
```

```python
# Program to print consonents
# Method 1
import string

st = input("Enter a string : ")
for char in st:
    if char in string,ascii_letters and char not in "aeiouAEIOU":
		print(char, end='')

# Method 2
st = input("Enter a string : ")
for char in st:
    if char.isalpha() and char not in "aeiouAEIOU":
		print(char, end='')
```

