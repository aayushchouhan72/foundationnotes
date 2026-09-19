from datetime import datetime, timedelta

while True:

    print()
    print("========== PAST DATE & TIME CALCULATOR ==========")
    print()
    print("1. Subtract Days")
    print("2. Subtract Weeks")
    print("3. Subtract Hours")
    print("4. Subtract Minutes")
    print("5. Exit")
    print()

    choice = int(input("Enter your choice: "))

    if choice == 1:

        day, month, year = map(
            int,
            input("Enter starting date (DD-MM-YYYY): ").split("-")
        )

        days = int(input("Enter number of days to subtract: "))

        start = datetime(year=year, month=month, day=day)

        past = start - timedelta(days=days)

        print()
        print("Starting Date    :", start.strftime("%d-%m-%Y"))
        print("Days Subtracted  :", days)
        print("Past Date        :", past.strftime("%d-%m-%Y"))

    elif choice == 2:

        day, month, year = map(
            int,
            input("Enter starting date (DD-MM-YYYY): ").split("-")
        )

        weeks = int(input("Enter number of weeks to subtract: "))

        start = datetime(year=year, month=month, day=day)

        past = start - timedelta(weeks=weeks)

        print()
        print("Starting Date    :", start.strftime("%d-%m-%Y"))
        print("Weeks Subtracted :", weeks)
        print("Past Date        :", past.strftime("%d-%m-%Y"))

    elif choice == 3:

        date_time = input(
            "Enter date and time (DD-MM-YYYY HH:MM): "
        )

        hours = int(input("Enter number of hours to subtract: "))

        start = datetime.strptime(
            date_time,
            "%d-%m-%Y %H:%M"
        )

        past = start - timedelta(hours=hours)

        print()
        print(
            "Starting Date & Time :",
            start.strftime("%d-%m-%Y %H:%M")
        )
        print("Hours Subtracted     :", hours)
        print(
            "Past Date & Time     :",
            past.strftime("%d-%m-%Y %H:%M")
        )

    elif choice == 4:

        date_time = input(
            "Enter date and time (DD-MM-YYYY HH:MM): "
        )

        minutes = int(
            input("Enter number of minutes to subtract: ")
        )

        start = datetime.strptime(
            date_time,
            "%d-%m-%Y %H:%M"
        )

        past = start - timedelta(minutes=minutes)

        print()
        print(
            "Starting Date & Time :",
            start.strftime("%d-%m-%Y %H:%M")
        )
        print("Minutes Subtracted   :", minutes)
        print(
            "Past Date & Time     :",
            past.strftime("%d-%m-%Y %H:%M")
        )

    elif choice == 5:

        print()
        print("Thank you for using Past Date & Time Calculator!")
        break

    else:

        print("Invalid choice!")