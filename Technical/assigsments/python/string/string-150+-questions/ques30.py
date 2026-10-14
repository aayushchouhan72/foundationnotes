# 30 Replace a word with another word. S = "old data", Old="old", New="new" "new data"

s= input("Enter the string ").split()
word = input("Enter the word ..")
replace = input("Enter the word to replace ...")
final=""

for i in s:
     if word == i:
          final+=replace+" "
     else:
          final+=i+" "
print(final)
