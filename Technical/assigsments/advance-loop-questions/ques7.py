n = int(input("Enter the number :-"))
sum=0
while n:
    dig = n%10
    sum+=dig  
    n=n//10
i=2
st=True
while i<=sum//2:
       if sum%i==0:
          break
       i+=1
else:
    print("Given  Digit sum  number is prime number")
    st=False

if st:
   print("Given Digit sum number not prime ")
     
    
  