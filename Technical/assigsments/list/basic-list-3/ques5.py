# ====================================================================
# 5. Equilibrium Index Finder
# ===========================

# Scenario

# Find an index where:

# # Sum of elements on the left side

# Sum of elements on the right side

# Requirements

# * Read N and list elements from user
# * Find equilibrium index
# * If not found, display message

# Test Case 1

# Input:
# [1, 3, 5, 2, 2]

# Output:
# Equilibrium Index = 2

# Explanation:
# 1 + 3 = 2 + 2

# Test Case 2

# Input:
# [1, 2, 3]

# Output:
# No Equilibrium Index Found

# ---
lis = list(map(int,input("Enter the number ").split(",")))
conti=[]
i=1
isequilibriumfound=False
while i <len(lis)-1:
    left=sum(lis[0:i])
    right=sum(lis[i+1:])
    if left ==  right:
         print(f"Equilibrium Index = {i}")
         isequilibriumfound=True
         break
    i+=1
if not isequilibriumfound:
      print("No Equilibrium Index Found")
    

    

