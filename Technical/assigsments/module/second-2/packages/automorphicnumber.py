
def Automorphic(x):
       numlen=len(str(x))
       squr=x**2
       removed = str(squr)[-numlen:]
       if removed ==  x:
             return True
       return False