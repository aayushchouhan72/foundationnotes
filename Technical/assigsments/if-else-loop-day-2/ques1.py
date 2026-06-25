'''
1. Sum of First N Natural Numbers
A teacher wants to reward students by giving points daily. On day 1, a student gets 1 point, day 2 → 2 points, and so on. This follows a natural number sequence.
Write a program to calculate the *total points earned after n days* by summing all natural numbers up to n using loops.

Input: n = 10
Output: Total Points = 55

'''


n = int(input("Enter number of term you went to add :- "))

print("by for loop")
sum  =  0;
for i in  range(1,n+1):
       sum+=i;
print(f"sum of values up to {n} is {sum}")

print("By while loop")

Sum=0
i=1
while i<=n:
       Sum=Sum+i
       i=i+1
print("some of 10 natural number is ",Sum)
