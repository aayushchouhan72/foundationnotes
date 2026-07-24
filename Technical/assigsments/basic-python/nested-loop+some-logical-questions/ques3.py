'''
Fibonacci Population Growth Tracker

A wildlife research team is studying the growth of a rare species.  
They observe that the population follows a Fibonacci pattern:

- Month 1 → 0 animals  
- Month 2 → 1 animal  
- Every next month → sum of previous two months  

The researchers want to analyze the growth pattern.

Write a program to:

- Read number of months n
- Generate Fibonacci series up to n months using loop
- Print population for each month
- Find total population observed
- Count how many months population exceeded 5

Input:
8

Output:
Population Growth:
0 1 1 2 3 5 8 13

Total Population = 33
Months with Population > 5 = 2

'''

end = int(input("Enter the number of month"))

a=0
b=1
sum=0
gerter5=0
for _ in range(end):
       sum +=a
       print(a,end=" ")
       if a>5:
          gerter5+=1
       c=a+b
       a=b
       b=c
       
print(f"Total Population ={sum} \nMonths with Population > 5 = {gerter5}")