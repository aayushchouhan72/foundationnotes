'''
9.Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime
'''
import math
n =int(input("Enter the number :- "))
oddc=0
evenc=0
while n:
   dig = n%10
   if dig %2 ==0:
        evenc+=1
   else:
        oddc+=1
   n=n//10

dif = abs(oddc-evenc)

sum=dif 
i=2
st=True
if sum>2:     
   while i<=sum//2:
       if sum == 0:
            break
       elif  sum%i==0:
          break
       i+=1
   else:
      print(f"Even count={evenc}\nodd count={oddc}\ndiffrence={dif}\nPrime number")
      st=False

   if st: 
      print(f"Even count={evenc}\nodd count={oddc}\ndiffrence={dif}\nNot Prime number")
else:
    print(f"Even count={evenc}\nodd count={oddc}\ndiffrence={dif}\nNot Prime number")     
  
