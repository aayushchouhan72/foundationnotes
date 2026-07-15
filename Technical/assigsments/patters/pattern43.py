
'''
1
12
123
1234
12345




'''


n= int(input("Enter the number of lines .."))


i=1
while i<=n:
    print()
    j=1
    temp=1
    while j<=n:
       if j>=(n+1)-i:
         print(temp,end="") 
         temp+=1  
       else:
         print(" ",end="")    
       j+=1
    i+=1            
     