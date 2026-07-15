n= int(input("Enter the number of lines .."))

i=1
while i<=n:
     j=1
     print()
     while j<n+1:
        if i == 1:
           print("*",end=" ")
        else: 
           print(" ",end=" ")
        j+=1
     i+=1