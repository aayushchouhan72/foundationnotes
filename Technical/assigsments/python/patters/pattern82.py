'''
    1
   212
  32123
 4321234
543212345


'''
n= int(input("Enter the number of lines .."))

i=1
m=1
while i<=n:
    j=1
    k=i+1
    print()
    while j<=n-i:
       print(" ",end="")
       j+=1
    j=1
    while j<=m:
       if j<=i:
          k-=1
          print(k,end="")
          
       else:
           k+=1 
           print(k,end="")
 
           
       j+=1 
    m+=2      
    i+=1