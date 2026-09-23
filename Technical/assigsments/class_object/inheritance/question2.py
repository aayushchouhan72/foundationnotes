
# ASSIGNMENT 2 — BANK ACCOUNT MANAGEMENT SYSTEM
# =============================================

# A bank provides different types of accounts.

# Create the following hierarchy:

# Account
# |
# +-------- SavingsAccount
# |
# +-------- PremiumSavingsAccount

# REQUIREMENTS:

# 1. Create a parent class Account.

# Attributes:

# * account_number
# * customer_name
# * balance

# 2. SavingsAccount should inherit from Account.

# Additional attribute:

# * interest_rate

# 3. PremiumSavingsAccount should inherit from SavingsAccount.

# Additional attribute:

# * cashback_percentage

# 4. Parent-class data must be initialized using super().

# 5. Create the following methods:

# display_account()
# deposit()
# withdraw()

# 6. Override display_account() in SavingsAccount.

# 7. Override display_account() again in PremiumSavingsAccount.

# 8. Each overridden method must call the parent method using super().

# 9. Demonstrate multilevel inheritance.

# 10. Balance must be encapsulated using:

# @property
# @balance.setter
# @balance.deleter

# 11. Balance cannot be negative.

# 12. Read all data from the user.

# INPUT:

# Enter Account Number:
# Enter Customer Name:
# Enter Initial Balance:
# Enter Account Type:

# 1. Savings Account
# 2. Premium Savings Account

# For Savings Account:

# Enter Interest Rate:

# For Premium Savings Account:

# Enter Interest Rate:
# Enter Cashback Percentage:

# Then ask:

# Enter amount to deposit:
# Enter amount to withdraw:

# SAMPLE INPUT:

# Enter Account Number: 1001
# Enter Customer Name: Amit
# Enter Initial Balance: 25000
# Enter Account Type: 2
# Enter Interest Rate: 7
# Enter Cashback Percentage: 2
# Enter amount to deposit: 5000
# Enter amount to withdraw: 3000

# EXPECTED OUTPUT:

# ## Account Details

# Account Number: 1001
# Customer Name: Amit
# Balance: 25000

# Account Type: Premium Savings Account
# Interest Rate: 7%
# Cashback Percentage: 2%

# After Deposit:
# Balance: 30000

# After Withdrawal:
# Balance: 27000

class Account():
    def __init__(self,account_number,customer_name,balance):
        self.account_number=account_number
        self.customer_name=customer_name
        self.balance=balance

    def display_account(self,Account,account_number,customer_name,balance):
        super(). __init__(account_number,customer_name,balance)

    def deposit(self,balance):
             self.balance+=balance

    def withdraw(self):
        if balance<self.balance:
            self.balance-=balance
        else:
            print("bhai tere paas to paise hi nhi h sale gareeb")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,price):
        self.__balance=price
        

    @balance.deleter
    def balance(self):
        del self.__balance

    
class Savingsaccount(Account):
    def __init__(self,interest_rate,account_number,customer_name,balance):
        print(interest_rate,account_number,customer_name,balance)
        super(). __init__(account_number,customer_name,balance)
        self.interest_rate=interest_rate

    def display_account(self):
        print(interest_rate,account_number,customer_name,balance)

    
class PremiumSavingsAccount(Savingsaccount):
    def __init__(self,cashback_percentage,interest_rate,account_number,customer_name,balance):
        super().__init__(interest_rate,account_number,customer_name,balance)
        self.cashback_percentage=cashback_percentage
    def display_account(self):
        print(interest_rate,account_number,customer_name,balance)

account_number=int(input("Enter Account Number:"))
customer_name=input("Enter Customer Name:")
balance=int(input("Enter Initial Balance:"))
cashback_percentage=int(input("enter cashback percentage here"))
interest_rate=int(input("enter interest_rate here"))
print("""what account type is yours" 
        1-  Savingsaccount
        2-  PremiumSavingsAccount """)


choice=int(input("enter the account type...1 or 2"))
if choice==1:
    obj=Savingsaccount(interest_rate,account_number,customer_name,balance)
    obj.display_account()

elif choice==2:
    obj=PremiumSavingsAccount(cashback_percentage,interest_rate,account_number,customer_name,balance)
    obj.display_account()