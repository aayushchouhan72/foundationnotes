count=1
def printnum(x):
    global count
    print(count,end=" ")
    count+=1
    if x==1:
        return 0
    return printnum(x-1)

printnum(8)