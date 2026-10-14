'''

***** *****
****   ****
***     ***
**       **
*         *



'''
n= int(input("Enter the number of lines .."))

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