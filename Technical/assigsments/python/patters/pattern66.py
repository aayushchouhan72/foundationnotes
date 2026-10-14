'''
    1
   1*1
  1***1
 1*****1
111111111





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
        if i<2:
              print(1,end=" ")
        elif i>2 and i<=n-1:
              if j == 1 or i == j:
                   print(1,end=" ")
              else:
                   print("*",end=" ")
        else:
            print(1,end=" ")     
        j+=1 
          
    i+=1