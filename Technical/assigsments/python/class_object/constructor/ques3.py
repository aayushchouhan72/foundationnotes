# Question 3: Online Shopping System
# Scenario

# An e-commerce company wants to calculate the final amount payable by customers after applying discounts.

# Requirements

# Create a class named Product with:

# product_id
# product_name
# quantity
# price_per_item

# Initialize the values using a constructor.

# Calculations
# Total Amount = Quantity × Price Per Item
# If Total Amount > ₹5000, Discount = 10%
# Otherwise, Discount = 5%
# Final Amount = Total Amount − Discount
# Sample Input
# Enter Product ID : P101
# Enter Product Name : Laptop
# Enter Quantity : 2
# Enter Price Per Item : 35000
# Sample Output
# ------ Shopping Bill ------
# Product ID        : P101
# Product Name      : Laptop
# Quantity          : 2
# Price Per Item    : 35000.0
# Total Amount      : ₹70000.0
# Discount          : ₹7000.0
# Final Amount      : ₹63000.0


class product:
    def __init__(self,e,n,s,p):
        self.pid=e
        self.pq=s
        self.pname=n
        self.ppr=p
      
    def billgen(self):
        if self.ppr*self.pq>5000:
            self.bill=self.ppr*self.pq-(self.ppr*self.pq)*0.10
            return self.ppr*self.pq*0.10
        else:
            self.bill=self.ppr*self.pq-(self.ppr*self.pq)*0.05
            return self.ppr*self.pq*0.10

    
pid = input("Enter the  product id ...")
pname= input("Enter the product name ...")
punit= int(input("Enter the quantity ..."))
pperp=float(input("Enter the per product price ..."))
s= product(pid,pname,punit,pperp)

print(f"""
------ Shopping Bill ------
Product ID        : {s.pid}
Product Name      : {s.pname}
Quantity          : {s.pq}
Price Per Item    : {s.ppr}
Total Amount      : {s.bill}
Discount          : {s.billgen()}
Final Amount      : {s.bill}
""")

