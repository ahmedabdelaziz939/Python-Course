# ------------------------
# -- Built In Functions --
# ------------------------
# enumerate()
# help()
# reversed()
# ------------------------

# # enumerate(iterable, start=0)

mySkills = ["Html", "Css", "Js", "PHP"]
# print(type(mySkills))

mySkillsWithCounter = enumerate(mySkills, 0)

# print(dict(mySkillsWithCounter))

for  skill in mySkillsWithCounter:

  print(f" {skill}")


##### help()

# print(help(sum))


##### reversed()
"""The reversed() function in Python is used to reverse the elements of an iterable 
and returns a reversed iterator. It does not modify the original iterable but provides a 
reversed view of it. Here's how you can use reversed():"""

# # Example with a list
original_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(original_list))
print(reversed_list)
# Output: [5, 4, 3, 2, 1]

# Example with a string
original_string = "Python"
reversed_string = ''.join(reversed(original_string))
print(reversed_string)
# Output: 'nohtyP'

# # Example with a tuple
original_tuple = (10, 20, 30, 40)
reversed_tuple = tuple(reversed(original_tuple))
print(reversed_tuple)
# Output: (40, 30, 20, 10)

"""
-reversed() is applied to a list, string, and tuple.
-For a list and tuple, reversed() returns an iterator, so we convert it to a list or tuple using 
  list() or tuple() to display the reversed result.
-For a string, we use ''.join() to concatenate the reversed characters back into a string.
"""