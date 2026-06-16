amount=  int(input("Enter the amount you went to convert"))

hunno =  int(amount/100)
amount = amount%100

fifno = int(amount/50)

amount =  amount%50

tenno =  int(amount/10)

print(f"You will get {hunno} of 100 and {fifno} of 50 and {tenno} of 10 ")