'''
   1
  1 1
 1 2 1
1 3 3 1
1 4 6 4 1




'''
n= int(input("Enter the number of lines .."))

i=1
k=1
m=3
while i<=n:
    j=1
    print()
    while j<=n-i:
       print(" ",end="")
       j+=1
    j=1
    while j<=i:
        if i<=2:
              print(1,end=" ")
        elif i>2 and i<=n-1:
              if j == 1 or i == j:
                   print(1,end=" ")
              else:
                   print(i-1,end=" ")
        else:
            if j == 1 or i == j:
                   print(1,end=" ")
            else:
                 if j<=3 :
                    print(j*2,end=" ")
                 else:
                    print(j*2-j,end=" ")      
        j+=1 
          
    i+=1