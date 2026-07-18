'''
6. Find Occurrence of a Word in a String

Product Review Analysis System

An e-commerce company wants to analyze customer reviews.

The company wants a Python program to count how many times a particular word appears in a review.

Input Sentence:


iphone is good and iphone battery is strong


Word:


iphone


Output:


2


'''

s= input("Enter the string .").split(" ")
check= input("Enter the word you wont to check")

count=0

for ch in s:
    if ch == check:
        
       count+=1

print(count)