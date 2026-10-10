# 2. Employee Salary Report

# A company stores employee salary information in employees.txt.

# Each record contains:

# EmployeeID,EmployeeName,Department,Salary
# Task

# Write a Python program to:

# Accept employee details.
# Store them in the file.
# Read the file.
# Display employees whose salary is greater than ₹50,000.
# Calculate the average salary.
# Sample Input
# Enter number of employees: 4

# 101,Ajay,IT,65000
# 102,Ravi,HR,45000
# 103,Priya,IT,72000
# 104,Amit,Sales,48000
# Expected Output
# Employees with Salary > 50000
# --------------------------------
# 101  Ajay   IT       65000
# 103  Priya  IT       72000
# Average Salary: 57500.00


number = int(input("Enter the number of employe ..."))

for _ in range(number):
    print("\n\n")
    EmployeeID = int(input("Enter the Employee id ..."))
    EmployeeName = input("Enter the Employee name ...")
    Department =  input("Enter the department ...")
    Salary= float(input("Enter the Salary ..."))
    with open("question2/employees.txt","+a") as f:
        f.write(f"{EmployeeID },{EmployeeName},{Department},{Salary},\n")

with open("question2/employees.txt","+r") as f:
    data = f.readlines()
total=0
for line in data:
   EmployeeID,EmployeeName,Department,Salary,e=line.split(",")
   if float(Salary)>50000:
       print(f"{EmployeeID}  {EmployeeName}   {Department}   {Salary}")
   total+=float(Salary)

print(f"Average Salary: {total/len(data)}")

