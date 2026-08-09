# 34 Find the shortest word. S = "find the shortest word" "the"

s= input("Enter the string ").split()
word=""
length=9
final=""

for i in s:
        if length>len(i) and i!=" ":
            word=i
            length=len(i)
print(word)