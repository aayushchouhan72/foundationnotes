'''
6. AI Chat Toxic Pattern Detector

An AI moderation system wants to detect whether a sentence contains three consecutive repeating characters.

If found:

text
Spam Pattern Found


Else:

text
Clean Message


### Input:

text
heyyy broooo welcome


### Output:

text
Spam Pattern Found
'''
str =  input("Enter the string ...")

i=-1
while i<len(str):
    i+=1
    if i>=len(str):
        break
    if str[i] == " ":
        continue
    else:
        j=i
        if j<len(str)-2:
            if str[j] == str[j+1] == str[j+2] :
                print("Spam pattern is found")
                break

if not (i<len(str)):
     print("Clean message")
                    
     