"""
Explain that errors in Python are categorized into three main types:
     - **Syntax Errors:** Errors in the code structure.
     - **Runtime Errors (Exceptions):** Errors that occur during the 
         execution of the program.
     - **Logical Errors:** Errors in the program's logic that do not 
         result in immediate errors but lead to incorrect results.
"""

##  **Syntax Errors:**
# print("Hello, World"  # Missing closing parenthesis

## **Runtime Errors (Exceptions):**
"""   
   - Introduce the concept of exceptions and how they are 
       raised during the execution of a program.
   - Common exceptions include: 
         `ZeroDivisionError`,
         `TypeError`, 
         `ValueError`, etc.
"""


## **Handling Exceptions with `try`, `except`, `else`, and `finally`:**
"""- Explain the `try` block for wrapping code that might raise an exception.
   - Use `except` to catch specific exceptions or a generic `except` for catching any exception.
   - Introduce the `else` block for code that should run if no exception occurs.
#    - The `finally` block is executed whether an exception occurs or not.
# """
# # print(10/0)
# try:
#     # Code that might raise an exception
#     result = 10 / 0
# except ZeroDivisionError as e:
#     # Code to handle the specific exception
#     print(f"Error: ")
# else:
#     # Code to run if no exception occurred
#     print("No exception occurred.")
# finally:
#     # Code that always runs, regardless of an exception
#     print("Finally block executed.")


## **Raising Exceptions (`raise`):**
""" 
- Teach how to intentionally raise exceptions using the `raise` statement.
- This can be used to indicate errors or exceptional conditions in your code.
# """
# try:
#        divide =lambda f,g:f/g
#        x=10
#        y=0
#        if y==0:
#           raise ValueError("Cannot divide by zero.")
#        result=divide(x,y)
       
# except Exception as e:
#        print(f"Error: {e}")

#################################################################################
# ## Raising Custom Exceptions:
class CustomError(Exception):
    pass

class ValueTooSmallError(CustomError):
    pass

class ValueTooLargeError(CustomError):
    pass

def check_value(x):
    if x < 0:
        raise ValueTooSmallError("Value is too small!")
    elif x > 100:
        raise ValueTooLargeError("Value is too large!")
    else:
        print("Value is within the acceptable range.")
try:
    check_value(-1)
except ValueTooSmallError :
    print(f"Caught an error: {str(ValueTooSmallError)}")
except ValueTooLargeError as e:
    print(f"Caught an error: {e}")

