
'''
55555
 4444
  333
   22
    1



'''


n= int(input("Enter the number of lines .."))


i=1
k=0
l=5
while i<=n:
    print()
    j=1
    
    while j<=n:
       if j>k:
           print(l,end="")   
                              
       else:
         print(" ",end="") 
         
       j+=1
    l-=1
    k+=1
    i+=1            
     thahthee
