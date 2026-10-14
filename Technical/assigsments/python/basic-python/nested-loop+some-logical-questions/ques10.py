'''

10.
Electricity Bill Processing System (Multi-House)

An electricity board processes bills for multiple houses in a society.

Write a program to:

- Read number of houses n
- For each house:
    - Read units consumed
    - Calculate bill using slab rates:

        First 100 units      → ₹5 per unit  
        Next 100 units      → ₹7 per unit  
        Above 200 units     → ₹10 per unit  

    - Apply conditions:
        - If bill > ₹2000 → add 10% surcharge  
        - If units < 50 → give ₹100 subsidy  

    - Print bill for each house

- After processing all houses:
    - Print total bill collected
    - Print highest bill

---

Input:
3
120
250
40

Output:
House 1 Bill = 640
House 2 Bill = 1700
House 3 Bill = 100

Total Collection = 2440
Highest Bill = 1700
'''

housenum = int(input("Enter the number of house ..."))

netbill = 0
max = 0
count=1
for i in range(housenum):
     units = int(input("Enter the number of units consumed.."))
     bill=0
     for i in range(1,units+1):
           if i<=100:
                bill+=5
           elif i>100 and i<=200:
                 bill+=7
           else:
                bill+=10
     if bill >2000:
             bill+=bill*0.10
     bill = bill-100 if units<50 else bill
     if max<bill:
            max=bill
     netbill+=bill
     print(f"House {count} Bill ={bill}")
     count+=1
print(f"Total Collection = {netbill} \nHighest Bill = {max}")

           
          
