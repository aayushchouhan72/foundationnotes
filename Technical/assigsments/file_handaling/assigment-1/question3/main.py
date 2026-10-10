


# 3. Online Shopping Order History

# An e-commerce company maintains order information in orders.txt.

# Each order contains:

# OrderID,CustomerName,Product,Quantity,Price
# Task

# Write a program to:

# Accept order details.
# Store them in the file.
# Read the file.
# Calculate total amount for each order.
# Display the order having the highest total amount.

# Formula:

# Total Amount = Quantity × Price
# Sample Input
# Enter number of orders: 3

# O101,Rahul,Laptop,1,55000
# O102,Priya,Mouse,3,800
# O103,Amit,Keyboard,2,1500
# Expected Output
# Order Details
# --------------------------------
# O101 Rahul Laptop   Quantity: 1 Total: 55000
# O102 Priya Mouse    Quantity: 3 Total: 2400
# O103 Amit Keyboard  Quantity: 2 Total: 3000

# Highest Order:
# Order ID: O101
# Customer: Rahul
# Total Amount: 55000
# ================


number = int(input("Enter the number of product ..."))

for _ in range(number):
    print("\n\n")
    OrderID = int(input("Enter the Order ID ..."))
    CustomerName = input("Enter the Customer Name ...")
    Product=  input("Enter the Product ...")
    Quantity= int(input("Enter the Quantity"))
    Price= float(input("Enter the Price ..."))
    with open("question2/employees.txt","+a") as f:
        f.write(f"{OrderID },{CustomerName},{Product},{Quantity},{Price}\n")

with open("question2/employees.txt","+r") as f:
    data = f.readlines()

*all,q,p,e=data[0].split(",")
amount=int(q)*int(p)
total=0
for line in data:
   OrderID,CustomerName,Product,Quantity,price,e=line.split(",")
   print(f"{OrderID },{CustomerName},{Product},Quantity:-{Quantity},Total:-{Quantity*Price}")
   if amount<Quantity*price:
     cus=line
oid,cname,pro,q,p,e=line.split(",")
print(f"""
Highest Order:
Order ID: {oid}
Customer: {cname}
Total Amount: {int(q)*int(p)}
""")