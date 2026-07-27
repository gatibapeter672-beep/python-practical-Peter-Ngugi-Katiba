"""
Task 4: Control Structures  Selection & Looping

This program demonstrates:
- Conditional statements (if-elif-else)
- For loop
- While loop
- Break and Continue
- Nested loops
"""

# a. Grade classification
marks = int(input("Enter student marks: "))

if marks >= 70:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 50:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)


# b. For loop (list of fruits)
fruits = ["apple", "banana", "mango", "orange", "grape"]

print("\nFruits List:")
for fruit in fruits:
    print(fruit)


# c. While loop (even numbers from 1 to 10)
print("\nEven numbers from 1 to 10:")
count = 1

while count <= 10:
    if count % 2 == 0:
        print(count)
    count += 1


# d. Break and Continue
print("\nBreak and Continue Example:")

for num in range(1, 11):
    if num == 5:
        continue  # Skip 5
    if num == 9:
        break     # Stop loop at 9
    print(num)


# e. Nested loop (3x3 multiplication table)
print("\n3x3 Multiplication Table:")

for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")
    print()  # Move to next line