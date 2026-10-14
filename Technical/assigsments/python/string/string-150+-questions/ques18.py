# Replace occurrences of a character.

st=  input("Enter the string ..")
char = input("previous char you wont to replace ...")
newchar = input("New character you wont add ...")
i=0 
final=""
while i<len(st):
     if st[i] == char: 
        final+=newchar
     else:
        final+=st[i]  
     i+=1
print(final)
