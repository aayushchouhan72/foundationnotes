'''
3.  Smart Chat Message Cleaner

A social media company noticed that users often enter messages with
unnecessary spaces. To improve readability and storage efficiency, the
system should remove extra spaces and keep only a single space between
words.

Input: Enter message: Java is easy

Output: Cleaned Message: Java is easy
'''

str =  input("Your entred string ...").strip()

finalmessage=""
flag=True
for i,ch in enumerate(str):
    if ch==" ":
        if flag:
            finalmessage+=" "
            flag=False
        continue
    else:
         finalmessage+=str[i]
         flag=True
    
print(finalmessage)
