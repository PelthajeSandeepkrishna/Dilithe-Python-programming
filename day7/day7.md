# Day7 Report

Pattern programming

# Example program

```python
# Program to print the following pattern
# Pattern 1:
# Input
#	Sample
# Output
#	S
#	Sa
#	Sam
#	Samp
#	Sampl
#	Sample
string = input()
for index in range(len(string)):
    print(string[:index+1])

# Pattern 2: Reverse of pattern 1
string = input()
for index in range(len(string),0,-1):
    print(string[:index])
```

```python
print(" " * 5 + "Sample")
```

```python
# Pattern 3:
string = input()
size = len(string)
for index in range(size):
	print(" "*(size-index-1),end="")
	print(string[:index+1])
```

```python
# Pattern 4: reverse of pattern 2
string = input()
size = len(string)
for index in range(size,0,-1):
    print(" "*size-index,end="")
    print(String[:index])
```

```python
# Print the following pattern
# Input
# Sam
# outputs
# SamSam
# Sa  Sa
# S    S

string = input()
size =len(string)
for i in range(size,0,-1):
    print(string[:i],end="")
    print(" "*(size-i)*2,end="")
    print(string[:i])
```

