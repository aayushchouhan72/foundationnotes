
'''
5
44
333
2222
11111





'''


n= int(input("Enter the number of lines .."))


i=1
temp=5
while i<=n:
    print()
    j=1
    while j<=n:
       if j>=(n+1)-i:
         print(temp,end="") 
          
       else:
         print(" ",end="") 
          
       j+=1
    temp-=1 
    i+=1            
     