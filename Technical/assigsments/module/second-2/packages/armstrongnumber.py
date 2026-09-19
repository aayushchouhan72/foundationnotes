
def armstrongnumber(x):
      sum = 0
      for i in str(x):
          sum += int(i)**len(str(x))  
      if sum ==  x:
             return True
      return False