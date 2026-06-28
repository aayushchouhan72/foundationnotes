'''
3. Display Numbers Ending with 5

A supermarket tracks token numbers ending in 5.
Write a program using loops to display numbers ending with 5 between two numbers.

Input:
10 40

Output:
15 25 35

'''


n = int(input("Enter the first number :- "))
m= int(input("Enter the second number :- "))


while n<=m:
       if n%5==0 and n%10!=0:
          print(n,end=" ")
       n+=1
