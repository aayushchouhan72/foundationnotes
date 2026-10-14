
'''
EEEEE
DDDD
CCC
BB
A

'''


n= int(input("Enter the number of lines .."))


i=1
ch=69
while i<=n:
    print()
    j=1
    while j<=(n+1)-i:
          print(chr(ch),end="")
          j+=1
    ch-=1
    i+=1            
     