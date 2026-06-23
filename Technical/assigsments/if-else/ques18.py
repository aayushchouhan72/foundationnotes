'''
8. A warehouse management system needs to identify the highest stock level among six different storage units to prioritize dispatch.
 The system should take the quantity of items stored in six units as input. It should compare all six values using nested conditions
 and determine which unit has the maximum stock. Display the highest stock value among all six units.

Input:
Unit1 = 120
Unit2 = 450
Unit3 = 300
Unit4 = 275
Unit5 = 500
Unit6 = 390

Output:
Highest Stock = 500
'''

unit1 = int(input("Enter the units 1 :-"))
unit2 = int(input("Enter the units 2 :-"))
unit3 = int(input("Enter the units 3 :-"))
unit4 = int(input("Enter the units 4 :-"))
unit5 = int(input("Enter the units 5 :-"))
unit6 = int(input("Enter the units 6 :-"))

if unit1 > unit2:
    if unit1 > unit3:
        if unit1 > unit4:
            if unit1 > unit5:
                if unit1 > unit6:
                    print("unit 1 is greatest ..")
                else:
                    print("unit 6 is greatest ..")
            else:
                if unit5 > unit6:
                    print("unit 5 is greatest ..")
                else:
                    print("unit 6 is greatest ..")

        else:
            if unit4 > unit5:
                if unit4 > unit6:
                    print("unit 4 is greatest ..")
                else:
                    print("unit 6 is greatest ..")
            else:
                if unit5 > unit6:
                    print("unit 5 is greatest")
                else:
                    print("unit 6 is greatest ..")

    else:
        if unit3 > unit4:
            if unit3 > unit5:
                if unit3 > unit6:
                    print("unit 3 is greatest ..")
                else:
                    print("unit 6 is greatest ..")
            else:
                if unit5 > unit6:
                    print("unit 5 is greatest ..")
                else:
                    print("unit 6 is greatest ..")

        else:
            if unit4 > unit5:
                if unit4 > unit6:
                    print("unit 4 is greatest ..")
                else:
                    print("unit 6 is greatest ..")
            else:
                if unit5 > unit6:
                    print("unit 5 is greatest ..")
                else:
                    print("unit 6 is greatest ..")

else:
    if unit2 > unit3:
        if unit2 > unit4:
            if unit2 > unit5:
                if unit2 > unit6:
                    print("unit 2 is greatest ..")
                else:
                    print("unit 6 is greatest ..")
            else:
                if unit5 > unit6:
                    print("unit 5 is greatest ..")
                else:
                    print("unit 6 is greatest ..")

        else:
            if unit4 > unit5:
                if unit4 > unit6:
                    print("unit 4 is greatest ..")
                else:
                    print("unit 6 is greatest ..")
            else:
                if unit5 > unit6:
                    print("unit 5 is greatest ..")
                else:
                    print("unit 6 is greatest ..")

    else:
        if unit3 > unit4:
            if unit3 > unit5:
                if unit3 > unit6:
                    print("unit 3 is greatest ..")
                else:
                    print("unit 6 is greatest ..")
            else:
                if unit5 > unit6:
                    print("unit 5 is greatest ..")
                else:
                    print("unit 6 is greatest ..")

        else:
            if unit4 > unit5:
                if unit4 > unit6:
                    print("unit 4 is greatest ..")
                else:
                    print("unit 6 is greatest ..")
            else:
                if unit5 > unit6:
                    print("unit 5 is greatest ..")
                else:
                    print("unit 6 is greatest ..")
   