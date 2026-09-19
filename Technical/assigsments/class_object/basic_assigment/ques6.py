class ElectricityBill:
    def __init__(self, cnumber, cname, units, rate, fixed):
        self.cnumber = cnumber
        self.cname = cname
        self.units = units
        self.rate = rate
        self.fixed = fixed

        self.energy_charge = 0
        self.total_bill = 0

    def calculate_energy_charge(self):
        self.energy_charge = self.units * self.rate

    def calculate_total_bill(self):
        self.total_bill = self.energy_charge + self.fixed

    def display_bill(self):
        print(f"""
Consumer Number  : {self.cnumber}
Consumer Name    : {self.cname}
Units Consumed   : {self.units}
Rate Per Unit    : {self.rate}
Fixed Charge     : {self.fixed}
Energy Charge    : {self.energy_charge}
Total Bill       : {self.total_bill}
""")


cnumber = input("Enter the Consumer Number ...")
cname = input("Enter the Consumer Name ...")
units = float(input("Enter the Units Consumed ..."))
rate = float(input("Enter the Rate Per Unit ..."))
fixed = float(input("Enter the Fixed Charge ..."))

e1 = ElectricityBill(cnumber, cname, units, rate, fixed)

e1.calculate_energy_charge()
e1.calculate_total_bill()
e1.display_bill()
