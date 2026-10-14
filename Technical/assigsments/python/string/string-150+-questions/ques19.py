# Find the highest frequency character.


st =  input("Enter the string ...")
visted = ""
prevcount,char=0,""
for i in st:
    if  i not in visted and i !=" ":
        count=0
        for j  in st :
            if i == j:
                 count+=1
        if prevcount<=count:
            prevcount,char=count,i
        visted+=i

print("highest frequecy char is ",char)
 
