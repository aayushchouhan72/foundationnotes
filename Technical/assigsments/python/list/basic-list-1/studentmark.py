# 1.Student Marks Management
# Create a program to store student marks in a List and perform operations.

# Requirements:

# Add student marks into a List
# Display all marks
# Find highest and lowest marks
# Count students who scored above 75

# Test Cases:

# Input: [45, 67, 89, 90, 76] → Highest = 90, Lowest = 45, Count Above 75 = 3
# Input: [10, 20, 30] → Highest = 30, Lowest = 10, Count Above 75 = 0
# Input: [100, 99, 98] → Highest = 100, Lowest = 98, Count Above 75 = 3


marks =  list(map(int,input("Enter the list ").split()))
marksmax=max(marks)
marksmin=min(marks)
countabove = int(input())
count=0
for  i  in marks:
    if countabove < i:
         count+=1

print(marks,f"max={marksmax}\nmin={marksmin}\ncount above{countabove} is {count}",end="\n")
