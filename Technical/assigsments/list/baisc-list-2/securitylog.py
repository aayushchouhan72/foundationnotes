
# 6.

# A security system logs employee entry IDs during a day.

# Only prime-numbered IDs are considered valid VIP entries.

# Tasks:

# Extract all prime IDs from the list
# Find the sum of prime IDs
# Find the maximum prime ID
# Count how many prime entries exist

# Input:
# A list of integers (may contain duplicates and non-prime numbers)

# Example 1

# Input:
# [12, 5, 7, 9, 11, 14, 17]

# Output:
# Prime IDs = [5, 7, 11, 17]
# Sum = 40
# Max = 17
# Count = 4

# Example 2

# Input:
# [4, 6, 8, 10]

# Output:
# Prime IDs = []
# Sum = 0
# Max = -1
# Count = 0


nums = list(map(int, input("Enter the numbers: ").split()))
sum=0
max=0
count=0
prime= []

for i in range(len(nums)):
            for j in range(2,nums[i]//2):
                    if nums[i]%j == 0:
                            break
            else:
                    prime.append(nums[i])
                    if max<nums[i]:
                            max=nums[i]
                    sum+=nums[i]
                    count+=1

print(f"Prime IDs = {prime}\nSum = {sum}\nMax = {max}\nCount = {count}")

