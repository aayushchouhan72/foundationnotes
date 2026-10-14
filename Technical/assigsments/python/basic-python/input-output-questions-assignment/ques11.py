hours,min,sec =  map(int,input("Enter the total duration 00:00:00").split(":"))

outsec = hours*3600
outsec = outsec + 60*min +sec

print(f"The  total time in second is :- {outsec}")

