
'''
1
10
101
1010
10101


'''


n= int(input("Enter the number of lines .."))


i=1
while i<=n:
    print()
    j=1
    k=1
    while j<=n:
       if j>=(n+1)-i:
           if i%2 != 0 :
                 if j%2 != 0:
                    print(k,end="")
                    k-=1
                 else:
                   print(k,end="")
                   k+=1
           else :
                if j%2 == 0:
                    print(k,end="")
                    k-=1
                else:
                   print(k,end="")
                   k+=1 
   
                        
       else:
         print(" ",end="") 
         
       j+=1
    i+=1            
     