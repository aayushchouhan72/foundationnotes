'''
                1               
               101            
              10101         
             1010101           
            101010101    
           10101010101

'''

n=int(input("Enter the number :- "))
i=1
m=1
while i<=n:
      print()
      j=1
      while j<=n-i:
            print(" ",end="")
            j+=1 
      j=1
      while j<=m:
            if j%2 == 0:
                  print("0",end="")
            else:
                  print("1",end="")
            j+=1
      i+=1       
      m+=2      