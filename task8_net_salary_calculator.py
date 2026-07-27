"""
Task 8: Net Salary Calculator
This program calculates an employee's net salary
based on gross pay and statutory deductions.
"""

# Input section
payroll_number = input("Enter payroll number: ")
name = input("Enter employee name: ")
gender = input("Enter gender: ")
department = input("Enter department: ")
basic_salary = float(input("Enter basic salary: "))

# Allowances
house_allowance = 6500
medical_allowance = 5500

# Gross pay
gross_pay = basic_salary + house_allowance + medical_allowance

# PAYE calculation (tax brackets)
if gross_pay <= 20000:
    paye = 0
elif gross_pay <= 30000:
    paye = 0.04 * gross_pay
elif gross_pay <= 40000:
    paye = 0.05 * gross_pay
else:
    paye = 0.06 * gross_pay

# NHIF and NSSF
nhif = 0.02 * gross_pay
nssf = 0.03 * basic_salary

# Total deductions and net pay
total_deductions = paye + nhif + nssf
net_pay = gross_pay - total_deductions

# Output
print("\n===== SALARY SLIP =====")
print("Payroll Number:", payroll_number)
print("Name:", name)
print("Gender:", gender)
print("Department:", department)

print("\n--- Earnings ---")
print("Basic Salary:", basic_salary)
print("House Allowance:", house_allowance)
print("Medical Allowance:", medical_allowance)
print("Gross Pay:", gross_pay)

print("\n--- Deductions ---")
print("PAYE:", paye)
print("NHIF:", nhif)
print("NSSF:", nssf)
print("Total Deductions:", total_deductions)

print("\nNet Pay:", net_pay)