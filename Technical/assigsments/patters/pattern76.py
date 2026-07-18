'''
1
12
123
1234
123
12
1

  j=1
     l=1
     while j<n:
         if j>i:
            print(l,end="")
         else:
            print(" ",end="") 
         l+=1
         j+=1           
     



'''

n= int(input("Enter the number of lines .."))
i=2
m=n*2-1
k=n
print()
while i<=m:
     print()
     if i == 1 :
          print()
     elif i == n*2:
          print()
          break
     else:
         if i<n:
             j=1
             l=5
             while j<=n:
                if j>=l:
                   print("x",end="")
                else:
                   print(" ",end="")
                l-=1
                j+=1
     i+=1


