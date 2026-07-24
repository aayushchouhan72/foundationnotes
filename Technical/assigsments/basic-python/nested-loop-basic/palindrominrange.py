'''
6.
Palindrome Number Range Checker

A barcode verification system checks for palindrome numbers within a specific range.
The user enters starting and ending numbers.
The system displays all palindrome numbers using nested loops.

Input:
Enter starting number: 100
Enter ending number: 200

Output:
Palindrome Numbers are:
101
111
121
131
141
151
161
171
181
191
'''

start=int(input("Enter the first number :-  "))
end = int(input("Enter the second number :- "))

for i  in range(start,end+1):
             rev=0
             num=i
             lent=len(str(i))
             for j in range(lent):
                  dig = num%10
                  rev=dig+rev*10
                  num//=10 
                 
             if rev == i :
                   print(rev)
