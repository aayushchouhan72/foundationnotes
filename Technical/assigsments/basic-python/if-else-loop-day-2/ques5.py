
'''# 5. Palindrome Check
# A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
# Write a program to *check whether a given number is a palindrome using loops*.

# Input: 121
# Output: Palindrome
# num=int(input("enterr  any number"))
# rev=0

# temp=num
# while num>0:
#     rev=rev*10+num%10
#     num=num//10
# if temp==sum:
#     print("palindrome")
# else:
#     print("not palindrome")'''
num=int(input("enterr  any number"))
rev=0

temp=num
for i in range(len(str(num))): 
    rev=rev*10+num%10
    num=num//10
if temp==rev:
    print("palindrome")
else:
    print("not palindrome")e")