
# 7.
# Vehicle Number Plate Checker

# The traffic department wants to validate vehicle registration numbers.

# Conditions:
# - First 2 characters should be alphabets
# - Next 2 should be digits
# - Total length should be 10

# Input:
# Enter vehicle number: MP04AB1234

# Output:
# Valid Vehicle Number
st = input("Enter your number plate number: ").swapcase()

res = ''

if len(st) == 10:
    
    if all(97 <= ord(num) <= 122 for num in st[0:2]):
        print(1)
        res += "1"

    if all(48 <= ord(num) <= 57 for num in st[2:4]):
        print(2)
        res += "1"

    if all(97 <= ord(num) <= 122 for num in st[4:6]):
        print(3)
        res += "1"

    if all(48 <= ord(num) <= 57 for num in st[6:10]):
        print(4)
        res += "1"

print("Result:", res)
if res == "1111":
    print("Valid vehicle number ..")
else:
    print("Invalid vehicle number ..")
