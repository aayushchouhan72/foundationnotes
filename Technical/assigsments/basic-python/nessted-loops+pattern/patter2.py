

s="ABCDE"
l=1
while l<=5:
       m=1
       index=0
       while m<=l:
            if len(s)>index:
               print(s[index],end=" ")
               index+=1  
               m+=1
       l+=1
       print()
