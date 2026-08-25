# 1.

# =========================================
# ONLINE SHOPPING CART
# ====================

# A shopping website stores purchased products in a dictionary where:
# Key = Product Name
# Value = Quantity Purchased

# Write a program to:

# * Accept a dictionary from the user.
# * Calculate and display the total quantity of products purchased.

# Sample Input:
# {"Laptop":2,"Mouse":3,"Keyboard":1}

# Sample Output:
# Total Quantity = 6

# ---

number = int(input("Enter the number of iteams"))

dic ={}
sum=0
for i in range(number):
     key = input("ENter the key ...")
     value=input("ENter the Value ...")
     dic[key] = value
     sum+=int(value)

print(dic)
print("Total Quantity =",sum)

