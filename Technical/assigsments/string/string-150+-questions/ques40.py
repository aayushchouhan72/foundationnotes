# 40 Search all occurrences of a word. S = "a b a b", Word = "b" 2, 6 (start indices)/

s= input("Enter the string ...").split()
word=input("Enter the word ...")
count=-1
for i in s:
    if word ==  i:
        print(count,",",end=" ",sep="")
    count=len(i)
 
