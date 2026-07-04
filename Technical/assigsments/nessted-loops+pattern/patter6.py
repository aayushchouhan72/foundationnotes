




l=1
while l<=5:
      
       m=1
       while m<=5:
          if m>=6-l:
                if m%2 == 0 and l%2==0:
                   print("0",end=" ")
                else:
                   print("1",end=" ")
          else:
             print(" ",end=" ")
          
          m+=1
       
       l+=1
       print()