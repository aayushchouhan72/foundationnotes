# ====================================================================
# 4. Longest Consecutive Sequence
# ===============================

# Scenario

# Find the longest sequence of consecutive numbers present in the list.

# Requirements

# * Read N and list elements from user
# * Find the length of the longest consecutive sequence
# * Display the sequence length

# Test Case 1

# Input:
# [100, 4, 200, 1, 3, 2]

# Output:
# Longest Consecutive Length = 4

# Explanation:
# Sequence = 1, 2, 3, 4

# Test Case 2

# Input:
# [10, 11, 12, 20]

# Output:
# Longest Consecutive Length = 3

# ---
lis = list(map(int,input("Enter the number ").split(",")))
lis=lis.sort()
count=0
first=lis[0]-1
for i in range(len(lis)):
    if  lis[i] == first[i]+1:
        count+=1
    else:
        break
    
