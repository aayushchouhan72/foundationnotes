# '''
# Find All Characters with Maximum Frequency
# Website Traffic Analysis System

# A web analytics company tracks user activity symbols in server logs.

# The company wants to identify all characters having the maximum frequency in the given string.

# Input:
# aabbbccddd
# Output:
# b d
# '''

st =  input("Enter your string")
wordcount=0
maxcount=0
finalstring=""
visted = ""

for ch in st:
    if ch not in visted:
        for sch in st:
            if sch == ch :
                wordcount+=1
                
        visted+=ch
        if wordcount>=maxcount:
            if wordcount>maxcount:
                finalstring=""
            finalstring+=ch
            maxcount=wordcount
            
    else:
        continue
    wordcount=0

print(finalstring)

