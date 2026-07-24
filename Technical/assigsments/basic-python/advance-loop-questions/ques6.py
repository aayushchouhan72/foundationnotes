'''
6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2

'''

n = int(input("Enter the number :- "))
faccou=0
samfac=9
i =2

while i<=n:
     if n%i==0:
          faccou+=1
          if samfac>i:
              samfac=i
     i+=1
print("composite number " if faccou>2 else "not composite number ")
print(f"Factors Count = {faccou+1}\nSmallest Factor = {samfac}")