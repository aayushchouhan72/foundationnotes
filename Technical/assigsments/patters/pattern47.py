
'''
A
AB
A_C
A__D
ABCDE


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
             print(chr(temp),end="")
             temp+=1  
          elif i>2 and i<n:
             if j == n or j == count+1:
                 print(chr(temp),end="")
                 temp+=1
                 count=0
             else:
                print("_",end="")
                temp+=1
          else:
              print(chr(temp),end="")
              temp+=1
       else:
         print(" ",end="") 
         count+=1
       j+=1
    i+=1            
     