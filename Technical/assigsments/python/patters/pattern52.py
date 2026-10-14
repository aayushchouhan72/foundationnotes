
'''
12345
 1__4
  1_3
   12
    1


'''


n= int(input("Enter the number of lines .."))


i=1
k=0
flag=False
while i<=n:
    print()
    j=1
    l=1
    while j<=n:
       if j>k:
          if i==1:
             print(l,end="")
             l+=1
             flag=True
          elif j>=2 and j<=n-1 and flag:
              if j==n or i == j:
                 print(l,end="")
                 l+=1
              else:
                  print("_",end="")
                  l+=1  
          else:
             print(l,end="") 
             l+=1               
       else:
         print(" ",end="") 
         
       j+=1
    k+=1
    i+=1            
     