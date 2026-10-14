'''
    1
   123
  12345
 1234567
123456789
'''







n= int(input("Enter the number of lines .."))

i=0
k=1
while i<n:
    j=1
    m=1
    print()
    while j<n-i:
        print(" ",end="")
        j+=1
    j=1
    while j<=k:
        print(m,end="")
        j+=1
        m+=1
    k+=2
    i+=1