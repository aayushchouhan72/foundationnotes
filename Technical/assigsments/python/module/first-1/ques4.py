from datetime import datetime, timedelta

while True:

    print()
    print("========== FUTURE DATE CALCULATOR ==========")
    print()
    print("1. Add Days")
    print("2. Add Weeks")
    print("3. Add Hours")
    print("4. Add Minutes")
    print("5. Exit")
    print()

    choice = int(input("Enter your choice: "))

    if choice == 1:

        day, month, year = map(
            int,
            input("Enter starting date (DD-MM-YYYY): ").split("-")
        )

        days = int(input("Enter number of days to add: "))

        start = datetime(year=year, month=month, day=day)

        future = start + timedelta(days=days)

        print()
        print("Starting Date :", start.strftime("%d-%m-%Y"))
        print("Days Added    :", days)
        print("Future Date   :", future.strftime("%d-%m-%Y"))

    elif choice == 2:

        day, month, year = map(
            int,
            input("Enter starting date (DD-MM-YYYY): ").split("-")
        )

        weeks = int(input("Enter number of weeks to add: "))

        start = datetime(year=year, month=month, day=day)

        future = start + timedelta(weeks=weeks)

        print()
        print("Starting Date :", start.strftime("%d-%m-%Y"))
        print("Weeks Added   :", weeks)
        print("Future Date   :", future.strftime("%d-%m-%Y"))

    elif choice == 3:

        date_time = input(
            "Enter date and time (DD-MM-YYYY HH:MM): "
        )

        hours = int(input("Enter number of hours to add: "))

        start = datetime.strptime(
            date_time,
            "%d-%m-%Y %H:%M"
        )

        future = start + timedelta(hours=hours)

        print()
        print(
            "Starting Date & Time :",
            start.strftime("%d-%m-%Y %H:%M")
        )
        print("Hours Added          :", hours)
        print(
            "Future Date & Time   :",
            future.strftime("%d-%m-%Y %H:%M")
        )

    elif choice == 4:

        date_time = input(
            "Enter date and time (DD-MM-YYYY HH:MM): "
        )

        minutes = int(input("Enter number of minutes to add: "))

        start = datetime.strptime(
            date_time,
            "%d-%m-%Y %H:%M"
        )

        future = start + timedelta(minutes=minutes)

        print()
        print(
            "Starting Date & Time :",
            start.strftime("%d-%m-%Y %H:%M")
        )
        print("Minutes Added        :", minutes)
        print(
            "Future Date & Time   :",
            future.strftime("%d-%m-%Y %H:%M")
        )

    elif choice == 5:

        print()
        print("Thank you for using Future Date Calculator!")
        break

    else:

        print("Invalid choice!")