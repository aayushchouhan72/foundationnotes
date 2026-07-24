start=int(input("Enter the first number :-  "))
end = int(input("Enter the second number :- "))

l=1
while l<=end:
       m=1
       while m<=l:
              
            if l%2 != 0:
               print("1",end=" ")
            else:
               print("0",end=" ")
            m+=1
       l+=1
       print()
       