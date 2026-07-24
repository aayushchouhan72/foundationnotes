'''
1.
Multiplication Table Generator

Scenario:
A school learning app helps students practice multiplication tables.
The user enters a number n, and the system prints multiplication tables from 1 to n using nested loops.

Input:
Enter limit: 3

Output:
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9

'''

start=int(input("Enter the first number :-  "))
end = int(input("Enter the second number :- "))

for i  in range(start,end+1):
        count=1
        for j in range(i,(i*10)+1,i):
               print(f"{i} X {count} = {j}")
        print() 