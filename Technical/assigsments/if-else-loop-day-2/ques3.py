'''
3. Multiplication Table
A shopkeeper wants to calculate bulk pricing for a product. If one item costs ₹n, then cost for multiple quantities can be calculated using multiplication.
Write a program to print the *multiplication table of a given number up to 10 using loops*.

Input: n = 6
Output:
6 x 1 = 6
6 x 2 = 12
...
6 x 10 = 60

---


'''

n = int(input("Enter the that table you went to print :- "))
m=1;

for i in range(n,n*10+1,n):
    print(f"{n} X {m} = {i}")
    m+=1

print("BY While loop...")
i=0
while i<10:
    i=i+1
    print(n,"x",i,"=",n*i)
