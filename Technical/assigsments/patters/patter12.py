'''
a
ab
abc
abcd
abcde



'''
n= int(input("Enter the number of lines .."))

i=1
while i<=n:
     j=1
     asc=65
     print()
     while j<=i:
         print(chr(asc),end=" ")
         j+=1
         asc+=1
     i+=1