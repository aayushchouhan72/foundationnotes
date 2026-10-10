# 4. Count Lines, Words and Characters in a File

# A content management company wants to analyze the size of a text document.

# Write a Python program that reads a file named "article.txt" and displays:

# 1. Total number of lines
# 2. Total number of words
# 3. Total number of characters

# Input File: article.txt

# Python is easy to learn.
# Python is powerful.
# Python is widely used in industry.

# Expected Output:

# Total Lines: 3
# Total Words: 14
# Total Characters: <calculate based on file content>

with open("question4/artical.txt","r") as f:
    data=f.readlines()

linecount=0
wordcount=0
charcount=0

for line in data:
    linecount+=1
    wordcount+=len(line.split())
    charcount+=len(line)-len(line.split())

print(f"""
Total Lines: {linecount}
Total Words: {wordcount}
Total Characters:{charcount}
""")
