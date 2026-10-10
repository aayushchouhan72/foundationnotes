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
from payment.payments import (
    UPIPayment,
    CreditCardPayment,
    DebitCardPayment,
    NetBankingPayment,
    WalletPayment
)


payments = {}


def make_payment():

    print("\n========================================")
    print("            MAKE PAYMENT")
    print("========================================")

    customer_name = input("Enter Customer Name: ")
    order_id = input("Enter Order ID: ")
    order_amount = float(input("Enter Order Amount: "))

    print("\nSelect Payment Method")

    print("1. UPI")
    print("2. Credit Card")
    print("3. Debit Card")
    print("4. Net Banking")
    print("5. Wallet")

    choice = input("Enter your choice: ")

    payment = None

    if choice == "1":

        upi_id = input("Enter UPI ID: ")
        upi_pin = input("Enter UPI PIN: ")

        payment = UPIPayment(
            customer_name,
            order_id,
            order_amount,
            upi_id,
            upi_pin
        )

    elif choice == "2":

        card_number = input("Enter Card Number: ")
        card_holder = input("Enter Card Holder Name: ")
        cvv = input("Enter CVV: ")
        expiry = input("Enter Expiry Date: ")

        payment = CreditCardPayment(
            customer_name,
            order_id,
            order_amount,
            card_number,
            card_holder,
            cvv,
            expiry
        )

    elif choice == "3":

        card_number = input("Enter Card Number: ")
        card_holder = input("Enter Card Holder Name: ")
        cvv = input("Enter CVV: ")
        expiry = input("Enter Expiry Date: ")

        payment = DebitCardPayment(
            customer_name,
            order_id,
            order_amount,
            card_number,
            card_holder,
            cvv,
            expiry
        )

    elif choice == "4":

        bank_name = input("Enter Bank Name: ")
        account_number = input("Enter Account Number: ")
        customer_id = input("Enter Customer ID: ")

        payment = NetBankingPayment(
            customer_name,
            order_id,
            order_amount,
            bank_name,
            account_number,
            customer_id
        )

    elif choice == "5":

        wallet_name = input("Enter Wallet Name: ")
        mobile_number = input("Enter Mobile Number: ")
        wallet_pin = input("Enter Wallet PIN: ")

        payment = WalletPayment(
            customer_name,
            order_id,
            order_amount,
            wallet_name,
            mobile_number,
            wallet_pin
        )

    else:

        print("Invalid payment method.")
        return

    payment.calculate_processing_fee()

    print("\n========================================")
    print("          PAYMENT PROCESSING")
    print("========================================")

    print(f"Customer Name       : {customer_name}")
    print(f"Order ID            : {order_id}")
    print(f"Payment Method      : {payment.payment_method}")

    print(f"\nOrder Amount        : Rs.{payment.order_amount:.2f}")
    print(f"Processing Fee      : Rs.{payment.processing_fee:.2f}")
    print(f"Final Amount        : Rs.{payment.final_amount:.2f}")

    print("\nValidating payment details...")

    if not payment.validate_payment():

        print("Payment validation failed.")
        return

    print("Payment details validated successfully.")

    print("\nAuthenticating payment...")

    if not payment.authenticate_payment():

        print("Authentication failed.")
        return

    print("Authentication successful.")

    print("\nProcessing payment...")

    payment.process_payment()

    print("Payment processed successfully.")

    print(f"\nTransaction ID      : {payment.transaction_id}")
    print(f"Payment Status      : {payment.status}")

    payments[order_id] = payment


def view_payment():

    order_id = input("\nEnter Order ID: ")

    if order_id not in payments:

        print("Payment record not found.")
        return

    payment = payments[order_id]

    print("\n========================================")
    print("          PAYMENT DETAILS")
    print("========================================")

    print(f"Order ID            : {payment.order_id}")
    print(f"Customer Name       : {payment.customer_name}")
    print(f"Payment Method      : {payment.payment_method}")
    print(f"Order Amount        : Rs.{payment.order_amount:.2f}")
    print(f"Processing Fee      : Rs.{payment.processing_fee:.2f}")
    print(f"Final Amount        : Rs.{payment.final_amount:.2f}")
    print(f"Transaction ID      : {payment.transaction_id}")
    print(f"Payment Status      : {payment.status}")

    print("========================================")


def main():

    while True:

        print("\n========================================")
        print("       ONLINE PAYMENT SYSTEM")
        print("========================================")

        print("1. Make Payment")
        print("2. View Payment Details")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            make_payment()

        elif choice == "2":

            view_payment()

        elif choice == "3":

            print("\nThank you for using Online Payment System.")
            break

        else:

            print("Invalid choice.")


main()
    
  