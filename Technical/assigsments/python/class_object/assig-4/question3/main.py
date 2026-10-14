# ============================================================
# ASSIGNMENT 3 – Product INVENTORY SYSTEM
# =======================================

# Create a `Product` class inside:

# models/Product.py

# ATTRIBUTES:

# * Product_id
# * Product_name
# * price
# * quantity

# TASKS:

# 1. Take details of 5 Products from the user.

# 2. Create Product objects.

# 3. Store all objects in a list.

# 4. Display all Products.

# 5. Calculate total value of each Product.

#    Total Value = Price × Quantity

# 6. Display Products whose quantity is less than 10.

# 7. Find the Product having the highest price.

# 8. Calculate total inventory value.

# 9. Search a Product using Product Id.

# SAMPLE INPUT:

# 101 Laptop 55000 5
# 102 Mouse 800 25
# 103 Keyboard 1500 12
# 104 Monitor 12000 7
# 105 Printer 9000 15

# EXPECTED OUTPUT:

# All Products:
# 101 Laptop 55000 5
# 102 Mouse 800 25
# 103 Keyboard 1500 12
# 104 Monitor 12000 7
# 105 Printer 9000 15

# Product Total Values:
# Laptop = 275000
# Mouse = 20000
# Keyboard = 18000
# Monitor = 84000
# Printer = 135000

# Low Stock Products:
# Laptop
# Monitor

# Highest Price Product:
# Laptop = 55000

# Total Inventory Value:
# 532000

# Search Product Id: 103

# Product Found:
# 103 Keyboard 1500 12

from models.product import Product
num= int(input("Enter the number of Product ..."))
Products=[]

for _ in range(num): 
     pid =  int(input("Enter the product id ..."))
     pname= input("Enter the Product name ...")
     pprice= int(input("Enter the Product salary ..."))
     pqan=int(input("Enter the student department ..."))
     obj=Product(pid,pname,pprice,pqan)
     Products.append(obj)


Product.display_products(Products)
Product.display_product_with_cost(Products)
Product.display_employe_it_dep(Products)
Product.highest_price_product(Products)
print(Product.sum_of_product_quantity(Products))
key =  int(input("Enter the key of product to Find ? "))
print(Product.product_find_by_key(Products))

