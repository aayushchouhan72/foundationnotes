'''5.
Cybercrime Log Analysis System

A cybersecurity company monitors encrypted login activity stored as character-based security logs.

During investigation, analysts need to identify the last character that repeats in the log sequence.
This helps detect the most recent duplicated activity pattern before a possible security breach.

Write a Python program to find the last repeating character in a given string.

If no repeating character exists, print:

No repeating character found
Input:
abccdbefga
Output:
a'''

st =  input("Enter the string ...")
mincount=len(st)
wordcount=0
vis=""
outs=''
for ch in st:
    if ch in vis:
        continue
    else:
        for sch in st:
            if sch == ch :
                wordcount+=1
       
        if wordcount<mincount:
           if wordcount != 1:
                outs = ch
                mincount=wordcount               
        vis+=ch
    wordcount=0
             
print(outs)