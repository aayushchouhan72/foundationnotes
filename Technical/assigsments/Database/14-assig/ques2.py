
# =========================================================
# ASSIGNMENT 2: EMPLOYEE MANAGEMENT SYSTEM
# =========================================================

# --------
# A company wants to maintain employee details, departments,
# salaries, and cities using Python PDBC.

# TABLE STRUCTURE
# ===============

# Table Name: employee_pdbc

# Column       Data Type
# --------------------------------
# eid          INT PRIMARY KEY
# ename        VARCHAR(50)
# department   VARCHAR(40)
# salary       DECIMAL(10,2)
# city         VARCHAR(30)


# SAMPLE DATA
# ===========

# eid   ename    department    salary      city
# ----------------------------------------------------
# 201   Amit     IT            45000.00    Indore
# 202   Priya    HR            40000.00    Bhopal
# 203   Rahul    IT            55000.00    Indore
# 204   Neha     Finance       50000.00    Ujjain
# 205   Karan    IT            60000.00    Indore


# MENU
# ====

# ===== EMPLOYEE MANAGEMENT SYSTEM =====
# 1. Add Employee
# 2. Display All Employees
# 3. Search Employee by Name
# 4. Update Employee Salary
# 5. Delete Employee
# 6. Exit

# Enter your choice:


# TASK 1: ADD EMPLOYEE
# ====================

# INPUT
# -----
# Enter your choice: 1
# Enter Employee ID: 206
# Enter Employee Name: Anjali
# Enter Department: HR
# Enter Salary: 42000
# Enter City: Dewas

# OUTPUT
# ------
# Employee inserted successfully.


# TASK 2: DISPLAY ALL EMPLOYEES
# =============================

# INPUT
# -----
# Enter your choice: 2

# OUTPUT
# ------
# ID    Name      Department    Salary      City
# ----------------------------------------------------
# 201   Amit      IT            45000.00    Indore
# 202   Priya     HR            40000.00    Bhopal
# 203   Rahul     IT            55000.00    Indore
# 204   Neha      Finance       50000.00    Ujjain
# 205   Karan     IT            60000.00    Indore
# 206   Anjali    HR            42000.00    Dewas


# TASK 3: SEARCH EMPLOYEE BY NAME USING LIKE
# ==========================================

# INPUT
# -----
# Enter your choice: 3
# Enter name to search: ra

# OUTPUT
# ------
# Matching employees:

# ID    Name      Department    Salary      City
# ----------------------------------------------------
# 203   Rahul     IT            55000.00    Indore
# 205   Karan     IT            60000.00    Indore

# NOTE
# ----
# Use:
# WHERE ename LIKE %s

# Pass:
# '%' + search_name + '%'


# TASK 4: UPDATE EMPLOYEE SALARY
# =============================

# INPUT
# -----
# Enter your choice: 4
# Enter Employee ID: 201
# Enter New Salary: 48000

# OUTPUT
# ------
# Employee salary updated successfully.


# TASK 5: DELETE EMPLOYEE
# =======================

# INPUT
# -----
# Enter your choice: 5
# Enter Employee ID: 202

# OUTPUT
# ------
# Employee deleted successfully.


# TASK 6: EXIT
# ============

# INPUT
# -----
# Enter your choice: 6

# OUTPUT
# ------
# Thank you for using Employee Management System.



import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='komal',
        database='assigment_pdbc'
    )

#  Application function 

def add_employee(id,name,dep,sal,city):
    
    try:
        db=connect_db()
        cur =db.cursor()
        cur.execute('insert into employee_pdbc(eid, ename, department, salary, city) values(%s,%s,%s,%s,%s)',(id,name,dep,sal,city))
        db.commit()
        print("User Added Successfully ✅✅")
    except mysql.connector.errors.ProgrammingError as e:
        print("Invalid provided data for connection",e)

def display_employee(display=True):
    try:
        db=connect_db()
        cur = db.cursor()
        cur.execute("SELECT * FROM employee_pdbc")
        rows = cur.fetchall()
        if display:
            print('ID    Name      Department    Salary      City')
            for row in rows:
                print(f'{row[0]}  {row[1]}   {row[2]}   {row[3]}   {row[4]}')
        return rows
    except mysql.connector.errors.ProgrammingError as e:
        print("Invalid provided data for connection",e)

def search_by_name(name):
    try:
        db=connect_db()
        cur = db.cursor()
        cur.execute("SELECT * FROM employee_pdbc where ename like %s",("%"+name+"%",))
        rows = cur.fetchall()
        if not rows:
             print("user not found ..")
             return
        print('ID    Name      Department    Salary      City')
        for row in rows:
                print(f'{row[0]}  {row[1]}   {row[2]}   {row[3]}   {row[4]}')
        return rows
    except mysql.connector.errors.ProgrammingError as e:
        print("Invalid provided data for connection",e)

def update_employee_sal(sid,newfee):
    try:
        db=connect_db()
        cur = db.cursor()
        cur.execute("update employee_pdbc set salary=%s where eid=%s",(newfee,sid))
        db.commit()
        print("User data is updated sucessfully ✅✅")
    except mysql.connector.errors.ProgrammingError as e:
        print("Invalid provided data for connection",e)
def delete_employee(sid):
    try:
        db=connect_db()
        cur = db.cursor()
        cur.execute("delete from employee_pdbc where eid=%s",(sid,))
        db.commit()
        print("User data is deleted sucessfully ✅✅")
    except mysql.connector.errors.ProgrammingError as e:
        print("Invalid provided data for connection",e)

# Custom Exception...

class Invalidname(Exception):
    pass

class Invaliddepartments(Exception):
    pass

class Invalidsalamount(Exception):
    pass

class Invalidusertoupdate(Exception):
    pass

class Invalidusertodelete(Exception):
    pass


#  Valid deparments 

departments = [
    "it",
    "hr",
    "finance",
    "marketing",
    "sales",
    "software development",
    "testing",
    "devops",
    "data science",
    "artificial intelligence",
    "cyber security",
    "cloud computing",
    "technical support",
    "research & development",
    "product management",
    "project management",
    "administration"
]
while True:
    print("""
 ===== STUDENT MANAGEMENT SYSTEM =====
 1. Add Employee
 2. Display All Employees
 3. Search Employee by Name
 4. Update Employee Salary
 5. Delete Employee
 6. Exit
""") 
    try:
        
        choice = int(input("Enter the choice"))
        match choice:
         case 1:
             id = int(input("Enter the id"))
             name=input("Enter the name ").lower()
             for i in name:
                if not( 97<= ord(i)<=122):
                    raise Invalidname("Enter the valid user name..")
             dep= input("Enter the course name ..").lower()
             if dep not in departments:
                  raise Invaliddepartments("Enter the valid departments")
             sal= float(input("Enter the salary amount .."))
             if sal<=0:
                 raise Invalidsalamount("Invalid salary  amount")
             city= input("Enter the city")
             add_employee(id,name,dep,sal,city)
         case 2:
              display_employee()
         case 3:
            name = input("Enter the name to search ")
            search_by_name(name)
         case 4:
              sid = int(input("Enter the employee id "))
              newfee= float(input("Enter new salary"))
              users =  display_employee(display=False)
              for row in users:
                   if row[0] == sid:
                       break
              else:
                  raise Invalidusertoupdate("Invalid user to update ")
              update_employee_sal(sid,newfee)
         case 5:
              sid = int(input("Enter the student id "))
              users =  display_employee(display=False)
              for row in users:
                   if row[0] == sid:
                       break
              else:
                  raise Invalidusertodelete("Invalid user to delete ")
              delete_employee(sid)
         case 6:
              print("Clossing an application")
              break
    except(Invaliddepartments,Invalidsalamount,Invalidname,Invalidusertoupdate,Invalidusertodelete) as e:
        print(e)
    except ValueError:
        print("Invalid value enter ")
    