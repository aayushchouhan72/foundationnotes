'''
6. Banking Fraud Detection System

A bank checks fraud risk based on transaction amount, location, device, and transaction count.

If amount is greater than or equal to 50000, then check location. If location is international, then check device. If device is new, then check transaction count. If transactions are more than 3, mark High Risk (Block); otherwise Medium Risk. If device is not new, mark Medium Risk.

If location is domestic, then check transaction count. If more than 5, mark Medium Risk; otherwise Low Risk.

If amount is less than 50000, then check unusual activity. If yes, then check device. If device is new, mark Medium Risk; otherwise Low Risk. If no unusual activity, mark Safe.

Input:
Amount = 70000
Location = international
Device = new
Transactions = 4

Output:
Risk Level = High Risk (Blocked)

'''

amu = int(input("Enter the transaction amount .."))
loc = input("Enter the location ..").lower()
dev = input("Enter the device ..").lower()
tra = int(input("Enter the transactions .."))

if amu>50000:
      if loc =="international":
               if dev == "new":
                      if tra >3:
                             print("High risk (Block)")
                      else:
                          print("You has Medium Risk")
               else:
                   print("you has Medium Risk")
      else:
           if tra>5:
                  print("You has Medium Risk..")
           else:
                print("You have low Risk...") 
else:
   if  'unusal' == True :
              if dev == "new"
                      print("It has Medium Risk")
              else:
                   print("You have low risk")
   else:
        print("It is safe")
     