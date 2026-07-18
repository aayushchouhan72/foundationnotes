'''
*     *
 *   *
  * *
   *
  * *
 *   *
*     *
'''

import math

n= int(input("Enter the number of lines it should  be odd"))
mid = math.ceil(n/2)
k=n
l=1
# if n%2:
#     i=1
#     print()
#     while i<=n:
#         if i<=mid:
#             j=1
#             while j<=n:
#                 if j == k or  j == l:
#                     print("*",end="")
#                 else:
#                     print(" ",end="")
#                 j+=1
#                 k-=1
#                 l+=1
#         else:  
#             pass  
#                 # j=1
#                 # while j<=n:
#                 #      if j == k or j == l:
#                 #          print("*",end="")
#                 #          k+=1
#                 #          l-=1
#                 #      else:
#                 #          print(" ",end="")
#                 #      j+=1
#                 #      k-=1
#                 #      l+=1
#         i+=1

                  
                 
# else:
#     print("ENter valid lines number like 1,3,5")

i=1
print()
while i<=n:
    print()
    j=1
    while j<=n:
        if j == l or j==k:
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    k-=1
    l+=1
    i+=1