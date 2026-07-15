'''
A
BB
CCC
DDDD
EEEEE
'''

n= int(input("Enter the number of lines .."))

i=1
num=65
while i<=n:
     j=1
     print()
     while j<=i:
         print(chr(num),end="")    
         
             
         j+=1
     num+=1
     i+=1