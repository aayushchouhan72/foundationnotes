# Assignment 3: Security PIN Verification (Palindrome Number)

# A bank allows customers to choose a special PIN. For promotional purposes, the bank rewards customers whose PIN is a palindrome (reads the same from left to right and right to left).

# As a software developer, write a recursive program to verify whether the entered PIN is a palindrome.

# Task

# Write a recursive function to reverse the given number and determine whether it is a palindrome.

# Input 1
# Enter PIN:
# 1221
# Output 1
# Palindrome Number
# Input 2
# Enter PIN:
# 1234
# Output 2
# Not a Palindrome Number


n = input("Enter the decimal number: ")
m=len(n)
count=0
def pincheck(x):
    global count
    if x=="" and x[0] ==  x[-1]:
         count+=1
         print(x[1:-1])
         return pincheck(x[1:-1])
    else:
        if count == m/2:
             return True
        else:
            return False


print(pincheck(n))
