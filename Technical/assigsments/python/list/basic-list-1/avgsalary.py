
# 2.Employee Salary Processing
# Store employee salaries in a List and calculate details.

# Requirements:

# Store salaries
# Find average salary
# Display salaries greater than average
# Remove salaries below 15000

# Test Cases:

# Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
# Input: [15000, 15000, 15000] → Average = 15000
# Input: [5000, 7000] → Remaining List = []



sal =  list(map(int,input("Enter the list ").split()))
sals=sum(sal)
avgsal =sals/len(sal)
print(avgsal)
for  i  in sal:
    if i >avgsal:
        print(i,end=" ")
