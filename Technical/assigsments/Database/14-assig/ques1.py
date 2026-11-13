# ASSIGNMENT 1: STUDENT MANAGEMENT SYSTEM
# =======================================

# -------
# A coaching institute wants to manage student records using
# Python Database Connectivity (PDBC).

# TABLE STRUCTURE
# ===============

# Table Name: student_pdbc

# Column       Data Type
# --------------------------------
# sid          INT PRIMARY KEY
# sname        VARCHAR(50)
# course       VARCHAR(50)
# fees         DECIMAL(10,2)
# city         VARCHAR(30)


# SAMPLE DATA
# ===========

# sid   sname    course    fees       city
# ------------------------------------------------
# 101   Amit     Python    15000.00   Indore
# 102   Priya    Java      18000.00   Bhopal
# 103   Rahul    Python    15000.00   Indore
# 104   Neha     Java      18000.00   Ujjain
# 105   Karan    MERN      20000.00   Indore


# MENU
# ====

# ===== STUDENT MANAGEMENT SYSTEM =====
# 1. Add Student
# 2. Display All Students
# 3. Search Student by Name
# 4. Update Student Fees
# 5. Delete Student
# 6. Exit

# Enter your choice:


# TASK 1: ADD STUDENT
# ===================

# INPUT
# -----
# Enter your choice: 1
# Enter Student ID: 106
# Enter Student Name: Anjali
# Enter Course: Python
# Enter Fees: 15000
# Enter City: Dewas

# OUTPUT
# ------
# Student inserted successfully.


# TASK 2: DISPLAY ALL STUDENTS
# ============================

# INPUT
# -----
# Enter your choice: 2

# OUTPUT
# ------
# ID    Name      Course    Fees       City
# ------------------------------------------------
# 101   Amit      Python    15000.00   Indore
# 102   Priya     Java      18000.00   Bhopal
# 103   Rahul     Python    15000.00   Indore
# 104   Neha      Java      18000.00   Ujjain
# 105   Karan     MERN      20000.00   Indore
# 106   Anjali    Python    15000.00   Dewas


# TASK 3: SEARCH STUDENT BY NAME USING LIKE
# =========================================

# INPUT
# -----
# Enter your choice: 3
# Enter name to search: an

# OUTPUT
# ------
# Matching students:

# ID    Name      Course    Fees       City
# ------------------------------------------------
# 105   Karan     MERN      20000.00   Indore
# 106   Anjali    Python    15000.00   Dewas

# NOTE
# ----
# Use a parameterized query with:
# WHERE sname LIKE %s

# Pass the search pattern:
# '%' + search_name + '%'


# TASK 4: UPDATE STUDENT FEES
# ===========================

# INPUT
# -----
# Enter your choice: 4
# Enter Student ID: 101
# Enter New Fees: 17000

# OUTPUT
# ------
# Student fees updated successfully.


# TASK 5: DELETE STUDENT
# ======================

# INPUT
# -----
# Enter your choice: 5
# Enter Student ID: 104

# OUTPUT
# ------
# Student deleted successfully.


# TASK 6: EXIT
# ============

# INPUT
# -----
# Enter your choice: 6

# OUTPUT
# ------
# Thank you for using Student Management System.


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

def add_student(id,name,course,fees,city):
    
    try:
        db=connect_db()
        cur =db.cursor()
        cur.execute('insert into student_pdbc(sid, sname, course, fees, city) values(%s,%s,%s,%s,%s)',(id,name,course,fees,city))
        db.commit()
        print("User Added Successfully ✅✅")
    except mysql.connector.errors.ProgrammingError as e:
        print("Invalid provided data for connection",e)

def display_students(display=True):
    try:
        db=connect_db()
        cur = db.cursor()
        cur.execute("SELECT * FROM student_pdbc")
        rows = cur.fetchall()
        if display:
            print('ID    Name      Course    Fees       City')
            for row in rows:
                print(f'{row[0]}  {row[1]}   {row[2]}   {row[3]}   {row[4]}')
        return rows
    except mysql.connector.errors.ProgrammingError as e:
        print("Invalid provided data for connection",e)

def search_by_name(name):
    try:
        db=connect_db()
        cur = db.cursor()
        cur.execute("SELECT * FROM student_pdbc where sname like %s",("%"+name+"%",))
        rows = cur.fetchall()
        if not rows:
             print("user not found ..")
             return
        print('ID    Name      Course    Fees       City')
        for row in rows:
            print(f'{row[0]}  {row[1]}   {row[2]}   {row[3]}   {row[4]}')
        return rows
    except mysql.connector.errors.ProgrammingError as e:
        print("Invalid provided data for connection",e)

def update_stu_fees(sid,newfees):
    try:
        db=connect_db()
        cur = db.cursor()
        cur.execute("update student_pdbc set fees=%s where sid=%s",(newfees,sid))
        db.commit()
        print("User data is updated sucessfully ✅✅")
    except mysql.connector.errors.ProgrammingError as e:
        print("Invalid provided data for connection",e)

def delete_stu(sid):
    try:
        db=connect_db()
        cur = db.cursor()
        cur.execute("delete from student_pdbc where sid=%s",(sid,))
        db.commit()
        print("User data is deleted sucessfully ✅✅")
    except mysql.connector.errors.ProgrammingError as e:
        print("Invalid provided data for connection",e)

# Custom Exception...

class Invalidname(Exception):
    pass

class Invalidsubject(Exception):
    pass

class Invalidfeeamount(Exception):
    pass

class Invalidusertoupdate(Exception):
    pass

class Invalidusertodelete(Exception):
    pass


subjects = [
    "python",
    "java",
    "c",
    "c++",
    "html",
    "css",
    "javascript",
    "react.js",
    "node.js",
    "express.js",
    "sql",
    "mysql",
    "mongodb",
    "dsa",
    "data science",
    "machine learning",
    "artificial intelligence",
    "django",
    "flask",
    "fastapi",
    "git & github",
    "mern stack",
    "web development",
    "full stack development",
    "cyber security",
    "cloud computing",
    "devops"
]
while True:
    print("""
 ===== STUDENT MANAGEMENT SYSTEM =====
 1. Add Student
 2. Display All Students
 3. Search Student by Name
 4. Update Student Fees
 5. Delete Student
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
             course= input("Enter the course name ..").lower()
             if course not in subjects:
                  raise Invalidsubject("Enter the valid subject")
             fees= float(input("Enter the fees amount .."))
             if fees<=0:
                 raise Invalidfeeamount("Invalid fees amount")
             city= input("Enter the city")
             add_student(id,name,course,fees,city)
         case 2:
              display_students()
         case 3:
            name = input("Enter the name to search ")
            search_by_name(name)
         case 4:
              sid = int(input("Enter the student id "))
              newfee= float(input("Enter new fees "))
              users =  display_students(display=False)
              for row in users:
                   if row[0] == sid:
                       break
              else:
                  raise Invalidusertoupdate("Invalid user to update ")
              update_stu_fees(sid,newfee)
         case 5:
              sid = int(input("Enter the student id "))
              users =  display_students(display=False)
              for row in users:
                   if row[0] == sid:
                       break
              else:
                  raise Invalidusertodelete("Invalid user to delete ")
              delete_stu(sid)
         case 6:
              print("Clossing an application")
              break
    except(Invalidsubject,Invalidfeeamount,Invalidname,Invalidusertoupdate,Invalidusertodelete) as e:
        print(e)
    except ValueError:
        print("Invalid value enter ")
    