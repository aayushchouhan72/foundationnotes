# 3.
# ONLINE SHOPPING SYSTEM

# Scenario:

# An e-commerce company wants to develop an Online Shopping System.
#  The application should be menu-driven and should demonstrate different types of arguments used in Python functions.

# MENU

# 1. Customer Registration
# 2. Product Information
# 3. Generate Invoice
# 4. Add Multiple Products
# 5. Display Customer Profile
# 6. Exit

# Requirements

# Choice 1 – Customer Registration

# * Accept Customer Name, Email, and Mobile Number.
# * Pass the values to a function using Positional Arguments.
# * Display the registered customer details.

# Choice 2 – Product Information

# * Accept Product Name, Price, and Category.
# * Call the function using Keyword Arguments.
# * Display the product details.

# Choice 3 – Generate Invoice

# * Accept Product Name and Price.
# * Tax Percentage should have a default value.
# * Use Default Arguments while generating the invoice.
# * Display the final amount.

# Choice 4 – Add Multiple Products

# * Allow the user to enter any number of product prices.
# * Pass all prices to a function using Variable Length Arguments (*args).
# * Calculate and display the total bill amount.

# Choice 5 – Display Customer Profile

# * Accept any number of customer details such as Name, City, Email, Mobile, Membership Type, etc.
# * Pass the details using Arbitrary Keyword Arguments (**kwargs).
# * Display all customer information.

# Choice 6 – Exit

# Sample Execution

# Enter Choice : 1

# Enter Name : Ajay
# Enter Email : [ajay@gmail.com](mailto:ajay@gmail.com)
# Enter Mobile : 9876543210

# Customer Registered Successfully

# ---

# Enter Choice : 2

# Enter Product Name : Laptop
# Enter Price : 55000
# Enter Category : Electronics

# Product Details Displayed Successfully

# ---

# Enter Choice : 3

# Enter Product Name : Laptop
# Enter Price : 55000

# Invoice Generated Successfully

# ---

# Enter Choice : 4

# Enter Number of Products : 4

# Enter Price 1 : 100
# Enter Price 2 : 200
# Enter Price 3 : 300
# Enter Price 4 : 400

# Total Bill Amount : 1000

# ---

# Enter Choice : 5

# Customer Profile Displayed Successfully

# ---

# Enter Choice : 6

# Thank You. Program Terminated.

# Important Instructions

# 1. Choice 1 must use Positional Arguments.
# 2. Choice 2 must use Keyword Arguments.
# 3. Choice 3 must use Default Arguments.
# 4. Choice 4 must use Variable Length Arguments (*args).
# 5. Choice 5 must use Arbitrary Keyword Arguments (**kwargs).
# 6. Use separate functions for each menu option.
# 7. Implement the solution using a menu-driven approach.
# 8. Maintain proper code readability and formatting.

# Note:
# Marks will be awarded based on the correct usage of the specified argument type in each menu option.


print("="*25)
print("ONLINE SHOPPING SYSTEM")
print("="*25)

def regisetercustomer(name ,email,number):
     return users.append({'name':name,"email":email,'number':number})

def productinfo(name,price,category):
     return product.append({'name':name,"price":price,'category':category})

def genrateinvoice(number=0):
     if number ==  0:
           print("Enter the valid number to check ")
           return
     sum=0
     for pro in product:
          sum += pro['price']
     return sum

def addmulti(n):
     sum=0
     count=1
     for pro in range(n):
          price=  int(input(f"Enter the price {count} :"))
          count+=1
          sum +=price
     return sum
            
users = []
product=[]   
while True:
  print('''
1. Customer Registration\n
2. Product Information\n
3. Generate Invoice\n
4. Add Multiple Products\n
5. Display Customer Profile\n
6. Exit

''')
  choice =  input("Enter the your choice ...")
  match choice:
      case "1":
            print("Customer Registration ...")
            name= input("Enter the number customer Name:-")
            email  = input("Enter the Email :- ")
            number  = input("Enter the number :- ")
            user =  regisetercustomer(name,email,number)
            print("User is registed successfully ...")
      case "2":
            print("Product Information ...")
            name= input("Enter the product Name :-")
            price  = int(input("Enter the price :- "))
            category = input("Enter the category :- ")
            user =  productinfo(name=name,price=price,category=category)
      case "3":
         print("Generate Invoice ...")
         totalbill =  genrateinvoice(number)
         print("Total bill is ",totalbill)
      case "4":
         print("Add Multiple Products ...")
         number = int(input("Enter the number of product :- "))
         print("Total Bill Amount : ",addmulti(number))
        
      case "5":
            print("Customer Profile displayed successfully ...")

      case "6":
           print("Thankyou for using an application")
           break
      case _:
           print("Enter the Invalid input")
