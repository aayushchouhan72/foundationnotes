'''
8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime

'''

n= int(input("Enter the number :- "))
max=0
min=9
sum=0

while n:
    dig = n%10
    if dig >max:
         max=dig
    if dig <min:
          min=dig
    sum +=dig
    n=n//10
i=2
st=True
while i<=sum//2:
       if sum%i==0:
          break
       i+=1
else:
    print(f"Largest={max}\nSmallest={min}\nSum={sum}\nPrime number")
    st=False

if st:
   print(f"Largest={max}\nSmallest={min}\nSum={sum}\n not Prime number")

     
  