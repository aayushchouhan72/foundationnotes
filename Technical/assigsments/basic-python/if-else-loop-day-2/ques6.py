# 6. Armstrong Number (3-digit)
# In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
# Write a program to *check whether a number is an Armstrong number using loops*.

# Input: 153
# Output: Armstrong
# num = int(input("Enter any number: "))
# temp = num
# sum= 0

# while num > 0:
#     r=num%10
#     sum =sum+r*r*r
#     num = num // 10

# if temp==sum:
#     print("Armstrong")
# else:
#     print("Not Armstrong")
num = int(input("Enter any number: "))
temp = num
sum=0
i=0
for i in range(3):
    
    r=num%10
    sum=sum+r*r*r
    num=num//10

if temp==sum:
    print("Armstrong")
else:
    print("Not Armstrong")