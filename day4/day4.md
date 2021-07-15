# Day3 Report

### Print function

```python
print("%.2f" % a) # for printing two digits after decimal 
```

### Dictionary

​	It stores key, value pair data.

```python
# Create empty dictionary
dict1 = {} # also can be created using dict()
dict1['name'] = "Sample"
dict1['score'] = 9.9
print(dict1)

# Output would be
# {'name':'Sample','score':'9.9'}

```

​	Key should be immutable type and value should be mutable.

```python
# 
tinydict = {'name':'sample','score':9.9}
# To display keys
print(tinydict.keys())
# To display values
print(tinydict.values())
# To delete key and value pair
del tinydict['score']
```

​	Keys are case sensitive.

### Program 4

​	Instructor explained the 4th program from given assignment.

### List and Input funtion

```python
# List unpacking
a,b,c = input().split()
print(a,b,c)

# output would be
```

### Higher Order Function

​	A function can accept function as a argument.

```python
# map(<function>,<sequence>)
list1 = ['1','2','3']
# To convert every items in list to int
list2 = map(int,list1)
list2 = list(list2)
print(list2)
# Output would be [1, 2, 3]

# So we can write
a,b,c = map(int, input().split()) 
# It splits input and assigns to a,b,c variable
```

### To be a good programmer

+ Time efficiency

+ Space

+ Code optimization