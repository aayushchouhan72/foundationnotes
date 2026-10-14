'''

5. Banking Security System
   A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password

Input:
Enter username: admin
Enter password: secure123

Output:
Valid user
Strong password

'''

username=  input("Enter the username :- ")
password =  input("Enter the  the password :- ")

if username == "admin":
     if len(password) >=8 and password == "secure123":
           print("Valid user\nStrong password")
     else:
         print("valid user but password is weak")
else:
    print("Enter valid username and password")