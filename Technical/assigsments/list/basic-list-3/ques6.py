# # ====================================================================
# 6. Product Except Self
# ======================

# Scenario

# For every element, calculate the product of all other elements except itself.

# Requirements

# * Read N and list elements from user
# * Create a new list containing products
# * Display the result

# Test Case 1

# Input:
# [1, 2, 3, 4]

# Output:
# [24, 12, 8, 6]

# Test Case 2

# Input:
# [2, 3, 5]

# Output:
# [15, 10, 6]

lis = list(map(int,input("Enter the number ").split(",")))
i=0
empty=[]

while i <len(lis):
    product=1
    print(product) 
    j=0
    while j<len(lis):
         if j == i:
              pass
         else:
              product*=lis[j]
         j+=1
    empty.append(product)    
    i+=1

print(empty)
