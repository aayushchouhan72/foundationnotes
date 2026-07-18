'''

***** *****
****   ****
***     ***
**       **
*         *



'''
n= int(input("Enter the number of lines .."))

i=1
l=n*2-1
m=n
p=n
k=i
o=0
while i<=n:
     print()
     j=1
     while j<=m:
         print("*",end="")
         j+=1
     j=1
     while j<=i:
          print("+",end="")
          j+=1 
     while j<=p:
          if j>=i-o:
            print("*",end="")
          else:
             print(" ",end="")
          j+=1
     o+=1
     p-=1
     m-=1
     i+=1