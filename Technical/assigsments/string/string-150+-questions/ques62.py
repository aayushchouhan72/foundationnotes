# 62Count vowels and consonants. S = "apple" Vowels: 2, Consonants: 3


st = input("Enter the string ....").lower()

vowels=0
consonants=0
con="aeiou"
for i in st:
    if  i in con:
         vowels+=1
    else:
        consonants+=1

print(f"Vowels: {vowels}, Consonants: {consonants}")