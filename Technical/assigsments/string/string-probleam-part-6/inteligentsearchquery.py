'''# 8. Intelligent Search Query Compressor

A search engine company wants to compress user queries.

## Rules:

* Count frequency of each character
* Display characters in sorted order
* Ignore spaces
* Case insensitive

### Input:

text
Google Search


### Output:

text
a1c1e2g2h1l1o2r1s1t1
'''
str =  input("Enter the string ...").lower()
tr=sorted(str)
for j in "abcdefghijklmnopqrstuvwxyz":
    if j in str:
           print(f'{j}{str.count(j)}',end="")
