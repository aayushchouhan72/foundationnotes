# Remove adjacent duplicates recursively. S = "azxxzy" "ay"
s =  input("Enter the string ...")
final=''
i=0
while i<len(s)//2:
     j=-(i+1)
     if not (s[i] == s[j]):
          final+=s[i]+s[j]
     i+=1
print(final)

     