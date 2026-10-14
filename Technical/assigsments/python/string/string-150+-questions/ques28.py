# Count occurrences of a word.

st =  input("Enter the string ...").strip().split()
word= input("Enter the word ...").strip()

i=0
index=0
while i<len(st):
      if st[i] == word:
            index+=1
      i+=1

print(f"count of {word} in string {index}")
