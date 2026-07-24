'''
9.
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number
'''
import math
n = int(input("Enter the number :- "))
m=n//10
len =  len(str(n))-1
sum=0
max=0
difs=""
num=0

while len:
      nd = n%10 
      md = m%10
      dif = abs(md-nd)
      sum +=dif
      if max<dif:
          max=dif
      num=dif+num*10
      difs =str(dif)+" "+difs
      m//=10
      n//=10
      len-=1;



if num%(len+1):
        print(f"Step Differences:{difs}\nSum:{sum}\nLargest:{max}\nBalanced Number")
else:
    print(f"Step Differences:{difs}\nSum:{sum}\nLargest:{max}\n Unbalanced Number")

    
    
      

