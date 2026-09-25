# Assignment 1 – Employee Bonus System

# Create a parent class Employee with the following attributes:

# employee_id
# employee_name
# salary

# Create two child classes:

# Developer
# Manager


# Requirements

# Take employee details from the user.
# Use super() to initialize the common attributes.
# Create a method calculate_bonus() in the parent class.
# Override calculate_bonus() in both child classes.
# Developer gets 10% of salary as bonus.
# Manager gets 20% of salary as bonus.
# Display employee details, bonus and total salary.
# Sample Input
# Enter Employee ID: 101
# Enter Employee Name: Rahul
# Enter Salary: 50000
# Enter Employee Type: Developer

# Expected Output
# ----- Employee Details -----
# Employee ID   : 101
# Employee Name : Rahul
# Salary        : 50000
# Employee Type : Developer
# Bonus         : 5000
# Total Amount  : 55000



# Assignment 2 – Vehicle Rental System

# Create a parent class Vehicle with:

# vehicle_no
# brand
# rent_per_day

# Create two child classes:

# Car
# Bike


# Requirements
# Take vehicle details and number of rental days from the user.
# Use super() to initialize common attributes.
# Create a method calculate_rent(days) in the parent class.
# Override the method in both child classes.
# For a Car, add ₹500 service charge to the rental amount.
# For a Bike, add ₹200 service charge.
# Display the final rental amount.
# Sample Input
# Enter Vehicle Number: MP09AB1234
# Enter Brand: Honda
# Enter Rent Per Day: 800
# Enter Number of Days: 3
# Enter Vehicle Type: Car
# Expected Output
# ----- Rental Details -----
# Vehicle Number : MP09AB1234
# Brand          : Honda
# Rent Per Day   : 800
# Number of Days : 3
# Vehicle Type   : Car
# Rental Amount  : 2400
# Service Charge : 500
# Final Amount   : 2900


# Assignment 3 – Bank Account System

# Create a parent class BankAccount with:

# account_no
# holder_name
# balance

# Create two child classes:

# SavingsAccount
# CurrentAccount
# Requirements
# Take account details from the user.
# Use super() to initialize the common attributes.
# Create a method calculate_interest() in the parent class.
# Override this method in both child classes.
# Savings Account gets 5% interest.
# Current Account gets 2% interest.
# Display the account details and calculated interest.
# Sample Input
# Enter Account Number: 1001
# Enter Holder Name: Amit
# Enter Balance: 50000
# Enter Account Type: Savings


# Expected Output
# ----- Account Details -----
# Account Number : 1001
# Holder Name    : Amit
# Balance        : 50000
# Account Type   : Savings
# Interest Rate  : 5%
# Interest       : 2500
# Amount After Interest : 52500

class Employee:
    def __init__(self,eid,ename,esal):
        self.employee_id=eid,
        self.employee_name=ename,
        self.salary=esal
    def calculate_bonus():
         pass


class Developer(Employee):
    def __init__(self,eid,ename,esal,erole):
         super().__init__(eid,ename,esal)
         self.role=erole
    def calculate_bonus(self):
         return self.salary+self.salary*0.10
    def display_details(self):
         print(f"""
# Employee ID   : {self.employee_id}
# Employee Name : {self.employee_name}
# Salary        : {self.salary}
# Employee Type : {self.role}
# Bonus         : {self.calculate_bonus()}
# Total Amount  : {self.calculate_bonus()+self.salary}
""")
class Manager(Employee):
    def __init__(self,eid,ename,esal,erole):
            super().__init__(eid,ename,esal)
            self.role=erole
    def calculate_bonus(self):
         return self.salary+self.salary*0.20
    def display_details(self):
         print(f"""
# Employee ID   : {self.employee_id}
# Employee Name : {self.employee_name}
# Salary        : {self.salary}
# Employee Type : {self.role}
# Bonus         : {self.calculate_bonus()}
# Total Amount  : {self.calculate_bonus()+self.salary}
""")

emp=Developer(101,"Aayush",9090,"dev")
emp.display_details()


class vehical:
    def __init__(self,vno,vbrand,vren):
        self.vehicle_no=vno,
        self.brand=vbrand,
        self.rent_per_day=vren
    def calculate_rent(days):
            pass


class car(vehical):
    def __init__(self,vno,vbrand,vren,vtype):
         super().__init__(vno,vbrand,vren)
         self.vehical_type=vtype
    def calculate_rent(self,days):
         return self.rent_per_day*days
    def  display_rent(self,days):
         print(f"""
# ----- Rental Details -----
# Vehicle Number :{self.vehicle_no}
# Brand          :{self.brand}
# Rent Per Day   :{self.rent_per_day} 
# Number of Days :{days}
# Vehicle Type   : {}
# Rental Amount  : 2400
# Service Charge : 500
# Final Amount   : 2900
""")
class Bike(vehical):
    def __init__(self,vno,vbrand,vren,vtype):
         super().__init__(vno,vbrand,vren)
         self.vehical_type=vtype
    def calculate_bonus(self):
         return self.salary+self.salary*0.20
    def display_details(self):
         print(f"""
# Employee ID   : {self.employee_id}
# Employee Name : {self.employee_name}
# Salary        : {self.salary}
# Employee Type : {self.role}
# Bonus         : {self.calculate_bonus()}
# Total Amount  : {self.calculate_bonus()+self.salary}
""")

emp=Developer(101,"Aayush",9090,"dev")
emp.display_details()





       
