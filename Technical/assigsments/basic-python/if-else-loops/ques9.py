'''
9. Student Attendance Eligibility System

A college determines whether a student is eligible to sit for exams based on attendance percentage:

* 75% and above → Eligible
* 60% to 74% → Eligible with warning
* Below 60% → Not eligible

Write a Python program to check eligibility.

Input:
Enter attendance percentage: 58

Output:
Status: Not Eligible

'''

att = int(input("Enter your attendance percentage :- "))

if att<60:
   print("Not eligible")
elif att>=60 and att<=74:
   print("Eligible with warning")
elif att>74:
   print("Eligible")

