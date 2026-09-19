from datetime import datetime, timedelta

day, month, year = map(
    int,
    input("Enter first date (DD-MM-YYYY): ").split("-")
)

day1, month1, year1 = map(
    int,
    input("Enter second date (DD-MM-YYYY): ").split("-")
)

first = datetime(year=year, month=month, day=day)
second = datetime(year=year1, month=month1, day=day1)

diff = second - first

days = diff.days
weeks = days // 7
hours = days * 24
minutes = hours * 60

print()
print("Days Difference:", days)
print("Weeks Difference:", weeks)
print("Hours Difference:", hours)
print("Minutes Difference:", minutes)