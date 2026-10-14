

from sumofdigit import *

def HarshadNumber(x):
    sum = digitsum(x)
    if x%sum == 0:
           return True 
    return False