class ExpenseTracker:
    def __init__(self, pname, salary, rent, food, travel, other):
        self.pname = pname
        self.salary = salary
        self.rent = rent
        self.food = food
        self.travel = travel
        self.other = other

        self.totalexpenses = 0
        self.savings = 0

    def calculate_total_expenses(self):
        self.totalexpenses = self.rent + self.food + self.travel + self.other

    def calculate_savings(self):
        self.savings = self.salary - self.totalexpenses

    def display_expense_report(self):
        print(f"""
Person Name       : {self.pname}
Monthly Salary    : {self.salary}
Rent              : {self.rent}
Food Expenses     : {self.food}
Travel Expenses   : {self.travel}
Other Expenses    : {self.other}
Total Expenses    : {self.totalexpenses}
Savings            : {self.savings}
""")


pname = input("Enter the Person Name ...")
salary = float(input("Enter the Monthly Salary ..."))
rent = float(input("Enter the Rent ..."))
food = float(input("Enter the Food Expenses ..."))
travel = float(input("Enter the Travel Expenses ..."))
other = float(input("Enter the Other Expenses ..."))

e1 = ExpenseTracker(pname, salary, rent, food, travel, other)

e1.calculate_total_expenses()
e1.calculate_savings()
e1.display_expense_report()
