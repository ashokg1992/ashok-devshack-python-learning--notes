# # Day-5 | 
#  ================================ Functions & Modules  ================================
 
# A function is a block of organized, reusable code that performs a specific task. It takes some input (parameters) and returns an output.

#  ++++++++++++++++++++++++++++++++++++++++++  Creating a Function:  +++++++++++++++++++++ +++++

def greet(name):      # This function prints a greeting message.
    print(f"Hello, {name}!")
    greet ( "ashok")

# +++++++++++++++++++++ Call the function - Example with a return statement:  + +++++++++++++++++  
def add(x, y):
    return x + y

result = add(3, 4)
print(result) 
 # Output: 7
 
#+++++++++++++++++++++++++++++++++++  Modules: ++++++++++++++++++++++++++++++++++++++++++++++++++++
 
# A module is a file containing Python definitions and statements. 
# The file name is the module name with the suffix .py.

# ++++++++++++++++++++++++++++++++++ Creating a Module: ++++++++++++++++++++++++++++++++++

# Let's say we create a file named math_operations.py with the following content:

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"
  
  
# ++++++++++++++++++++++++++++++++++  Using a Module: ++++++++++++++++++++++++++++++++++

# In another Python file, you can import and use the functions from the module:

import  math_operations
result_add =  math_operations.add(3, 4)
result_subtract =  math_operations.subtract(7, 2)

print(result_add)     # Output: 7
print(result_subtract)  # Output: 5

# +++++++++++++++++++++++++ Using Specific Functions: +++++++++++++++++++++++++++

# You can also import specific functions from a module:

from  math_operations import multiply, divide
result_multiply = multiply(5, 6)
result_divide = divide(8, 2)

print(result_multiply)  # Output: 30
print(result_divide)    # Output: 4.0

#++++++++++++++++++++++  Benefits of Functions and Modules: ++++++++++++++++++++++

# Reusability: Functions allow you to write code once and use it multiple times.

# Modularity: Modules help in organizing code into logical units, making it easier to manage.

# Abstraction: Functions allow you to focus on what a piece of code does rather than how it does it.

# Readability: Well-defined functions and modules make code more understandable.

# Testing and Debugging: Functions and modules facilitate easier testing and debugging of code segments.

# Collaboration: Modules enable multiple programmers to work on different parts of a project simultaneously.

# Remember to give your functions and modules descriptive names and include comments or docstrings to explain their purpose and usage. This makes your code more understandable and maintainable.

# Using functions and modules is a best practice in Python programming and contributes to writing clean, efficient, and organized code.