'''
   *
  ***
 ***** 
******* 
 ***** 
  *** 
   *


'''

n = int(input("Enter the number of lines: "))
k=1
m=1
l=((n*2)-1)-2
for i in range(1,(n*2)+1):
       print()
       if i<=n:
            j=1
            while j<=n-i:
                  print(" ",end="")
                  j+=1
            j=1
            while j<=m:
                 if j%2 == 0:
                      print("*",end="")
                 else:
                      print("*",end="")
                 j+=1                   
            m+=2
       else:
            j=1
            while j<=k:
                  print(" ",end="")
                  j+=1
                 
            j=1
            while j<=l:
                 if j%2 == 0:
                      print("*",end="")
                 else:
                      print("*",end="")
                 j+=1 
            l-=2                  
            m-=2
            k+=1
           