
# *12. Multiplication of Digits*
# A puzzle game calculates a score by multiplying all digits of a number together. After calculating the score, the game also checks whether the final score is even or odd to assign a bonus.
# Write a program to *find the product of all digits of a number using loops and then check whether the result is even or odd*.

# Input: 1234
# Output: 24
# Even
# num = int(input("Enter any number: "))
# mul=1
# while num>0:
#     digit=num%10
#     mul=product*digit
#     num=num//10
# print(mul)
# if mul%2==0:
#     print("Even")
# else:
#     print("Odd")
# num1 = int(input("Enter the number one"))

# num2 = int(input("Enter the number two"))

# if num1==num2:
#     print("Both numbers are equal entred number should be different ..")
# elif num1<num2:
#     for i in range(num1,num2 + 1,1):
#          print(i,end=" ")
# else:
#     for i in range(num1,num2-1,-1):
#             print(i,end=" ")
ques 13 
num1 = int(input("Enter the number one"))

num2 = int(input("Enter the number two"))

if num1==num2:
    print("Both numbers are equal entred number should be different ..")
elif num1<num2:
    for i in range(num1,num2 + 1,1):
         print(i,end=" ")
else:
    for i in range(num1,num2-1,-1):
            print(i,end=" ")