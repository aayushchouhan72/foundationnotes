'''# 7. Enterprise Password Pattern Strength Analyzer

A cybersecurity company wants to validate advanced passwords.

## Conditions:

* Minimum 10 characters
* At least:

  * 1 uppercase letter
  * 1 lowercase letter
  * 1 digit
  * 1 special character
* No consecutive repeating characters
* No spaces allowed

### Input:

text
Pyth@n1234


### Output:

text
Strong Password


### Input:

text
Paaass@12


### Output:

text
Weak Password


'''
pas = input("Enter the password ...")
isrepating =False
isconspecial=False
iscontainuppercase=False
iscontainlowercase=False
iscontaindigit=False
iscontainingspace=False
specialstr= "!#$%&'()*+,-./:;<=>?@"
for ch in pas:
    if ord(ch) in range(65,91):
        iscontainlowercase=True
    if ord(ch) in range(97,123):
        iscontainuppercase=True
    if ord(ch) in range(48,58):
        iscontaindigit=True
    if ch == " ":
        iscontainingspace=True
    if ch in specialstr:
        isconspecial=True
    if ch*2 in pas:
        isrepating=True

if not isrepating and isconspecial and iscontaindigit and not iscontainingspace and iscontainlowercase and iscontainuppercase and isconspecial and len(pas)>=10:
    print("Strong password .....")
elif isrepating and isconspecial and iscontaindigit and not iscontainingspace and iscontainlowercase and iscontainuppercase and isconspecial and len(pas)>=10:
     print("Weak password ......")
else:
    print("invalid  password ....")
    