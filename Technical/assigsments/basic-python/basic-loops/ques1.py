'''1. Largest Digit in Number
A cybersecurity company checks numeric passwords used in smart lockers. To identify password strength, the system finds the highest digit present in the entered password. Higher digits indicate stronger variation in the password pattern.
Write a program to find the largest digit in a number using loops.

Input:
57294

Output:
Largest Digit = 9'''


n = int(input("ENter the number  "))

max= 0;

while n:
     check =  n%10
     if check>max:
          max = check
     n= n//10

print("The maximum digit in given number ..",max)
      