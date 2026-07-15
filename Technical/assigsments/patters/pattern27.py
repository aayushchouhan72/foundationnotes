
'''
1
10
1 1
1  0
10101




'''


n= int(input("Enter the number of lines .."))

i=1
flag=True
while i<=n:
     print()
     j=1
     while j<=i:
        if i<3 :
           if j%2==0:
              print(0,end="")
           else:
              print(1,end="")
        elif i>2 and i<n:
              if j==1 or i == j:
                     if j%2==0:
                          print(0,end="")
                     else:
                          print(1,end="")
              else:
                   print(" ",end="")
        
        else: 
            if j%2==0:
                 print(0,end="")
            else:
                 print(1,end="")
            
       
                 
        
        j+=1
     i+=1



