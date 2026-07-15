'''
6 5 4 3 2 1
  6 5 4 3 2
    6 5 4 3
      6 5 4
        6 5
'''




l=1
while l<=5:
       m=1
       k=6
       while m<=6:
          if m>=l:
               print(k,end=" ")
               k-=1
          else:
             print(" ",end=" ")
          
          m+=1
       
       l+=1
       print()