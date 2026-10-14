# 5. Smart Warehouse Dispatch System

# A warehouse decides dispatch strategy based on stock availability, priority level, and delivery distance.

# If stock is at least 100, then check priority. If high priority, then check distance. If distance is up to 200, dispatch immediately; otherwise use fast courier. If priority is not high, then check if stock is at least 300. If yes, bulk dispatch; otherwise normal dispatch. If stock is less than 100, then check if stock is at least 50. If yes, and priority is high, partially dispatch; otherwise hold. If stock is below 50, mark out of stock.

# Input:
# Stock = 120
# Priority = high
# Distance = 300

# Output:
# Dispatch Status = Dispatch via Fast Courier
stock = int(input("Enter stock: "))
priority = input("Enter priority: ")
distance = int(input("Enter distance: "))

if stock >= 100 and priority == "high" and distance <= 200:
    print("Dispatch Status = Dispatch Immediately")

elif stock >= 100 and priority == "high" and distance > 200:
    print("Dispatch Status = Dispatch via Fast Courier")

elif stock >= 300 and priority != "high":
    print("Dispatch Status = Bulk Dispatch")

elif stock >= 50 and priority == "high":
    print("Dispatch Status = Partially Dispatch")

elif stock < 50:
    print("Dispatch Status = Out of Stock")

else:
    print("Dispatch Status = Normal Dispatch")
        