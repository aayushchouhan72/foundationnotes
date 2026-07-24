totelsec = int(input("Enter the number of seconds of vedio"))

hours=int(totelsec/3600)
totelsec=totelsec%3600

minutes=int(totelsec/60)
totelsec=totelsec%60

sec = totelsec;

print(F"Hours:{hours},Minutes:{minutes},Seconds:{sec}")