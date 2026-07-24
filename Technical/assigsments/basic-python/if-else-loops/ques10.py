'''

10. Mobile Data Plan Advisor


A telecom company suggests the most suitable data plan based on a user’s daily data usage:

* More than 3GB/day → Premium Plan
* 1GB to 3GB/day → Standard Plan
* Less than 1GB/day → Basic Plan

Write a Python program to recommend a plan.

Input:
Enter daily data usage: 0.8

Output:
Recommended Plan: Basic Plan

'''

data = int(input("Enter  number of data you use daily"))

if data<1:
   print("Less than 1GB/day → Basic Plan")
elif data>=1 and data<=3 :
   print("1GB to 3GB/day → Standard Plan")
else :
   print("More than 3GB/day → Premium Plan")