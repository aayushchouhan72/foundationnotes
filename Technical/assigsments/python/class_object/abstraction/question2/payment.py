# ============================================================
# QUESTION 1: ONLINE PAYMENT MANAGEMENT SYSTEM
# ============================================================

# Develop a MENU-DRIVEN Online Payment Management System for an
# e-commerce company.

# The company supports different payment methods:

# 1. UPI
# 2. Credit Card
# 3. Debit Card
# 4. Net Banking
# 5. Wallet

# Every payment method follows a common payment process, but the
# actual validation, authentication, processing fee and payment
# processing logic are different.

# Therefore, the system must be designed using ABSTRACTION.

# ------------------------------------------------------------
# ABSTRACT CLASS:
# ------------------------------------------------------------

# Create an abstract class named:

# Payment

# The class should define the following abstract methods:

# 1. validate_payment()
# 2. calculate_processing_fee()
# 3. authenticate_payment()
# 4. process_payment()
# 5. generate_receipt()

# Create separate child classes for:

# 1. UPIPayment
# 2. CreditCardPayment
# 3. DebitCardPayment
# 4. NetBankingPayment
# 5. WalletPayment

# Each child class must provide its own implementation of all
# required abstract methods.

# ------------------------------------------------------------
# MAIN MENU:
# ------------------------------------------------------------

# ========================================
#        ONLINE PAYMENT SYSTEM
# ========================================

# 1. Make Payment
# 2. View Payment Details
# 3. Exit

# Enter your choice:

# ------------------------------------------------------------
# OPTION 1: MAKE PAYMENT
# ------------------------------------------------------------

# Ask the user to enter:

# Customer Name
# Order ID
# Order Amount

# Then display:

# Select Payment Method

# 1. UPI
# 2. Credit Card
# 3. Debit Card
# 4. Net Banking
# 5. Wallet

# Enter your choice:

# ------------------------------------------------------------
# UPI:
# ------------------------------------------------------------

# Input:

# UPI ID
# UPI PIN

# Processing Fee:

# 0%

# ------------------------------------------------------------
# CREDIT CARD:
# ------------------------------------------------------------

# Input:

# Card Number
# Card Holder Name
# CVV
# Expiry Date

# Processing Fee:

# 2% of Order Amount

# ------------------------------------------------------------
# DEBIT CARD:
# ------------------------------------------------------------

# Input:

# Card Number
# Card Holder Name
# CVV
# Expiry Date

# Processing Fee:

# 1% of Order Amount

# ------------------------------------------------------------
# NET BANKING:
# ------------------------------------------------------------

# Input:

# Bank Name
# Account Number
# Customer ID

# Processing Fee:

# 0.5% of Order Amount

# ------------------------------------------------------------
# WALLET:
# ------------------------------------------------------------

# Input:

# Wallet Name
# Mobile Number
# Wallet PIN

# Processing Fee:

# 1.5% of Order Amount

# ------------------------------------------------------------
# SAMPLE INPUT:
# ------------------------------------------------------------

# Enter Customer Name: Rahul
# Enter Order ID: ORD1052
# Enter Order Amount: 5000

# Select Payment Method:

# 1. UPI
# 2. Credit Card
# 3. Debit Card
# 4. Net Banking
# 5. Wallet

# Enter your choice: 2

# Enter Card Number: 4567891234567890
# Enter Card Holder Name: Rahul Singh
# Enter CVV: 321
# Enter Expiry Date: 12/29

# ------------------------------------------------------------
# EXPECTED OUTPUT:
# ------------------------------------------------------------

# ========================================
#           PAYMENT PROCESSING
# ========================================

# Customer Name       : Rahul
# Order ID            : ORD1052
# Payment Method      : Credit Card

# Order Amount        : Rs.5000.00
# Processing Fee      : Rs.100.00
# Final Amount        : Rs.5100.00

# Validating payment details...
# Payment details validated successfully.

# Authenticating payment...
# Authentication successful.

# Processing payment...
# Payment processed successfully.

# Transaction ID      : TXN785421
# Payment Status      : SUCCESS

# ========================================

# OPTION 2: VIEW PAYMENT DETAILS
# ------------------------------------------------------------

# Ask:

# Enter Order ID:

# If the order exists, display:

# Order ID
# Customer Name
# Payment Method
# Order Amount
# Processing Fee
# Final Amount
# Transaction ID
# Payment Status

# If the order does not exist:

# Payment record not found.

# OPTION 3:

# Display:

# Thank you for using Online Payment System.




from abc import ABC, abstractmethod
class Payment(ABC):
    def __init__(self,Customer_Name,Order_ID,order_fee):
        self.Customer_Name=Customer_Name
        self.Order_ID=Order_ID
        self.order_fee=order_fee
    @abstractmethod
    def validate_payment(self):
        pass 
    @abstractmethod
    def calculate_processing_fee(self):
        pass
    @abstractmethod
    def authenticate_payment(self):
        pass
    @abstractmethod
    def process_payment(self):
        pass
    @abstractmethod
    def generate_receipt(self):
        pass

class UPIPayment(Payment):
    def __init__(self,UPI_ID,UPI_PIN,Customer_Name,Order_ID,order_fee):
        super(). __init__(Customer_Name,Order_ID,order_fee)
        self.UPI_ID=UPI_ID
        self.UPI_PIN=UPI_PIN

    def validate_payment(self):
        if self.UPI_ID=="" or self.UPI_PIN=="":
            print("invalid detail h bhai")
            return False
        else:
            print("details validate successfully dost")
            return True
   
    def calculate_processing_fee(self):
        self.processing_fee=self.order_fee*0/100
        return self.processing_fee
    def authenticate_payment(self):
        if self.UPI_PIN=="1234":
            print("UPI authentication done successfully")
            return True
        else:
            print("Authentication failed")
            return False
  
    def process_payment(self):
        self.total=self.processing_fee+self.order_fee
        print("Payment hogya ")
        return True
    
    def generate_receipt(self):
        print("----- PAYMENT RECEIPT -----")  
        print("Customer Name:",self.Customer_Name)
        print("Order ID:",self.Order_ID)         
        print("Payment Method: UPI") 
        print("Order Amount:",self.order_fee) 
        print("Processing Fee:",self.processing_fee) 
        print("Total Amount:",self.total)

         
class CreditCardPayment(Payment):
    def __init__(self,Card_Number,Card_Holder_Name,CVV,Expiry_Date,Customer_Name,Order_ID,order_fee):
        super(). __init__(Customer_Name,Order_ID,order_fee)
        self.Card_Number=Card_Number
        self.Card_Holder_Name=Card_Holder_Name
        self.CVV=CVV
        self.Expiry_Date=Expiry_Date
    def validate_payment(self):
        if self.Card_Number=="" or self.Card_Holder_Name == "" or self.CVV=="" or self.Expiry_Date=="":
            print("details nhi h bhai aapki")
            return False
        else:
            print("details validate successfully dost")
            return True
   
    def calculate_processing_fee(self):
        self.processing_fee=self.order_fee*2/100
        return self.processing_fee
  
    def authenticate_payment(self):
        if self.CVV=="1234":
            print("UPI authentication done successfully")
            return True
        else:
            print("Authentication failed")
            return False
  
    def process_payment(self):
        self.total=self.processing_fee+self.order_fee
        print("Payment hogya ")
        return True
  
    def generate_receipt(self):
        print("----- PAYMENT RECEIPT -----")  
        print("Customer Name:",self.Customer_Name)
        print("Order ID:",self.Order_ID)         
        print("Payment Method: Credit Card Payment") 
        print("Order Amount:",self.order_fee) 
        print("Processing Fee:",self.processing_fee) 
        print("Total Amount:",self.total)

        
class DebitCardPayment(Payment):
    def __init__(self,Card_Number,Card_Holder_Name,CVV,Expiry_Date,Customer_Name,Order_ID,order_fee):
        super(). __init__(Customer_Name,Order_ID,order_fee)
        self.Card_Number=Card_Number
        self.Card_Holder_Name=Card_Holder_Name
        self.CVV=CVV
        self.Expiry_Date=Expiry_Date
    def validate_payment(self):
        if self.Card_Number=="" or self.Card_Holder_Name == "" or self.CVV=="" or self.Expiry_Date=="":
            print("details nhi h bhai aapki")
            return False
        else:
            print("details validate successfully dost")
            return True
  
    def calculate_processing_fee(self):
        self.processing_fee=self.order_fee*1/100
        return self.processing_fee

    def authenticate_payment(self):
        if self.CVV=="1234":
            print("debit card authentication done successfully")
            return True
        else:
            print("Authentication failed")
            return False      

    def process_payment(self):
        self.total=self.processing_fee+self.order_fee
        print("Payment hogya ")
        return True

    def generate_receipt(self):
        print("----- PAYMENT RECEIPT -----")  
        print("Customer Name:",self.Customer_Name)
        print("Order ID:",self.Order_ID)         
        print("Payment Method: Debit Card Payment") 
        print("Order Amount:",self.order_fee) 
        print("Processing Fee:",self.processing_fee) 
        print("Total Amount:",self.total)


class  NetBankingPayment(Payment):
    def __init__(self,Bank_name,Account_Number,Customer_ID,Customer_Name,Order_ID,order_fee):
        super(). __init__(Customer_Name,Order_ID,order_fee)
        self.Bank_name=Bank_name
        self.Account_Number=Account_Number
        self.Customer_ID=Customer_ID
    def validate_payment(self):
        if self.Bank_name=="" or self.Account_Number == "" or self.Customer_ID=="":
            print("details nhi h bhai aapki")
            return False
        else:
            print("details validate successfully dost")
            return True

    def calculate_processing_fee(self):
        self.processing_fee=self.order_fee*0.5/100
        return self.processing_fee

        
    def authenticate_payment(self):
        if self.Customer_ID=="1234":
            print("net banking authentication done successfully")
            return True
        else:
            print("Authentication failed")
            return False

    def process_payment(self):
        self.total=self.processing_fee+self.order_fee
        print("Payment hogya ")
        return True

    def generate_receipt(self):
        print("----- PAYMENT RECEIPT -----")  
        print("Customer Name:",self.Customer_Name)
        print("Order ID:",self.Order_ID)         
        print("Payment Method: Net Banking Payment") 
        print("Order Amount:",self.order_fee) 
        print("Processing Fee:",self.processing_fee) 
        print("Total Amount:",self.total)
    

class WalletPayment(Payment):
    def __init__(self,Wallet_Name,Mobile_Number,Wallet_PIN,Customer_Name,Order_ID,order_fee):
        super(). __init__(Customer_Name,Order_ID,order_fee)
        self.Wallet_Name=Wallet_Name
        self.Mobile_Number=Mobile_Number
        self.Wallet_PIN=Wallet_PIN
    def validate_payment(self):
        if self.Wallet_Name=="" or self.Mobile_Number== "" or self.Wallet_PIN=="":
            print("details nhi h bhai aapki")
            return False
        else:
            print("details validate successfully dost")
            return True
 
    def calculate_processing_fee(self):
        self.processing_fee=self.order_fee*1.5/100
        return self.processing_fee

    def authenticate_payment(self):
        if self.Wallet_PIN=="1234":
            print("wallet payment authentication done successfully")
            return True
        else:
            print("Authentication failed")
            return False

    def process_payment(self):
        self.total=self.processing_fee+self.order_fee
        print("Payment hogya ")
        return True

    def generate_receipt(self):
        print("----- PAYMENT RECEIPT -----")  
        print("Customer Name:",self.Customer_Name)
        print("Order ID:",self.Order_ID)         
        print("Payment Method: Wallet Payment") 
        print("Order Amount:",self.order_fee) 
        print("Processing Fee:",self.processing_fee) 
        print("Total Amount:",self.total)










