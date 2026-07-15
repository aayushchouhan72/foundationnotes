'''
11111
 2222
  333
   44
    5




'''


n= int(input("Enter the number of lines .."))


i=1
k=0
while i<=n:
    print()
    j=1
    ch=65
    while j<=n:
       if j>k:
         print(i,end="")                         
       else:
         print(" ",end="") 
         
       j+=1
    k+=1
    i+=1            
     