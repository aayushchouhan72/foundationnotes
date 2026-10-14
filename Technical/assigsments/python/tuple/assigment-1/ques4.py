
# 4.
# Find common elements in three sorted arrays.
# Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
# Note: can you take care of the duplicates without using any additional Data Structure?
# Example 1:
# Input:
# n1 = 6; A = {1, 5, 10, 20, 40, 80}
# n2 = 5; B = {6, 7, 20, 80, 100}
# n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
# Output: 20 80
# Explanation: 20 and 80 are the only
# common elements in A, B and C.

lis1 =  list(map(str,input("Enter the numbers ...").split(",")))
lis2 =  list(map(str,input("Enter the numbers ...").split(",")))
lis3 =  list(map(str,input("Enter the numbers ...").split(",")))

maxlen = lis1 if len(lis1)>len(lis2) and len(lis1)>len(lis3) else lis2 if len(lis2)>len(lis1) and len(lis2)>len(lis3) else lis3

new=[]
for i in maxlen:
     if i in lis2 and i in lis1 and i in lis3:
           new.append(i)

print(*new)