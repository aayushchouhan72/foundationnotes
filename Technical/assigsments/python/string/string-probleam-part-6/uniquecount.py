'''
# 3. Secure Banking Transaction Analyzer

A banking server generates encrypted transaction IDs using letters and digits.

The fraud detection team wants a Python program to find the first digit that does not repeat in the transaction ID.

If no unique digit exists, print:

text
No unique digit found


### Input:

text
A122334455667789


### Output:

text
8
'''
str = input("Enter the word ...")
visted=""
status=True

for ch in str[1::]:
    if ch not in visted:
        if str.count(ch) == 1 :
            print(ch)
            status=False
            break
    else:
        continue

if status:
     print("Not Unique Character Exist ...")