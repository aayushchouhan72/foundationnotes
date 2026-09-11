
from sumofdigit import * 

def spyNumber(x):
      pro = 1
      for i in str(x):
            pro*=int(i) 
      sum = digitsum(x)
      if sum == pro:
             return True
      return False
      