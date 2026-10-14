'''
9.
Abundant Number Detector

A financial system analyzes surplus numbers.

An Abundant Number:
Sum of proper factors > number

Write a program to check Abundant Number.

Input:
12

Output:
Abundant Number
'''
n= int(input("enter the number :- "))

sum=0
i=1

while i<=n//2:
      if n%i == 0:
         sum +=i
      i+=1
else:
     if sum>n:
           print("Abundent Number >..")
     else:
           print("Number is not Abundent Number ")
