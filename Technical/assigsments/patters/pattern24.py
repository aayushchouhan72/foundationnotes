'''
*
**
*@*
*@@*
* * * * *


'''


n= int(input("Enter the number of lines .."))

i=1
flag=True
var=97
while i<=n:
     j=1
     print()
     while j<=i and flag:
          print("*",end="")
          
          j+=1
     j=1
     while i>2 and i<n and j<=i:
     
          if j==1 or j==i:
             print("*",end="")
            
          else:
             print("@",end="")
            
          j+=1
     j=1
     while i==n and j<=i:
           print("*",end=" ")
          
           j+=1

     if i == 2:
         flag=False    
     i+=1

