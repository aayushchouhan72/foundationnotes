'''
5.
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password

'''

pas = input("Enter your password").strip()
resstring = ""
i=1
flag=True
containspace=False
while i<len(pas):
    if pas[0] in range(65,91) and flag:
           resstring+="1"
 
    elif pas[-1] in "0987654321" and flag:
           resstring+="1"
    
    elif pas[i] in range(34,64):
           resstring+="1"

    elif pas[i] == " ":
            containspace=True

    flag=False
    i+=1

if len(pas) in range(8,16) and not resstring.count("0") :
               print("Secure pass",resstring)
else:
    print("Make secure password.. ")
       
    
  
    
