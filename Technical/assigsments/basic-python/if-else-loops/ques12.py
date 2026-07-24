'''

12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680

''' 
bill  = int(input("Enter the your  bill amount :- "))


if 1000>bill:
   print(f"Your need to  pay amount {bill + bill*0.05}")
elif 10001<=bill and bill<=5000:
      if bill > 3000:
          print(f"Your need to  pay amount {bill + 300 + (bill*0.12)}")
      else:
          print(f"Your need to  pay amount {bill + bill*0.12}")
   
else: 
   print(f"Your need to  pay amount {bill + 300 + (bill*0.12)}")