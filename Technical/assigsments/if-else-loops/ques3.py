'''
3. Income Tax Department System

The Income Tax Department needs a system to calculate tax payable by citizens based on their annual income:

* Up to ₹2,50,000 → No tax
* ₹2,50,001 to ₹5,00,000 → 5% tax
* ₹5,00,001 to ₹10,00,000 → 20% tax
* Above ₹10,00,000 → 30% tax

Write a Python program to calculate the tax amount.

Input:
Enter annual income: 800000

Output:
Tax Payable: ₹110000

'''

sal = int(input("Enter your salary"))

if 25e4 >= sal :
      print("your comes under not tax category")
elif 250001<sal and sal<500000:
      print("tax on your income is ",sal*0.05)
elif 500001<sal and sal>1e6:
      print("tax on your income is ",sal*0.20)
else :
     print("tax on your income is ",sal*0.30)
           