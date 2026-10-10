from abc import ABC, abstractmethod
import random


class Payment(ABC):

    def __init__(self, customer_name, order_id, order_amount):
        self.customer_name = customer_name
        self.order_id = order_id
        self.order_amount = order_amount
        self.processing_fee = 0
        self.final_amount = 0
        self.transaction_id = None
        self.status = "PENDING"

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

    def __init__(self, customer_name, order_id, order_amount,
                 upi_id, upi_pin):

        super().__init__(customer_name, order_id, order_amount)

        self.upi_id = upi_id
        self.upi_pin = upi_pin
        self.payment_method = "UPI"

    def validate_payment(self):

        if "@" in self.upi_id and len(self.upi_pin) == 4:
            return True

        return False

    def calculate_processing_fee(self):

        self.processing_fee = 0
        self.final_amount = self.order_amount

    def authenticate_payment(self):

        return len(self.upi_pin) == 4

    def process_payment(self):

        self.transaction_id = "TXN" + str(random.randint(100000, 999999))
        self.status = "SUCCESS"

    def generate_receipt(self):

        return {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "payment_method": self.payment_method,
            "order_amount": self.order_amount,
            "processing_fee": self.processing_fee,
            "final_amount": self.final_amount,
            "transaction_id": self.transaction_id,
            "status": self.status
        }


class CreditCardPayment(Payment):

    def __init__(self, customer_name, order_id, order_amount,
                 card_number, card_holder_name, cvv, expiry_date):

        super().__init__(customer_name, order_id, order_amount)

        self.card_number = card_number
        self.card_holder_name = card_holder_name
        self.cvv = cvv
        self.expiry_date = expiry_date
        self.payment_method = "Credit Card"

    def validate_payment(self):

        if (len(self.card_number) == 16 and
                len(self.cvv) == 3 and
                self.expiry_date):

            return True

        return False

    def calculate_processing_fee(self):

        self.processing_fee = self.order_amount * 0.02
        self.final_amount = self.order_amount + self.processing_fee

    def authenticate_payment(self):

        return len(self.cvv) == 3

    def process_payment(self):

        self.transaction_id = "TXN" + str(random.randint(100000, 999999))
        self.status = "SUCCESS"

    def generate_receipt(self):

        return {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "payment_method": self.payment_method,
            "order_amount": self.order_amount,
            "processing_fee": self.processing_fee,
            "final_amount": self.final_amount,
            "transaction_id": self.transaction_id,
            "status": self.status
        }


class DebitCardPayment(Payment):

    def __init__(self, customer_name, order_id, order_amount,
                 card_number, card_holder_name, cvv, expiry_date):

        super().__init__(customer_name, order_id, order_amount)

        self.card_number = card_number
        self.card_holder_name = card_holder_name
        self.cvv = cvv
        self.expiry_date = expiry_date
        self.payment_method = "Debit Card"

    def validate_payment(self):

        if (len(self.card_number) == 16 and
                len(self.cvv) == 3 and
                self.expiry_date):

            return True

        return False

    def calculate_processing_fee(self):

        self.processing_fee = self.order_amount * 0.01
        self.final_amount = self.order_amount + self.processing_fee

    def authenticate_payment(self):

        return len(self.cvv) == 3

    def process_payment(self):

        self.transaction_id = "TXN" + str(random.randint(100000, 999999))
        self.status = "SUCCESS"

    def generate_receipt(self):

        return {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "payment_method": self.payment_method,
            "order_amount": self.order_amount,
            "processing_fee": self.processing_fee,
            "final_amount": self.final_amount,
            "transaction_id": self.transaction_id,
            "status": self.status
        }


class NetBankingPayment(Payment):

    def __init__(self, customer_name, order_id, order_amount,
                 bank_name, account_number, customer_id):

        super().__init__(customer_name, order_id, order_amount)

        self.bank_name = bank_name
        self.account_number = account_number
        self.customer_id = customer_id
        self.payment_method = "Net Banking"

    def validate_payment(self):

        if self.bank_name and self.account_number and self.customer_id:
            return True

        return False

    def calculate_processing_fee(self):

        self.processing_fee = self.order_amount * 0.005
        self.final_amount = self.order_amount + self.processing_fee

    def authenticate_payment(self):

        return bool(self.customer_id)

    def process_payment(self):

        self.transaction_id = "TXN" + str(random.randint(100000, 999999))
        self.status = "SUCCESS"

    def generate_receipt(self):

        return {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "payment_method": self.payment_method,
            "order_amount": self.order_amount,
            "processing_fee": self.processing_fee,
            "final_amount": self.final_amount,
            "transaction_id": self.transaction_id,
            "status": self.status
        }


class WalletPayment(Payment):

    def __init__(self, customer_name, order_id, order_amount,
                 wallet_name, mobile_number, wallet_pin):

        super().__init__(customer_name, order_id, order_amount)

        self.wallet_name = wallet_name
        self.mobile_number = mobile_number
        self.wallet_pin = wallet_pin
        self.payment_method = "Wallet"

    def validate_payment(self):

        if self.wallet_name and len(self.mobile_number) == 10:
            return True

        return False

    def calculate_processing_fee(self):

        self.processing_fee = self.order_amount * 0.015
        self.final_amount = self.order_amount + self.processing_fee

    def authenticate_payment(self):

        return len(self.wallet_pin) == 4

    def process_payment(self):

        self.transaction_id = "TXN" + str(random.randint(100000, 999999))
        self.status = "SUCCESS"

    def generate_receipt(self):

        return {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "payment_method": self.payment_method,
            "order_amount": self.order_amount,
            "processing_fee": self.processing_fee,
            "final_amount": self.final_amount,
            "transaction_id": self.transaction_id,
            "status": self.status
        }