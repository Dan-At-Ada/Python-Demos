"""
Python Basics: Functions
This demo covers how to create and use functions in Python.
"""

# Basic function
def greet(name):
    """Simple function that returns a greeting."""
    return f"Hello, {name}!"

# Function with default parameters
def calculate_area(length, width=1):
    """Calculate area with optional width parameter."""
    return length * width

# Function with variable number of arguments
def sum_numbers(*args):
    """Sum any number of arguments."""
    return sum(args)

# Function with keyword arguments
def create_person(name, **kwargs):
    """Create a person with optional attributes."""
    person = {"name": name}
    person.update(kwargs)
    return person

# Lambda functions (anonymous functions)
square = lambda x: x ** 2

# Function that returns another function
def create_multiplier(n):
    """Create a function that multiplies by n."""
    def multiplier(x):
        return x * n
    return multiplier

# Testing the functions
print(greet("Python"))
print(f"Area (5x3): {calculate_area(5, 3)}")
print(f"Area (5x1): {calculate_area(5)}")
print(f"Sum of numbers: {sum_numbers(1, 2, 3, 4, 5)}")

person = create_person("Alice", age=25, city="New York")
print(f"Created person: {person}")

print(f"Square of 4: {square(4)}")

double = create_multiplier(2)
print(f"Double of 5: {double(5)}")

# Challenges for students:
# 1. Create a function that takes a list of numbers and returns their average
# 2. Write a function that checks if a string is a palindrome
# 3. Create a function that takes a list of words and returns the longest word
# 4. Write a function that generates Fibonacci numbers up to a given limit
# 5. Create a function that takes a list of numbers and returns a new list with only the even numbers
# 6. Write a function that takes a string and returns the number of vowels in it
# 7. Create a function that takes two lists and returns their intersection (common elements)
# 8. Write a function that takes a number and returns its factorial using recursion 