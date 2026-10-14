''' 
1. Product of Odd Numbers up to N

A puzzle game rewards players by multiplying odd numbers up to n.
Write a program using loops to find product of odd numbers.

Input:
5

Output:
15

'''

n = int(input("Enter the your number :- "))
pro=1
while n:
    if n%2!=0:
       pro *=n
    n-=1
print("Product is ",pro)         