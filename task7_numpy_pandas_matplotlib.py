"""
Task 7: NumPy, Pandas & Matplotlib

This program demonstrates:
- NumPy arrays and operations
- Pandas DataFrame and filtering
- Matplotlib charts
"""

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# b. NumPy - 1D array
array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("NumPy Array:", array_1d)
print("Mean:", np.mean(array_1d))
print("Sum:", np.sum(array_1d))

# Reshape to 2x5
reshaped = array_1d.reshape(2, 5)
print("Reshaped (2x5):\n", reshaped)



# c. NumPy - element-wise operations
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])

print("\nAddition:", array_a + array_b)
print("Subtraction:", array_a - array_b)
print("Multiplication:", array_a * array_b)
print("Division:", array_a / array_b)



# d. Pandas - DataFrame
data = {
    "Name": ["Peter", "John", "Mary", "Ann", "David"],
    "Marks": [78, 45, 88, 60, 30],
    "Course": ["CS", "IT", "CS", "IT", "CS"],
    "Year": [2, 1, 3, 2, 1]
}

df = pd.DataFrame(data)
print("\nDataFrame:\n", df)



# e. Filter marks > 50
filtered = df[df["Marks"] > 50]
print("\nStudents with Marks > 50:\n", filtered)



# f. Bar Chart
plt.figure()
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()



# g. Line Graph
weeks = ["Week1", "Week2", "Week3", "Week4"]
savings = [100, 150, 200, 250]

plt.figure()
plt.plot(weeks, savings, marker='o')
plt.title("Weekly Savings Trend")
plt.xlabel("Week")
plt.ylabel("Amount Saved")
plt.savefig("savings_trend.png")  # Save as PNG
plt.show()