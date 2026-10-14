'''
57    
       X 
      X X 
     X___X
    X_____X
   X X X X X





'''

n= int(input("Enter n"))
i = 1


while i<=n:
    j=1
    print()
    while j<n-i:
        print(" ",end="")
        j+=1
    j=1

    while j<=i:
          if i == 1 and j==1 :
             print("x",end=" ")
          elif i==2 and j<=2:
               print("X",end=" ")
          elif i>2 and i<=n-1:
               if j==1 or  j==i:
                   print("X",end="")
               else:
                   print("_",end="_")
          else:
              print("X",end=" ")
               
          j+=1
        
    i+=1