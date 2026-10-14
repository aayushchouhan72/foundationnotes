'''

7.

 Alternate Digit Prime Checker


A math lab adds alternate digits from right side.


Write a program to:


- Find sum of alternate digits

- Check whether sum is Prime or Not


Input:

12345


Output:

Alternate Sum = 9

Not Prime

'''

n= int(input("Enter the number :- "))
it =True
sum=0

while n:
    dig =n%10
    if it:
       sum+=dig
       it = False
    else:
       it =True 
    n//=10
m=sum
i=2
count =0
while i<m:
     if m%i == 0:
          count+=1
          break
     i+=1
else:
  print(f"Alternate digit sum number {sum} is prime number :- ")

if count:
   print(f"Alternate digit sum number {sum} is not prime number :- ")

