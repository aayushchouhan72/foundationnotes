'''
1. Electricity Department Billing System


The electricity department of a city wants to automate the monthly bill generation process for its customers. The bill is calculated based on slab-wise unit consumption:

* First 100 units are charged at ₹5 per unit
* Next 100 units (101–200) are charged at ₹7 per unit
* Units above 200 are charged at ₹10 per unit

Write a Python program to calculate the total electricity bill based on the number of units consumed.

Input:
Enter units consumed: 250

Output:
Total Electricity Bill: ₹1950
'''


unit = int(input("Enter unit you consumed this mounth :- "))
bill =0

for i in range(1,unit+1,1):
      if i<=100:
          bill = bill+5
      elif i>100 and i<=200:
          bill = bill+7
      elif i>200:
          bill= bill+10
      print(bill)
print(f"Total bill of this mounth = {bill}")