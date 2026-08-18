# 6Count number of sentences in a paragraph. P = "This. Is. Test." 3

sentence = input("Enter the string ...")

count=0
for i in sentence:
    if i == ".":
         count+=1

print(count)