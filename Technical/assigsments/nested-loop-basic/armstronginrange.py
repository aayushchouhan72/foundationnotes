'''
4.
Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407

'''
import math
start=int(input("Enter the first number :-  "))
end = int(input("Enter the second number :- "))

for i  in range(start,end+1):
             lent= len(str(i))
             sum=0
             num=i
             for j in range(3):
                  dig = num%10
                  sum=sum+(dig**3)
                  num//=10 
                 
             if sum == i :
                   print(sum)
