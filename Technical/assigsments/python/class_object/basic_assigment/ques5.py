class ShoppingBill:
    def __init__(self, pname, price, quantity, discount, gst):
        self.pname = pname
        self.price = price
        self.quantity = quantity
        self.discount = discount
        self.gst = gst

        self.subtotal = 0
        self.discount_amount = 0
        self.discounted_amount = 0
        self.gst_amount = 0
        self.final_bill = 0

    def calculate_subtotal(self):
        self.subtotal = self.price * self.quantity

    def calculate_discount(self):
        self.discount_amount = self.subtotal * self.discount / 100
        self.discounted_amount = self.subtotal - self.discount_amount

    def calculate_gst(self):
        self.gst_amount = self.discounted_amount * self.gst / 100

    def calculate_final_bill(self):
        self.final_bill = self.discounted_amount + self.gst_amount

    def display_bill(self):
        print(f"""
Product Name       : {self.pname}
Product Price      : {self.price}
Quantity            : {self.quantity}
Subtotal            : {self.subtotal}
Discount Percentage : {self.discount}%
Discount Amount     : {self.discount_amount}
Discounted Amount   : {self.discounted_amount}
GST Percentage      : {self.gst}%
GST Amount          : {self.gst_amount}
Final Bill          : {self.final_bill}
""")


pname = input("Enter the Product Name ...")
price = float(input("Enter the Product Price ..."))
quantity = int(input("Enter the Quantity ..."))
discount = float(input("Enter the Discount Percentage ..."))
gst = float(input("Enter the GST Percentage ..."))

s1 = ShoppingBill(pname, price, quantity, discount, gst)

s1.calculate_subtotal()
s1.calculate_discount()
s1.calculate_gst()
s1.calculate_final_bill()
s1.display_bill()