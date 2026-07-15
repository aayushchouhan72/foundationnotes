
'''
ABCDE
ABCD
ABC
AB
A

'''


n= int(input("Enter the number of lines .."))


i=1
while i<=n:
    print()
    j=1
    ch=65
    while j<=(n+1)-i:
          print(chr(ch),end="")
          ch+=1
          j+=1
    i+=1            
     