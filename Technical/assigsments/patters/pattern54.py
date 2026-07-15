
'''
ABCDE
 A__D
  A_C
   AB
    A




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
          if i==1:
             print(chr(ch),end="")
             ch+=1
          elif j>=2 and j<=n-1:
              if j==n or i == j:
                 print(chr(ch),end="")
                 ch+=1
              else:
                  print("_",end="")
                  ch+=1
                    
          else:
             print(chr(ch),end="")
             ch+=1 
                         
       else:
         print(" ",end="") 
         
       j+=1
    k+=1
    i+=1            
     