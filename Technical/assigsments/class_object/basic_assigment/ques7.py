class MobilePlan:
    def __init__(self, cname, mnumber, totaldata, useddata, validity):
        self.cname = cname
        self.mnumber = mnumber
        self.totaldata = totaldata
        self.useddata = useddata
        self.validity = validity

        self.remainingdata = 0
        self.usagepercentage = 0

    def calculate_remaining_data(self):
        self.remainingdata = self.totaldata - self.useddata

    def calculate_usage_percentage(self):
        self.usagepercentage = (self.useddata / self.totaldata) * 100

    def display_plan(self):
        print(f"""
Customer Name       : {self.cname}
Mobile Number       : {self.mnumber}
Total Data          : {self.totaldata} GB
Used Data           : {self.useddata} GB
Validity            : {self.validity} days
Remaining Data      : {self.remainingdata} GB
Usage Percentage    : {self.usagepercentage}%
""")


cname = input("Enter the Customer Name ...")
mnumber = input("Enter the Mobile Number ...")
totaldata = float(input("Enter the Total Data in GB ..."))
useddata = float(input("Enter the Used Data in GB ..."))
validity = int(input("Enter the Validity in days ..."))

m1 = MobilePlan(cname, mnumber, totaldata, useddata, validity)

m1.calculate_remaining_data()
m1.calculate_usage_percentage()
m1.display_plan()