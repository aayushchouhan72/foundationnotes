# 1
# 01
# 101
# 0101
# 10101

# codrne for it 

# n=int(input("Enter the number of "))

# i=1
# while i<=n:
#       print()
#       j=1
#       m= 0 if i%2==0 else 1
#       if i%2 == 0:
#         k=0
#       else:
#         k=1
#       while j<=i:
#         if k%2 != 0:
#             print(1,end=" ")
#             k+=1
#         else:
#             print(0,end=" ")
#             k+=1          
#         j+=1
#       i+=1      

# 1
# 10
# 101
# 1010
# 10101

n= int(input("Enter the number of lines ..."))

i=1
# while i<=n:
#     j=1
#     print()
#     while j<=i:
#         if j%2 == 0:
#              print(0,end=" ")
#         else:
#              print(1,end=" ")
#         j+=1
#     i+=1     


# *
# * *
# *  *
# *    *
# * * * * *

# while i<=n:
#     j=1
#     print()
#     while j<=i:
#         if j<=2 and i<=2:
#             print("*",end=" ")
#         elif i>5-i and i<=4:
#             if j == 1 :
#                print("*",end=" ")
#             elif i == j:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         else:
#             print("*",end=" ")        
#         j+=1
#     i+=1


# 1
# 12
# 1 3
# 1  4
# 12345

while i<=n:
    j=1
    print()
    while j<=i:
        if j<=2 and i<=2:
            print(j,end="")
        elif i>5-i and i<=4:
            if j == 1 :
               print(j,end="")
            elif i == j:
                print(j,end="")
            else:
                print(" ",end="")
        else:
            print(j,end="")        
        j+=1
    i+=1

    
    






