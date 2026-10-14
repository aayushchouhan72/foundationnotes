'''
A B C D E
 A B C D
  A B C
   A B
    A

'''

n= int(input("Enter the number of lines .."))
i=1
while i<=n:
    
    j=1
    m=65
    while j<=i-1:
        print(" ",end="")
        j+=1
    j=1
    while j<=(n+1)-i:
         print(chr(m),end=" ")
         m+=1
         j+=1
         
    print()
    i+=1


