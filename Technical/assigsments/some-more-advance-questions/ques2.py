'''
2. Multi Stage Prime Lock System


A smart locker opens only if final derived number is prime.


Write a program to:


- Find sum of digits

- Find product of digits

- Find difference between product and sum

- Count digits in difference

- Add digit count to difference

- Check whether final result is Prime or Not


Input:

234


Output:

Sum = 9

Product = 24

Difference = 15

Digits = 2

Final Result = 17

Prime


'''
import math
n= int(input("Enter the number :- "))
sum=0
product=1
temp=n
while temp:
      dig=temp%10
      sum+=dig
      product*=dig
      temp=temp//10
diff = product-sum

count=0
hold=diff
while diff:
      count+=1
      diff//=10

final = hold+count

i=2
while i<final//2:
      if final%i:
          print(f"Sum = {sum}\nProduct = {product}\nDifference = {hold}\nDigits = {count}\nFinal Result = {final}\nnot Prime")
          break
      i+=1
else:
    print(f"Sum = {sum}\nProduct = {product}\nDifference = {diff}\nDigits = {count}\nFinal Result = {final}\n Prime")
  
   