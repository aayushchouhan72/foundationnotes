def printnum(x):
    print(x,end=" ")
    if x==1:
        return 0
    return printnum(x-1)

printnum(8)