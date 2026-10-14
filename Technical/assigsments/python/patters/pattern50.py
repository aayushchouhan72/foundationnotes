
'''
12345
 1234
  123
   12
    1


'''


n= int(input("Enter the number of lines .."))


i=1
k=0
while i<=n:
    print()
    j=1
    l=1
    while j<=n:
       if j>k:
           print(l,end="")   
           l+=1                    
       else:
         print(" ",end="") 
         
       j+=1
    k+=1
    i+=1            
     