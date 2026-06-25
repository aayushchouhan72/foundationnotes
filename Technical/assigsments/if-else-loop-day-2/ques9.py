# 9. Check All Digits Are Even*
# A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
# Write a program to *check whether all digits of a number are even using loops*.

# Input: 2468
# Output: All Even

# Input: 2456
# Output: Not All Even
# num = int(input("Enter any number"))
# count = 0

# while num > 0:
#     digit = num % 10
#     if digit % 2 != 0:
#         count = count + 1
#     num = num // 10


# if count == 0:
#     print("All Even")
# else:
#     print("Not All Even")
num = input("Enter number :- ")
count=0
for i in num :
    i = int(i)
    if i%2!=0:
       count+=1

if count:
    print("ALL NUmbers are not even")
else: 
    print("All Number are even")("All Number are even")