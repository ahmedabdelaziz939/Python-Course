"""
When to Use Tuples:
Tuples are often used when the order of elements matters, and you want to 
create a collection of values that 
should not be modified during the program's execution.
"""

## Syntax
# my_tuple = (1, 2, 3, 'a', 'b')

## Immutable
# my_tuple[0] = 10  # This will raise an error since tuples are immutable

## Accessing Elements
# print(my_tuple[2])  # Output: 3

## Immutable
## Tuples are immutable, meaning once they are created, their elements cannot be changed or modified.
# my_tuple[0] = 10  # This will raise an error since tuples are immutable

## Accessing Elements:
## Elements in a tuple are accessed using indexing, similar to lists.
# print(my_tuple[2])  # Output: 3

## Slicing
# subset = my_tuple[1:4]  # Output: (2, 3, 'a')

## Length
#print(len(my_tuple))  # Output: 5

## Concatenation
# tuple1 = (1, 2, 3)
# tuple2 = ('a', 'b', 'c')
# concatenated_tuple = tuple1 + tuple2  # Output: (1, 2, 3, 'a', 'b', 'c')

## Repetition
## Tuples can be repeated using the * operator.
# repeated_tuple = my_tuple * 2  # Output: (1, 2, 3, 'a', 'b', 1, 2, 3, 'a', 'b')

## Tuple Methods
# count_a = my_tuple.count('a')  # Count occurrences of 'a'
# index_b = my_tuple.index('b')  # Find the index of 'b'


## Tuple Unpacking
# a, b, c, d, e = my_tuple

## Nested Tuples:
# nested_tuple = ((1, 2), ('a', 'b'))

## Throwaway Variable:
## When you don't need the value of a particular element in a tuple (or any sequence), 
## you can use an underscore as a placeholder.
# my_tuple = (1, 2, 3, 4, 5)
# _, second_element, _, _, fifth_element = my_tuple

## Ignoring Values:
## The underscore can be used to ignore a value when unpacking. 
## For example, if you only care about the first and last elements of a tuple:
# my_tuple = (10, 20, 30, 40, 50)
# first, *_, last = my_tuple



