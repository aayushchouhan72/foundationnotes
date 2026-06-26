'''
7. Power of a Number
A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power.
Write a program to calculate n raised to power p using loops.

Input:
2 5

Output:
32
'''
num = int(input("Enter the number :- "))
pow = num%10

num=num//10
if num:
  answer=1
  while pow: 
     answer*=num
     pow-=1
  print(answer)
else:
     print("Number must contain 2 digit")


     

