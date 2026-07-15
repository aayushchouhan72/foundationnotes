
'''
5
54
543
5432
54321



'''


n= int(input("Enter the number of lines .."))

i=1
flag=True
while i<=n:
     j=1
     var=5
     print()
     while j<=i and flag:
          print(var,end="")
          var-=1
          j+=1
     j=1
     while i>2 and i<n and j<=i:
     
          if j==1 or j==i:
             print(var,end="")
             var-=1
            
          else:
             print(var,end="")
             var-=1
            
          j+=1
     j=1
     while i==n and j<=i:
           print(var,end="")
           var-=1
           j+=1

     if i == 2:
         flag=False    
     i+=1



