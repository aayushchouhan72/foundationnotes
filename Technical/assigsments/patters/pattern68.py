'''
    #
   *#* 
  **#** 
 ***#*** 
****#****







'''
n= int(input("Enter the number of lines .."))

i=1
k=1
m="#"
while i<=n:
    print()
    j=1
    while j<=n-i:
        print(" ",end="")
        j+=1
    print(m.center(k,"*"))
       
    k+=2
    i+=1