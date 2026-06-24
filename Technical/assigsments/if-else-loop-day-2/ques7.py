'''

*7. Count Even Digits*
A data analyst is analyzing numeric IDs and needs to determine how many digits in the ID are even.
Write a program to *count the number of even digits in a given number using loops*.

Input: 123456
Output: Even digits count = 3


'''


num = input("Enter number :- ")
count=0;
for i in num :
    i = int(i)
    if i%2==0:
       count+=1

print(f"Number of even digit in number is {count}")
