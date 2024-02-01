 
# To take user inputs , you can use the input() function.
# By default, input() returns a string, so you'll need to convert it to the desired data type (int, float, or string) using int(), float(), or leave it as is.

# ========================= User Inputs ================================================================

# user_input_int = int(input("Enter an integer: "))   # Taking an integer input
# user_input_float = float(input("Enter a float: "))  # Taking a floating-point input
# user_input_string = input("Enter a string: ")   # Taking a string input

# # Printing the inputs
# print(f"You entered an integer: {user_input_int}")  # f use is- to print the stirng data inside " "
# print(f"You entered a float: {user_input_float}")
# print(f"You entered a string: {user_input_string}")
 
# #   int(input(...))  - to take an integer input, 
# #   float(input(...))  - for a floating-point input, 
# #   input(...) alone is used for a string input.

# - Keep in mind that if the user provides input that cannot be converted to the specified data type, a ValueError will be raised.
# - You might want to handle this using try-except blocks if necessary.
 
 
 
# //////////////////////  //////////////////////////////////////////////////
 
 
 
# for i in range(10):
#     if i == 18:
#         break
#     print(i)
# else:
#     print("Loop completed with  a break.")