
'''
*****
####
***
##
*


'''


n= int(input("Enter the number of lines .."))


i=1
while i<=n:
    print()
    j=1
    while j<=(n+1)-i:
          if i%2!=0:
             print("*",end="")
          else:
             print("#",end="") 
          j+=1
 
    i+=1            
     