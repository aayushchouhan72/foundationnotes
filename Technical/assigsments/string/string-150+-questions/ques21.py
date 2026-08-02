# Find the first non-repeating character.

st =  input("Enter the string ...")
visted = ""
prevcount,char=9,""
for i in st:
    if  i not in visted and i !=" ":
        count=0
        for j  in st :
            if i == j:
                 count+=1
        if count == 1:
            print("First none repeating  char is ",i)
            break
        visted+=i

