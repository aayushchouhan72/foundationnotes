
# *13. Number Range Display System (if-elif with loops)*
# A number analysis tool processes two input values and displays numbers between them based on their relationship.

# * If the first number is less than the second, display numbers in ascending order
# * If the first number is greater than the second, display numbers in descending order
# * If both numbers are equal, display "Both numbers are same"

# Write a program using *if-elif-else and loops* to implement this logic.

# Input: 5, 10
# Output: 5 6 7 8 9 10

# Input: 10, 5
# Output: 10 9 8 7 6 5

# Input: 7, 7
# # Output: Both numbers are same
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))



# if num1<num2:
#     while num1<=num2:
#         print(num1)
#         num1=num1+1

# elif num1>num2:
#     while num1>=num2:
#         print(num1)
#         num1=num1-1

# else:
#     print("Both numbers are same")
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