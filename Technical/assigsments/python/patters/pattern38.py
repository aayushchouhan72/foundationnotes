
'''
55555
4  4
3 3
22
1



'''


n= int(input("Enter the number of lines .."))


i=1
ch=5
while i<=n:
    print()
    j=1
    while j<=(n+1)-i:
          if i == 1:
             print(ch,end="")
             
          elif i>1 and i<=n-2:
             if j== 1 or  j == (n+1)-i :
                 print(ch,end="")
                 
             else:
                 print(" ",end="")
                 
          else:
              print(ch,end="")
              
 
          j+=1
    ch-=1
    i+=1            
     