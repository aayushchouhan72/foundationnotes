principle = int(input("Enter the  principle amount"))
rate = int(input("Enter the rate at which you went money"))
time = int(input("Enter the time in years"))


amount = principle*(1+(rate/100))**time

print(f"Amount after interest = {amount}")
