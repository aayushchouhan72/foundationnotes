# Toggle the case of each character in a string.


st = input("First string :-").strip()
i=0
final=''
while i <len(st):
     if st[i].isalpha():
           if 65<=ord(st[i])<=90:
                 final+=chr(ord(st[i])+32)
           else:
                final+=chr(ord(st[i])-32)
     elif st[i] == " ":
            final+=" "
     i+=1
print("Final string :- ",final)
                 