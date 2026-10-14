
# ====================================================================
# 10. Find Duplicate Numbers
# ==========================

# Scenario

# A company stores employee IDs in a list. Some IDs may appear more than once due to data entry errors.

# Requirements

# * Read N and list elements from user
# * Find all duplicate numbers
# * Store duplicates in another list
# * Count total duplicate numbers
# * Display duplicates in sorted order

# Test Case 1

# Input:
# [1, 2, 3, 2, 4, 5, 1]

# Output:
# Duplicate Numbers = [1, 2]
# Count = 2

# Test Case 2

# Input:
# [10, 20, 30]

lis = list(map(int,input("Enter the number ").split(",")))
visted =[]
repeted =[]

for i in lis:
    if i not in visted:
         visted.append(i)
    else:
         repeted.append(i)

if repeted:
    print("This are the repeted character in this list ",repeted)
else:
      print("Not repeted character in  the given list ..")
