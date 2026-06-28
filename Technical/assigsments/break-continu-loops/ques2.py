'''
2. Count Numbers Divisible by 7 Between Two Numbers

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4

'''

n = int(input("Enter the first number :- "))
m= int(input("Enter the second number :- "))
con=0

while n<=m:
       if n%7==0:
          con+=1
       n+=1
print("number are divisible by 7 in this range :- ",con)