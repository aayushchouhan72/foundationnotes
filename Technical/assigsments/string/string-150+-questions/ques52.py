# 52 Remove all special characters. S = "a!@b#c" "abc"

s=input("Enter the string")
final=""

for i in s:
    if  i.isdigit() or i.isalpha():
        final+=i      
print(final)