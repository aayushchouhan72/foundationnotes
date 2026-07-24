'''
6. Automorphic Number Checker

A digital security company designs smart lockers that open only for special self-matching numeric codes. When a user enters a number, the system squares the number and checks whether the result ends with the same digits as the original code. If yes, the locker grants access.

An automorphic number is a number whose square ends with the same number.

Example:
25² = 625

Write a program using loops to check whether the entered number is an Automorphic number.

Input:
25

Output:
Automorphic Number

'''
n = int(input("ENter the number :- "))
sqr = n**2
m= 2 if len(str(sqr))>=3 else 1
while m:
    if n%10==sqr%10:
         n=n//10
         sqr=sqr//10
         m-=1
    else:
       break
if m!=0:
    print("Given  Not Automorphic number..")
else:
    print("Given  Automorphic number..")