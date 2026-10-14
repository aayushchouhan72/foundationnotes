
'''
n online shopping platform provides discounts to customers based on their total purchase amount:

* Above ₹5000 → 20% discount
* ₹2000 to ₹5000 → 10% discount
* Below ₹2000 → 5% discount

Write a Python program to calculate the final amount after discount.

Input:
Enter purchase amount: 4500

Output:
Final Amount: ₹4050

'''

billcost = int(input("ENter the iteam price"))

if billcost<2000:
   print("YOur are eligble for the 5% discount ",billcost-billcost*0.05)
elif billcost>=2000 and billcost<5000 :
   print("YOur are eligble for the 10% discount ",billcost-billcost*0.10)
else:
   print("YOur are eligble for the 20% discount ",billcost-billcost*0.20)