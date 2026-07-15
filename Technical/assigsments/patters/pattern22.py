'''
A
AB
A C
A  D
ABCDE

'''


n= int(input("Enter the number of lines .."))

i=1
flag=True
while i<=n:
     j=1
     print()
     var=65
     while j<=i and flag:
          print(chr(var),end="")
          var+=1
          j+=1
     j=1
     while i>2 and i<n and j<=i:
     
          if j==1 or j==i:
             print(chr(var),end="")
             var+=1
          else:
             print(" ",end="")
             var+=1
          j+=1
     j=1
     while i==n and j<=i:
           print(chr(var),end="")
           var+=1
           j+=1

     if i == 2:
         flag=False    
     i+=1


