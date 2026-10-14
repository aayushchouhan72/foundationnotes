
'''
ABCDE
A  D
A C
AB
A


'''


n= int(input("Enter the number of lines .."))


i=1
while i<=n:
    print()
    j=1
    chrs=65
    while j<=(n+1)-i:
          if i == 1:
             print(chr(chrs),end="")
             chrs+=1
          elif i>1 and i<=n-2:
             if j== 1 or  j == (n+1)-i :
                 print(chr(chrs),end="")
                 chrs+=1
             else:
                 print(" ",end="")
                 chrs+=1
          else:
              print(chr(chrs),end="")
              chrs+=1
 
          j+=1
 
    i+=1            
     