'''
1.
Find the Longest Substring Without Repeating Characters
Cybersecurity Session Tracking System

A cybersecurity company monitors user session IDs generated during secure login sessions.

To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.

Input:
abcabcbb
Output:
abc
'''

st =  input("Enter your string .....")
string=""
sample=''
for  chr1 in st:
    sample+=chr1
    for ch in st:
        if ch not in sample:
              sample+=ch
        else:
             break
    if len(sample)>len(string):
        string=sample
    if len(sample) == len(st):
        break
    sample=""

print(string)