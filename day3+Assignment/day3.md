# Day3 Report

Number

1. Int

2. Float

3. Complex

   ```python
   # a+bj
   a = 10 +5j # a is real, b is imaginary, j**2 = -1 .
   a.real	gives 10 in return.
   a.img gives 5 in return.
   ```

String

+ Collection of sequence of charector
+ It is enclosed with  `""`  or  `''`
+ `\"` and `\'` used with 
+ `'''comment'''`triple quote is used for multiline comments
+ It supports reverse index like -1
+ Index starts with 0.
+ Supports slicing [:]
  + syntax `[<startindex​>:<endindex>:<​stepindex>]`

+ Default step index is 1.
+ Supports repetition `*` like `print("foo"*200)`
+ `+` is used for string concatenation. 

List

+ Its Mutable means we can modify items in list. 
+ Collection of dissimilar data items enclosed with in `[]`
+ It maintains Insertion order.
+ It supports indexing, slicing, repetition, concatenation.
+ performance is slow and bitwise lager than tuple.

Tuple

+ Its Immutable means cannot delete items in tuple.
+ Collection is dissimilar data items enclosed in `()`.
+ performance is higher than list and smaller in bitwise.

Functions

+ input()
  + syntax

+ print()
  + syntax

## Example program

```python
# Program to calculate compound interest

# Getting input from user
principal = int(input("princial amount :"))
rate = float(input("Interest rate :"))
years = float(input("Number of years :"))

# Calculating compund interest
interest = principal*(1+rate/100)**years

# Printing the result 
print("Compound Interest :",round(interest,2)) #gives two digits after decimal
```

```python
# Program to print Simple Interest

# Getting input from user
principal = int(input("princial amount :"))
rate = int(input("Interest rate :"))
years = float(input("Number of years :"))

# Calculating Simple interest
interest = (principal*years*rate)/100

# Printing the result 
print("Compound Interest :",round(interest,2)) #gives two digits after decimal
```

```python
# Used for further code
max() #Gives max value
min() #Gives min values
```

