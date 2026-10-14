
# ============================================================
# ASSIGNMENT 1 – STUDENT MANAGEMENT SYSTEM
# ========================================

# Create a `Student` class inside:

# models/student.py

# ATTRIBUTES:

# * roll_no
# * name
# * marks

# TASKS:

# 1. Take details of 5 students from the user.
# 2. Create a Student object for each student.
# 3. Store all Student objects inside a list.
# 4. Display all students.
# 5. Display students whose marks are greater than 60.
# 6. Find the student having the highest marks.
# 7. Calculate the average marks of all students.

# SAMPLE INPUT:

# Enter Roll No: 101
# Enter Name: Amit
# Enter Marks: 78

# Enter Roll No: 102
# Enter Name: Rahul
# Enter Marks: 55

# Enter Roll No: 103
# Enter Name: Priya
# Enter Marks: 91

# Enter Roll No: 104
# Enter Name: Neha
# Enter Marks: 67

# Enter Roll No: 105
# Enter Name: Rohit
# Enter Marks: 45

# EXPECTED OUTPUT:

# All Students:
# 101 Amit 78
# 102 Rahul 55
# 103 Priya 91
# 104 Neha 67
# 105 Rohit 45

# Students having marks greater than 60:
# 101 Amit 78
# 103 Priya 91
# 104 Neha 67

# Highest Marks:
# 103 Priya 91

# Average Marks:
# 67.2

from models.class_module import Student
num= int(input("Enter the number of student ..."))
Students=[]
for _ in range(num): 
     sname= input("Enter the student name ...")
     rno =int(input("Enter the student roll number ..."))
     smarks= int(input("Enter the student marks ..."))
     obj=Student(rno,sname,smarks)
     Students.append(obj)

Student.display_Student(Students)
Student.display_Student_greter_60(Students)
Student.highest_marks_student(Students)
print(Student.average_marks_of_Student(Students))

