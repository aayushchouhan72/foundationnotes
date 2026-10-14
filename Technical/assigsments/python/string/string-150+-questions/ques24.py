# Check if all characters in a string are unique.
st =  input("Enter the string ...").strip()
char=""
for i in st:
        count=0
        for j  in st :
            if i == j:
                 count+=1
        if count != 1:
            print("this string contain  repeating char")
            break
else:
     print("this string contain nono repeating char")