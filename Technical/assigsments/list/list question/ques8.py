# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true

 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109


prices = list(map(int,input("enter the list elements ...").split(",")))
m = max(prices)
print(m)
index = prices.index(m)
print(index)
s=prices[index:]
print(s)
mi =  min(s)
print(mi)
if mi>m:
   print( 0)
else:
   print(m-mi)