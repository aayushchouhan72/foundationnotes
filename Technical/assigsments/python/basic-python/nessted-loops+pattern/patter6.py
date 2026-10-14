
#         1
#       1 0
#     1 0 1
#   1 0 1 0
# 1 0 1 0 1 
l=1
while l<=5:
      
       m=1
       count=1 
       while m<=5: 
             
          if m>=6-l:
            # print(count)
            var="1" if count%2 != 0 else "0"
            print(var,end=" ") 
            count+=1
            # print(count)
          else:
             print(" ",end=" ")
            
          m+=1
       l+=1
       print()