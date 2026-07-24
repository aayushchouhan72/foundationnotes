
# *8. Count Odd Digits*
# A banking system flags IDs with too many odd digits for further verification.
# Write a program to *count the number of odd digits in a given number using loops*.

# Input: 123456
# Output: Odd digits count = 3
# num = int(input("Enter any number"))
# count = 0

# while num > 0:
#     digit = num % 10
#     if digit % 2 != 0:
#         count = count + 1
#     num = num // 10
# print(count)
num = input("Enter number :- ")
count=0;
for i in num :
    i = int(i)
    if i%2!=0:
       count+=1

print(f" Number of odd digit in number is {count}")
