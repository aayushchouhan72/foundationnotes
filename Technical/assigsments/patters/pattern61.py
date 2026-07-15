'''
    *
   ***
  *****
 *******
*********
'''







n= int(input("Enter the number of lines .."))

i=0
k=1
while i<n:
    j=1
    print()
    while j<n-i:
        print(" ",end="")
        j+=1
    j=1
    while j<=k:
        print("*",end="")
        j+=1
    k+=2
    i+=1