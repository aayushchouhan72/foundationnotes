
# Code
# Testcase
# Testcase
# Test Result
# 67. Add Binary
# Easy
# Topics
# premium lock icon
# Companies
# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

a= input("Enter the first binary number ..")
b = input("Enter the second binary number ..")

anum =0
pow=0
i=-1
while i>-len(a)+1:
       anum+=int(a[i])*2**pow
       print(anum)
       pow+=1
       i-=1
print(anum)
     