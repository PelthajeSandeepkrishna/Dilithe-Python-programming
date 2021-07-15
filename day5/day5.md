# Day5 Report

### Control Structure

There are three types:

+ Sequential

+ Selective

  + if statements

  + syntax:

    + ```python 
      if <condition>:
          <statements>
      elif <conition>:
          <statements>
      else:
          <statements>
      ```

  + Nested if 

    + ```python
      if <condition>:
          <statements>
          if <condition>:
              <statement>
          else:
              <statement>
      elif <conition>:
          <statements>
      else:
          <statements>
      ```

  + condition using logical operator using

    + ```python
      if <condition> and <condition> and <condition3>:
          <statement>
      # if any one condition is false will terminate the statement.
      # if all are true then statement is executed.
      ```

    + ```python
      if <condition> or <condition> or <condition3>:
          <statement>
      # if all condition are false then the statement will be terminated.
      # if any one condition is true statement is executed.
      ```

+ Iterative

### Reference websites

​	[pythontutor.com]() for code visualize code.

### Example Programs

```python
# Program to calculate the bill
product_name = input("Product Name: ")
price = int(input("Price: "))
qty = int(input("Quantity: "))
amount = price * qty
if amount >= 5000:
    discount = amount * 15/100
else:
    discount = 0
net_amount = amount - discount
print("Bill amount: %10.2f"%float(amount))
print("Less (-)   : %10.2f"%discount)
print("            ----------")
print("Net Amount : %10.2f"%net_amount)
print("            ----------")
```



```python
# Program to calculate the interest (Simple and Compound Interest)
principal = int(input("Peinciple : "))
rate = float(input("Rate of Interest : "))
years = float(input("Years : "))

print("1.Simple Interest")
print("2.Compond Interest")
choice = int(input("Enter your choice : "))
if choice == 1:
    interest = (principal * rate * years) / 100
else:
    interest = principal*(1+rate/100)**years
print("Interest : %.2f"%interest)
```



```python
# Check whether the num is divisible ny 2
num = int(input("Enter the Number : "))
if num % 2 == 0:
    if num % 3 == 0:
        print (num + " is divisible by 2 and 3")
    else:
        print (num + " is divisible by 2 and not by 3")
elif num % 3 == 0:
    print (num + " is divisible by 3 not by 2")
else:
    print (num + " is not divisible by 2 and 3")
```



```python
data = 100
if data:
    print("Data exists")
if data != 100:
    print("Data is not 100")
```

