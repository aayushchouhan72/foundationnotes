# 9 Search all occurrences of a character. S = "banana", Char='a' 1, 3, 5 (indices)

s = input("Enter the string ...")

word = input("ENter the char >>")
count=-1
for i  in s:
     count+=1
     if i ==  word:
          print(count,",",end=" ")