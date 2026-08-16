# =====================================================================
# QUESTION 2: STUDENT RESULT PROCESSING
# =====================================

# A training institute wants to manage student records using NamedTuple.

# Fields:
# roll_no, name, course, marks

# Requirements:

# 1. Read N student records from the user and store them in a list of NamedTuples.

# ---

# 2. Display all student details.

# ---

# 3. Find and display the topper of the class.

# ---

# 4. Count and display the number of students scoring above 80 marks.

# ---

# 5. Calculate and display the average marks.

# ---

# 6. Accept a course name from the user and display all students enrolled in that course.

# ---

# Test Case:

# Input:
# Enter number of students: 4

# 1 Ravi Python 85
# 2 Anjali Java 78
# 3 Karan Python 92
# 4 Pooja Testing 88

# Enter course: Python

# Expected Output:
# Topper:
# 3 Karan Python 92

# Students Above 80:
# 3

# Average Marks:
# 85.75

# Students in Python Course:
# 1 Ravi Python 85
# 3 Karan Python 92

# =


from collections import namedtuple 

student =  namedtuple("Student",["roll_no", "name", "course", "marks"])

lis=[]

number =  int(input("Enter the number of employes "))

for i in range(number):
    roll = int(input("Enter Roll number ...."))
    name =  input("Enter The strudent name ....")
    course = input("Enter the course ....")
    marks = float(input("Enter the Marks ...."))
    lis.append(student(roll,name,course,marks))

countabove80=0
maxmarks=0
summarks=0
for i  in lis:
     print("Employe data ")
     print(i.roll_no,i.name,i.course,i.marks,sep="\n")
     if i.marks>maxmarks:
          maxmarks=i.marks
     if i.marks>80:
          countabove80+=1
     summarks+=i.marks
     print()
     print()

print(f"Average marks is {summarks/number}\nMaximum marks is {maxmarks}\nCount above 80 is {countabove80}")