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
lis.sort()
conti=[]
count=0
i=1
while i <len(lis):
    if ( lis[i]-lis[i-1] ) == 1:
         conti.append(lis[i])
    i+=1

print(len(conti)+1)


    
