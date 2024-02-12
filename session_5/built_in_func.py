##  lambinbda expression
## lambda arguments: expression
# add = lambda x, y: x + y
# result = add(3, 5)
# print(result)  # Output: 8


## all()
"""
The all() function returns True if all elements of
the iterable are true (or if the iterable is empty).
"""
numbers = [1, 4, 5, 7]
result = all(x % 2 == 1 for x in numbers)
print(result)  # Output: True


## any()
"""
The  function returns any()True if any element of 
the iterable is true. If the iterable is empty, it returns False.
"""
# numbers = [0, 2, 4, 6, 8]
# result = any(x % 2 == 1 for x in numbers)
# print(result)  # Output: False

# ## bin()
# """The bin() function converts an integer to a binary string"""
# decimal_number = 10
# binary_string = (decimal_number)
# print(binary_string)  # Output: '0b1010'

## id()
# # """The id() function returns the identity (memory address) of an object."""
# x = 42
# y=43
# identity = id(x)
# print(identity)  # Output: Memory address of x
# print(id(y))
## sum()
"""The sum() function returns the sum of all items in an iterable."""

# numbers = [1, 2, 3, 4, 5]
# total = sum(numbers)
# print(total)  # Output: 15


## round()
"""The round() function rounds a floating-point number to the nearest integer."""
float_number = 3.14159
rounded_number = round(float_number, 3)
print(rounded_number)  # Output: 3.14


## range()
"""The range() function generates a sequence of numbers"""

# numbers = list(range(5))
# print(numbers)  # Output: [0, 1, 2, 3, 4]

## print()
"""The print() function outputs the specified message to the console."""
# print("Hello, Python!")
# # Output: Hello, Python!
# name="ahmed abdelaziz ali"
# a=name.split()
# print(name,sep="_")

## abs()
""" The abs() function returns the absolute value of a number."""
# number = -7
# absolute_value = abs(number)
# print(absolute_value)  # Output: 7

## pow()
"""The pow() function returns the result of raising a number to a specified power."""
# result = pow(2, 3)
# print(result)  # Output: 8

## min()
"""
The min() function returns the smallest item 
in an iterable or the smallest of two or more arguments.
"""
# numbers = [3, 1, 4, 1, 5, 9, 2]
# minimum_value = min(numbers)
# print(minimum_value)  # Output: 1

## max()
"""
The max() function returns the largest item in 
an iterable or the largest of two or more arguments.
"""
# numbers = [3, 1, 4, 1, 5, 9, 2]
# maximum_value = max(numbers)
# print(maximum_value)  # Output: 9


## slice()
"""
The slice() function creates a slice object representing the set 
of indices specified by range(start, stop, step).
"""
# numbers = [56,14,20,30,26,56,70]
# sliced_numbers = numbers[slice(2, 8, 2)]
# print(sliced_numbers)  # Output: [2, 4, 6]

## map(function, iterable)
# Squaring each element in a list
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(lambda x: x**2, numbers)
# result = list(squared_numbers)
# print(result)
# # Output: [1, 4, 9, 16, 25]

# ## filter(function, iterable)
# # Filtering even numbers from a list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# result = list(even_numbers)
# print(result)
# # Output: [2, 4, 6, 8, 10]

"""
from functools import reduce
reduce(function, iterable, initializer=None)
"""
from functools import reduce
# # Calculating the product of all elements in a list
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda y: y**2, numbers)
print(product)
# Output: 120
