"""Sets are particularly useful when you need to 
perform operations on unique elements or need to test membership efficiently"""

## Creating Sets:
# my_set = {1, 2, 4, 5}
## You can also create a set using the set() constructor.
# another_set = set([2, 4, 6, 8, 10])

## Unique Elements
## Sets automatically remove duplicate elements, ensuring that all elements are unique.
# my_set = {1, 2, 2, 3, 3, 4, 5, 5}  # Result: {1, 2, 3, 4, 5}


## Operations on Sets
## Sets support various operations 
## such as union, intersection, difference, and symmetric difference.
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}

# union_set = set1 | set2        # Union: {1, 2, 3, 4, 5}
# intersection_set = set1 & set2  # Intersection: {3}
# difference_set = set1 - set2    # Difference: {1, 2}
# symmetric_difference_set = set1 ^ set2  # Symmetric Difference: {1, 2, 4, 5}

## Adding and Removing Elements
## You can add elements to a set using the add() method and remove 
## elements using the remove() or discard() method.
# my_set.add(6)
# my_set.remove(3)
# print(my_set)


"""The discard() method removes an element 
## if it's present and does nothing if the element is not found.""" 
# my_set.discard(3)  # No error if 3 is not present
# print(my_set) 

## Membership Test:
## You can check if an element is present in a set using the in keyword.
# print(2 in my_set)  # Output: True

## Iterating Over Sets:
## You can use a for loop to iterate over the elements of a set. 
# for element in my_set:
#     print(element)

## Frozensets:
## Python also has a built-in type called frozenset, which is an immutable version of a set.
# immutable_set = frozenset([1, 2, 3])


## Set Methods:

## pop(): Removes and returns an arbitrary element from the set.
## clear(): Removes all elements from the set.
## copy(): Returns a shallow copy of the set.
## issubset(): Returns True if the set is a subset of another set.
## issuperset(): Returns True if the set is a superset of another set.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
# set1.pop()
# print(set1)
set2.clear()
print(set2)
set3 = set1.copy()
set3.add(6)
print(set3)
# is_subset = set1.issubset(set3)
# print(is_subset)
# is_superset = set1.issuperset(set3)
# print(is_superset)


## Updating Sets
## Sets can be updated using methods like update() and intersection_update().

# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# set1.update(set2)  # Adds elements from set2 to set1: {1, 2, 3, 4}
# set1.intersection_update(set2)  # Updates set1 with the intersection: {2, 3}

## Set Operations with Other Data Types
# set1 = {1, 2, 3}
# my_list = [2, 3, 4]
# set_from_list = set(my_list)  # Converts a list to a set


##  Set Comprehension:
##  Similar to list comprehensions, Python supports set comprehensions.
# squared_numbers = {x**2 for x in range(5)}  # Output: {0, 1, 4, 9, 16}


# set1={True,1,55,5555,0,False}
# print(set1)