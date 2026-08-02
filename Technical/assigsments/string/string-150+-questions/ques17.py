# Remove occurrences of a character.

st=  input("Enter the string ..")
char = input("Enter the char")
i=0 
final=""
while i<len(st):
     if st[i] == char: 
         pass
     else:
          final+=st[i]  
     i+=1
print(final)
