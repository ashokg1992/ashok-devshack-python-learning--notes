 
# To take user inputs , you can use the input() function.
# By default, input() returns a string, so you'll need to convert it to the desired data type (int, float, or string) using int(), float(), or leave it as is.

# ========================= User Inputs ================================================================

user_input_int = int(input("Enter an integer: "))   # Taking an integer input
user_input_float = float(input("Enter a float: "))  # Taking a floating-point input
user_input_string = input("Enter a string: ")   # Taking a string input

# # Printing the inputs
print(f"You entered an integer: {user_input_int}")  # f use is- to print the stirng data inside " "
print(f"You entered a float: {user_input_float}")
print(f"You entered a string: {user_input_string}")
 
#   int(input(...))  - to take an integer input, 
#   float(input(...))  - for a floating-point input, 
#   input(...) alone is used for a string input.

# - Keep in mind that if the user provides input that cannot be converted to the specified data type, a ValueError will be raised.
# - You might want to handle this using try-except blocks if necessary.
 
 
 
# ============================= Control Statements =============================
 
#   Control Statements:
#     if, else, elif,   nested if statements 

# ++++++++++++++++++++++++ if statement: +++++++++++++++++++++++++
 
    
# Example 1: Checking if a number is positive
num = 10
if num > 0:
    print("The number is positive.")
    
# ++++++++++++++++++++++++ if-else statement: ++++++++++++++++++++++++
 
 # Checking if a number is even or odd
num = 7
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
    
# ++++++++++++++++++++++++ elif statement: ++++++++++++++++++++++++
  
# Example 3: Determining the grade based on a score
score = 75
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")
    
# ++++++++++++++++++++++++ Nested if statements: ++++++++++++++++++++++++
   
# Example 4: Nested if statements to determine eligibility for a loan
income = 50000
credit_score = 700
if income >= 60000:
    if credit_score >= 700:
        print("You are eligible for a loan with a low interest rate.")
    else:
        print("You are eligible for a loan with a higher interest rate.")
else:
    print("You are not eligible for a loan.")
    
# In the last example, we have a nested if statement. This means there is an if statement inside another if statement. The inner if statement is only executed if the condition of the outer if statement is true.


#=================================== Loops  ===========================================

#  +++++++++++++++++++++++++++++++++  1. For Loops: +++++++++++++++++++++++++++++++++ 
 

# Use for loops to iterate over a sequence (e.g., a list, tuple, or string).

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
    
# +++++++++++++++++++++++++++++++++  2. While Loops: +++++++++++++++++++++++++++++++++
 
# Use while loops to repeatedly execute a block of code while a condition is True.

count = 0
while count < 5:
    print(count)
    count += 1
    
# +++++++++++++++++++++++++++++++++ 3. Break and Continue: +++++++++++++++++++++++++++++++++
#   
# Use break to exit a loop prematurely, and continue to skip the current iteration.

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i == 5:
        continue
    print(i)
    
# +++++++++++++++++++++++++++++++++ 4. Looping through Dictionaries: +++++++++++++++++++++++++++++++++
 
# You can loop through the keys, values, or items of a dictionary.

person = {'name': 'John', 'age': 30, 'city': 'New York'}
for key, value in person.items():
    print(f'{key}: {value}')
    
# +++++++++++++++++++++ 5. Loop Control with Else: ++++++++++++++++++

#You can use an else block with a loop, which executes when the loop completes without hitting a break.
for i in range(5):
    print(i)
else:
    print("Loop completed without a break.")

    
# +++++++++++++++++++++++++++++++++ 6. List Comprehensions: +++++++++++++++++++++++++++++++++
 
# A concise way to create lists.

numbers = [i for i in range(10) if i % 2 == 0]
print (numbers)

# These control structures and loops are powerful tools in Python that allow you to build complex programs and automate repetitive tasks. Practice using them in various scenarios to become proficient in controlling the flow of your code. Happy coding! 🚀

#+++++++++++++++++++++++++++   SAMPLE PROGRAM +++++++++++++++++++++++++++++++++++

# Certainly! Below is a sample Python program that demonstrates user inputs, control statements (if-else), and loops (for loop and while loop):

name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:       # Control statement (if-else)
    print(f"Hello {name}! You are eligible to vote.")
else:
    print(f"Hello {name}! You are not yet eligible to vote. You can vote in {18 - age} years.")

print("Printing numbers from 1 to 5 using a for loop:")   # # For loop
for i in range(1, 6):
    print(i)

# While loop
num = int(input("Enter a number: "))
fact = 1
i = 1

while i <= num:
    fact *= i
    i += 1

print(f"The factorial of {num} is: {fact}")


# This program does the following:

# Takes user inputs for name and age.
# Uses an if-else statement to check if the user is eligible to vote based on their age.
# Prints numbers from 1 to 5 using a for loop.
# Calculates the factorial of a number using a while loop.
# Here's an example of how the program would work:

# Enter your name: Alice
# Enter your age: 22
# Hello Alice! You are eligible to vote.
# Printing numbers from 1 to 5 using a for loop:
# 1
# 2
# 3
# 4
# 5
# Enter a number: 5
# The factorial of 5 is: 120
# This program showcases the use of user inputs, control statements (if-else), and loops (for loop and while loop) in Pyth
 
 
 
 
 
 
  
for i in range(10):
    if i == 18:
        break
    print(i)
else:
    print("Loop completed with  a break.")