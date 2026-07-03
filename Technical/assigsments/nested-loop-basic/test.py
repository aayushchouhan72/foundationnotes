n= int(input("Enter number rows "))
m=int(input("Enter number colums"))

i=1
k=m

while i<=n:
      c=0
      j=1
      print()
      while j<=k:
            if j<=i:
               print(j,end="")
            elif j<=k-i:
                 print("*",end="")
            else:
                c=(k+1)-j
                print(c,end="")
                c-=1
            j+=1
      i+=1   
     