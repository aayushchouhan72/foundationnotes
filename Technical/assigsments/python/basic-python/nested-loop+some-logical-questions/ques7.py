'''
7.
Adam Number Verification System – Question

A high-security digital system is designed to validate special mirrored numbers known as Adam Numbers before granting access to sensitive data.

When a user enters a numeric code, the system performs a dual verification process:

* It calculates the square of the entered number.
* It reverses the number and calculates the square of the reversed value.
* Finally, it checks whether both results are mirror images (reverses) of each other.

A number is called an Adam Number if:
The square of the number and the square of its reverse are reverses of each other.

Task:
Write a Python program to check whether a given number is an Adam Number or not.

Examples:

Input:
12
Output:
Adam Number

Input:
13
Output:
Not an Adam Number

Input:
11
Output:
Adam Number

Example:
12 → 12² = 144, reverse(12) = 21 → 21² = 441 → reverse of 144
'''

n= int(input("Enter the number .. "))
temp=n
ensqr= str(n**2)

revnum=0

while temp:
     dig = temp%10
     revnum = dig + revnum*10
     temp//=10

revsqr = str(revnum**2)

if len(revsqr) == len(ensqr):
         j=len(revsqr)-1
         for i in range(j+1):
             if revsqr[i]!=ensqr[j-i]:
                      print("Not an Adam number ...")
                      break
         else:
             print("Given number is an Adam nuber ...")  
else:
    print("Not an Adam number ...")
                      




