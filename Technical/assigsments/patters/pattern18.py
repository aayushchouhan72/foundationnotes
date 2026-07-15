'''
1
10
101
1010
10101

'''

n= int(input("Enter the number of lines .."))

i=1
while i<=n:
     j=1
     print()
     var=1
     while j<=i:
         if j%2 == 0:
            var-=1
            print(var,end="")
            var+=1
         else:
            print(var,end="")
         
         j+=1
     i+=1