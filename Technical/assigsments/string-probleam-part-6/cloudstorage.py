'''
 4. Cloud Storage Duplicate File Name Resolver

A cloud storage company stores uploaded filenames from users.

Sometimes multiple duplicate filenames are uploaded.

The system should:

* Keep the first occurrence unchanged
* Add (1), (2), (3)... for duplicates

### Input:

text
file file image file image data


### Output:

text
file file(1) image file(2) image(1) data
'''

str =  input("Enter the string ....")
final=""
visstr = ""
for word in str.split(" "):
    if word not in visstr:
           final+=word+" "
           visstr+=word
    else:
         wordcoun = final.count(word)
         final += f"{word}({wordcoun})"+" "

print(final)