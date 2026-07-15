
'''
123456
54321
1234
321
12



'''


n= int(input("Enter the number of lines .."))


i=n+1

oddstart=n
flag=True
while i>1:
    print()
    j=1
    k=i
    while j<=i:
          if i%2:
             print(k,end="")
             k-=1

             
          else:
             print(j,end="")
          j+=1
    flag=False
    i-=1            
     