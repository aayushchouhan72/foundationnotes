'''
  



'''

n = 9      
m = 7      
for i in range(n):
    for j in range(m):
       
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            print("*", end="")
        elif i == j:
            print("*", end="")
        
        elif i + j == m - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()  