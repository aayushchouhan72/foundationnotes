# QNO 1: Bank Account Management System

# ABC Bank wants to develop a software application to manage customer accounts.

# Each customer has:

# Account Number
# Customer Name
# Account Balance

# A customer should be able to:

# Deposit money
# Withdraw money
# Check account balance
# Transfer money to another customer

# The bank also wants to maintain information that is common for all customers:

# Bank Name
# Interest Rate

# The bank management may change the interest rate in the future, and the change should apply to all customers.

# Additionally, the application should provide some utility operations:

# Validate whether an account number is valid.
# Calculate interest on a given amount.
# Generate a transaction ID.
# Requirements

# Class Variables

# bank_name
# interest_rate

# Instance Variables

# account_no
# customer_name
# balance

# Instance Methods

# deposit(amount)
# withdraw(amount)
# transfer_money(receiver, amount)
# display_balance()

# Class Methods

# change_interest_rate(new_rate)
# change_bank_name(new_name)
# display_bank_info()

# Static Methods

# validate_account_number(account_no)
# calculate_interest(amount, rate)
# generate_transaction_id()

# Sample Input
# Customer 1
# Account No : 1001
# Name       : deepika
# Balance    : 50000

# Customer 2
# Account No : 1002
# Name       : Priya
# Balance    : 30000

# Deposit Amount : 10000
# Transfer Amount : 15000
# New Interest Rate : 7.5
# Sample Output
# Customer : deepika
# Balance  : 45000

# Customer : Priya
# Balance  : 45000

# Bank Name      : ABC Bank
# Interest Rate  : 7.5%
# Transaction ID : TXN1025

# Task: Design a Python class named BankAccount and implement all the above methods using instance methods, class methods, and static methods appropriately.

import random


class BankAccount:

  
    bank_name = "ABC Bank"
    interest_rate = 5.0

  
    def __init__(self, account_no, customer_name, balance):
        self.account_no = account_no
        self.customer_name = customer_name
        self.balance = balance



    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def transfer_money(self, receiver, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            receiver.balance += amount

            print("Transfer successful.")
            print("Transaction ID:", BankAccount.generate_transaction_id())
        else:
            print("Transfer failed.")

    def display_balance(self):
        print("Customer :", self.customer_name)
        print("Balance  :", self.balance)

   

    @classmethod
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @classmethod
    def display_bank_info(cls):
        print("Bank Name     :", cls.bank_name)
        print("Interest Rate :", cls.interest_rate, "%")

    

    @staticmethod
    def validate_account_number(account_no):
        return len(str(account_no)) == 4 and str(account_no).isdigit()

    @staticmethod
    def calculate_interest(amount, rate):
        return (amount * rate) / 100

    @staticmethod
    def generate_transaction_id():
        return "TXN" + str(random.randint(1000, 9999))




customer1 = BankAccount(1001, "deepika", 50000)
customer2 = BankAccount(1002, "Priya", 30000)

customer1.deposit(10000)

customer1.transfer_money(customer2, 15000)

customer1.display_balance()
customer2.display_balance()

BankAccount.change_interest_rate(7.5)

BankAccount.display_bank_info()

print("Transaction ID :", BankAccount.generate_transaction_id())









