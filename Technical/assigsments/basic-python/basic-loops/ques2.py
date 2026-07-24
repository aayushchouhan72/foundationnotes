'''
2. Smallest Digit in Number
A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.

Input:
57294

Output:
Smallest Digit = 2


'''

n = int(input("ENter the number  "))

min=n%10
n=n//10

while n :
     temp  = n%10
     if min>temp:
        min=temp
     n= n//10

print("Minimum digit in the given number is ..",min)      