"""
ASSIGNMENT 3:
Module 4: Functions & Modules in Python




Task 1: Calculate Factorial Using a Function

"""

# using for loop
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

fact_num = int(input("Enter a number: "))

result = factorial(fact_num)
print(f"The factorial of {fact_num} is: {result}")

# using recursive method

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

user_input = int(input("Enter your number: "))
result = factorial(user_input)
print(f"The factorial of {user_input} is: {result}")


"""
Task 2: Using the Math Module for Calculations
"""

import math

my_input = int(input("Enter your number: "))
square_root = math.sqrt(my_input)
print(f"The square root: {square_root}")

natural_logarithm = math.log(my_input)
print(f"Logarithm: {natural_logarithm}")

sin_num = math.sin(my_input)
print(f"Sin: {sin_num}")

