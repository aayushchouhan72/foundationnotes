phoneprice = int(input("Enter the phone price:- "))
downpayment=  int(input("Enter amount you went to pay right now"))
intrestrate=int(input("Enter the intrest rate"))
dur=  int(input("Enter the duration to repay"))
remamount= phoneprice-downpayment

remamountwithinterst=remamount*(1+(intrestrate/100))
intallment=remamount/dur

print(f"Remaining Amount = {remamount}\nTotal with intrest = {remamountwithinterst}\nMouthly EMI = {intallment}")


