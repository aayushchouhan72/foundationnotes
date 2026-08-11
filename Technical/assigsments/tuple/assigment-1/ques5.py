
# 5.

# Rearrange the array in alternating positive and negative items
# Given an unsorted array Arr of N positive and negative numbers.
# Your task is to create an array of alternate positive and negative numbers
# without changing the relative order of positive and negative numbers.
# Note: Array should start with positive number.

# Example 1:
# Input:
# N = 9
# Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
# Output:
# 9 -2 4 -1 5 -5 0 -3 2
# Example 2:
# Input:
# N = 10
# Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
# Output:
# 5 -5 2 -2 4 -8 7 1 8 0

lis1 =  list(map(int,input("Enter the numbers ...").split(",")))

lis1.sort()

i=0
k=0
j=-1


new=[]

while i<len(lis1):
    if i%2 == 0:
        new.append(lis1[j])
        j-=1
    else:
        new.append(lis1[k])
        k+=1
    i+=1

print(new)
