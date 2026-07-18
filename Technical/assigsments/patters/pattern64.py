'''
    *
   *_*
  *___* 
 *_____* 
*********


'''
n= int(input("Enter the number of lines .."))

i=1
k=1
while i<=n:
    j=1
    print()
    while j<(n+1)-i:
        print(" ",end="")
        j+=1
    j=1
    while j<=k:
        if j==1:
           print("*",end="")
        elif i>1 and i<=n-1:
            if j==1 or j == k:
                print("*",end="")
            else:
                print("_",end="") 
        else:
            print("*",end="")
        j+=1
    k+=2
    i+=1