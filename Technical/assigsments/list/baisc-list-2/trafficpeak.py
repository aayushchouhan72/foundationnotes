'''

2.
Smart City Traffic Peak Load Analyzer

Problem Statement

A smart city monitors traffic density at different time intervals in a day.

An element is called a peak traffic point if it is greater than or equal to its adjacent elements.

You are given an array traffic[] of size N.

Tasks:

Find all peak elements
Calculate the sum of all peak traffic values
Find the product of all peak traffic values
Return the maximum peak value

Note:
If only one element exists, it is the only peak.

Test Case 1

Input:
traffic = [10, 50, 30, 70, 60, 90, 80]

Output:
Peaks = [50, 70, 90]
Sum = 210
Product = 315000
Max Peak = 90

Test Case 2

Input:
traffic = [100, 200, 150, 180, 170]

Output:
Peaks = [200, 180]
Sum = 380
Product = 36000
Max Peak = 200

Test Case 3

Input:
traffic = [5]

Output:
Peaks = [5]
Sum = 5
Product = 5
Max Peak = 5

'''

nums = list(map(int, input("Enter the numbers: ").split()))

peaks = []

for i in range(len(nums)):
    if i == 0:
        if nums[i] > nums[i + 1]:
            peaks.append(nums[i])

    elif i == len(nums) - 1:
        peaks.append(nums[i])

    else:
        if nums[i] > nums[i + 1] and nums[i] > nums[i - 1]:
            peaks.append(nums[i])

product = 1
sum = 0
maxpeak = 0

for i in peaks:
    product *= i
    sum += i
    if maxpeak < i:
        maxpeak = i

print(f"peaks = {peaks}")
print(f"sum = {sum}")
print(f"product = {product}")
print(f"maxpeak = {maxpeak}")