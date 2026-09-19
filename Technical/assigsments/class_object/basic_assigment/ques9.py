class Product:
    def __init__(self, pid, pname, price, quantity):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

        self.stockvalue = 0

    def add_stock(self, amount):
        self.quantity += amount
        print("Stock added successfully ...")

    def sell_product(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            print("Product sold successfully ...")
        else:
            print("Stock is not sufficient ...")

    def calculate_stock_value(self):
        self.stockvalue = self.price * self.quantity

    def display_product(self):
        print(f"""
Product ID          : {self.pid}
Product Name        : {self.pname}
Price               : {self.price}
Available Quantity  : {self.quantity}
Total Stock Value   : {self.stockvalue}
""")


pid = input("Enter the Product ID ...")
pname = input("Enter the Product Name ...")
price = float(input("Enter the Price ..."))
quantity = int(input("Enter the Initial Quantity ..."))

p1 = Product(pid, pname, price, quantity)

p1.add_stock(5)
p1.sell_product(3)
p1.calculate_stock_value()
p1.display_product()