'''

4. Electricity Bill Management System

You are developing an Electricity Bill Management System for a power distribution company. The system helps calculate electricity bills for customers based on their unit consumption.

Sometimes, the operator may try to calculate the bill or apply surcharge before entering the number of units consumed. Your system must handle such situations properly.

👉 Important Condition:
If units are not entered, the system should display:
"Please enter units consumed first"
and should not perform further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Units Consumed
2 → Calculate Bill Amount

* First 100 units → ₹5 per unit
* Next 100 units → ₹7 per unit
* Above 200 units → ₹10 per unit
  3 → Apply Surcharge
* If bill > 2000 → 10% surcharge
* Otherwise → 5% surcharge
  4 → Display Final Bill
  5 → Exit

---

Sample Run 1:
Input:
Enter your choice: 2

Output:
Please enter units consumed first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter units consumed: 250

Output:
Units recorded successfully

---

Sample Run 3:
Input:
Enter your choice: 2

Output:
Bill Amount: 1700

(Explanation: 100×5 = 500, 100×7 = 700, 50×10 = 500 → Total = 1700)

---

Sample Run 4:
Input:
Enter your choice: 3

Output:
Surcharge: 85

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
----- Final Bill -----
Units: 250
Bill Amount: 1700
Surcharge: 85
Total Payable: 1785

---

Sample Run 6 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 7 (Exit):
Input:
Enter your choice: 5

Output:
Exiting system... Thank you!

---
'''



units =0
bill=0
charge=0
final_bill=0

while True:
     print("1 → Enter Units Consumed")
     print("2 → Calculate Bill Amount")
     print("3 → Apply Surcharge")
     print("4 → Display Final Bill")
     print("5 → Exit")
     choice = int(input("Enter the Choice :- "))
     match choice :
           case 1:
                 units = int(input("Enter the your merter reading"))
                 if units <0:
                       print("Enter the valid Reading ...")
                       units = int(input("Enter the your merter reading"))
                 else:
                     print("Your meter reading is saved ...")
 
           case 2:
                   temp= units 
                   while temp:
                        if temp<=100:
                             bill+=5
                        elif temp>100 and temp<=200:
                             bill+=7
                        else: 
                             bill+=10  
                        temp-=1     
           case 3:
                if bill>0:
                       if bill>2000:
                               charge = bill*0.10
                               final=bill+charge
                       else:
                               charge =bill*0.05
                               final=bill+charge
                else:
                    print("Calculate bill first ..")
           case 4:
                 if bill >0 and charge>0:
                       print("===============BILL===============")
                       print(f"\tUnits:{units}\n\tBill Amount :{bill}\n\tSurcharge :{charge}\n\tTotal Payable :{final}")
                 else:
                     print("Calculate bill and surchages first the we proceed further ...")
           case 5:
                 print("Closeing  the Application ..")
                 print( 'Thankyou👍👍')
                 break
     

