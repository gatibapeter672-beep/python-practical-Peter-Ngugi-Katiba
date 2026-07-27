"""
Task 3: Python Data Types

This program demonstrates different Python data types and operations:
- Integer, Float, Boolean
- String operations
- List, Tuple, Set, Dictionary
- Type casting
"""

# a. Integer
num_int = 10
print("Integer:", num_int)
print("Type:", type(num_int))


# b. Float
num_float = 5.5
print("\nFloat:", num_float)
print("Addition:", num_float + 2.5)


# c. Boolean
is_active = True
print("\nBoolean:", is_active)

if is_active:
    print("The system is active")


# d. String
text = "Hello"
text2 = "World"

# Concatenation
combined = text + " " + text2
print("\nConcatenation:", combined)

# Slicing
print("Slicing (first 3 chars):", combined[:3])

# Length
print("Length:", len(combined))


# e. List
fruits = ["apple", "banana", "mango", "orange", "grape"]
print("\nOriginal List:", fruits)

# Append
fruits.append("pineapple")
print("After append:", fruits)

# Remove
fruits.remove("banana")
print("After remove:", fruits)

# Indexing
print("First item:", fruits[0])


# f. Tuple (immutable)
my_tuple = (1, 2, 3)

try:
    my_tuple[0] = 10  
except TypeError:
    print("\nTuple is immutable (cannot be changed)")


# g. Set (removes duplicates)
numbers = {1, 2, 2, 3, 4, 4}
print("\nSet (duplicates removed):", numbers)


# h. Dictionary
student = {
    "name": "Peter",
    "age": 20,
    "course": "Computer Science"
}

# Access
print("\nStudent Name:", student["name"])

# Add
student["year"] = 2
print("After adding year:", student)

# Delete
del student["age"]
print("After deleting age:", student)


# i. Type Casting
num_str = "100"

# Convert string to int
converted_int = int(num_str)
print("\nString to Int:", converted_int)

# Convert int to float
converted_float = float(converted_int)
print("Int to Float:", converted_float)

# Convert float to string
converted_str = str(converted_float)
print("Float to String:", converted_str)