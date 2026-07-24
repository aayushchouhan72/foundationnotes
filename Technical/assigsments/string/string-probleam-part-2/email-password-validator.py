# Email Username Validator

# A company wants to check whether an employee email username is valid before creating an official account.

# Conditions:
# - Username should start with a letter
# - Username can contain letters, digits, underscore (_)
# - No spaces allowed
# - Length should be between 5 and 12 characters

# Input:
# Enter username: ajay_123

# Output:
# Valid Username

email=input("Enter your email...")
username=input("Enter username...")



if email.endswith(("@gmail.com","@yahoo.com")):
    if 97<=ord(username[0])>=122 or  65<=ord(username[0])>=90:
        if username.isspace():
            print("Username not contain an space ..")
        else:
             if all(ch.isalnum() or ch == "_" for ch in username) and not username.isspace() and username.count("_") > 0:
                 if len(username)>=5 and len(username)<=15:
                                print("Valid user name...")
                 else:
                      print("Entered username should be in range of 5 to 15")
             else:
                 print("Entred passwprd only contain digit ,char ,underscore")
    else:
        print("User must Start With Charecter..")
else:
    print("Enter Vaid email First ..")