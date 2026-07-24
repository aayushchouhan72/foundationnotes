'''
10.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime
'''
n=int(input("Enter the number: "))

temp=n
zerocount=0
digitsum=0
smallest=9

while temp>0:
    digit=temp%10
    digitsum+=digit

    if digit==0:
        zerocount+=1

    if digit<smallest:
        smallest=digit

    temp//=10

final=(zerocount+digitsum)*smallest

print("Zero Count =",zerocount)
print("Sum =",digitsum)
print("Smallest Digit =",smallest)
print("Final Result =",final)

if final<2:
    print("Not Prime")
else:
    i=2
    while i<=final//2:
        if final%i==0:
            print("Not Prime")
            break
        i+=1
    else:
        print("Prime")