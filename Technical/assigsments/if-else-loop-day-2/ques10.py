# . Even Numbers Between Two Numbers*
# A teacher wants to assign only even roll numbers for a special activity. The system should display all even numbers between two given numbers.
# Write a program to *display all even numbers between two numbers using loops*.

# Input: 10, 20
# Output: 10 12 14 16 18 20
# num1=int(input("enter num1"))
# num2=int(input("enter num2"))
# while num1<=num2:
#     if num1%2==0:
#         print(num1)
#     num1=num1+1
num1 = int(input("Enter the first number :- "))
num2 = int(input("Enter the Second number :- "))

if num1%2 == 0: 
        for i in range(num1,num2+1,2):
             print(i,end=" ")
else:
        for i in range(num1+1,num2+1,2):
             print(i,end=" ")