'''
1
00
111
0000
11111



'''
n= int(input("Enter the number of lines .."))

i=1
while i<=n:
     j=1
     print()
     while j<=i:
         if i%2==0:
            print("0",end=" ")
         else:
            print("1", end =" ")
        
         j+=1
     i+=1