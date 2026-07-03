start=int(input("Enter the first number :-  "))
end = int(input("Enter the second number :- "))

sum=0
while start<=end:
        con=start
        if con%9==0:
           sum+=con
        start+=1
        
         
        
print(sum)