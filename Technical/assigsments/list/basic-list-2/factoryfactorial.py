
# 7.
# Factory Production – Factorial Expansion List

# Problem Statement

# A factory produces items where production capacity is defined using factorial growth.

# Given a list of numbers, replace each number with its factorial value.

# Then perform analysis on the resulting list.

# Tasks:

# Convert each element to factorial
# Find sum of all factorial values
# Find maximum factorial value
# Count how many factorial values are even

# Input:
# A list of integers

# Example 1

# Input:
# [3, 4, 5]

# Processing:
# 3! = 6
# 4! = 24
# 5! = 120

# Output:
# [6, 24, 120]
# Sum = 150
# Max = 120
# Even Count = 3



nums = list(map(int, input("Enter the numbers: ").split()))

faclist=[]
count=0
for  i in nums:
    j=1
    fac=1
    while j<=i:
         fac*=j
       
         j+=1
    faclist.append(fac)
    if fac%2 == 0:
          count+=1

print(f"{faclist}\nSum ={sum(faclist)}\nMax={max(faclist)}\nEven Count ={count}")
     

          