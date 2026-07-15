'''
1
12
1 3
1  4
12345


'''

n= int(input("Enter the number of lines .."))

i=1
while i<=n:
     j=1
     print()
     var=1
     while j<=n and i<=n-1:
         if i == j or j==1:
            print(var,end="")
            var+=1
         else:
            print(" ",end="")
            var+=1
         j+=1
     k=i
     j=1
     while  j<=i and  k == n:
           print(var,end="")
           var+=1
           j+=1
         
     i+=1


