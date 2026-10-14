'''
2.  Corporate Employee Short ID Generator

A multinational company wants to automatically generate short IDs for
employees while creating official email accounts. The system should take
the employee’s full name and create an ID using the first character of
each word.

Conditions: - Take first character of every word - Convert all
characters to uppercase

Input: Enter employee name: ajay singh thakur

Output: Employee Short ID: AST

'''

str =  input("Enter the your name")

str = str.split(" ")

shortname=""

for ch in str:
    
    shortname+=ch[0].upper()

print(f"Employee short ID is {shortname}")
    
    