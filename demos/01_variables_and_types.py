"""
Python Basics: Variables and Data Types
This demo covers the fundamental data types in Python and how to work with them.
"""

# Basic Data Types
# 1. Numbers
integer_number = 42
float_number = 3.14
complex_number = 2 + 3j

# 2. Strings
simple_string = "Hello, Python!"
multiline_string = """This is a
multiline string"""

# 3. Boolean
is_true = True
is_false = False

# 4. None
empty_value = None

# Type checking
print(f"Type of integer_number: {type(integer_number)}")
print(f"Type of float_number: {type(float_number)}")
print(f"Type of simple_string: {type(simple_string)}")
print(f"Type of is_true: {type(is_true)}")
print(f"Type of empty_value: {type(empty_value)}")

# Type conversion
string_to_number = "123"
converted_number = int(string_to_number)
print(f"Converted string to number: {converted_number}")

number_to_string = 456
converted_string = str(number_to_string)
print(f"Converted number to string: {converted_string}")

# Challenges for students:
# 1. Create variables of different types and print their values
# 2. Try converting between different types (e.g., string to float, int to string)
# 3. What happens when you try to convert "hello" to an integer?
# 4. Create a variable that combines a string and a number using string formatting
# 5. Try using the bool() function on different values (0, 1, empty string, None) 