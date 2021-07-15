# Day13 Report

## set() datatype:

### syntax:

ste1 = {1, 2, 3, "a", "bc"}

- It does not maintain the index order.
- It does not support indexing.(Not subscriptable)
- It allows only unique elements. (No duplicate elements.) If a duplicate element is added to set, it just rejects it. But doesn't give an error.
- It doesn't support repetition operator. i.e., set1 * 2
- Set concatenation is not possible.

### Creating empty set:

set1 = set() -Will create a set.

But, set1 = {} -wont create a set. It will create a dictionary.

### Adding data to set:

- Append is not supported by set.

Syntax to add data to set:

set1.add() #Only one element can be added to a set by using add.

To add multiple elements:

set1.update([1,2,3,4])

### Removing elements from a set:

set1.remove() #Giving elements not in the set will give a key error

set1.discard() #Wont give an error if the element isn't present in the set.

set1.pop() #can also be used if element is to be returned.

### Finding difference between sets:

```
set1 = {"Apple", "Orange", "Mango"}
set2 = {"Grapes", "Mango", "Apple", "Banana"}
set3 = set1 - set2
set4 = set2 - set1
print(set3)
print(set4)

#Output will be:
{'Orange'}
{'Banana', 'Grapes'}
```

set3 = set1.difference(set2) #can also be used

set4 = set.difference(set1,set2,set3) #can be used to compare multiple sets.

### Set operations:

```
set1.issubset(set2)
set1.union(set2)
set1.issuperset(set2)
set1.isdisjoint(set2)
```

