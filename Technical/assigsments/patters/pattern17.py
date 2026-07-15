'''
*
##
***
####
*****


'''

n= int(input("Enter the number of lines .."))

i=1
while i<=n:
     j=1
     print()
     while j<=i:
         if i%2 == 0 :
            print("#",end="")
         else:
             print("*",end="") 
         j+=1
     i+=1