'''
*********
 ******* 
  ***** 
   ***
    * 

'''

n= int(input("Enter the number of lines .."))
m=n*2-1
i=1
while i<=n:
    print()
    j=1
    while j<=i-1:
        print(" ",end="")
        j+=1
    j=1
    while j<=m:
         print("*",end="")
         j+=1
    m-=2
    i+=1
