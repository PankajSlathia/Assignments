"""ASSIGNMENT 2:

Task 1: Check if a Number is Even or Odd"""


number:int = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is Even Number")
else:
    print(f"{number} is Odd Number")


# Task 2: Sum of Integers from 1 to 50 Using a Loop
num_sum = 0
for num in range(1, 51):
    num_sum += num
print('The Sum of number from 1 to 50 is ', num_sum)