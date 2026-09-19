# Assignment 2: Employee Salary Calculator

# A company wants to calculate an employee's gross salary.

# Create a class Employee with the following attributes:

# Employee ID

# Employee name

# Basic salary

# HRA percentage

# DA percentage

# Create the following methods:

# calculate_hra() – Calculate HRA.

# calculate_da() – Calculate DA.

# calculate_gross_salary() – Calculate gross salary.

# display_salary() – Display employee salary details.

# Formula:

# HRA = Basic Salary × HRA Percentage / 100
# DA = Basic Salary × DA Percentage / 100
# Gross Salary = Basic Salary + HRA + DA

class student:
    def __init__(self,e,m,s,h,d):
         self.eid= e
         self.ename= m
         self.ebasic=s
         self.hra=h
         self.da=d
    def calculate_hra(self):
        self.ahra=self.ebasic*self.hra/100
        return self.hra
    def alculate_da(self) :
        self.ada = self.ebasic*self.da/100
        return self.ada
    def calculate_gross_salary(self):
        self.gross= self.ebasic+self.ada+self.ahra
        return self.gross
    def display_salary(self):
        print(f"""
Employe name   :{self.eid}
Employe number :{self.ename}
Basic salary   :{self.ebasic}
HRA on salary  :{self.ahra}
DA on salary   :{self.ada}
Net salary     :{self.gross}
""")
empid= input("Enter the employe id  ...")
empnumber= input("Enter the roll number ...")
basicsalary= float(input("Enter the Basic salary ..."))
hrap= int(input("Enter the hra percentage ..."))
dap= int(input("Enter the da percentage ..."))
s1 =  student(empid,empnumber,basicsalary,hrap,dap)

s1.calculate_hra()
s1.alculate_da()
s1.calculate_gross_salary()
s1.display_salary()