def primenumber(x):
    isprime=False
    for i in range(2,x):
           if x%i ==  0:
                  return isprime
    else:
          isprime=True
    return isprime
