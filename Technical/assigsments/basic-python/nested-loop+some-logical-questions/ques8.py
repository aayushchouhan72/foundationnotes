'''

8.
Trimorphic Number Analyzer

A coding system checks cube-based patterns.

A Trimorphic Number:
Cube of number ends with the same number.

Example:
4³ = 64

Write a program to check Trimorphic Number.

Input:
4

Output:
Trimorphic Number

'''
n= int(input("Enter the number :- "))

m= len(str(n)) if len(str(n)) != 1 else 1

cube= n**3

while m :
     dig =cube%10
     numdig = n%10
     if dig != numdig :
           print("Given number is not Trimorphic number ....")
           break
     else:
         m-=1
else:
     print("Given number is Trimorphic number ....")
                