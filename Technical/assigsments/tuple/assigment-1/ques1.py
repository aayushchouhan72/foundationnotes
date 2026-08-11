# 1. Count Pairs with Difference K

# A company records the ages of employees. Find how many pairs of employees have an age difference exactly equal to K.

# Problem Statement:

# Given an array of employee ages and an integer K, count the number of pairs whose absolute difference is K.

# Example:

# Input:

# N = 5
# K = 2
# ages[] = {1, 5, 3, 4, 2}

# Output:

# 3

# Explanation:

# (1,3), (3,5), (2,4)
import math 
lis =  list(map(int,input("Enter the numbers ...").split(",")))
# lis =  lis.sort()
dif = int(input("Enter the diffrence ..."))
tup=[]
for i in lis:
    for j in lis:
         if i == j:
            continue
         if int(math.fabs(i-j)) == dif:
            tup.append((i,j))
print(*tup)
    
             


