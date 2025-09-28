"""
ASSIGNMENT 5:
Module 6: Data Structures and Strings in Python

"""
# Task 1: Create a Dictionary of Student Marks

student_names = ["Ram", "Sham", "Sohan"]
student_marks = [30, 40, 60]
student_dict = {}
for name in student_names:
    for marks in student_marks:
        student_dict[name] = marks

name = input("Enter the Student's name: ")
if name in student_dict:
    print(f"{name}'s marks: {student_dict[name]}")
else:
    print("Student not found")



# Task 2: Demonstrate List Slicing

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
extracted_list = my_list[:5]
print(f"Extracted first five elements: {extracted_list}")

# method 1
print(f"Reversed extracted elements: {list(reversed(extracted_list))}")

# method 2
print(f"Reversed extracted elements: {extracted_list[::-1]}")
