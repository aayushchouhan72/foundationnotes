'''
*        *
**      **
***    ***
****  ****
***** *****


'''
n= int(input("Enter the number of lines .."))

i=1
l=n*2-1
m=l
k=i
while i<=n:
     print("*"*i," "*l,"*"*i)
     l-=2
     i+=1