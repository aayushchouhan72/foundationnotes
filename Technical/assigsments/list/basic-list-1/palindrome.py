# 4.
# Palindrome Number List Checker
# Scenario

# A system checks lucky numbers which are palindromes.

# Requirements
# Check palindrome numbers
# Store palindrome numbers in list
# Count palindrome numbers
# Find largest palindrome
# Sort palindrome list
# Test Cases

# Input:
# [121, 131, 20, 44, 55, 100]

# Output:

# Palindromes: [121, 131, 44, 55]
# Count: 4
# Largest: 131
# Sorted: [44, 55, 121, 131]

nums=  list(map(int,input("Enter the list ").split()))
pal=[]
count=0
largest=0
for i in nums:
    if str(i)[::-1] == str(i):
        if largest < i :
            largest=i
        count+=1
        pal.append(i)

sort = sorted(pal)
print(f"# Palindromes: {pal}\nCount: {count}\nLargest: {largest}\nSorted:{sort}")


