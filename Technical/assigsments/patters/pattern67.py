'''
    A
   B B
  C   C
 D     D
EEEEEEEEE






'''
n= int(input("Enter the number of lines .."))

i=1
k=1
m=65
while i<=n:
    j=1
    print()
    while j<=n-i:
       print(" ",end="")
       j+=1
    j=1
    while j<=k:
        if i<2:
              print(chr(m),end=" ")
        elif i>1 and i<=n-1:
              if j == 1 or i == j:
                   print(chr(m),end=" ")
              else:
                   print(" ",end=" ")
        else:
            print(chr(m),end="")   
         
        j+=1 
    k+=2
    m+=1      
    i+=1