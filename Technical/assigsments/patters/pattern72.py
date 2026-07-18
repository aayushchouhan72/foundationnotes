'''
123456789
 1     7
  1   5
   1 3
    1


'''

n= int(input("Enter the number of lines .."))
i=1
m=n*2-1
while i<=n:
    j=1
    while j<=i-1:
        print(" ",end="")
        j+=1
    j=1
    while j<=m:
         if i == 1:
             print(j,end="")
         elif j==1 or j==m:
             print(j,end="")
         else:
             print(" ",end="")
         j+=1
    m-=2    
    print()
    i+=1


