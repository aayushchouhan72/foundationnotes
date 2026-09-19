# Assignment 1 — Age Calculator

# Create a program that accepts the user's date of birth and calculates:

# Current age in years
# Completed months
# Total number of days lived
# Next birthday date
# Number of days remaining for the next birthday

# Input:

# Enter DOB (DD-MM-YYYY): 15-08-1998

# Expected Output:

# Age: 28 years
# Total Days Lived: XXXXX days
# Next Birthday: 15-08-2027
# Days Remaining: XX days


from datetime import datetime,timedelta,strptime
year,month,day= map(int,input("Enter the data of birth in formate YYYY-MM-DD").split("-"))

dob =  datetime(year=year,month=month,day=day)
todaydate=datetime.now()

diff = todaydate-dob

age = todaydate.year-dob.year

thisyearbirthday=datetime(year=todaydate.year,month=month,day=day)

nextbirthdate=thisyearbirthday+timedelta(days=365)

nextbirthdate=strptime(nextbirthdate,"%d-%m-%y")


print("Age :",age)
print("Total Days Lived :",diff)
print("Next Birthday:",nextbirthdate)
print("Days left :",nextbirthdate-todaydate)



