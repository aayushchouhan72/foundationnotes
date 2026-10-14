'''

5. An ATM system processes withdrawal requests. The system should take account balance,
 withdrawal amount, and PIN status (correct or incorrect) as input. If the balance is
greater than or equal to the withdrawal amount, then check the withdrawal limit.
If the withdrawal amount is less than or equal to 10000, then check the PIN.
 If the PIN is correct, display "Transaction Successful"; otherwise, display "Invalid PIN".
If the withdrawal amount exceeds 10000, display "Limit Exceeded". If the balance is less than the
 withdrawal amount, display "Insufficient Balance".

Input:
Balance = 20000
Withdrawal Amount = 8000
PIN = correct

Output:
Transaction Successful
1

'''

bal = float(input("Enter the salary"))
withd = int(input("Enter the amount to withdrawal "))
pinstatus = input("enter pin status")

if bal >= withd:
         if withd <= 10000:
             if pinstatus == "correct"
                  print("Transaction Successful")
             else:
                  print("Enter the correct pin")
             
         else:
             print("Limit Exceeded")
else:
    print("Insufficient Balance")
   
           







