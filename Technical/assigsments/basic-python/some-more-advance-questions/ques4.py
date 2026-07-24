'''
.Unique Digit Security Scanner


A smart locker accepts only numbers whose all digits are unique.


Write a program using for-else loop to:


- Check every digit

- If any repeated digit found reject

- Else accept


Input:

57294


Output:

Valid Unique Code
'''
n=int(input("Enter number .."))
temp = str(n)
seen=""

for i in temp:
    if i in seen:
        print("Given number is not unique..")
        break
    else:
        seen+=i
else:
    print("Given number is unique ..")
               






















