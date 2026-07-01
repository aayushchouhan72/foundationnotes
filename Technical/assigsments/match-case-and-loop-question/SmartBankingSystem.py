'''
3.

 Smart Banking System

Scenario:
You are developing a Smart Banking System for a bank to help customers perform basic banking operations such as deposit, withdrawal, balance checking, and interest calculation.

Sometimes, users may try to withdraw money or check balance before depositing any amount. Your system must handle such situations properly.

👉 Important Condition:
If no amount has been deposited yet, the system should display:
"No balance available. Please deposit first"
and should not allow withdrawal, balance check, or interest calculation.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Deposit Money
2 → Withdraw Money
3 → Check Balance
4 → Apply Interest

* Balance > 50000 → 5% interest
* Otherwise → 3% interest
  5 → Exit

---

Sample Run 1:
Input:
Enter your choice: 2

Output:
No balance available. Please deposit first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter amount to deposit: 10000

Output:
Amount deposited successfully

---

Sample Run 3:
Input:
Enter your choice: 3

Output:
Current Balance: 10000

---

Sample Run 4:
Input:
Enter your choice: 2
Enter amount to withdraw: 15000

Output:
Insufficient balance

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
Interest added: 300
Updated Balance: 10300

---

Sample Run 6:
Input:
Enter your choice: 2
Enter amount to withdraw: 5000

Output:
Withdrawal successful

---

Sample Run 7 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 8 (Exit):
Input:
Enter your choice: 5

Output:
Exiting system... Thank you!

--

'''




depo=0
withdraw=0
bal=0
intrest=0


while True:
     print("1 → Deposit Money")
     print("2 → Withdraw Money")
     print("3 → Check Balance")
     print("4 →  Apply Interest")
     print("5 → Exit")      
     choice = int(input("Enter your Choice :- "))
     match choice:
           case 1:
                  depo = int(input("Enter the amount that you went to deposit .."))
                  if depo>0:
                      print('Amount deposited successfully ..')
                      bal+=depo
                  else:
                      print("Enter Valid amount to Deposit  ..")                      
           case 2:
                 if bal==0:
                       print("No balance available. Please deposit first") 
                 else:
                     withdraw = int(input("Enter amount that you went to withdraw .."))
                     if withdraw < bal: 
                             print("Amount With draw successfully..")
                             bal-=withdraw
                     else:
                         print("Withdraw is Failed bcoz your Account not  have sufficent fund ") 
                         
                    
           case 3:
               print(f"Amount is {bal}")
                  
           case 4:
               if bal>0:
                 if bal>50000:
                    intrest =bal*0.05
                    bal+=intrest      
                 else:
                   intrest =bal*0.03
                   bal+=intrest 
               else:
                   print("Gareeb put some money in your account..")  
        
           case 5:
                 print("Closeing application ...")
                 print("Thankyou 👍👍👍")
                 break
           case __:
                 print("You enter the wrong option or invalid option..")
          