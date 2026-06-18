billamu =  int(input("Enter the bil amount"))
fribnum=  int(input("Enter the number of friends"))

netbill = billamu
netbill +=billamu*0.15

billperson = netbill/fribnum

print(f"Final Bill = {netbill} \n Each Person Pays = {billperson}")



