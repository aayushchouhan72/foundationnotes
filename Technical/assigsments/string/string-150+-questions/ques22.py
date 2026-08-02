# Find the last repeating character.

st =  input("Enter the string ...").strip()
char=""
for i in st:
        count=0
        for j  in st :
            if i == j:
                 count+=1
        if count > 1:
            char=i


print("Last Repeating char ",char)