
# 3.
# Industrial Sensor Peak Energy Monitoring System

# Problem Statement

# A factory machine records energy consumption at regular intervals.

# A peak is defined as a value greater than or equal to its neighbors.

# Tasks:

# Find all peak energy values
# Compute sum of squares of peak values
# Compute average of peak values
# Return difference between max peak and min peak
# If no peaks, return -1

# Test Case 1

# Input:
# energy = [20, 40, 30, 60, 50]

# Output:
# Peaks = [40, 60]
# Sum of squares = 5200
# Average = 50
# Difference = 20

# Test Case 2

# Input:
# energy = [10, 20, 15, 25, 20, 30]

# Output:
# Peaks = [20, 25, 30]
# Sum of squares = 1525
# Average = 25
# Difference = 10

# Test Case 3

# Input:
# energy = [5]

# Output:
# Peaks = [5]
# Sum of squares = 25
# Average = 5
# Difference = 0

nums = list(map(int, input("Enter the numbers: ").split()))

peaks = []

for i in range(len(nums)):
    if i == 0:
        if nums[i] > nums[i + 1]:
            peaks.append(nums[i])

    elif i == len(nums) - 1:
        if nums[i]>nums[i-1]:
             peaks.append(nums[i])

    else:
        if nums[i] > nums[i + 1] and nums[i] > nums[i - 1]:
            peaks.append(nums[i])

product = 1
sumsqrs = 0
sum=0
maxpeak = 0
diff = max(peaks)-min(peaks)

for i in peaks:
    product *= i
    sum+=i
    sumsqrs+= i**2
    if maxpeak < i:
        maxpeak = i
print(max(peaks),min(peaks))
print(f"peaks = {peaks}")
print(f"sum of squares = {sumsqrs}")
print(f"Average = {int(sum/len(peaks))}")
print(f"Difffrence= {diff}")