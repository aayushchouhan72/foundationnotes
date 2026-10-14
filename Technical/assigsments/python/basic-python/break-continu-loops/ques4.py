'''

4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number
'''


n= int(input("Enter the number :- "))
sum=0
temp=n
while n:
      dig = n%10
      fac=1
      while dig :
            fac *=dig
            dig-=1
      sum +=fac
      n=n//10
if sum == temp:
     print("Given number is strong number ")

else:
    print("Given number is not string ")           
    