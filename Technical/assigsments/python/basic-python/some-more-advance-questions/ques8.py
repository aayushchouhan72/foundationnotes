'''
8.

 ATM Note Counter


A bank ATM dispenses ₹100 notes.


Write a program to:


- Read withdrawal amount

- Count how many ₹100 notes needed using loop


Input:

700


Output:

Notes = 7

'''

n= int(input("Enter the number "))

if n%100 == 0:
    i=1
    while True:
       if i*100 == n:
           print(f"There is {i} notes of 100 are required..")
           break
       else:
         i+=1
else:
    print("Plz Enter the multiple of 100")