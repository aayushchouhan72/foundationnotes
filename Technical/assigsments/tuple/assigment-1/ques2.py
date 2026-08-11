
# 2.
# Secure Password Analysis

# A cybersecurity team wants to identify pairs of passwords having no common characters.

# Problem Statement:

# Given N strings, count the number of pairs that do not share any common character.

# Example:

# Input

# N = 4
# passwords[] = {"abc", "de", "fg", "ad"}

# Output

# 3

# Explanation

# ("abc","de")
# ("abc","fg")
# ("de","fg")


lis =  list(map(str,input("Enter the numbers ...").split(",")))
tup=[]
for i in lis:
    for j in lis:
         if i == j:
            continue
         k=0
         first=""
         second=""
         while k<len(i) and k<len(j):
             if i[k] not in  second and j[k] not in first:
                 first+=i[k]
                 second+=j[k]
                 
 
              
         
print(tup)

