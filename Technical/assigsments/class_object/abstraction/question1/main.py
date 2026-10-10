
from payment.payment import  UPIPayment,  CreditCardPayment ,DebitCardPayment , NetBankingPayment, WalletPayment

# class ObjectCreater:



while True:
    print("""
------------------------------------------------------------
MAIN MENU:
------------------------------------------------------------

========================================
       ONLINE PAYMENT SYSTEM
========================================

1. Make Payment
2. View Payment Details
3. Exit
    """)
    global obj
    choice=int(input("enter you choice:"))
    match choice:
        case 1:
            Customer_Name=input("enter Customer Name : ")
            Order_ID=int(input("enter Order ID :"))
            order_fee=int(input("enter order fee : "))
            while True:
                print("""
                Select Payment Method

                        1. UPI
                        2. Credit Card
                        3. Debit Card
                        4. Net Banking
                        5. Wallet
                """)
                a=int(input("Enter your choice:"))
                match a:
                    case 1:
                        UPI_ID=int(input("Enter the UPI ID :- "))
                        UPI_PIN=input("Enter the upi pin :- ")
                        obj = UPIPayment(UPI_ID,UPI_PIN,Customer_Name,Order_ID,order_fee)
                        obj.validate_payment()
                        obj.calculate_processing_fee()
                        obj.authenticate_payment()
                        obj.process_payment()
                    case 2:
                        Card_Number=int(input("Enter the Card_Number :- "))
                        Card_Holder_Name=input("Enter the Card_Holder_Name :- ")
                        CVV=int(input("Enter the CVV :- "))
                        Expiry_Date=int(input("Enter the UPI ID :- "))
                        obj.validate_payment()
                        obj.calculate_processing_fee()
                        obj.authenticate_payment()
                        obj.process_payment()
                        
                    case 3:
                        Card_Number=int(input("Enter the Card_Number :- "))
                        Card_Holder_Name=int(input("Enter the Card HolderName :- "))
                        CVV=int(input("Enter the CVV:- "))
                        Expiry_Date=int(input("Enter the UPI ID :- "))
                        obj.validate_payment()
                        obj.calculate_processing_fee()
                        obj.authenticate_payment()
                        obj.process_payment()
                                          
                    case 4:
                        Bank_name=input("Enter the bank name:-")
                        Account_Number=int(input("Enter the Account Number :- "))
                        obj.validate_payment()
                        obj.calculate_processing_fee()
                        obj.authenticate_payment()
                        obj.process_payment()
                                        
                    case 5:
                        Wallet_Name=input("enter wallet name: ")
                        Mobile_Number=int(input("enter the mobile number::"))
                        Wallet_PIN=int(input("enter your wallet pin here"))
                        obj.validate_payment()
                        obj.calculate_processing_fee()
                        obj.authenticate_payment()
                        obj.process_payment()
                    case 6:
                        break                     
        case 2:
            if obj: 
                obj.generate_receipt()    
            else: 
                print("plz create an object first .....")
        case 3:
            print("EXIT")

        case __:
            print("Invalid choice")

