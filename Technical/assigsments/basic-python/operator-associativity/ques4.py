speed = int(input("Enter the speed of car in km/hr"))
hours,minutes=map(int,input("Enter the time you taken to travel").split(":"))
totalmin=hours*60+minutes

totaltime=totalmin/60
distance=  totaltime*speed

print(f"Total Time = {totaltime}\nDistance = {distance}")


