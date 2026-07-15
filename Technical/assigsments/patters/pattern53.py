
'''
55555
 4__4
  3_3
   22
    1



'''


n= int(input("Enter the number of lines .."))


i=1
k=0
while i<=n:
    print()
    j=1
    while j<=n:
       if j>k:
          if i==1:
             print(i,end="")
          elif j>=2 and j<=n-1:
              if j==n or i == j:
                 print(i,end="")
                 
              else:
                  print("_",end="")
                    
          else:
             print(i,end="") 
                         
       else:
         print(" ",end="") 
         
       j+=1
    k+=1
    i+=1            
     