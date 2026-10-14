'''
1
12
123
1234
123
12
1

'''

n= int(input("Enter the number of lines .."))
i=1
m=n*2-2
k=m//2
print()
while i<=m:
     print()
     if i<=m//2:
          j=1
          while j<=i:
               print(j,end="")
               j+=1
     else:
          j=1
          while j<k:
               print(j,end="")
               j+=1
          k-=1
     i+=1


