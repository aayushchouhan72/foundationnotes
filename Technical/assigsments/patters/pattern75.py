'''
x
xx
xxx
xxxx
xxx
xx
x


'''

n= int(input("Enter the number of lines .."))
i=1
m=n*2-1
k=n-1
while i<=m:
    print()
    l=1
    if i<=n:
       if i == 1:
            print(" ",end="")
       else:
           j=1
           while j <=i-1:
               print(l,end="") 
               l+=1
               j+=1    
    else:
       if i == m:
            print(" ",end="")
       else:
           j=1
           while j <=k-1:
               print(l,end="") 
               l+=1
               j+=1  
       k-=1 
    
    i+=1


