# Count total words in a string.
st =  input("Enter the string ...").strip()
i=0
count=0
while i <len(st):
      if st[i] == " ":
            count+=1
      i+=1

print("Total word in the Given string is :- ",count+1)