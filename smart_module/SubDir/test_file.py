# Example of a simple variable
greeting = "Hello, World!"

# Example of a variable using input
username = input("Enter your username:")

# Example of nested variables
first_name = "John"
last_name = "Doe"
middle_name = "Edward"
full_name = first_name + " " + middle_name + " " + last_name

# Example of deeply nested variables
address_line1 = "221B Baker Street"
address_line2 = "Apt 42"
city = "London"
full_address = address_line1 + ", " + address_line2 + ", " + city

# Example of a nested variable with input
age = input("Enter your age:")
user_info = f"{username}, {age} years old"
user_bio = f"Name: {full_name}, Address: {full_address}, Info: {user_info}"

# Example of safe variables with calculations
constant_value = 42
calculated_value = constant_value * 2
nested_calculation = calculated_value + 10
final_result = f"Final value: {nested_calculation}"