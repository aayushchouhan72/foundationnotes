def sumn(n):
    if n==0:
        return n
    return n+sumn(n-1)

print(sumn(20))