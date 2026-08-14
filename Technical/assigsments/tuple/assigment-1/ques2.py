
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
        for k in j:
             if k  in i:
                 print('hiiii')
                 break
        else:
            tup.append((i,j))
       
 
              
         
print(tup)

