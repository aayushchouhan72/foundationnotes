class Customer:

    def __init__(self, customer_id, customer_name, city, purchase_amount):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.city = city
        self.purchase_amount = purchase_amount

    def display(self):
        print(
            self.customer_id,
            self.customer_name,
            self.city,
            self.purchase_amount
        )