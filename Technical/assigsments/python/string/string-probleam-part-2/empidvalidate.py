'''
4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID

'''

st= input("Enter the employe id ...").lower().strip()

if st.startswith("emp"):
    if  len(st) == 8:
         if all(48<=ord(n)<=57 for n in st[3:]):
              print("Valid Employee ID")
         else:
            print("not Valid Employee id ::-->")
    else:
          print("Length of string is not Valid ...")      
         
else:
     print("Enter valid employe id ...") 
