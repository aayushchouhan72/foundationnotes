'''
7. Remove Duplicate Words from a String

Voice Assistant Noise Correction System

A voice assistant records spoken commands from users.

Due to microphone disturbance and network lag, some words are repeated multiple times.

The company wants a Python program that removes duplicate words while maintaining the original order.

``
hello hello how are are you

'''

s= input("Enter the string .").split(" ")
final=""

count=0

for ch in s:
    if ch in final:
        pass
    else:
         final+=ch+" "

print(final)