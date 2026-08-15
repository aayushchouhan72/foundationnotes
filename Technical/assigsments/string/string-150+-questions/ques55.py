# 55 Reverse only vowels. S = "hello" "holle"
s=input("Enter the string ...")
vowel=""
mid=""
final=""
vowels="aeiouAEIOU"
for i in s:
    if i in vowels:
        vowel+=i
    else:
        mid+=i

vowel=vowel[::-1]
vowelptr=0
for i in s:
    if i in vowel:
        final+=vowel[vowelptr]
        vowelptr+=1
    else:
        final+=i

print(final)