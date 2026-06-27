'''
6. Banking Fraud Detection System

A bank monitors transactions based on amount, location, OTP verification, and account age.

If transaction amount is at least 10000, then check location. If international, then check OTP verification. If verified, allow; otherwise block. If location is domestic, then check if amount is at least 50000. If yes, check account age. If account age is at least 2 years, allow; otherwise flag. If amount is less than 50000, allow. If transaction amount is less than 10000, then check unusual activity. If yes, flag; otherwise allow.

Input:
Transaction Amount = 60000
Location = domestic
Account Age = 1

Output:
Transaction Status = Flagged

'''

amu = int(input("Enter your transation amount :- "))
loc = input("Enter your location :- ").lower()
accage = int(input("Enter your account age :- "))
otpstatus = input("Enter your OTP verified status :- ").lower()


if amu >=10e3 :
      if loc == "international":
            if otpstatus == "verified":
                    print("Allowed")
            else: 
                  print("YOur are bolcked")
      elif loc = "domestic":
            if amu >=50e3:
                   if age >=2:
                        print("YOu are allowed..")
                   else: 
                       print("You are flag")
            elif amu<50e3:
                 if amu>10e3:
                     if "activity" == "unusaual"
                          print("You are flaged ")
                     else:
                          print("Your are allowed")
             