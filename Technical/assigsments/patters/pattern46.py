
'''
1
11
1*1
1**1
11111


'''


n= int(input("Enter the number of lines .."))


i=1
while i<=n:
    print()
    j=1
    temp=65
    count=0
    while j<=n:
       if j>=(n+1)-i:
          if i<3:
             print("1",end="")  
          elif i>2 and i<n:
             if j == n or j == count+1:
                 print("1",end="")
                 count=0
             else:
                print("*",end="")
          else:
              print("1",end="")
       else:
         print(" ",end="") 
         count+=1
       j+=1
    i+=1            
     