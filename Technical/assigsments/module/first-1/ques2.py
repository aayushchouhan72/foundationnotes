# 2.
#  Employee Joining & Experience System

# Create an employee experience calculator.

# Read:

# Employee name
# Joining date
# Current date

# Calculate:

# Total days worked
# Total years worked
# Total months approximately
# Experience in Years Months Days
# Whether employee has completed 1 year
# Whether employee has completed 5 years

# Example:

# Enter employee name: Rahul
# Enter joining date: 10-06-2021
# Enter current date: 10-09-2026

# Output:

# Employee: Rahul
# Joining Date: 10-06-2021
# Experience: 5 Years 3 Months 0 Days
# Total Days Worked: 1918
# 5 Years Completed: Yes
from datetime import datetime
from dateutil.relativedelta import relativedelta

name = input("Enter employee name: ")

day, month, year = map(
    int,
    input("Enter joining date in format DD-MM-YYYY: ").split("-")
)

day1, month1, year1 = map(
    int,
    input("Enter current date in format DD-MM-YYYY: ").split("-")
)

start = datetime(year=year, month=month, day=day)
current = datetime(year=year1, month=month1, day=day1)

# Calculate exact experience
diff = relativedelta(current, start)

# Calculate total days
total_days = (current - start).days

print()
print("Employee:", name)
print("Joining Date:", start.strftime("%d-%m-%Y"))
print("Experience:", diff.years, "Years", diff.months, "Months", diff.days, "Days")
print("Total Days Worked:", total_days)

# Check 1 year and 5 years
if diff.years >= 1:
    print("1 Year Completed: Yes")
else:
    print("1 Year Completed: No")

if diff.years >= 5:
    print("5 Years Completed: Yes")
else:
    print("5 Years Completed: No")

# Total approximate months
total_months = diff.years * 12 + diff.months
print("Total Months Approximately:", total_months)