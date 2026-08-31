# 2.

# ASSIGNMENT: ONLINE COURSE ENROLLMENT & STUDENT MANAGEMENT SYSTEM

# A training institute offers multiple courses such as Python, Java, Full Stack Development, Data Science, and React.

# Currently, student enrollment details are maintained manually in Excel sheets. As the number of students is increasing, the institute wants to develop a Student Management System using Python.

# The system should store student records in a nested dictionary where:

# Key → Student ID
# Value → Dictionary containing student information

# Each student record should contain:

# Student Name
# Course Name
# Mobile Number
# Fees
# City
# Sample Data Structure
# {
# 101:{
#     "name":"Ajay",
#     "course":"Python",
#     "mobile":"9876543210",
#     "fees":25000,
#     "city":"Indore"
# },
# 102:{
#     "name":"Ravi",
#     "course":"Java",
#     "mobile":"9876500000",
#     "fees":22000,
#     "city":"Bhopal"
# }
# }
# Menu Driven Program

# Display the following menu repeatedly until the user chooses Exit.

# =========================================
#  STUDENT MANAGEMENT SYSTEM
# =========================================

# 1. Add New Student
# 2. Search Student
# 3. Update Course
# 4. Delete Student
# 5. Display All Students
# 6. Count Total Students
# 7. Display Students By Course
# 8. Display Students By City
# 9. Find Student Paying Highest Fees
# 10. Find Student Paying Lowest Fees
# 11. Exit
# Functional Requirements
# 1. Add New Student

# Accept the following details:

# Student ID
# Student Name
# Course Name
# Mobile Number
# Fees
# City

# Store the information in the nested dictionary.

# Validation

# If Student ID already exists:

# Student ID Already Exists
# 2. Search Student

# Accept Student ID from the user.

# If found, display complete student information.

# Sample Output
# Student ID : 101
# Name       : Ajay
# Course     : Python
# Mobile     : 9876543210
# Fees       : 25000
# City       : Indore

# If not found:

# Student Not Found
# 3. Update Course

# Accept Student ID.

# If found:

# Ask for new course name.
# Update the course.
# Sample Output
# Course Updated Successfully
# 4. Delete Student

# Accept Student ID.

# If found:

# Delete the record.
# Sample Output
# Student Deleted Successfully

# Otherwise:

# Student Not Found
# 5. Display All Students

# Display all student records in a proper format.

# Sample Output
# -----------------------------------
# Student ID : 101
# Name       : Ajay
# Course     : Python
# Fees       : 25000
# -----------------------------------

# Student ID : 102
# Name       : Ravi
# Course     : Java
# Fees       : 22000
# -----------------------------------
# 6. Count Total Students

# Display total number of students enrolled.

# Sample Output
# Total Students : 45
# 7. Display Students By Course

# Accept a course name from the user.

# Display all students enrolled in that course.

# Sample Output
# Enter Course : Python

# 101  Ajay
# 105  Neha
# 112  Aman

# If no students are found:

# No Students Found
# 8. Display Students By City

# Accept city name from the user.

# Display all students belonging to that city.

# Sample Output
# Enter City : Indore

# 101  Ajay
# 108  Ravi
# 115  Pooja
# 9. Find Student Paying Highest Fees

# Display complete details of the student who has paid the highest fees.

# Sample Output
# Highest Fee Paying Student

# Student ID : 121
# Name       : Neha
# Course     : Data Science
# Fees       : 50000
# 10. Find Student Paying Lowest Fees

# Display complete details of the student who has paid the lowest fees.

# Sample Output
# Lowest Fee Paying Student

# Student ID : 131
# Name       : Aman
# Course     : React
# Fees       : 15000
# 11. Exit

# Terminate the application.

# Sample Output
# Thank You For Using Student Management System

student={
     101: {
        "name": "Ajay",
        "course": "Python",
        "mobile": "9876543210",
        "fees": 25000,
        "city": "Indore"
    },
    102: {
        "name": "Ravi",
        "course": "Java",
        "mobile": "9876500000",
        "fees": 22000,
        "city": "Bhopal"
    },
    103: {
        "name": "Aman",
        "course": "JavaScript",
        "mobile": "9876512345",
        "fees": 28000,
        "city": "Ujjain"
    },
    104: {
        "name": "Neha",
        "course": "Python",
        "mobile": "9876523456",
        "fees": 25000,
        "city": "Dewas"
    },
    105: {
        "name": "Priya",
        "course": "React",
        "mobile": "9876534567",
        "fees": 30000,
        "city": "Indore"
    },
    106: {
        "name": "Rohit",
        "course": "Java",
        "mobile": "9876545678",
        "fees": 22000,
        "city": "Bhopal"
    }
}
while True:
    print("""
=========================================
        STUDENT MANAGEMENT SYSTEM
=========================================

1. Add New Student
2. Search Student
3. Update Course
4. Delete Student
5. Display All Students
6. Count Total Students
7. Display Students By Course
8. Display Students By City
9. Find Student Paying Highest Fees
10. Find Student Paying Lowest Fees
11. Exit
""")
    
    choice  = input("Enter the your choice")
    match choice:
         case "1":
             print("Entering the new student ...")
             sid =int(input("Enter the student id ..."))
             pname= input("Enter the student name ...")
             pnumber= input("Enter the number ...")
             pcourse = input("Enter the course ...")
             pfees = input("Enter the course Fees ...")
             pcity = input("Enter the City of student ...")

             if sid not in student:
                  student.update({sid :{
                        "name": pname,
                        "course": pcourse,
                        "mobile": pnumber,
                        "fees": pfees,
                        "city": pcity
                       }})
             else:
                  print("student is already exists")
         case "2":
             print("Wellcome to search student section .....")
             sid =  int(input("Enter the student id ..."))
             if  sid in student:
                    student =  student[sid]
                    for k,v in student.items():
                         print(f"{k} : {v}")
             else:
                  print("student id not in record ...")
         case "3":
            print("Wellcome to update student couses secction .....")
            sid =  int(input("Enter the student id ..."))
            if  sid in student:
                  newcours = input("Enter the course of student...")
                  student[sid]["disease"] =  newcours
                  print("course updated successfully ...")
            else:
                 print("student id not in record ...")
         case "4":
              sid =  int(input("Enter the student id ..."))
              if  sid in student:
                   del student[sid]
                   print(student)
              else:
                   print("student id not in record ...")
              
         case "5":
               for k,v in student.iteams():
                    for j,k in v.iteams():
                         print(f"{j} : {k}")
         case "6":
             print("Total student count ",len(student))
         case "7":
            print("Wellcome to Display student By course")
            course =  int(input("Enter the course  ...."))
            for k,v in student.items():
                 for j,k in v.items():
                       if k == course:
                             print(f"{k}:{v['name']}")
         case "8":
              print("wellcome to seen first student funtionlity ....")
              city=  int(input("Enter the course  ...."))
              for k,v in student.items():
                  for j,k in v.items():
                        if k == city:
                              print(f"{k}:{v['city']}")
         case "9":
               print("max fee")
               max=0
               st=None
               for k,v in student.items():
                    if student[k]['fees']>max:
                         max=student[k]['fees']
                         st=k
               print(f"student {student[k]['name'] } and fees {max}")
         case "10":
              print("max fee")
              max=99999999999999999999999999999999999999999999999999999999999999999999999999999
              st=None
              for k,v in student.items():
                   if student[k]['fees']<max:
                        max=student[k]['fees']
                        st=k
              print(f"student {student[k]['name'] } and fees {max}")
         case "11":
              print("Thank You For Using Hospital student Management System😎😎👍👍")
              break
         case __:
             print("Enter the Vaild Choice ")