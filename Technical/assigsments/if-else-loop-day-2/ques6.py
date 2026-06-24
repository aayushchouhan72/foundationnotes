'''
6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.

Input: 153
Output: Armstrong

'''
num = int(input("Enter number that you went to  check :- "))
temp = num;
check = 0;
              
while num : 
     check += (num%10)**3
     print(check)
     num = num//10

print("it is Armstrong  number " if temp == check else "It is not Armstrong number ")
     