'''

5.
Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code
'''

st = input("Enter your number ...").lower()
revst=st[::-1]
if st == revst:
     print("Entred number is  palindrom number ...")
else:
      print("Entred number is not palindrom number ..")