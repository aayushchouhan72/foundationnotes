'''
a
bc
def
ghij
klmno

'''

n= int(input("Enter the number of lines .."))

i=1
num=97
while i<=n:
     j=1
     print()
     while j<=i:
         print(chr(num),end="")    
         
         num+=1    
         j+=1
     i+=1