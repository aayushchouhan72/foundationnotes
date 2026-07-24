sec =  int(input("Enter the video duration in seconds"))

hours =  sec//3600
remsec = sec%3600

min  = remsec//60
remsec = min%60


print(f"Hours = {hours}\nMinutes = {min}\nSeconds = {remsec}")

