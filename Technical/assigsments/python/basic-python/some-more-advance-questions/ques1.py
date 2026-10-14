'''
1. Triple Operation Prime Verification System


A cybersecurity company generates a security score from entered access code.


Write a program to:


- Find sum of digits of the number

- Reverse the number

- Find absolute difference between original number and reverse

- Add digit sum and difference

- Check whether final result is Prime or Not Prime


Input:

4215


Output:

Sum of Digits = 12

Reverse = 5124

Difference = 909

Final Result = 921

Not Prime


'''
import math
n= int(input("Enter the number :- "))
hold=n
sum = 0
while hold:
    dig= hold%10
    sum+=dig 
    hold=hold//10

rev=0
temp=n
while temp:
     rev =temp%10+rev*10
     temp=temp//10

diff = abs(rev-n)

final= sum+diff
i=2
while i<final//2:
      if final%i:
          print(f"Sum = {sum}\nReverse = {rev}\nDifference = {diff}\nFinal Result = {final}\nnot Prime")
          break
      i+=1
else:
    print(f"Digite Sum = {sum}\nReverse = {rev}\nDifference = {diff}\nFinal Result = {final}\n Prime")
  
   
      

