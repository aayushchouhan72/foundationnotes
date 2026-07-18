'''
***** *****
****   ****
***     ***
**       **
*         *
*         *
**       **
***     ***
****   ****
***** *****
'''

n= int(input("enter the number lines ..."))

i=1
m=n*2+1
l=6
k=0
while i<=n:
     print()
     j=1
     while j<=m:
        if j>=l-k and j<=l+k:
             print(" ",end="")
        else:
            print("*",end="")
        j+=1
     
     k+=1
     i+=1
i=1
l=n*2+1
k=n*2+1

while i<=n:
     print()
     j=1
     while j<=k:
         if j>i and j<l:
              print(" ",end="")
         else:
              print("*",end="")
         j+=1
     l-=1
     i+=1