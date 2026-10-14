salary = int(input("Enter your salary"))
wokingday =  int(input("Enter number of days you worked"))
wokinghours = int(input("Enter the hours you works in a day"))

ondaywage = salary/wokingday

onhourewage = ondaywage/wokinghours

print(f"salary per day = {ondaywage} \nSalary per hours = {onhourewage}")