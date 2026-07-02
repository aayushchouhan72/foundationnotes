'''
2.
Perfect Number Analyzer

A mathematics research system analyzes special numbers within a given range.
The user enters a starting number and ending number.
The system checks every number in that range and displays all Perfect Numbers using nested loops.

(A Perfect Number is a number whose sum of proper divisors is equal to the number itself.)

Input:
Enter starting number: 1
Enter ending number: 1000

Output:
Perfect Numbers are:
6
28
496

'''

start=int(input("Enter the first number :-  "))
end = int(input("Enter the second number :- "))

for i  in range(start,end+1):
        sum=0
        lent = len(str(i))
        for j in range(1,i//2+1):
               if i%j ==0 :
                 sum+=j
        if sum == i:
               print(sum,end=" ")
         
         