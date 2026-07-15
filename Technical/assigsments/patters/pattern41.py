
'''
A
BCD
EFGHI
JKLMNOP



'''


n= int(input("Enter the number of lines .."))


i=1
k=0
chi=65
while i<n:
    print()
    j=1
    while j<=i+k:
       print(chr(chi),end="")            
       j+=1
       chi+=1
    k+=1
    i+=1            
     