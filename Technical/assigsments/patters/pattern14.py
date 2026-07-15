'''
1
23
456
78910


'''

n= int(input("Enter the number of lines .."))

i=1
num=1
while i<=n:
     j=1
     print()
     while j<=i:
         if num >10:
            break
         print(num,end="")    
         num+=1
             
         j+=1
     i+=1