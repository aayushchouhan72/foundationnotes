# ============================================================
# ASSIGNMENT 1 — EMPLOYEE MANAGEMENT SYSTEM
# =========================================

# SCENARIO:

# A company wants to maintain information about different types of employees.

# Create the following class hierarchy:

# Employee
# |
# +-------- Developer
# |
# +-------- Manager

# REQUIREMENTS:

# 1. Create a parent class Employee.

# Employee should contain:

# * employee_id
# * employee_name
# * salary

# 2. Create Developer and Manager classes that inherit from Employee.

# 3. Employee should have a method:

# display_details()

# 4. Developer should have:

# programming_language

# and a method:

# write_code()

# 5. Manager should have:

# team_size

# and a method:

# manage_team()

# 6. The child-class constructors must initialize parent-class data using super().

# 7. Override display_details() in both child classes.

# 8. From the overridden method, call the parent display_details() using super().

# 9. salary must be encapsulated.

# Implement:

# @property
# @salary.setter
# @salary.deleter

# 10. Salary setter must reject salary <= 0.

# 11. Read ALL employee information from the user.

# INPUT REQUIREMENT:

# Ask the user:

# Enter Employee ID:
# Enter Employee Name:
# Enter Salary:
# Enter Employee Type:

# 1. Developer
# 2. Manager

# If Developer:

# Enter Programming Language:

# If Manager:

# Enter Team Size:

# SAMPLE INPUT:

# Enter Employee ID: 101
# Enter Employee Name: Rahul
# Enter Salary: 45000
# Enter Employee Type: 1
# Enter Programming Language: Python

# EXPECTED OUTPUT:

# ## Employee Details

# Employee ID: 101
# Employee Name: Rahul
# Salary: 45000
# Role: Developer
# Programming Language: Python

# Rahul is developing applications using Python.

# ============================================================

class Employee:
    def __init__(self, employee_id, employee_name, salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.salary = salary

    def display_details(self):
        print("\n## Employee Details")
        print(f"Employee ID: {self.employee_id}")
        print(f"Employee Name: {self.employee_name}")
        print(f"Salary: {self.salary}")


class Developer(Employee):
    def __init__(self, employee_id, employee_name, salary, programming_language):
        super().__init__(employee_id, employee_name, salary)
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()
        print("Role: Developer")
        print(f"Programming Language: {self.programming_language}")

    def write_code(self):
        print(
            f"\n{self.employee_name} is developing applications using "
            f"{self.programming_language}."
        )


class Manager(Employee):
    def __init__(self, employee_id, employee_name, salary, team_size):
        super().__init__(employee_id, employee_name, salary)
        self.team_size = team_size

    def display_details(self):
        super().display_details()
        print("Role: Manager")
        print(f"Team Size: {self.team_size}")

    def manage_team(self):
        print(
            f"\n{self.employee_name} is managing a team of "
            f"{self.team_size} employees."
        )


class Employee(Employee):
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value <= 0:
            raise ValueError("Salary must be greater than 0.")
        self._salary = value

    @salary.deleter
    def salary(self):
        del self._salary


employee_id = input("Enter Employee ID: ")
employee_name = input("Enter Employee Name: ")
salary = float(input("Enter Salary: "))

print("Enter Employee Type:")
print("1. Developer")
print("2. Manager")

employee_type = int(input("Enter Employee Type: "))

if employee_type == 1:
    programming_language = input("Enter Programming Language: ")
    employee = Developer(
        employee_id,
        employee_name,
        salary,
        programming_language
    )
    employee.display_details()
    employee.write_code()

elif employee_type == 2:
    team_size = int(input("Enter Team Size: "))
    employee = Manager(
        employee_id,
        employee_name,
        salary,
        team_size
    )
    employee.display_details()
    employee.manage_team()

else:
    print("Invalid Employee Type.")