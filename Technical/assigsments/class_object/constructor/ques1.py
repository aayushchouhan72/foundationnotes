# Question 1: Employee Salary Management System
# Scenario

# A company wants to automate employee salary calculations. The HR department needs a system that calculates the gross salary of an employee by including allowances.

# Requirements

# Create a class named Employee with the following attributes:

# employee_id
# employee_name
# basic_salary

# Initialize the values using a constructor.

# Calculations
# HRA = 20% of Basic Salary
# DA = 15% of Basic Salary
# Gross Salary = Basic Salary + HRA + DA
# Sample Input
# Enter Employee ID : E101
# Enter Employee Name : Rahul Sharma
# Enter Basic Salary : 50000
# Sample Output
# ------ Employee Salary Details ------
# Employee ID      : E101
# Employee Name    : Rahul Sharma
# Basic Salary     : 50000.0
# HRA              : 10000.0
# DA               : 7500.0
# Gross Salary     : 67500.0

class student:
    def __init__(self,e,n,s):
        self.employeid=e
        self.employesalary=s
        self.employename=n
    def hracal(self):
         self.hra= self.employesalary*0.20
         return self.employesalary*0.20
    def dacal(self):
        self.da=self.employesalary*0.15
        return self.employesalary*0.15
    def netsal(self):
        return self.employesalary+self.hra+self.da
eid = input("Enter the employe id ...")
ename= input("Enter the employe name ...")
esal= float(input("Enter the basic salary ..."))
s= student(eid,ename,esal)

print(f"""
------ Employee Salary Details ------
Employee ID      : {s.employeid}
Employee Name    : {s.employename}
Basic Salary     : {s.employesalary}
HRA              : {s.hracal()}
DA               : {s.dacal()}
Gross Salary     : {s.netsal()}
""")



