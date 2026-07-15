
'''
*
*#
*#*
*#*#
*#*#*



'''


n= int(input("Enter the number of lines .."))

i=1
flag=True
while i<=n:
     print()
     j=1
     while j<=i:
        if j%2 == 0:
           print('#',end="")
        else:
           print('*',end="")
        j+=1
     i+=1



