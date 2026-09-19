class Guest:

    def __init__(self, guest_id, guest_name, number_of_days, room_charge_per_day):

        self.guest_id = guest_id
        self.guest_name = guest_name
        self.number_of_days = number_of_days
        self.room_charge_per_day = room_charge_per_day

    def calculate_bill(self):

        # Calculate Room Bill
        self.room_bill = self.number_of_days * self.room_charge_per_day

        # Calculate GST (12%)
        self.gst = self.room_bill * 0.12

        # Calculate Final Bill
        self.final_bill = self.room_bill + self.gst
guest_id = input("Enter Guest ID : ")
guest_name = input("Enter Guest Name : ")
number_of_days = int(input("Enter Number of Days : "))
room_charge_per_day = float(input("Enter Room Charge Per Day : "))



g = Guest(
    guest_id,
    guest_name,
    number_of_days,
    room_charge_per_day
)



g.calculate_bill()


print("""
------ Hotel Bill ------
""")

print("Guest ID              :", g.guest_id)
print("Guest Name            :", g.guest_name)
print("Number of Days        :", g.number_of_days)
print("Room Charge Per Day   : ₹", g.room_charge_per_day)
print("Room Bill             : ₹", g.room_bill)
print("GST (12%)             : ₹", g.gst)
print("Final Bill            : ₹", g.final_bill)


