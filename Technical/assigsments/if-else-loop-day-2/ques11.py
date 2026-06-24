'''
11. Count Occurrence of a Digit*
A system logs repeated digits in a number for pattern analysis and reporting.
Write a program to *count how many times a given digit appears in a number using loops*.

Input: Number = 122312, Digit = 2
Output: 3

'''

num = input("Enter number :- ")
dig =  int(input("Enter number you went to check :- "))

count = 0;
for i in num:
    i = int(i)
    if i==dig:
       count+=1
print(f"The number {dig}  aapair {count} times in the number ")