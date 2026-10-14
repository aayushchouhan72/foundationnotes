# Find the first occurrence of a character.

st=  input("Enter the string ..")
char = input("Enter the char")
i=0 
while i<len(st):
     if st[i] == char:
           print("Given char is found at the index ",i)
           break
     i+=1