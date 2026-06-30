'''5.Number Stability Analyzer


A science lab studies whether digits are in increasing order.


Write a program using for-else loop:


- If every next digit is greater than previous print Stable Number

- Else Unstable Number


Input:

12359


Output:

Stable Number
'''

n = int(input("Enter the your number .."))
m=n//10
st=False



while m:
     d1= m%10
     d2=n%10  
     if d1<d2:
       pass
     else:
        print("Given number is not stable number ..")
        break
     n//=10
     m//=10
else:
      print("Given number is strong number ..")   
