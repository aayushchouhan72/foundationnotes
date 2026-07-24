dis = int(input("Enter the  Distance you traveled"))
mileage = int(input("Enter the milage of car"))
petrolprice = float(input("Enter the petrol price in ruppess" ))


usedpetrol = dis/mileage

cost =  petrolprice*usedpetrol

print(f"Petrol Used = {usedpetrol}\nTotal cost = {cost}")

