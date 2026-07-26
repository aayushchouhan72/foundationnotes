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

s = input("Enter the string: ")

longest = ""
current = ""

for ch in s:
    if ch not in current:
        current+=ch
    else:
        while ch in current:
            current=current[1:]
        current+=ch
    if len(current)>len(longest):
        longest=current
print("Longest substring:", longest,current)
print("Length:", len(longest))