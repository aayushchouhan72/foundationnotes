# ====================================================================
# 8. Majority Element Detector
# ============================

# Scenario

# Find an element occurring more than N/2 times.

# Requirements

# * Read N and list elements from user
# * Find majority element
# * If not present, display appropriate message

# Test Case 1

# Input:
# [2, 2, 1, 2, 3, 2, 2]

# Output:
# Majority Element = 2

# Test Case 2

# Input:
# [1, 2, 3, 4]

# Output:
# No Majority Element Found

# ---

lis = list(map(int,input("Enter the number ...").split(",")))

for i in lis:
    if lis.count(i) > len(lis)/2:
         print("Majority Element = ",i)
         break
else:
    print("Not majority element in the list ...")