from datetime import datetime, timedelta

while True:

    print()
    print("========== EMPLOYEE & PROJECT DATE CALCULATOR ==========")
    print()
    print("1. Calculate Probation End Date")
    print("2. Calculate Project Deadline")
    print("3. Calculate Notice Period End Date")
    print("4. Calculate Days Remaining for Deadline")
    print("5. Check Employee Work Anniversary")
    print("6. Exit")
    print()

    choice = int(input("Enter your choice: "))

    # CASE 1
    if choice == 1:

        day, month, year = map(
            int,
            input("Enter employee joining date (DD-MM-YYYY): ").split("-")
        )

        days = int(input("Enter probation period in days: "))

        joining = datetime(
            year=year,
            month=month,
            day=day
        )

        probation = joining + timedelta(days=days)

        print()
        print(
            "Joining Date       :",
            joining.strftime("%d-%m-%Y")
        )
        print("Probation Period   :", days, "days")
        print(
            "Probation End Date :",
            probation.strftime("%d-%m-%Y")
        )

    # CASE 2
    elif choice == 2:

        day, month, year = map(
            int,
            input("Enter project start date (DD-MM-YYYY): ").split("-")
        )

        days = int(input("Enter project duration in days: "))

        start = datetime(
            year=year,
            month=month,
            day=day
        )

        deadline = start + timedelta(days=days)

        print()
        print(
            "Project Start Date :",
            start.strftime("%d-%m-%Y")
        )
        print("Project Duration   :", days, "days")
        print(
            "Project Deadline   :",
            deadline.strftime("%d-%m-%Y")
        )

    # CASE 3
    elif choice == 3:

        day, month, year = map(
            int,
            input("Enter resignation date (DD-MM-YYYY): ").split("-")
        )

        days = int(input("Enter notice period in days: "))

        resignation = datetime(
            year=year,
            month=month,
            day=day
        )

        last_working = resignation + timedelta(days=days - 1)

        print()
        print(
            "Resignation Date :",
            resignation.strftime("%d-%m-%Y")
        )
        print("Notice Period    :", days, "days")
        print(
            "Last Working Date:",
            last_working.strftime("%d-%m-%Y")
        )

    # CASE 4
    elif choice == 4:

        day, month, year = map(
            int,
            input("Enter current date (DD-MM-YYYY): ").split("-")
        )

        day1, month1, year1 = map(
            int,
            input("Enter project deadline (DD-MM-YYYY): ").split("-")
        )

        current = datetime(
            year=year,
            month=month,
            day=day
        )

        deadline = datetime(
            year=year1,
            month=month1,
            day=day1
        )

        diff = deadline - current

        print()
        print(
            "Current Date     :",
            current.strftime("%d-%m-%Y")
        )
        print(
            "Project Deadline :",
            deadline.strftime("%d-%m-%Y")
        )

        if diff.days >= 0:

            print("Days Remaining   :", diff.days, "days")

        else:

            overdue = current - deadline

            print("Deadline Status  : Deadline has already passed")
            print("Days Overdue     :", overdue.days, "days")

    # CASE 5
    elif choice == 5:

        day, month, year = map(
            int,
            input("Enter employee joining date (DD-MM-YYYY): ").split("-")
        )

        day1, month1, year1 = map(
            int,
            input("Enter current date (DD-MM-YYYY): ").split("-")
        )

        joining = datetime(
            year=year,
            month=month,
            day=day
        )

        current = datetime(
            year=year1,
            month=month1,
            day=day1
        )

        print()
        print(
            "Joining Date :",
            joining.strftime("%d-%m-%Y")
        )
        print(
            "Current Date :",
            current.strftime("%d-%m-%Y")
        )

        if joining.day == current.day and joining.month == current.month:

            completed_years = current.year - joining.year

            print()
            print("Work Anniversary: YES")
            print("Completed Years  :", completed_years, "years")

        else:

            completed_years = current.year - joining.year

            if (current.month, current.day) < (joining.month, joining.day):
                completed_years = completed_years - 1

            print()
            print("Work Anniversary: NO")
            print("Completed Years  :", completed_years, "years")

    # CASE 6
    elif choice == 6:

        print()
        print("Thank you for using Employee & Project Date Calculator!")
        break

    else:

        print()
        print("Invalid choice!")