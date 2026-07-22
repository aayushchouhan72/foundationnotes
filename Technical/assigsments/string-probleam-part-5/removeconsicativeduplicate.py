'''
Replace Consecutive Duplicate Characters with Single Character
Data Compression System

A cloud storage company wants to reduce unnecessary repeated characters in text logs.

Write a Python program that replaces consecutive duplicate characters with a single occurrence.

Input:
aaabbbccccdddaa
Output:
abcda
'''


st =  input("Enter your string .....")
string=""
i=0
for ch in st:
    if ch not in string:
        string+=ch
print(string)         
             

print(string) 