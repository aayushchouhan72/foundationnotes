'''
9.

 Bike Service Kilometer Checker


A bike needs service every 3000 km.


Write a program to:


- Read travelled kilometers

- Print every service checkpoint till entered km


Input:

10000


Output:

3000 6000 9000

'''

n= int(input("Enter the distance you went to travel:- "))
count=3000
while count<n:
      print(count, end=" ")
      count+=3000
