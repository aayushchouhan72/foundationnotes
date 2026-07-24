'''
4.Spy Number Detector

A cybersecurity system flags special numeric codes.

A number is called a Spy Number if:
Sum of digits = Product of digits

Write a program to check whether the entered number is Spy Number or Not.

Input:
1124

Output:
Spy Number
'''

n= int(input("Enter number :- "))
pro=1
sum=0

while n:
     dig = n%10
     pro*=dig
     sum+=dig
     n//=10

if sum == pro:
      print("Given number is spy number ...")
else:
     print("Given number is not spy number ...")