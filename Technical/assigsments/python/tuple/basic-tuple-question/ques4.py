# =====================================================================
# QUESTION 4: ONLINE SHOPPING ORDERS
# ==================================

# An online shopping company stores customer orders using NamedTuple.

# Fields:
# order_id, customer_name, product_name, amount

# Requirements:

# 1. Read N order records from the user and store them in a list of NamedTuples.

# ---

# 2. Display all order details.

# ---

# 3. Find and display the order having the highest amount.

# ---

# 4. Calculate and display total sales.

# ---

# 5. Count the number of orders whose amount is greater than ₹10,000.

# ---

# Test Case:

# Input:
# Enter number of orders: 5

# O101 Rahul Laptop 55000
# O102 Priya Mouse 800
# O103 Amit Mobile 25000
# O104 Neha Keyboard 1500
# O105 Rakesh TV 45000

# Expected Output:
# Highest Value Order:
# O101 Rahul Laptop 55000

# Total Sales:
# 127300

# Orders Above ₹10,000:
# 3
# # 



from collections import namedtuple 

student =  namedtuple("Student",["order_id", "customer_name", "product_name", "amount"])

lis=[]
number =  int(input("Enter the number of orders "))

print()
for i in range(number):
    print()
    order_id = int(input("Enter the order id ...."))
    customer_name =  input("Enter the customer ....")
    product_name = input("Enter the product name ....")
    amount = int(input("Enter product price ...."))
    lis.append(student(order_id, customer_name, product_name, amount))
    print()
patentabove10t=0
user=0
maximum =0
total=0
for i  in lis:
     print(i.order_id, i.customer_name, i.product_name, i.amount)
     if i.amount>10000:
          patentabove10t+=1
     if maximum<i.amount:
          user = i
          maximum=i.amount
     total+=i.amount
     print()

print(f"maximum order price is {user.amount} and user is {user} \ncustomer above 10,000 is {patentabove10t}\ntotle sales is {total}")
