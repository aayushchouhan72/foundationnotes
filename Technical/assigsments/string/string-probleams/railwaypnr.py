# 6.
# Railway Ticket PNR Analyzer

# A railway department wants to verify whether a PNR number is valid.

# Conditions:
# - PNR must start with "PNR"
# - Total length should be 12 characters
# - Remaining characters should be digits

# Input:
# Enter PNR: PNR123456789

# Output:
# Valid PNR Number

number = str(input("Enter your pnr number ").lower())
digcount=0
i=0
if len(number)>12 or len(number)<12 and number[0:3]=="pnr":
      print("Enter Valid number ...")
else:
    while i<len(number):
        if i>2:
            if number[i].isdigit(): 
                  digcount+=1
        else:
                 break
        i+=1
    else:
        if digcount == 9 :
              print("Vlaid PNR Number ...")

if i>len(number):
      print("Not Vlaid pnr Number ...")
            