# Count total occurrences of a character.
st=  input("Enter the string ..")
char = input("Enter the char")
i=0 
occ=0
while i<len(st):
     if st[i] == char: 
         occ+=1   
     i+=1
print("Given char is found at the index ",occ)
