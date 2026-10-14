# Print all characters that occur exactly twice.

st =  input("Enter the string ...").strip()
printed=""
char=""
for i in st:
        
        count=0
        for j  in st :
            if i == j:
                 count+=1
        if count  == 2 :
            print("",end="") if i  in printed else print(i,end=" ")
            printed+=i


