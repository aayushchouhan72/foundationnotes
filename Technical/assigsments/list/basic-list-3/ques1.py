
# 1. First Non-Repeating Number
#    ====================================================================

# Scenario

# An online voting system stores vote IDs in a list.

# Find the first vote ID that appears only once.

# Requirements

# * Read N and list elements from user
# * Find the first non-repeating number
# * If no such number exists, display an appropriate message

# Test Case 1

# Input:
# [4, 5, 1, 2, 1, 2, 4]

# Output:
# First Non-Repeating Number = 5

# Test Case 2

# Input:
# [7, 7, 8, 8]

# Output:
# No Non-Repeating Number Found

# ---

lis = list(map(int,input("Enter the number ").split()))
isrepetedfound=False
checklist=[]

for i in lis:
    if i not in checklist:
        if  lis.count(i) == 1:
             print(f"Repeted Character is {i}")
             isrepetedfound=True

             break
        checklist.append(i)

if not isrepetedfound:
    print("Not repeted word in this list...")
