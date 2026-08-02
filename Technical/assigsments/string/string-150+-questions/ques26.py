# Find the first occurrence of a word.

st =  input("Enter the string ...").strip().split()
word= input("Enter the word ...").strip()

i=0
index=-1
while i<len(st):
      if st[i] == word:
            print("Word at index ",index)
      index+=len(st[i])+1
      i+=1
      
