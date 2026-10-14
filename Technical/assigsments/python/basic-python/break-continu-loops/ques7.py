'''
7. Duck Number Checker

A verification system is used by an e-commerce company to validate promotional coupon numbers. Coupon numbers containing at least one zero in between digits are considered special duck numbers. However, if the number starts with zero, it is rejected immediately.

A duck number is a number that contains at least one zero but does not start with zero.

Example:
1023

Write a program using loops to check whether the entered number is a Duck number.

Input:
1023

Output:
Duck Number
'''
n = input("Enter the number :- ") 
n=str(int(n)//10)
count=0
zcount=0
for i in n:
     if count!=0:
         if i == "0":
             zcount+=1
     count+=1 
    
     

if zcount:
     print("Given number is duck number ")
else:
     print("Given number not duck number ")