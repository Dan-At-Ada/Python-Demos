"""
Python Basics: Lists and Tuples
This demo covers the fundamental data structures for storing collections of items.
"""

# Lists (mutable)
my_list = [1, 2, 3, 4, 5]
print(f"Original list: {my_list}")

# List operations
my_list.append(6)  # Add to end
print(f"After append: {my_list}")

my_list.insert(0, 0)  # Insert at index
print(f"After insert: {my_list}")

my_list.remove(3)  # Remove value
print(f"After remove: {my_list}")

popped_value = my_list.pop()  # Remove and return last item
print(f"Popped value: {popped_value}")
print(f"After pop: {my_list}")

# List slicing
print(f"First three items: {my_list[:3]}")
print(f"Last two items: {my_list[-2:]}")
print(f"Every other item: {my_list[::2]}")

# List comprehension (important for data processing)
squares = [x**2 for x in range(5)]
print(f"Squares using list comprehension: {squares}")

# Tuples (immutable)
my_tuple = (1, 2, 3, 4, 5)
print(f"\nOriginal tuple: {my_tuple}")

# Tuple unpacking
a, b, c, d, e = my_tuple
print(f"Unpacked values: a={a}, b={b}, c={c}, d={d}, e={e}")

# Tuple operations
print(f"Length of tuple: {len(my_tuple)}")
print(f"Index of 3: {my_tuple.index(3)}")
print(f"Count of 2: {my_tuple.count(2)}")

# Challenges for students:
# 1. Create a list of numbers and find the sum of all even numbers
# 2. Create a list of strings and sort them alphabetically
# 3. Create a tuple of coordinates (x, y, z) and unpack them into separate variables
# 4. Use list comprehension to create a list of all numbers divisible by 3 between 1 and 100
# 5. Create a list of tuples where each tuple contains a name and age, then sort by age
# 6. Try to modify a tuple (what happens?) and explain why
# 7. Create a function that takes a list and returns a new list with all duplicates removed 