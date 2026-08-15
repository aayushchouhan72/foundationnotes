# 56Reverse only consonants. S = "apple" "eplpa"
s = input("Enter the string ...")

consonant = ""
mid = ""
final = ""

vowels = "aeiouAEIOU"

for i in s:
    if i.isalpha() and i not in vowels:
        consonant += i
    else:
        mid += i

consonant = consonant[::-1]

consonantptr = 0

for i in s:
    if i.isalpha() and i not in vowels:
        final += consonant[consonantptr]
        consonantptr += 1
    else:
        final += i

print(final)