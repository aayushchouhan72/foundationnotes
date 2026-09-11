def NeonNumber(x):
      squr=x**2
      dig=0
      for i in str(squr):
            dig += int(i)
      if dig ==  x:
            return True
      return False 