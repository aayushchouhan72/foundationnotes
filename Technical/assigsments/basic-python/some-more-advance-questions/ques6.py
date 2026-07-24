'''
6.

Next Prime Cabin Number Generator


A luxury hotel gives only prime numbered cabins to VIP guests.


Manager enters the last allotted cabin number.

System must find the next available prime cabin number.


Write a program using loops.


Input:

24


Output:

Next Prime Cabin = 29



'''
n= int(input("Enter the number :- "))

m=n+1

while True:
     i=2
     while i<m:
         if m%i == 0:
             break
         i+=1
     else:
        print(f"Next prime number is {m}")
        break
     m+=1

   
