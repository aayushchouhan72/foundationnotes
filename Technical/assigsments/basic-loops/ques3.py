'''
3. First Digit of Number
A university receives thousands of application IDs. The first digit of each ID represents the department code, so the admission software must read the first digit quickly.
Write a program to find the first digit of a number using loops.

Input:
53892

Output:
First Digit = 5

'''


num = int(input("Enter the number .."))
while num :
      res = num%10
      num=  num//10
print("First digit of number is ..",num)
     