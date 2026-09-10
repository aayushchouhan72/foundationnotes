def printname(x):
    if not x:
         return
    print("Hello")
    return printname(x-1)
printname(5)
