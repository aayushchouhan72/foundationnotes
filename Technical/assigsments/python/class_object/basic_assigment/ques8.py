class Car:
    def __init__(self, brand, model, distance, fuel, petrolprice):
        self.brand = brand
        self.model = model
        self.distance = distance
        self.fuel = fuel
        self.petrolprice = petrolprice

        self.mileage = 0
        self.fuelcost = 0

    def calculate_mileage(self):
        self.mileage = self.distance / self.fuel

    def calculate_fuel_cost(self):
        self.fuelcost = self.fuel * self.petrolprice

    def display_trip_details(self):
        print(f"""
Car Brand          : {self.brand}
Car Model          : {self.model}
Distance Travelled : {self.distance} km
Fuel Consumed      : {self.fuel} litres
Petrol Price       : {self.petrolprice}
Mileage            : {self.mileage} km/l
Fuel Cost          : {self.fuelcost}
""")


brand = input("Enter the Car Brand ...")
model = input("Enter the Car Model ...")
distance = float(input("Enter the Distance Travelled ..."))
fuel = float(input("Enter the Fuel Consumed ..."))
petrolprice = float(input("Enter the Petrol Price ..."))

c1 = Car(brand, model, distance, fuel, petrolprice)

c1.calculate_mileage()
c1.calculate_fuel_cost()
c1.display_trip_details()