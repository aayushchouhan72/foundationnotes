
# Question 4: Student Result Processing System
# Scenario

# A college wants to automate result generation by calculating total marks, percentage, and grade.

# Requirements

# Create a class named Student with:

# roll_number
# student_name
# marks1
# marks2
# marks3

# Initialize the values using a constructor.

# Calculations
# Total = Marks1 + Marks2 + Marks3
# Percentage = Total / 3
# Grade Criteria
# Percentage Grade
# 90 and above A
# 75 to 89 B
# 60 to 74 C
# Below 60 D
# Sample Input
# Enter Roll Number : 101
# Enter Student Name : Priya Sharma
# Enter Marks in Subject 1 : 85
# Enter Marks in Subject 2 : 90
# Enter Marks in Subject 3 : 88
# Sample Output
# ------ Student Result ------
# Roll Number      : 101
# Student Name     : Priya Sharma
# Total Marks      : 263
# Percentage       : 87.67
# Grade            : B

class Student:

    def __init__(self, roll_number, student_name, marks1, marks2, marks3):

        self.roll_number = roll_number
        self.student_name = student_name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def validate_marks(self):

        if self.marks1 < 0 or self.marks1 > 100:
            return False

        if self.marks2 < 0 or self.marks2 > 100:
            return False

        if self.marks3 < 0 or self.marks3 > 100:
            return False

        return True

    def calculate_result(self):

        if self.validate_marks() == False:
            print("Invalid marks! Marks must be between 0 and 100.")
            return

     
        self.total = self.marks1 + self.marks2 + self.marks3

        
        self.percentage = self.total / 3

        if self.percentage >= 90:
            self.grade = "A"

        elif self.percentage >= 75:
            self.grade = "B"

        elif self.percentage >= 60:
            self.grade = "C"

        else:
            self.grade = "D"


# Taking input

roll_number = int(input("Enter Roll Number : "))
student_name = input("Enter Student Name : ")

marks1 = float(input("Enter Marks in Subject 1 : "))
marks2 = float(input("Enter Marks in Subject 2 : "))
marks3 = float(input("Enter Marks in Subject 3 : "))




s = Student(roll_number, student_name, marks1, marks2, marks3)



s.calculate_result()




if s.validate_marks():

    print("""
------ Student Result ------
""")

    print("Roll Number   :", s.roll_number)
    print("Student Name  :", s.student_name)
    print("Total Marks   :", s.total)
    print("Percentage    :", f"{s.percentage:.2f}")
    print("Grade         :", s.grade)
