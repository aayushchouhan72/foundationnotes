# 6.
#  Mobile Recharge System

# A telecom company issues lucky recharge coupons only if the coupon number is prime.

# Task

# Write a recursive function to determine whether a given number is prime.

# Input
# Enter Coupon Number:
# 29
# Output
# Prime Number


n = int(input("Enter The number of months ..."))
m=n
def prime(n):
    if m%n ==  0:
         return "Not prime"
    elif n  == 2 :
          return "Prime"
    return prime(n-1)

if n ==  2 or n<2:
      print("Its prime")
else:
     print(prime(n-1))