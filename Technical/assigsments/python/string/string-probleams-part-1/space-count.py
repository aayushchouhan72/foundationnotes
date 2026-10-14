'''2.
Space Counter in Chat Messages

A chat application wants to calculate how many spaces are used in a message.

Input: Enter chat message: Good morning everyone how are you

Output: Total spaces: 5
'''

st = input("Enter your chat Message :::---").strip()
count=0
for i in st:
     if i.isspace() :
        count+=1
else:
    print(f"Total space :- {count} ")