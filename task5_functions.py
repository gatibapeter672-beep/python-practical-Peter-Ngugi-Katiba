"""
Task 5: Functions in Python

This program demonstrates:
- Built-in functions
- User-defined functions
- Default parameters
- *args usage
- Lambda functions
- Variable scope
"""

# a. Built-in functions
numbers = [4, 2, 9, 1, 5]

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Sorted:", sorted(numbers))


# b. User-defined function
def calculate_area(length, width):
    return length * width

area = calculate_area(5, 3)
print("\nArea of rectangle:", area)


# c. Function with default parameters
def greet(name="Guest"):
    print("Hello,", name)

greet("Peter")
greet()  # uses default value


# d. Function with *args
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print("\nSum using *args:", add_numbers(1, 2, 3, 4))


# e. Lambda function with map()
numbers_list = [1, 2, 3, 4]

squared = list(map(lambda x: x ** 2, numbers_list))
print("\nSquared values:", squared)


# f. Variable scope
x = 10  # global variable

def show_scope():
    global x
    x = 20  # modifying global variable
    y = 5   # local variable
    print("\nInside function - x:", x)
    print("Inside function - y:", y)

show_scope()

print("Outside function - x:", x)