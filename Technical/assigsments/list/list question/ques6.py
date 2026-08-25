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

a=input("Enter the first binary number ....")
b=input("Enter the second binary number ....")

ad=0
j=-1
for i in range(len(a)):
    ad+=(2**int(i))*int(a[j])
    j-=1

bd=0
j=-1
for i in range(len(b)):
    bd+=(2**int(i))*int(b[j])
    j-=1


print(bin(ad+bd))