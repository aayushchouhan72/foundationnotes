'''
1. Prime Security Code Checker

A high-security research lab uses numeric passcodes to unlock restricted doors. To improve security,
 only prime numbers are accepted because they have exactly two factors and are harder to predict using common patterns.

When an employee enters a code, the system must verify whether the number is prime. If yes, access is granted; otherwise, access is denied.

Write a program to check whether the entered number is Prime or Not Prime.

Input:
29

Output:
Prime Number

'''
import math
n=int(input("Enter the password number:- "))

i=2
while i<=int(math.sqrt(n)):
      if n%i==0:
           break 
      i+=1
else:
    print("Given number is prime number so the access is granted to the user ..")

if i<int(math.sqrt(n)):
     print("Given number is not prime number so access is denied ")