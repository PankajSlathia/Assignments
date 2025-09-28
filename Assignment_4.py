"""
ASSIGNMENT 4:

Module 5: Files, Exceptions, and Errors in Python

"""
# Task 1: Read a File and Handle Errors

try:
    with open("sample.txt", 'r') as my_file:
        data=my_file.readlines()
        print("Reading File Contents:")
        for num, line in enumerate(data):
            line = line.rstrip('\n')
            print(f"Line {num}: {line}")

except FileNotFoundError:
    print("Error: The File %s not found", my_file)


# Task 2: Write and Append Data to a File

with open("output.txt", 'w+') as output_file:
    user_input = input("Enter Text to write to the file: ")
    output_file.write(user_input)
    print(f"Data successfully written to {output_file.name}")
    additional_lines = input("Enter Additional text to append: ")
    output_file.write( '\n' + additional_lines)
    print("Data successfully appended")
    output_file.seek(0)
    final_content = output_file.readlines()
    print(f"\nFinal content of {output_file.name}:")
    for line in final_content:
        print(line.strip())
