'''
4. Reverse a Number
A security system stores OTP codes in reverse format for encryption to increase data safety. Reversing a number means extracting digits and rebuilding it in reverse order.
Write a program to *reverse a given integer using loops*.

Input: 1234
Output: 4321

'''


n = input("Enter your number")
rev = ""
for i in n:
    rev= i+rev

print(rev)