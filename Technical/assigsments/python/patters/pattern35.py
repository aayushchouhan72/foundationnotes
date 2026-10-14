
'''
*****
*  *
* *
**
*


'''


n= int(input("Enter the number of lines .."))


i=1
while i<=n:
    print()
    j=1
    while j<=(n+1)-i:
          if i == 1:
             print("*",end="")
          elif i>1 and i<=n-2:
             if j== 1 or  j == (n+1)-i :
                 print("*",end="")
             else:
                 print(" ",end="")
          else:
              print("*",end="")
 
          j+=1
 
    i+=1            
     