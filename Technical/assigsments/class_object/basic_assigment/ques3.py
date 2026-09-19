# Assignment 3: Bank Account Operations
#  A bank wants to perform basic operations on a customer's account.

# Create a class BankAccount with the following attributes:

# Account number

# Account holder name

# Balance

# Create the following methods:

# deposit() – Add an amount to the balance.

# withdraw() – Subtract an amount from the balance.

# display_account() – Display account details and final balance.

# Sample data:

# Account Number: 1001
# Account Holder: Rahul
# Opening Balance: 25000
# Deposit: 5000
# Withdrawal: 3000

# Expected result:

# Final Balance: 27000

# # 

class BankAccount:
    def __init__(self, accnumber, accname, openingbal):
        self.accnumber = accnumber
        self.accname = accname
        self.openingbal = openingbal
        self.bal = openingbal
        self.total_deposit = 0
        self.total_withdraw = 0

    def deposit(self, amount):
        self.bal += amount
        self.total_deposit += amount
        print("Amount deposited successfully...")

    def withdraw(self, amount):
        if self.bal >= amount:
            self.bal -= amount
            self.total_withdraw += amount
            print("Amount withdrawn successfully...")
        else:
            print("Account balance is not sufficient...")

    def display_account(self):
        print(f"""
Account Number   : {self.accnumber}
Account Holder   : {self.accname}
Opening Balance  : {self.openingbal}
Deposit          : {self.total_deposit}
Withdrawal       : {self.total_withdraw}
Final Balance    : {self.bal}
""")

accnumber = input("Enter the Account Number: ")
accname = input("Enter the Account Holder Name: ")
openingbal = float(input("Enter the Opening Balance: "))


s1 = BankAccount(accnumber, accname, openingbal)

s1.deposit(5000)
s1.withdraw(3000)

s1.display_account()