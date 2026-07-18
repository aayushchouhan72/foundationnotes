'''
3. Find the First Non-Repeated Character

Railway Ticket Fraud Detection System

The railway department generates ticket reference IDs automatically.

Sometimes, due to technical issues, many characters get repeated inside the ticket ID.

The department wants a Python program that finds the first character that appears only once in the string.

Example 1

Input:
aabbccddefg
Output:


e
'''

str =  input("ENter the string ...")
rep=""
for ch in str:
      if str.count(ch)>1:
         pass
      else:
         rep+=ch
else:
    print("Repeted characters are ..",rep)
    