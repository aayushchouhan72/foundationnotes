
'''
*
**
****
*******
***********


'''


n= int(input("Enter the number of lines .."))


i=1
m=2
pevcount=2
while i<=n:
    print()
    j=1
    flag=True
    helper=i
    count=0
    while helper :
       if i>2:
          break
       while i<=2 and j<=i:
          print("*",end="")
          j+=1
       helper-=1
       
    else: 
       flag=False
    if flag:
       j=1
       temp=pevcount+m
       while temp:
             print("*",end="")
             count+=1
             temp-=1
       pevcount=count
       m+=1
        
    i+=1            
     