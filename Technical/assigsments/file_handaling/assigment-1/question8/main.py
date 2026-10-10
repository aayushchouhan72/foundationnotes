# 8. Count Words Starting With a Particular Letter

# A search engine wants to analyze words beginning with a particular character.

# Write a Python program that:

# 1. Reads a file named "article.txt".
# 2. Accepts a character from the user.
# 3. Counts the number of words starting with that character.

# Input File: article.txt

# Python programming provides powerful features.
# Programming helps developers build applications.

# Sample Input:

# Enter character: p

# Expected Output:

# Words starting with 'p': <display count>

wordcheck= input("Enter the letter to check..")
with open("question5/pargraph.txt","r") as f:
    data=f.read()
count=0
for i in data.split():
    if i[0] == wordcheck.lower():
        count+=1

print(f"The word start with given latter {wordcheck} is",count)

