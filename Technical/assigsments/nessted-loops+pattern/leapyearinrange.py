import math
start=int(input("Enter the first number :-  "))
end = int(input("Enter the second number :- "))

while start<=end:  
         if start%4==0 or start%400==0:
             print(f"{start}",end=" ")
         start+=1
        
         
        