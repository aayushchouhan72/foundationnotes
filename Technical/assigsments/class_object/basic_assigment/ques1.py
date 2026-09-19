# Assignment 1: Student Result Calculator

#  A school wants to calculate the total marks and percentage of a student.

# Create a class Student with the following attributes:

# Student name

# Roll number

# Marks in English

# Marks in Mathematics

# Marks in Science

# Create the following methods:

# calculate_total() – Calculate the total marks.

# calculate_percentage() – Calculate the percentage.

# display_result() – Display student details, total, and percentage.

# Expected output:

# Student Name: Ajay
# Roll Number: 101
# Total Marks: 240
# Percentage: 80.0%

class student:
    def __init__(self,e,m,s):
         self.e= e
         self.m= m
         self.s=s
    def calculate_total(self):
        self.t=e+m+s
        return self.t
    def calculate_percentage(self):
        return self.t/3
name = input("Enter the name ...")
roll = input("Enter the roll number ...")
e,m,s= list(map(int,input("Enter the marks ").split()))
s1 =  student(e,m,s)

print(f"Student Name: {name}\nRoll Number: {roll} \nTotal Marks: {s1.calculate_total()}\nPercentage: {s1.calculate_percentage()}%")