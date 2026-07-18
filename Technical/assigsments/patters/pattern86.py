#     1
#     2
#     3
#     4
# 123454321
#     4
#     3
#     2
#     1

n = int(input("Enter the n"))
m=n*2
k=2
p=4
for i in range(1,m):
    print()
    for j in range(1,m):
        if j == n:
             if i>n:
                 print(i-k,end="")
             else:
                 print(i,end="")
        else:
             if i == n:
                 if j>=n:
                     print(p,end="")
                     p-=1
                 else:
                     print(j,end="")
                     
             else:
                  print(" ",end="") 
                 
    if i>n:
        k+=2                
                       