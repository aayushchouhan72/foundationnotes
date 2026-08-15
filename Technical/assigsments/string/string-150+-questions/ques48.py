# 48 Remove all vowels. S = "aeiou XYZ" " XYZ" 4
s=input("Enter the string ...")
final=""
vowel="aeiouAEIOU"
for i in s:
     if i not in vowel:
         final+=i
print(final)