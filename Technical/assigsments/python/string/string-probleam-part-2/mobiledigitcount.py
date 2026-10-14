# 2.
# Mobile Number Digit Counter

# A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.

# Input:
# Enter contact number: +91 98765-43210

# Output:
# Total digits: 12


num = input("Enter your number  valid phone number should like this  +91 00000-00000 ...")

if num[:3] == "+91":
    if num.count(" "):
        if all(48<=ord(n)<=57 or n == "-" for n in num[3:].strip()) and "-" in num:
            print(f"Total digits {(len(num[3:].strip())+2)-1}")
        else:
             print("not Valid phone number ...")
    else:
        print("number should has space")
else:
    print("Enter Valid phone number..")


      