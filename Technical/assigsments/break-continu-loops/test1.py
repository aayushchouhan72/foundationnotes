'''n= int(input("Enter the number :- "))
sqr = n**2
m= 2 if len(str(n))>=3 else 1

while m :
    sd= sqr%10
    nd = n%10
    if nd == sd:
         sqr= sqr//10
         n= n//10
         m-=1
    else:
        break
if m!=0:
     print("Given number is not automorphic number ")
else:
     print("Given number is automorphic number ")'''

''' Duck number code'''
n = int(input("Enter the number :- "))
count=0.
n= str(n)
zcount=0
for i in n:
    if count == 0:
          if i=="0":
               break;   
               print("Enter number is not duck number")     
    if  count!=0 and i=="0":
          zcount+=1
          break
    count+=1

if zcount:
       print("given number is duck number ..")
else: print("Given number is not duck number .. ")

