# Question 2: Electricity Bill Calculator
# Scenario


# An electricity company wants to generate monthly bills for its customers.

# Requirements

# Create a class named Customer with:

# customer_id
# customer_name
# units_consumed

# Initialize the values using a constructor.

# Calculations
# Cost per Unit = ₹8
# Fixed Charge = ₹150
# Total Bill = (Units × 8) + 150
# Sample Input
# Enter Customer ID : C101
# Enter Customer Name : Amit Verma
# Enter Units Consumed : 350
# Sample Output
# ------ Electricity Bill ------
# Customer ID       : C101
# Customer Name     : Amit Verma
# Units Consumed    : 350
# Total Bill Amount : ₹2950.0

class customer:
    def __init__(self,e,n,s):
        self.cid=e
        self.uconsumed=s
        self.cname=n
        self.fixed=150
        self.cost=8
    def billcal(self):
        self.bill=self.uconsumed*self.cost+self.fixed
        return self.bill
    
cid = input("Enter the  customer id ...")
cname= input("Enter the customer name ...")
cunit= int(input("Enter the consumed unit..."))
s= customer(cid,cname,cunit)

print(f"""
------ Electricity Bill ------
Customer ID       : {s.cid}
Customer Name     : {s.cname}
Units Consumed    : {s.uconsumed}
Total Bill Amount : {s.billcal()}
""")

