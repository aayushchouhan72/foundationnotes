# 6. Find the Longest Word

# A document-processing application needs to identify the longest word in a text document.

# Write a Python program that reads a file named "article.txt" and finds the longest word in the file.

# Input File: article.txt

# Python programming language is powerful.
# Developers use Python for application development.

# Expected Output:

# Longest Word: programming
# Length: 11
# # 

with open("question5/pargraph.txt","r") as f:
    data=f.read()
mlen=len(data.split()[0])
for i in data.split():
    if len(i)>mlen:
        mlen=len(i)
        word=i

print("max len is ",mlen,word)
