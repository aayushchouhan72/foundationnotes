# 7. Count Occurrence of a Particular Word

# A company wants to analyze how frequently a particular keyword appears in a document.

# Write a Python program that:

# 1. Reads a file named "article.txt".
# 2. Accepts a word from the user.
# 3. Counts how many times the given word occurs in the file.

# Input File: article.txt

# Python is simple.
# Python is powerful.
# Many developers use Python.
# Python is popular.

# Sample Input:

# Enter word to search: Python

# Expected Output:

# Python occurs 4 times in the file.

# ---

wordcheck= input("Enter the word to check..")
with open("question5/pargraph.txt","r") as f:
    data=f.read()
count=0
for i in data.split():
    if i == wordcheck.lower():
        count+=1

print("The given word occured ",count)
