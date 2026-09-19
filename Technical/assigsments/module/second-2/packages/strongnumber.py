def strongnumber(x):
      num=0 
      def factorial(y):
            fac=1
            for i in range(y+1):
                  fac*=i
            return fac   
      for i in str(x):
             num+=factorial(int(i))
      return num