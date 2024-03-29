# Sets

## Overview

  A Set is a data structure in Python that looks very similar to a list or array. In contrast to other structures in Python though, the order of items within a set is irrelevant to the functionality. Python lists or stacks can have multiple duplicate values where 
stacks can only have unique values. This makes it easier to identify elements within a set because we can user operations to find and edit elements with a high degree of efficiency. Sets are capable of storing multiple types of data
 including strings, ints, or booleans.

## Key Terms
- Set: A data structure which is defined by characteristics of being unordered and containing no duplicate values.
- Hashing: The process by which items within a set can be access and modified by a defined index location.
- Hashing Function: The function that assigns items to a numerical index within a set.
- Sparse List: A set which is not completely filled.
- Open Addressing/Chaining: Operations to resolve conflicts when managing a set.

## Comparisons

  Sets share components with multiple other data structures in Python. the most obvious comparison is to a list. The structure appears similar but a set cannot have duplicates and the order of items is irrelevant. This is because we don't access items in a set by index 
but by looking for the element itself. Dictionaries are ordered and can be changed unlike sets but also do not allow duplicates just like sets. Dictionaries can also hold multiple types of data. We can also access items in a dictionary by referencing the key value pair we want without having to search each element of the dictionary 
giving it an O(1) efficiency.
```python
# List
my_list = [1, 5, 4, 2, 2, 3]   # Duplicate values are allowed in lists
item = my_list[1]   # Element accessed by index
```
```python
# Dictionary
my_dict = {"first: 1, "second": 2, "third": 3}   # No duplicate keys
item = my_dict["first"}   # Access items by referencing the key:value pair
```

```python
# Set
thisset = {"grape", "banana", "cherry", 4, 2}   # No specific order
if "apple" in thisset:  # Check and access an item without using an index
	print("apple")
else:
	print("no")
```

## Hashing

### Efficiency

  Hashing is important for facilitating the 0(1) efficiency that sets have. Searching through an entire list one item at a time has an efficiency of 0(n). This is because the time it takes to find the item in the list is directly proportional to its position. To have O(1) efficiency, 
we would need to know exactly where the desired item's index is from the beginning. There is a way to know the item's position though. In a set, every item has a defined location sored as what is called a **hash**. Then a program can simply look for the hash and get the item 
immediately. 

### Hash Function
  This is accomplished through hashing. Lets look at a real world example: You have a collection of movies across several shelves. You could search through the entire
collection to try and find the movie you want, but you might have to check the entire collection before you find it! Hashing lets you assign each movie a value based on its location. Each of the values is now a part of a map
of your collection. The next time you look for a movie, you can pull out the map and find the value of the movie you want so you can go directly to the right shelf to find it. 

  For a programming example, lets say we want to make a list of all values from 0 to 9. The function **index(n) = n** could help us achieve this. Each value would determine its position in the list. If we add n = 7, the index in the list would also be 7. This example would require that 
  the list be size 10 exactly. 
  
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
|   | 1 |   |   | 4 |   |   | 7 | 8 |   |

With a few other values added to the list, we can see how the formula works for finding elements. Our formula lets us find values because we've mapped their locations to an index. This in particular is a sparse set because it may not have values in every available space.
This also helps illustrate that there can only be one spot for any value because there would be nowhere for a duplicate to go since the space is already full.

### hash()

In cases where we have to perform operations as a part of creating a set, we can use the built in hash(n) function. Non-integer values will be converted into a value that will vary between individual runs but will always be consistent within a single execution. The only item
that cannot be hashed with this method is a list.


## Conflicts

